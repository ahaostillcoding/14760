        (() => {
          const DAYS = [
  {
    "date": "2026-08-17",
    "href": "/14760/"
  },
  {
    "date": "2026-08-14",
    "href": "/14760/briefs/2026-08-14.html"
  },
  {
    "date": "2026-06-30",
    "href": "/14760/briefs/2026-06-30.html"
  },
  {
    "date": "2026-06-26",
    "href": "/14760/briefs/2026-06-26.html"
  },
  {
    "date": "2026-06-25",
    "href": "/14760/briefs/2026-06-25.html"
  },
  {
    "date": "2026-06-24",
    "href": "/14760/briefs/2026-06-24.html"
  },
  {
    "date": "2026-06-23",
    "href": "/14760/briefs/2026-06-23.html"
  },
  {
    "date": "2026-06-22",
    "href": "/14760/briefs/2026-06-22.html"
  },
  {
    "date": "2026-06-17",
    "href": "/14760/briefs/2026-06-17.html"
  },
  {
    "date": "2026-06-16",
    "href": "/14760/briefs/2026-06-16.html"
  },
  {
    "date": "2026-06-15",
    "href": "/14760/briefs/2026-06-15.html"
  },
  {
    "date": "2026-06-12",
    "href": "/14760/briefs/2026-06-12.html"
  }
];
          const currentDate = document.body.getAttribute("data-brief-date");
          const mount = document.querySelector("[data-brief-switcher]");
          if (!mount || !currentDate) return;

          const nav = document.createElement("nav");
          nav.className = "brief-switcher";

          const label = document.createElement("div");
          label.className = "brief-switcher-label";
          label.textContent = "日期切换";
          nav.appendChild(label);

          const buttons = document.createElement("div");
          buttons.className = "brief-switcher-buttons";

          DAYS.forEach((item) => {
            const link = document.createElement("a");
            link.className = "brief-switcher-button" + (item.date === currentDate ? " is-active" : "");
            link.href = item.href;
            link.textContent = item.date;
            buttons.appendChild(link);
          });

          nav.appendChild(buttons);
          mount.appendChild(nav);
        })();
