# Wraps each page body in pages/ with the shared header and footer. Run: python3 build.py
# shortcut: string templates, no generator. Upgrade to a static site generator only if pages need shared lists.
import pathlib, re
ROOT = pathlib.Path(__file__).parent
NAV = [('', 'Apps and support'), ('privacy/', 'Privacy'), ('security/', 'Security')]
TPL = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<header>
  <a class="name" href="{up}">Obsidian Ridge Labs</a>
  <nav>{nav}</nav>
</header>
<main>
{body}
</main>
<footer>
  <p>Obsidian Ridge Labs, Las Vegas, Nevada, USA. Support: <a href="mailto:support@obsidianridgelabs.com">support@obsidianridgelabs.com</a>.
  Atlassian, Jira and Confluence are trademarks of Atlassian. Our apps are not made or endorsed by Atlassian.</p>
</footer>
</body>
</html>
'''
for src in sorted((ROOT / 'pages').glob('*.html')):
    text = src.read_text()
    meta = dict(re.findall(r'^<!-- (\w+): (.*?) -->$', text, re.M))
    body = re.sub(r'^<!-- \w+: .*? -->\n', '', text, flags=re.M).strip()
    out = meta['path']  # '' for the home page, 'privacy/' and so on
    up = '../' * out.count('/')
    nav = ''.join(f'<a href="{up}{p}"{" aria-current=\"page\"" if p == out else ""}>{n}</a>' for p, n in NAV)
    dest = ROOT / out / 'index.html'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(TPL.format(title=meta['title'], desc=meta['desc'], up=up, nav=nav, body=body))
    assert '—' not in dest.read_text() and '–' not in dest.read_text(), f'dash in {dest}'
    print('wrote', dest.relative_to(ROOT))
