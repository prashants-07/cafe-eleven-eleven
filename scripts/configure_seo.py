from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape
import sys,re
base=sys.argv[1].rstrip('/') if len(sys.argv)>1 else ''
if urlparse(base).scheme not in ('https','http') or not urlparse(base).netloc:raise SystemExit('Usage: python scripts/configure_seo.py https://ACCOUNT.github.io/REPOSITORY')
r=Path(__file__).resolve().parent.parent
pages=['index','about','menu','gallery','order','contact']
for page in pages:
 p=r/(page+'.html');s=p.read_text(encoding='utf-8')
 s=re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>','',s)
 s=re.sub(r'<meta property="og:image"[^>]*>',f'<meta property="og:image" content="{escape(base)}/assets/images/hero/cafe.jpg">',s)
 s=s.replace('</head>',f'<link rel="canonical" href="{escape(base)}/{page}.html"><meta property="og:url" content="{escape(base)}/{page}.html"></head>')
 p.write_text(s,encoding='utf-8')
(r/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{escape(base)}/{p}.html</loc></url>' for p in pages)+'</urlset>',encoding='utf-8')
(r/'robots.txt').write_text('User-agent: *'+chr(10)+'Allow: /'+chr(10)+'Sitemap: '+base+'/sitemap.xml'+chr(10),encoding='utf-8')
print('Configured SEO for',base)
