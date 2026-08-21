#!/usr/bin/env python3
"""Build the static site.

Edit content in src/*.body.html and styling in src/site.css, then run:

    python3 build.py

Each page is written to the repo root as a self-contained HTML file
(the stylesheet is inlined), so GitHub Pages needs nothing else.
"""

from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"

PAGES = {
    "index.html":    ("Bar Oryan | Earthquake cycles, geodesy, and hazard", "home"),
    "research.html": ("Research | Bar Oryan", "research"),
    "join.html":     ("Join the group | Bar Oryan", "join"),
    "teaching.html": ("Teaching | Bar Oryan", "teaching"),
    "projects.html": ("DIY projects | Bar Oryan", "diy"),
}

NAV = [
    ("index.html", "Home", "home"),
    ("research.html", "Research", "research"),
    ("join.html", "Join the group", "join"),
    ("teaching.html", "Teaching", "teaching"),
    ("projects.html", "DIY", "diy"),
    ("https://couplingcloud.ucsd.edu", "Coupling Cloud", "cloud"),
    ("CV/CV_BarOryan.pdf", "CV", "cv"),
]

DESC = ("Bar Oryan is an Assistant Professor in Earth and Environmental Sciences at "
        "Lehigh University, studying subduction earthquake cycles with geodesy, "
        "numerical simulations, and geomorphology.")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Bar Oryan">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><clipPath id='t'><rect width='32' height='32' rx='7'/></clipPath><clipPath id='h'><path d='M-4 -4 L36 -4 L36 22.50 L-4 9.50 Z'/></clipPath><clipPath id='f'><path d='M-4 9.50 L36 22.50 L36 36 L-4 36 Z'/></clipPath></defs><g clip-path='url(%23t)'><rect width='32' height='32' fill='%23241a33'/><g clip-path='url(%23f)'><path d='M622.0 -191.0Q622.0 -103.0 560.5 -51.5Q499.0 0.0 389.0 0.0H62.0V-702.0H378.0Q485.0 -702.0 545.5 -653.0Q606.0 -604.0 606.0 -520.0Q606.0 -458.0 573.5 -417.0Q541.0 -376.0 487.0 -360.0Q548.0 -347.0 585.0 -299.5Q622.0 -252.0 622.0 -191.0ZM233.0 -418.0H345.0Q387.0 -418.0 409.5 -436.5Q432.0 -455.0 432.0 -491.0Q432.0 -527.0 409.5 -546.0Q387.0 -565.0 345.0 -565.0H233.0ZM449.0 -214.0Q449.0 -251.0 424.5 -272.0Q400.0 -293.0 357.0 -293.0H233.0V-138.0H359.0Q402.0 -138.0 425.5 -157.5Q449.0 -177.0 449.0 -214.0Z' transform='translate(7.29 25.62) scale(0.026429)' fill='%23f8f5f0'/></g><g clip-path='url(%23h)'><path d='M622.0 -191.0Q622.0 -103.0 560.5 -51.5Q499.0 0.0 389.0 0.0H62.0V-702.0H378.0Q485.0 -702.0 545.5 -653.0Q606.0 -604.0 606.0 -520.0Q606.0 -458.0 573.5 -417.0Q541.0 -376.0 487.0 -360.0Q548.0 -347.0 585.0 -299.5Q622.0 -252.0 622.0 -191.0ZM233.0 -418.0H345.0Q387.0 -418.0 409.5 -436.5Q432.0 -455.0 432.0 -491.0Q432.0 -527.0 409.5 -546.0Q387.0 -565.0 345.0 -565.0H233.0ZM449.0 -214.0Q449.0 -251.0 424.5 -272.0Q400.0 -293.0 357.0 -293.0H233.0V-138.0H359.0Q402.0 -138.0 425.5 -157.5Q449.0 -177.0 449.0 -214.0Z' transform='translate(4.06 24.57) scale(0.026429)' fill='%23f8f5f0'/></g><path d='M4.09 12.13 L27.91 19.87' fill='none' stroke='%23e6ab33' stroke-width='1.9' stroke-linecap='round'/></g></svg>">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,400..700&family=Newsreader:opsz,wght@6..72,300..600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="index.html">Bar&nbsp;Oryan</a>
    <nav aria-label="Main">
{nav}
    </nav>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>Contact</h4>
        <a href="mailto:bar.oryan@lehigh.edu">bar.oryan@lehigh.edu</a><br>
        STEPS 576<br>
        1 West Packer Avenue<br>
        Bethlehem, PA 18015
      </div>
      <div>
        <h4>Elsewhere</h4>
        <a href="https://scholar.google.com/citations?user=iiuYSY8AAAAJ&amp;hl=en">Google Scholar</a><br>
        <a href="https://github.com/baroryan">GitHub</a><br>
        <a href="https://couplingcloud.ucsd.edu">Coupling Cloud</a><br>
        <a href="CV/CV_BarOryan.pdf">Curriculum vitae</a>
      </div>
      <div>
        <h4>Department</h4>
        <a href="https://ees.cas.lehigh.edu/">Earth &amp; Environmental Sciences</a><br>
        <a href="https://ees.cas.lehigh.edu/graduate/admissions">Graduate admissions</a><br>
        <a href="https://www.lehigh.edu">Lehigh University</a>
      </div>
    </div>
    <p class="colophon">
      <span>&copy; 2026 Bar Oryan &middot; Bethlehem, Pennsylvania</span>
      <span class="updated">Webpage last updated Aug 2026</span>
    </p>
  </div>
</footer>
</body>
</html>
"""


def build():
    css = (SRC / "site.css").read_text()
    for filename, (title, key) in PAGES.items():
        nav = "\n".join(
            '      <a href="{href}"{cur}>{label}</a>'.format(
                href=href, label=label,
                cur=' aria-current="page"' if slug == key else "")
            for href, label, slug in NAV
        )
        body = (SRC / filename.replace(".html", ".body.html")).read_text()
        if "{{COPALIS}}" in body:          # inline the photo so the page is self-contained
            import base64
            data = base64.b64encode((ROOT / "cascadia" / "copalis.jpg").read_bytes()).decode()
            body = body.replace("{{COPALIS}}", "data:image/jpeg;base64," + data)
        page = HEAD.format(title=title, desc=DESC, css=css, nav=nav) + body + FOOTER
        (ROOT / filename).write_text(page)
        print("wrote", filename)


REDIRECTS = {
    "about_me.html": "index.html",
    "DIY.html": "projects.html",
    "DIYFull.html": "projects.html",
}

REDIRECT_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>Moved</title>
</head>
<body><p>This page has moved. <a href="{target}">Continue &rarr;</a></p></body>
</html>
"""


def redirects():
    """Keep old URLs alive — they are linked from elsewhere."""
    for old, target in REDIRECTS.items():
        (ROOT / old).write_text(REDIRECT_TMPL.format(target=target))
        print("wrote", old, "->", target)


if __name__ == "__main__":
    build()
    redirects()
