// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Music Histories contributors
import {COUNTRIES, countryCode, destinationsFor} from './route.mjs';

const $ = id => document.getElementById(id);
const params = new URLSearchParams(location.search);
const select = $('country');
const names = typeof Intl.DisplayNames === 'function' ? new Intl.DisplayNames(['en'], {type:'region'}) : null;
for (const code of [...COUNTRIES].sort((a,b) => (names?.of(a) || a).localeCompare(names?.of(b) || b))) {
  const option = document.createElement('option');
  option.value = code;
  option.textContent = names?.of(code) || code;
  select.append(option);
}
let saved = '';
try { saved = localStorage.getItem('mh-country') || ''; } catch {}
select.value = countryCode(params.get('country') || saved);

function element(tag, text, cls) {
  const el = document.createElement(tag);
  el.textContent = text;
  if (cls) el.className = cls;
  return el;
}
function link(text, url, cls) {
  const a = element('a', text, cls);
  a.href = url;
  return a;
}
function report(resource, destination) {
  const issue = new URL('https://github.com/blue-ridge-code/music-histories/issues/new');
  issue.searchParams.set('template', 'link-report.yml');
  issue.searchParams.set('title', `Update source for ${resource.id}`);
  issue.searchParams.set('resource_id', resource.id);
  if (destination) issue.searchParams.set('destination_id', destination.id);
  if (select.value) issue.searchParams.set('country', select.value);
  return issue.href;
}
let registry;
function render() {
  $('content').replaceChildren();
  const id = params.get('id');
  if (!id) {
    const ul = element('ul', '', 'catalog');
    for (const resource of registry.resources) {
      const li = element('li','');
      li.append(link(resource.title, `?id=${encodeURIComponent(resource.id)}`), element('small', `${resource.kind === 'film' ? 'Film' : 'Listening'} · ${resource.id}`));
      ul.append(li);
    }
    $('content').append(ul);
    return;
  }
  const resource = registry.resources.find(r => r.id === id);
  if (!resource) {
    $('title').textContent = 'We couldn’t find that link.';
    $('intro').textContent = 'Check the printed link or browse the full directory.';
    $('content').append(link('Browse films and listening', './'));
    return;
  }
  $('title').textContent = resource.title;
  $('intro').textContent = resource.kind === 'film' ? 'Find a viewing source for this film.' : 'Find the recording for your listening assignment.';
  const identity = element('section', '', 'assignment');
  if (resource.preferred_recording) identity.append(element('p', `Preferred recording: ${resource.preferred_recording}`));
  identity.append(element('p', resource.assignment || 'Check your chapter for the exact assignment.'));
  $('content').append(identity);
  if (resource.retired) $('content').append(element('p', 'This assignment has been retired. Its ID is preserved so old workbook links remain identifiable.', 'notice'));
  if (!select.value) $('content').append(element('p', 'Choose a country to include country-specific alternatives. The sources below have no confirmed country coverage.', 'notice'));
  const destinations = destinationsFor(resource, select.value);
  if (!destinations.length) $('content').append(element('p', 'No source is currently listed for this choice. The community can add a suitable publication; check back here later.', 'notice'));
  for (const d of destinations) {
    const card = element('article', '', 'card');
    card.append(element('span', d.availability === 'reported_available' ? 'Availability reported — may change' : 'Availability unverified', 'badge'));
    card.append(element('h2', d.label));
    card.append(element('p', `${d.relationship === 'curated_recording' ? 'Curated selection — see recording notes' : d.relationship === 'same_recording' ? 'Same curated recording' : d.relationship === 'same_film' ? 'Same film' : 'Alternative performance — differs from the preferred recording'} · ${d.access.replaceAll('_',' ')}`, 'meta'));
    if (d.notes) card.append(element('p', d.notes));
    card.append(element('p', d.last_verified_on ? `Last human availability check: ${d.last_verified_on}${d.verified_country ? ` (${d.verified_country})` : ''}` : 'No country-specific human availability check recorded.', 'meta'));
    card.append(link('Open source →', d.url, 'open'));
    const p = element('p',''); p.append(link('Report a problem or suggest a replacement', report(resource,d)));card.append(p);
    $('content').append(card);
  }
  const p = element('p','');p.append(link('Suggest another source',report(resource)),document.createTextNode(' · '),link('Browse all films and listening','./'));$('content').append(p);
}
select.addEventListener('change', () => {
  try { if(select.value) localStorage.setItem('mh-country',select.value); else localStorage.removeItem('mh-country'); } catch {}
  const url = new URL(location.href);
  if (select.value) url.searchParams.set('country',select.value);else url.searchParams.delete('country');
  history.replaceState(null,'',url);
  render();
});
try {
  const response = await fetch('./resources.json');
  if (!response.ok) throw new Error('Registry could not be loaded');
  registry = await response.json();
  render();
} catch {
  $('content').replaceChildren(element('p','The source directory is temporarily unavailable. Please try again later or browse the registry on GitHub.','notice'),link('View registry','https://github.com/blue-ridge-code/music-histories/blob/main/links/resources.json'));
}
