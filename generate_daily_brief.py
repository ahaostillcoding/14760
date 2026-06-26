from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


REPO = Path(__file__).resolve().parent
BRIEFS_DIR = REPO / "briefs"
ASSETS_DIR = REPO / "assets"
REPORTS_DIR = ASSETS_DIR / "reports"

CURRENT_DATE = "2026-06-26"
ARCHIVE_DATES = [
    "2026-06-26",
    "2026-06-25",
    "2026-06-24",
    "2026-06-23",
    "2026-06-22",
    "2026-06-18",
    "2026-06-17",
    "2026-06-16",
    "2026-06-15",
    "2026-06-12",
]


def make_switcher_days() -> list[dict[str, str]]:
    days: list[dict[str, str]] = []
    for index, day in enumerate(ARCHIVE_DATES):
        href = "/14760/" if index == 0 else f"/14760/briefs/{day}.html"
        days.append({"date": day, "href": href})
    return days


def make_html(page_date: str, prefix: str) -> str:
    report_js = f"{prefix}assets/reports/{page_date}.js"
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="zh-CN">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>\u6bcf\u65e5 GitHub + \u79d1\u6280\u65b0\u95fb\u70ed\u70b9\u7b80\u62a5</title>
            <meta
              name="description"
              content="{page_date} \u4e2d\u6587\u65e5\u62a5\uff1aGitHub \u5f00\u6e90\u9879\u76ee\u89c2\u5bdf\u3001\u6bcf\u65e5\u79d1\u6280\u70ed\u70b9\u3001\u6bcf\u65e5\u65b0\u95fb\u70ed\u70b9\u4e0e Vibe Coding \u5efa\u8bae\u3002"
            />
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
            <link
              href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Noto+Sans+SC:wght@400;500;700;900&display=swap"
              rel="stylesheet"
            />
            <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
            <link rel="stylesheet" href="{prefix}switcher.css" />
            <link rel="stylesheet" href="{prefix}assets/daily-brief.css" />
            <script defer src="{prefix}switcher.js"></script>
            <script defer src="{report_js}"></script>
            <script defer src="{prefix}assets/daily-brief-app.js"></script>
          </head>
          <body data-brief-date="{page_date}">
            <div data-brief-switcher></div>
            <div id="root"></div>
          </body>
        </html>
        """
    )


def make_switcher_js() -> str:
    payload = json.dumps(make_switcher_days(), ensure_ascii=False, indent=2)
    return dedent(
        f"""\
        (() => {{
          const DAYS = {payload};
          const currentDate = document.body.getAttribute("data-brief-date");
          const mount = document.querySelector("[data-brief-switcher]");
          if (!mount || !currentDate) return;

          const nav = document.createElement("nav");
          nav.className = "brief-switcher";

          const label = document.createElement("div");
          label.className = "brief-switcher-label";
          label.textContent = "\u65e5\u671f\u5207\u6362";
          nav.appendChild(label);

          const buttons = document.createElement("div");
          buttons.className = "brief-switcher-buttons";

          DAYS.forEach((item) => {{
            const link = document.createElement("a");
            link.className = "brief-switcher-button" + (item.date === currentDate ? " is-active" : "");
            link.href = item.href;
            link.textContent = item.date;
            buttons.appendChild(link);
          }});

          nav.appendChild(buttons);
          mount.appendChild(nav);
        }})();
        """
    )


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    BRIEFS_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    write_text(REPO / "switcher.js", make_switcher_js())
    write_text(REPO / "index.html", make_html(CURRENT_DATE, "./"))

    for day in ARCHIVE_DATES:
        report_path = REPORTS_DIR / f"{day}.js"
        if report_path.exists():
            write_text(BRIEFS_DIR / f"{day}.html", make_html(day, "../"))


if __name__ == "__main__":
    main()
