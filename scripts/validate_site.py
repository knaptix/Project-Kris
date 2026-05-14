from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = ROOT / "index.html"
styles = ROOT / "styles.css"
app = ROOT / "app.js"

html = index.read_text(encoding="utf-8")
css = styles.read_text(encoding="utf-8")
js = app.read_text(encoding="utf-8")

HTMLParser().feed(html)

required_html = [
    "The Football",
    "Media Engine",
    "Complete 60-Day Growth Strategy",
    "styles.css",
    "app.js",
    "community-panel-1",
]
required_css = [":root", ".hero", ".community-showcase", "@media (max-width: 760px)"]
required_js = ["scroll-progress", "data-tabs", "IntersectionObserver"]

missing_html = [text for text in required_html if text not in html]
missing_css = [text for text in required_css if text not in css]
missing_js = [text for text in required_js if text not in js]

if missing_html or missing_css or missing_js:
    raise SystemExit(
        "Site validation failed. "
        f"Missing HTML markers: {missing_html}. "
        f"Missing CSS markers: {missing_css}. "
        f"Missing JS markers: {missing_js}."
    )

print("Site validation passed")
