(function () {
  var days = [
    { date: "2026-06-18", href: "/14760/" },
    { date: "2026-06-17", href: "/14760/briefs/2026-06-17.html" },
    { date: "2026-06-16", href: "/14760/briefs/2026-06-16.html" },
    { date: "2026-06-15", href: "/14760/briefs/2026-06-15.html" },
    { date: "2026-06-12", href: "/14760/briefs/2026-06-12.html" }
  ];

  var path = window.location.pathname.replace(/index\.html$/, "");
  var currentDate = "2026-06-18";

  for (var i = 0; i < days.length; i += 1) {
    if (path === days[i].href.replace(/index\.html$/, "")) {
      currentDate = days[i].date;
      break;
    }
  }

  var nav = document.createElement("nav");
  nav.className = "brief-switcher";

  var label = document.createElement("span");
  label.className = "brief-switcher-label";
  label.textContent = "\u5207\u6362\u7b80\u62a5\u65e5\u671f";

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
