"""Set approved public URLs locally; this script never publishes anything."""
from pathlib import Path
from urllib.parse import urlsplit
import json,re,html
root=Path(__file__).resolve().parent.parent
config=json.loads((root/'site-config.json').read_text())
origin=config.get('public_origin')
if not origin:
 raise SystemExit('Set the confirmed HTTPS public_origin in site-config.json first.')
p=urlsplit(origin)
if p.scheme!='https' or not p.netloc or p.path not in ('','/') or p.query or p.fragment:
 raise SystemExit('public_origin must be an HTTPS origin without a path, query or fragment.')
origin=origin.rstrip('/')
for file,route in [('index.html','/'),('support/index.html','/support/'),('privacy/index.html','/privacy/')]:
 path=root/file;s=path.read_text();url=html.escape(origin+route,quote=True)
 block=f'<!-- PUBLIC_ORIGIN_START --><link rel="canonical" href="{url}"><meta property="og:url" content="{url}"><!-- PUBLIC_ORIGIN_END -->'
 s=re.sub(r'<!-- PUBLIC_ORIGIN_START -->.*?<!-- PUBLIC_ORIGIN_END -->',lambda _:block,s,flags=re.S)
 s=re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*(")',lambda m:m[1]+html.escape(origin+'/assets/social-preview.png',quote=True)+m[2],s)
 path.write_text(s)
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+html.escape(origin+r)+'</loc></url>\n' for r in ['/','/support/','/privacy/'])+'</urlset>\n')
print('Local metadata configured. Nothing was published.')
