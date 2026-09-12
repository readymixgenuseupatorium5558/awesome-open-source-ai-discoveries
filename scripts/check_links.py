"""Check catalog source URLs. Inconclusive network responses are never reported as success."""
import concurrent.futures
import json
import pathlib
import sys
import urllib.error
import urllib.request

root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
urls=sorted({u for e in data['entries'] for u in [e['url'],*e['source_urls'],*[e[k] for k in ['demo_url','test_evidence_url'] if e.get(k)]]})

def check(url):
    request=urllib.request.Request(url,headers={'User-Agent':'QuicqDev-Catalog-LinkCheck/1.0','Range':'bytes=0-1023'})
    try:
        with urllib.request.urlopen(request,timeout=30) as response:
            return {'url':url,'status':response.status,'result':'reachable','resolved_url':response.url}
    except urllib.error.HTTPError as error:
        return {'url':url,'status':error.code,'result':'broken' if error.code in [404,410] else 'inconclusive'}
    except Exception as error:
        return {'url':url,'status':None,'result':'inconclusive','error':str(error)}

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(check,urls))
print(json.dumps(results,indent=2))
broken=sum(r['result']=='broken' for r in results)
uncertain=sum(r['result']=='inconclusive' for r in results)
print(f'{len(results)} URLs: {broken} broken, {uncertain} inconclusive.')
sys.exit(1 if broken else 2 if uncertain else 0)
