"use strict";

const assert = require("node:assert/strict");
const {
  draftStorageKey,
  readStoredDraft,
  writeStoredDraft,
  clearStoredDraft,
  refreshDisposition,
  orderQueueEntries,
  mediaMarkup,
  entryKey,
  localDrafts,
} = require("../review-queue/app.js");

class MemoryStorage {
  constructor() { this.values = new Map(); }
  getItem(key) { return this.values.has(key) ? this.values.get(key) : null; }
  setItem(key, value) { this.values.set(key, String(value)); }
  removeItem(key) { this.values.delete(key); }
}

function entry(id = "RD-001", version = "sample-v1", source = "sample") {
  return { id, version, source_id: source, source_name: "Sample", entry_key: `${source}:${id}` };
}

function testDraftRoundTrip() {
  const storage = new MemoryStorage();
  const item = entry();
  writeStoredDraft(item, "approve", "Checked exact version.", storage, "2026-08-15T18:00:00Z");
  const restored = readStoredDraft(item, storage);
  assert.equal(restored.choice, "approve");
  assert.equal(restored.entry_key, item.entry_key);
}

function testDraftsAreSourceEntryAndVersionScoped() {
  const storage = new MemoryStorage();
  const first = entry("RD-001", "v1", "one");
  const second = entry("RD-001", "v1", "two");
  writeStoredDraft(first, "approve", "first", storage);
  writeStoredDraft(second, "revise", "second", storage);
  assert.equal(readStoredDraft(first, storage).notes, "first");
  assert.equal(readStoredDraft(second, storage).notes, "second");
  assert.equal(readStoredDraft(entry("RD-001", "v2", "one"), storage), null);
  assert.notEqual(draftStorageKey(first), draftStorageKey(second));
}

function testInvalidDraftIsDiscarded() {
  const storage = new MemoryStorage();
  const item = entry();
  storage.setItem(draftStorageKey(item), "not-json");
  assert.equal(readStoredDraft(item, storage), null);
  assert.equal(storage.getItem(draftStorageKey(item)), null);
}

function testClearRemovesBrowserDraft() {
  const storage = new MemoryStorage();
  const item = entry();
  writeStoredDraft(item, "approve", "", storage);
  clearStoredDraft(item, storage);
  assert.equal(readStoredDraft(item, storage), null);
  assert.equal(localDrafts.has(draftStorageKey(item)), false);
}

function testPollingDoesNotReplaceActiveReview() {
  assert.equal(refreshDisposition({ activeEditable: true, hasLocalDraft: false, serverCompleted: false }), "defer");
  assert.equal(refreshDisposition({ activeEditable: true, hasLocalDraft: true, serverCompleted: true }), "conflict");
}

function testOpenEntriesComeFirstAndNewestFirst() {
  const items = [
    { ...entry("OPEN-OLD"), enqueued_at: "2026-08-15T12:00:00Z" },
    { ...entry("DONE"), enqueued_at: "2026-08-15T15:00:00Z" },
    { ...entry("OPEN-NEW"), enqueued_at: "2026-08-15T14:00:00Z" },
  ];
  const ordered = orderQueueEntries(items, {
    [entryKey(items[1])]: { status: "completed", completed_at: "2026-08-15T15:30:00Z" },
  });
  assert.deepEqual(ordered.map((item) => item.id), ["OPEN-NEW", "OPEN-OLD", "DONE"]);
}

function testLocalMediaUsesDeclaredSourceRoute() {
  const markup = mediaMarkup({
    ...entry(),
    media: { type: "video", src: "media/cut.mp4", captions: "media/cut.vtt" },
  });
  assert.match(markup, /\/media\/sample\/media\/cut\.mp4/);
  assert.match(markup, /\/media\/sample\/media\/cut\.vtt/);
}

function testLinkedArtifactRemainsDirect() {
  const markup = mediaMarkup({
    ...entry(),
    media: { type: "link", label: "Issue", href: "https://github.com/example/project/issues/1" },
  });
  assert.match(markup, /Open reviewed item/);
  assert.match(markup, /https:\/\/github\.com\/example\/project\/issues\/1/);
}

[
  testDraftRoundTrip,
  testDraftsAreSourceEntryAndVersionScoped,
  testInvalidDraftIsDiscarded,
  testClearRemovesBrowserDraft,
  testPollingDoesNotReplaceActiveReview,
  testOpenEntriesComeFirstAndNewestFirst,
  testLocalMediaUsesDeclaredSourceRoute,
  testLinkedArtifactRemainsDirect,
].forEach((test) => test());

console.log("human review queue client tests: 8 passed");
