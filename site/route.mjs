// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Music Histories contributors
export const COUNTRIES = 'AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW'.split(' ');

export function countryCode(value) {
  const code = String(value || '').toUpperCase();
  return COUNTRIES.includes(code) ? code : '';
}

export function destinationsFor(resource, country) {
  if (resource.retired) return [];
  const code = countryCode(country);
  return resource.destinations
    .filter(d => !['unavailable', 'retired'].includes(d.availability))
    .filter(d => !code || !d.excluded_countries.includes(code))
    .filter(d => d.countries.includes('*') || (code && d.countries.includes(code)))
    .sort((a, b) => {
      // Country-specific alternatives first; retain explicit curator priority.
      const score = d => code && d.countries.includes(code) ? 0 : 1;
      return score(a) - score(b) || a.priority - b.priority || a.id.localeCompare(b.id);
    });
}
