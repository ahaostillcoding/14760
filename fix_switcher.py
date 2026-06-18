from pathlib import Path


REPO = Path(__file__).resolve().parent
BRIEFS = REPO / "briefs"

CSS = """.brief-switcher-spacer { height: 72px; }
.brief-switcher { position: fixed; top: 12px; left: 50%; z-index: 9999; transform: translateX(-50%); width: min(1120px, calc(100% - 24px)); padding: 12px 14px; display: flex; align-items: center; justify-content: space-between; gap: 12px; border: 1px solid rgba(24, 35, 45, 0.12); border-radius: 18px; background: rgba(255, 251, 246, 0.88); backdrop-filter: blur(16px); box-shadow: 0 18px 42px rgba(20, 30, 39, 0.12); }
.brief-switcher-label { color: #51606f; font-size: 13px; font-weight: 700; white-space: nowrap; }
.brief-switcher-buttons { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 8px; }
.brief-switcher-button { display: inline-flex; align-items: center; justify-content: center; min-height: 38px; padding: 0 14px; border-radius: 999px; border: 1px solid rgba(24, 35, 45, 0.12); background: rgba(255, 255, 255, 0.78); color: #18232d; font-size: 13px; font-weight: 700; text-decoration: none; transition: transform 160ms ease, border-color 160ms ease, background 160ms ease; }
.brief-switcher-button:hover { transform: translateY(-1px); border-color: rgba(14, 102, 95, 0.4); }
.brief-switcher-button.is-active { background: #0e665f; border-color: #0e665f; color: #f8fbfb; }
@media (max-width: 720px) { .brief-switcher-spacer { height: 110px; } .brief-switcher { top: 8px; width: calc(100% - 16px); padding: 10px 12px; border-radius: 16px; align-items: flex-start; flex-direction: column; } .brief-switcher-buttons { justify-content: flex-start; } }
"""

JS = """(function () {
  var days = [
    { date: "2026-06-18", href: "/14760/" },
    { date: "2026-06-17", href: "/14760/briefs/2026-06-17.html" },
    { date: "2026-06-16", href: "/14760/briefs/2026-06-16.html" },
    { date: "2026-06-15", href: "/14760/briefs/2026-06-15.html" },
    { date: "2026-06-12", href: "/14760/briefs/2026-06-12.html" }
  ];

  var path = window.location.pathname.replace(/index\\.html$/, "");
  var currentDate = "2026-06-18";

  for (var i = 0; i < days.length; i += 1) {
    if (path === days[i].href.replace(/index\\.html$/, "")) {
      currentDate = days[i].date;
      break;
    }
  }

  var nav = document.createElement("nav");
  nav.className = "brief-switcher";

  var label = document.createElement("span");
  label.className = "brief-switcher-label";
  label.textContent = "切换简报日期";

  var buttons = document.createElement("div");
  buttons.className = "brief-switcher-buttons";

  for (var j = 0; j < days.length; j += 1) {
    var item = days[j];
    var link = document.createElement("a");
    link.className = "brief-switcher-button" + (item.date === currentDate ? " is-active" : "");
    link.href = item.href;
    link.textContent = item.date;
    buttons.appendChild(link);
  }

  nav.appendChild(label);
  nav.appendChild(buttons);

  var spacer = document.createElement("div");
  spacer.className = "brief-switcher-spacer";

  document.body.insertBefore(nav, document.body.firstChild);
  document.body.insertBefore(spacer, nav.nextSibling);
})();
"""

DAYS = [
    ("2026-06-18", "index.html"),
    ("2026-06-17", "briefs/2026-06-17.html"),
    ("2026-06-16", "briefs/2026-06-16.html"),
    ("2026-06-15", "briefs/2026-06-15.html"),
    ("2026-06-12", "briefs/2026-06-12.html"),
]


def strip_between(text: str, start_marker: str, end_marker: str) -> str:
    while start_marker in text:
        start = text.index(start_marker)
        end = text.index(end_marker, start) + len(end_marker)
        text = text[:start] + text[end:]
    return text


def patch_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = strip_between(text, '<style id="brief-switcher-style">', "</style>")
    text = strip_between(text, '<nav class="brief-switcher">', "</nav>")
    text = text.replace("padding-top: 72px;\n", "")
    text = text.replace("padding-top: 110px;\n", "")
    text = text.replace('body {\n          padding-top: 110px;\n        }\n\n', "")

    css_href = "./switcher.css" if path.name == "index.html" else "../switcher.css"
    js_src = "./switcher.js" if path.name == "index.html" else "../switcher.js"

    if css_href not in text:
        injection = (
            f'    <link rel="stylesheet" href="{css_href}" />\n'
            f'    <script defer src="{js_src}"></script>\n'
        )
        text = text.replace("</head>", injection + "  </head>", 1)

    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    (REPO / "switcher.css").write_text(CSS, encoding="utf-8", newline="\n")
    (REPO / "switcher.js").write_text(JS, encoding="utf-8", newline="\n")

    files = [REPO / "index.html"] + sorted(BRIEFS.glob("*.html"))
    for file in files:
        patch_html(file)
        print(f"patched {file.relative_to(REPO).as_posix()}")


if __name__ == "__main__":
    main()
