from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = ROOT / "index.html"
styles = ROOT / "styles.css"

html = index.read_text(encoding="utf-8")
css = styles.read_text(encoding="utf-8")

HTMLParser().feed(html)

required_html = [
    "The Football",
    "Media Engine",
    "Complete 60-Day Growth Strategy",
    "styles.css",
]
required_css = [":root", ".hero", "@media (max-width: 760px)"]

missing_html = [text for text in required_html if text not in html]
missing_css = [text for text in required_css if text not in css]

if missing_html or missing_css:
    raise SystemExit(
        "Site validation failed. "
        f"Missing HTML markers: {missing_html}. "
        f"Missing CSS markers: {missing_css}."
    )

print("Site validation passed")
