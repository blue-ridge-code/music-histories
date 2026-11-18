// SPDX-License-Identifier: MIT
import test from 'node:test';
import assert from 'node:assert/strict';
import {countryCode, destinationsFor} from '../../site/route.mjs';

const d = (id,countries=['*'],extra={}) => ({id,countries,excluded_countries:[],availability:'unknown',priority:10,...extra});
const r = (...destinations) => ({retired:false,destinations});
test('country choice accepts valid codes, never infers country from language', () => {
  assert.equal(countryCode('gb'),'GB');assert.equal(countryCode('en-US'),'');assert.equal(countryCode('ZZ'),'');
});
test('country-specific source outranks unspecified fallback', () => {
  assert.deepEqual(destinationsFor(r(d('fallback'),d('us',['US'])), 'US').map(x=>x.id),['us','fallback']);
});
test('country boundaries and exclusions are respected', () => {
  assert.deepEqual(destinationsFor(r(d('de',['DE']),d('fallback',['*'],{excluded_countries:['US']})),'US'),[]);
});
test('without country only unspecified sources appear', () => {
  assert.deepEqual(destinationsFor(r(d('de',['DE']),d('fallback')),'').map(x=>x.id),['fallback']);
});
test('dead and retired destinations are hidden without deleting IDs', () => {
  assert.deepEqual(destinationsFor(r(d('dead',['*'],{availability:'unavailable'}),d('old',['*'],{availability:'retired'})),'US'),[]);
});
test('retired assignments retain identity but have no active routes', () => {
  assert.deepEqual(destinationsFor({...r(d('live')),retired:true},'US'),[]);
});
test('unknown availability remains visible without claiming it is playable', () => {
  assert.equal(destinationsFor(r(d('unknown')),'US')[0].availability,'unknown');
});
test('curator priority sorts alternatives deterministically without mutating registry', () => {
  const resource=r(d('second',['US'],{priority:20}),d('first',['US'],{priority:1}));
  assert.deepEqual(destinationsFor(resource,'US').map(x=>x.id),['first','second']);
  assert.equal(resource.destinations[0].id,'second');
});
test('a missing destination produces an empty result', () => assert.deepEqual(destinationsFor(r(),'US'),[]));
