#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Music Histories contributors
"""Report bounded HTTP observations; never claim playback, rights, or geo-availability."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.parse import urlsplit
from urllib.request import Request,build_opener,HTTPRedirectHandler

ROOT=Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--limit',type=int,default=0)
    p.add_argument('--output',default='/tmp/music-histories-link-health.json')
    args=p.parse_args()
    data=json.loads((ROOT/'links/resources.json').read_text())
    allowed=set(json.loads((ROOT/'links/config.json').read_text())['http_check_hosts'])
    class SafeRedirects(HTTPRedirectHandler):
        def redirect_request(self,req,fp,code,msg,headers,newurl):
            if urlsplit(newurl).scheme!='https' or urlsplit(newurl).hostname not in allowed:
                raise URLError('Redirect host requires maintainer review')
            return super().redirect_request(req,fp,code,msg,headers,newurl)
    targets=[(r['id'],d) for r in data['resources'] for d in r['destinations'] if d['availability']!='retired']
    if args.limit:targets=targets[:args.limit]
    def probe(item):
        rid,d=item
        result={'resource_id':rid,'destination_id':d['id'],'observed_at':datetime.now(timezone.utc).isoformat(),'http_status':None,'observation':'not_checked'}
        if urlsplit(d['url']).scheme!='https' or urlsplit(d['url']).hostname not in allowed:
            result['observation']='host_not_enabled_for_checks';return result
        try:
            request=Request(d['url'],headers={'User-Agent':'MusicHistories-LinkHealth/1.0'})
            with build_opener(SafeRedirects()).open(request,timeout=15) as response:
                response.read(65536)
                result.update(http_status=response.status,observation='http_reachable_playback_unverified')
        except HTTPError as e:
            result.update(http_status=e.code,observation='http_error_requires_review')
        except (URLError,TimeoutError,OSError):result['observation']='network_error_inconclusive'
        return result
    with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(probe,targets))
    output={'scope':'HTTP from this runner only; not a playback or regional availability test','observations':results}
    Path(args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(f'Wrote {len(results)} observations to {args.output}; registry unchanged')


if __name__=='__main__':main()
