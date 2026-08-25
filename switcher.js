(() => {
  const DAYS = [
    { date: "2026-08-25", href: "/14760/" },
    { date: "2026-08-21", href: "/14760/briefs/2026-08-21.html" },
    { date: "2026-08-18", href: "/14760/briefs/2026-08-18.html" },
    { date: "2026-08-17", href: "/14760/briefs/2026-08-17.html" },
    { date: "2026-08-14", href: "/14760/briefs/2026-08-14.html" },
    { date: "2026-06-30", href: "/14760/briefs/2026-06-30.html" },
    { date: "2026-06-26", href: "/14760/briefs/2026-06-26.html" },
    { date: "2026-06-25", href: "/14760/briefs/2026-06-25.html" },
    { date: "2026-06-24", href: "/14760/briefs/2026-06-24.html" },
    { date: "2026-06-23", href: "/14760/briefs/2026-06-23.html" }
  ];
  const currentDate = document.body.getAttribute("data-brief-date");
  const mount = document.querySelector("[data-brief-switcher]");
  if (!mount || !currentDate) return;
  const nav = document.createElement("nav");
  nav.className = "brief-switcher";
  const label = document.createElement("div");
  label.className = "brief-switcher-label";
  label.textContent = "日期切换";
  const buttons = document.createElement("div");
  buttons.className = "brief-switcher-buttons";
  DAYS.forEach((item) => {
    const link = document.createElement("a");
    link.className = "brief-switcher-button" + (item.date === currentDate ? " is-active" : "");
    link.href = item.href;
    link.textContent = item.date;
    buttons.appendChild(link);
  });
  nav.append(label, buttons);
  mount.appendChild(nav);
})();