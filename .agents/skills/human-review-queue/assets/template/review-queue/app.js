const LEGACY_KEY = "human-review-queue-legacy-v1";
const DRAFT_KEY_PREFIX = "human-review-queue-draft-v1:";

let csrfToken = "";
let entries = [];
let responses = {};
let actions = {};
let currentIndex = 0;
let notice = "";
let reviewer = {};
let reviewers = [];
let identityMode = "single_local";
const localDrafts = new Map();

const esc = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

function sessionStore() {
  if (typeof window === "undefined") return null;
  try {
    return window.sessionStorage;
  } catch {
    return null;
  }
}

function draftStorageKey(entry) {
  return `${DRAFT_KEY_PREFIX}${encodeURIComponent(`${entryKey(entry)}|${entry.version}`)}`;
}

function entryKey(entry) {
  return entry.entry_key || `${entry.source_id || "current"}:${entry.id}`;
}

function reviewerQuery() {
  if (typeof window === "undefined") return "";
  const id = new URLSearchParams(window.location.search).get("reviewer");
  return id ? `reviewer=${encodeURIComponent(id)}` : "";
}

function apiUrl(path) {
  const query = reviewerQuery();
  return query ? `${path}${path.includes("?") ? "&" : "?"}${query}` : path;
}

function readStoredDraft(entry, storage = sessionStore()) {
  if (!storage) return null;
  try {
    const raw = storage.getItem(draftStorageKey(entry));
    if (!raw) return null;
    const draft = JSON.parse(raw);
    if (
      draft?.schema_version !== 1
      || draft.entry_key !== entryKey(entry)
      || draft.reviewed_version !== entry.version
      || typeof draft.choice !== "string"
      || typeof draft.notes !== "string"
    ) {
      storage.removeItem(draftStorageKey(entry));
      return null;
    }
    return draft;
  } catch {
    storage.removeItem(draftStorageKey(entry));
    return null;
  }
}

function localDraftFor(entry) {
  const key = draftStorageKey(entry);
  if (localDrafts.has(key)) return localDrafts.get(key);
  const draft = readStoredDraft(entry);
  if (draft) localDrafts.set(key, draft);
  return draft;
}

function writeStoredDraft(entry, choice, notes, storage = sessionStore(), updatedAt = new Date().toISOString()) {
  const draft = {
    schema_version: 1,
    entry_key: entryKey(entry),
    entry_id: entry.id,
    source_id: entry.source_id,
    reviewed_version: entry.version,
    choice,
    notes,
    status: "pending",
    updated_at: updatedAt,
  };
  localDrafts.set(draftStorageKey(entry), draft);
  storage?.setItem(draftStorageKey(entry), JSON.stringify(draft));
  return draft;
}

function clearStoredDraft(entry, storage = sessionStore()) {
  localDrafts.delete(draftStorageKey(entry));
  storage?.removeItem(draftStorageKey(entry));
}

async function api(path, options = {}) {
  const response = await fetch(apiUrl(path), {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(csrfToken ? { "X-Review-Queue-Token": csrfToken } : {}),
      ...(options.headers || {}),
    },
  });
  const body = await response.json();
  if (!response.ok) throw new Error(body.error || `Request failed: ${response.status}`);
  return body;
}

function applyState(state) {
  const currentEntryId = entries[currentIndex]?.entry_key;
  responses = state.responses || {};
  actions = state.actions || {};
  reviewer = state.reviewer || reviewer;
  reviewers = state.reviewers || reviewers;
  identityMode = state.identity_mode || identityMode;
  entries = orderQueueEntries(state.entries || entries, responses);
  const preservedIndex = currentEntryId
    ? entries.findIndex((entry) => entry.entry_key === currentEntryId)
    : -1;
  currentIndex = preservedIndex >= 0
    ? preservedIndex
    : Math.min(currentIndex, Math.max(0, entries.length - 1));
}

async function loadState() {
  const body = await api("/api/review-queue");
  csrfToken = body.csrf_token;
  applyState(body);
  await importLegacyState();
  const conflict = entries.find((entry) => serverResponseFor(entry).status === "completed" && localDraftFor(entry));
  if (conflict) {
    notice = `${conflict.id} was completed after a local draft was saved. The recorded decision is shown; the local draft remains in this browser session.`;
  }
}

async function importLegacyState() {
  const raw = sessionStorage.getItem(LEGACY_KEY);
  if (!raw || sessionStorage.getItem(`${LEGACY_KEY}-imported`)) return;
  const legacy = JSON.parse(raw);
  const completed = Object.values(legacy.responses || {}).filter((item) => item.status === "completed").length;
  if (!completed) return;
  const body = await api("/api/review-queue/import", { method: "POST", body: JSON.stringify(legacy) });
  applyState(body.state);
  sessionStorage.setItem(`${LEGACY_KEY}-imported`, new Date().toISOString());
  notice = `${completed} earlier response${completed === 1 ? "" : "s"} imported and recorded.`;
}

function serverResponseFor(entry) {
  return responses[entryKey(entry)] || {};
}

function responseFor(entry) {
  const serverResponse = serverResponseFor(entry);
  if (serverResponse.status === "completed") return serverResponse;
  return localDraftFor(entry) || serverResponse;
}

function statusFor(entry) {
  const response = responseFor(entry);
  if (response.status === "completed") return "completed";
  if (response.choice || response.notes) return "draft";
  return "pending";
}

function queueTimestamp(entry, response, completed) {
  const candidates = completed
    ? [response.completed_at, response.received_at, entry.enqueued_at, entry.created_at]
    : [entry.enqueued_at, entry.created_at];
  for (const candidate of candidates) {
    const timestamp = Date.parse(candidate || "");
    if (Number.isFinite(timestamp)) return timestamp;
  }
  return null;
}

function orderQueueEntries(sourceEntries, responseMap = {}) {
  return sourceEntries.map((entry, sourceIndex) => {
    const response = responseMap[entryKey(entry)] || {};
    const completed = response.status === "completed";
    return {
      entry,
      sourceIndex,
      completed,
      timestamp: queueTimestamp(entry, response, completed),
    };
  }).sort((left, right) => {
    if (left.completed !== right.completed) return left.completed ? 1 : -1;
    if (left.timestamp !== null && right.timestamp !== null && left.timestamp !== right.timestamp) {
      return right.timestamp - left.timestamp;
    }
    if (left.timestamp !== null && right.timestamp === null) return -1;
    if (left.timestamp === null && right.timestamp !== null) return 1;
    return right.sourceIndex - left.sourceIndex;
  }).map(({ entry }) => entry);
}

function actionFor(entry) {
  return actions[entryKey(entry)] || null;
}

function actionLabel(entry) {
  const action = actionFor(entry);
  if (!action) return "Awaiting response";
  if (action.status === "queued") return "Agent work queued";
  if (action.status === "recorded") return "Decision recorded · no dispatch needed";
  if (action.last_error) return "Recorded · agent handoff retrying";
  return "Recorded · agent handoff pending";
}

function queueList() {
  const indexed = entries.map((entry, index) => ({ entry, index }));
  const open = indexed.filter(({ entry }) => statusFor(entry) !== "completed");
  const completed = indexed.filter(({ entry }) => statusFor(entry) === "completed");
  const openRows = open.map(({ entry, index }) => `
    <button class="queue-entry ${index === currentIndex ? "current" : ""}" data-go="${index}">
      <span class="status-dot ${statusFor(entry)}" aria-hidden="true"></span>
      <span class="queue-entry-details"><strong>${esc(entry.title)}</strong><small>${esc(entry.source_name)} · ${esc(entry.id)} · ${esc(statusFor(entry))}</small></span>
    </button>`).join("");
  const completedRows = completed.map(({ entry, index }) => `
    <button class="queue-entry completed-row ${index === currentIndex ? "current" : ""}" data-go="${index}" title="${esc(entry.title)}">
      <span class="status-dot completed" aria-hidden="true"></span>
      <span class="queue-entry-title">${esc(entry.title)}</span>
      <span class="completion-label">Complete</span>
    </button>`).join("");
  return `<nav class="queue-list" aria-label="Review queue">
    <section class="queue-section" aria-labelledby="open-decisions-heading">
      <h2 class="queue-section-heading" id="open-decisions-heading"><span>Open decisions</span><strong>${open.length}</strong></h2>
      ${openRows || '<p class="queue-section-empty">No open decisions</p>'}
    </section>
    <section class="queue-section completed-section" aria-labelledby="completed-decisions-heading">
      <h2 class="queue-section-heading" id="completed-decisions-heading"><span>Completed</span><strong>${completed.length}</strong></h2>
      ${completedRows || '<p class="queue-section-empty">No completed decisions</p>'}
    </section>
  </nav>`;
}

function mediaMarkup(entry) {
  const media = entry.media || { type: "none" };
  const localMedia = (value) => `/media/${encodeURIComponent(entry.source_id)}/${String(value).replace(/^\/+/, "")}`;
  if (media.type === "video") {
    const captions = media.captions
      ? `<track kind="captions" src="${esc(localMedia(media.captions))}" srclang="en" label="English" default />`
      : "";
    return `<video controls preload="metadata" src="${esc(localMedia(media.src))}">${captions}</video>`;
  }
  if (media.type === "audio") return `<div class="audio-stage"><div class="wave" aria-hidden="true"></div><audio controls preload="metadata" src="${esc(localMedia(media.src))}"></audio></div>`;
  if (media.type === "image") return `<img class="review-image" src="${esc(localMedia(media.src))}" alt="Visual candidate under review" />`;
  if (media.type === "link") {
    return `<div class="artifact-card linked-artifact"><span>Reviewed item</span><strong>${esc(media.label || entry.version)}</strong><p>This item cannot be shown inside the queue.</p><a href="${esc(media.href)}" target="_blank" rel="noreferrer">Open reviewed item</a></div>`;
  }
  return `<div class="artifact-card"><span>Interface review</span><strong>${esc(entry.version)}</strong><p>The page itself is the reviewed artifact.</p></div>`;
}

function reviewPath(entry) {
  const history = entry.routing_state?.history || [];
  const prior = history.length
    ? `<div class="criteria"><p class="eyebrow">Prior route decisions</p><ul>${history.map((item) => `<li><strong>${esc(item.reviewer_id)}</strong> · ${esc(item.stage_id)} · ${esc(item.choice_label)}${item.notes ? ` — ${esc(item.notes)}` : ""}</li>`).join("")}</ul></div>`
    : "";
  return `<section class="review-path"><p class="eyebrow">Review path</p><h2>Do this before deciding</h2><ol>${entry.steps.map((step) => `<li>${esc(step)}</li>`).join("")}</ol><div class="criteria"><p class="eyebrow">Success looks like</p><ul>${entry.criteria.map((criterion) => `<li>${esc(criterion)}</li>`).join("")}</ul></div>${prior}</section>`;
}

function decisionForm(entry) {
  const response = responseFor(entry);
  const selected = response.choice || "";
  const completed = response.status === "completed";
  return `<form id="decision-form" data-id="${esc(entry.id)}" data-source="${esc(entry.source_id)}" data-key="${esc(entryKey(entry))}">
    <p class="eyebrow">Decision</p>
    <h2>${esc(entry.question)}</h2>
    <div class="recommendation"><strong>Recommendation</strong><p>${esc(entry.recommendation)}</p></div>
    <fieldset ${completed ? "disabled" : ""}>
      <legend class="sr-only">Choose one response</legend>
      ${entry.options.map((option) => `<label class="option ${selected === option.value ? "selected" : ""}"><input type="radio" name="choice" value="${esc(option.value)}" ${selected === option.value ? "checked" : ""} /><span><strong>${esc(option.label)}${option.recommended ? " <em>(Recommended)</em>" : ""}</strong><small>${esc(option.effect)}</small></span></label>`).join("")}
      <label class="option ${selected === "other" ? "selected" : ""}"><input type="radio" name="choice" value="other" ${selected === "other" ? "checked" : ""} /><span><strong>Other</strong><small>Describe a different disposition or a combination.</small></span></label>
    </fieldset>
    <label class="notes"><span>${selected === "other" ? "Other response (required)" : "Notes or timecodes (optional)"}</span><textarea name="notes" rows="4" ${completed ? "disabled" : ""}>${esc(response.notes || "")}</textarea></label>
    ${completed ? `<div class="recorded"><strong>Response recorded</strong><span>${esc(actionLabel(entry))}</span>${actionFor(entry)?.dispatch_issue_url ? `<a href="${esc(actionFor(entry).dispatch_issue_url)}">Open agent Issue</a>` : ""}</div>` : `<div class="form-actions"><button type="button" class="secondary" data-draft>Save draft</button><button type="submit" class="primary">Complete decision</button></div>`}
    <p class="record-note">Completing this form writes an append-only decision record. A configured adapter starts only the declared follow-up and keeps the entry boundary.</p>
  </form>`;
}

function reviewerNavigation() {
  if (identityMode !== "local_switcher") return `<span class="service-state">${esc(reviewer.display_name || reviewer.id || "Reviewer")} · automatic handoff</span>`;
  const links = reviewers.map((item) => `<a href="/review-queue/?reviewer=${encodeURIComponent(item.id)}" ${item.id === reviewer.id ? 'aria-current="page"' : ""}>${esc(item.display_name)}</a>`).join("");
  return `<nav class="reviewer-links" aria-label="Local reviewer switcher">${links}</nav>`;
}

function render() {
  if (!entries.length) {
    document.querySelector("#app").innerHTML = `<main class="empty"><h1>No review entries</h1><p>An agent can add the next bounded handoff with the review-queue CLI.</p></main>`;
    return;
  }
  const entry = entries[currentIndex];
  const complete = entries.filter((item) => statusFor(item) === "completed").length;
  document.querySelector("#app").innerHTML = `
    <header><a href="/review-queue/${reviewerQuery() ? `?${reviewerQuery()}` : ""}" class="brand">HUMAN <span>Review queue</span></a><div><strong>${complete}/${entries.length}</strong> completed</div>${reviewerNavigation()}</header>
    ${notice ? `<div class="notice" role="status">${esc(notice)}</div>` : ""}
    <main class="workspace">
      <aside class="queue-column"><p class="eyebrow">All decisions</p><h1>Review queue</h1>${queueList()}</aside>
      <section class="review-column"><div class="item-heading"><div><p class="eyebrow">${esc(entry.kind)} · Type ${esc(entry.touchpoint)} · ${esc(entry.source_name)}</p><h1>${esc(entry.title)}</h1><p>${esc(entry.project)} · ${esc(entry.issue)} · ${esc(entry.due)}</p></div><span class="status-pill ${statusFor(entry)}">${esc(statusFor(entry))}</span></div><div class="media-panel"><div class="media-label"><strong>${esc(entry.media.label)}</strong><span>${esc(entry.version)}</span></div>${mediaMarkup(entry)}</div>${reviewPath(entry)}<div class="item-nav"><button class="secondary" data-prev ${currentIndex === 0 ? "disabled" : ""}>← Previous</button><span>${currentIndex + 1} of ${entries.length}</span><button class="secondary" data-next ${currentIndex === entries.length - 1 ? "disabled" : ""}>Next →</button></div></section>
      <aside class="decision-column">${decisionForm(entry)}</aside>
    </main>`;
  bindEvents();
}

function go(index) {
  currentIndex = Math.max(0, Math.min(entries.length - 1, index));
  render();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function entryForForm(form) {
  return entries.find((entry) => entryKey(entry) === form?.dataset.key) || null;
}

function formValues(form) {
  const data = new FormData(form);
  return {
    choice: String(data.get("choice") || ""),
    notes: String(data.get("notes") || ""),
  };
}

function updateDraftPresentation(form, choice) {
  form.querySelectorAll(".option").forEach((label) => {
    const input = label.querySelector("input[name=choice]");
    label.classList.toggle("selected", Boolean(input?.checked));
  });
  const notesLabel = form.querySelector(".notes span");
  if (notesLabel) notesLabel.textContent = choice === "other" ? "Other response (required)" : "Notes or timecodes (optional)";
  const statusPill = document.querySelector(".status-pill");
  if (statusPill) {
    statusPill.classList.remove("pending", "completed");
    statusPill.classList.add("draft");
    statusPill.textContent = "draft";
  }
  const queueStatus = document.querySelector(`.queue-entry[data-go="${currentIndex}"] small`);
  const entry = entryForForm(form);
  if (queueStatus && entry) queueStatus.textContent = `${entry.id} · draft`;
}

function persistFormDraft(form) {
  const entry = entryForForm(form);
  if (!entry || serverResponseFor(entry).status === "completed") return null;
  const { choice, notes } = formValues(form);
  const draft = writeStoredDraft(entry, choice, notes);
  updateDraftPresentation(form, choice);
  return draft;
}

function bindEvents() {
  document.querySelectorAll("[data-go]").forEach((button) => button.addEventListener("click", () => go(Number(button.dataset.go))));
  document.querySelector("[data-prev]")?.addEventListener("click", () => go(currentIndex - 1));
  document.querySelector("[data-next]")?.addEventListener("click", () => go(currentIndex + 1));
  document.querySelectorAll("input[name=choice]").forEach((input) => input.addEventListener("change", () => {
    persistFormDraft(input.closest("form"));
  }));
  document.querySelector("#decision-form textarea[name=notes]")?.addEventListener("input", (event) => {
    persistFormDraft(event.target.closest("form"));
  });
  document.querySelector("[data-draft]")?.addEventListener("click", async (event) => {
    await submitForm(event.target.closest("form"), "pending");
  });
  document.querySelector("#decision-form")?.addEventListener("submit", async (event) => {
    event.preventDefault();
    await submitForm(event.target, "completed");
  });
}

async function submitForm(form, status) {
  const data = new FormData(form);
  const choice = String(data.get("choice") || "");
  const notes = String(data.get("notes") || "").trim();
  if (status === "completed" && !choice) return alert("Choose one response before completing this entry.");
  if (choice === "other" && !notes) return alert("Describe the Other response before completing this entry.");
  const entry = entryForForm(form);
  if (entry) writeStoredDraft(entry, choice, String(data.get("notes") || ""));
  try {
    const body = await api("/api/review-queue/respond", {
      method: "POST",
      body: JSON.stringify({ source_id: form.dataset.source, entry_id: form.dataset.id, choice, notes, status, completed_at: status === "completed" ? new Date().toISOString() : null }),
    });
    applyState(body.state);
    if (entry) clearStoredDraft(entry);
    notice = status === "completed" ? "Decision recorded. Agent handoff will continue automatically." : "Draft saved locally.";
    const nextPending = entries.findIndex((entry) => statusFor(entry) !== "completed");
    if (status === "completed" && nextPending >= 0) currentIndex = nextPending;
    render();
  } catch (error) {
    notice = `Could not save: ${error.message}`;
    render();
  }
}

function refreshDisposition({ activeEditable, hasLocalDraft, serverCompleted }) {
  if (serverCompleted && hasLocalDraft) return "conflict";
  if (serverCompleted) return "render";
  if (activeEditable) return "defer";
  return "render";
}

function showRefreshConflict(entry) {
  notice = `${entry.id} was completed in another tab or process. Your local draft is preserved in this browser session, but the recorded decision now controls.`;
  let banner = document.querySelector(".notice");
  if (!banner) {
    document.querySelector("header")?.insertAdjacentHTML("afterend", '<div class="notice" role="status"></div>');
    banner = document.querySelector(".notice");
  }
  if (banner) banner.textContent = notice;
  document.querySelectorAll("#decision-form input, #decision-form textarea, #decision-form button").forEach((control) => {
    control.disabled = true;
  });
}

function markPassiveRefresh() {
  const serviceState = document.querySelector(".service-state");
  if (serviceState) serviceState.textContent = "Local · synced without interrupting review";
}

async function refresh() {
  try {
    const visibleEntryId = entries[currentIndex]?.entry_key;
    const visibleEntry = entries[currentIndex];
    const activeForm = document.querySelector("#decision-form");
    const activeEditable = Boolean(activeForm && !activeForm.querySelector("fieldset")?.disabled);
    const hasLocalDraft = Boolean(visibleEntry && localDraftFor(visibleEntry));
    const body = await api("/api/review-queue");
    csrfToken = body.csrf_token;
    applyState(body);
    if (notice.startsWith("Could not save:") && responses[visibleEntryId]?.status === "completed") {
      notice = "Decision is recorded. The earlier save error is resolved.";
    }
    const updatedEntry = entries.find((entry) => entry.entry_key === visibleEntryId);
    const disposition = refreshDisposition({
      activeEditable,
      hasLocalDraft,
      serverCompleted: Boolean(updatedEntry && serverResponseFor(updatedEntry).status === "completed"),
    });
    if (disposition === "conflict") {
      showRefreshConflict(updatedEntry);
    } else if (disposition === "defer") {
      markPassiveRefresh();
    } else {
      render();
    }
  } catch {
    // Keep the last visible state. The next scheduled refresh retries.
  }
}

function scheduleRefresh() {
  const actionPending = Object.values(actions).some((action) => action.status === "pending");
  const delay = actionPending ? 10000 : 60000;
  setTimeout(async () => {
    await refresh();
    scheduleRefresh();
  }, delay);
}

const clientTestApi = {
  draftStorageKey,
  readStoredDraft,
  writeStoredDraft,
  clearStoredDraft,
  refreshDisposition,
  orderQueueEntries,
  mediaMarkup,
  entryKey,
  localDrafts,
};

if (typeof module !== "undefined" && module.exports) module.exports = clientTestApi;

if (typeof document !== "undefined") {
  loadState().then(() => {
    render();
    scheduleRefresh();
  }).catch((error) => {
    document.querySelector("#app").innerHTML = `<main class="empty"><h1>Review queue unavailable</h1><p>${esc(error.message)}</p><p>Run <code>&amp; .\\scripts\\start-human-review-queue.ps1 -NoDispatch</code>.</p></main>`;
  });
}
