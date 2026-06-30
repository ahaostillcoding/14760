(() => {
  const report = window.DAILY_REPORT;
  if (!report) {
    throw new Error("DAILY_REPORT is missing");
  }

  const h = React.createElement;

  const TEXT = {
    projectPurpose: "\u4e3b\u8981\u7528\u9014",
    projectHighlight: "\u6838\u5fc3\u4eae\u70b9",
    projectWhyNow: "\u4e3a\u4ec0\u4e48\u73b0\u5728\u503c\u5f97\u770b",
    sourceLink: "\u6765\u6e90\u94fe\u63a5",
    viewProject: "\u67e5\u770b\u9879\u76ee",
    openArticle: "\u6253\u5f00\u539f\u6587",
    eventSummary: "\u4e8b\u4ef6\u6458\u8981",
    impact: "\u5f71\u54cd\u5224\u65ad",
    audience: "\u9002\u5408\u5173\u6ce8\u7684\u4eba\u7fa4",
    ideaWhat: "\u53ef\u4ee5\u505a\u4ec0\u4e48",
    ideaStack: "\u9002\u5408\u6280\u672f\u6808 / \u7ec4\u4ef6",
    ideaMvp: "MVP \u601d\u8def",
    readNav: "\u9605\u8bfb\u5bfc\u822a",
    quickJudgment: "\u4e00\u53e5\u8bdd\u5224\u65ad",
    projectTrend: "\u9879\u76ee\u8d8b\u52bf\u89c2\u5bdf",
    sections: [
      "\u6a21\u5757\u4e00 | GitHub \u5f00\u6e90\u9879\u76ee\u89c2\u5bdf",
      "\u6a21\u5757\u4e8c | \u6bcf\u65e5\u79d1\u6280\u70ed\u70b9",
      "\u6a21\u5757\u4e09 | \u6bcf\u65e5\u65b0\u95fb\u70ed\u70b9",
      "\u6a21\u5757\u56db | Vibe Coding \u9879\u76ee\u5efa\u8bae",
      "\u6a21\u5757\u4e94 | \u4eca\u65e5\u603b\u8d8b\u52bf\u5224\u65ad",
    ],
  };

  function Pill(props) {
    return h("span", { className: props.tone === "chip" ? "chip" : "tag" }, props.children);
  }

  function SectionHeader(props) {
    return h(
      "div",
      { id: props.id },
      h(
        "div",
        { className: "section-head" },
        h("div", null, h("h2", null, props.title), h("p", { className: "section-desc" }, props.desc)),
        h(
          "div",
          { className: "chip-row" },
          ...(props.chips || []).map((chip) => h(Pill, { key: chip, tone: "chip" }, chip))
        )
      )
    );
  }

  function ProjectCard(props) {
    const item = props.item;
    return h(
      "article",
      { className: "card span-6" },
      h(
        "div",
        { className: "card-header" },
        h("div", null, h("h3", null, item.name), h("p", { className: "card-subtitle" }, item.source)),
        item.stars
          ? h(
              "div",
              { className: "stat" },
              h("strong", null, item.stars),
              h("span", null, "GitHub Stars")
            )
          : null
      ),
      h("div", { className: "tag-row", style: { marginTop: 14 } }, ...item.tags.map((tag) => h(Pill, { key: tag }, tag))),
      h("div", { className: "key-block" }, h("strong", null, TEXT.projectPurpose), h("p", null, item.purpose)),
      h("div", { className: "key-block" }, h("strong", null, TEXT.projectHighlight), h("p", null, item.highlight)),
      h("div", { className: "key-block" }, h("strong", null, TEXT.projectWhyNow), h("p", null, item.whyNow)),
      h(
        "div",
        { className: "meta" },
        h("span", { className: "mini-title" }, TEXT.sourceLink),
        h("a", { className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }, TEXT.viewProject)
      )
    );
  }

  function NewsCard(props) {
    const item = props.item;
    return h(
      "article",
      { className: "card span-4" },
      h("div", { className: "card-header" }, h("div", null, h("h3", null, item.title), h("p", { className: "card-subtitle" }, item.source))),
      h("div", { className: "tag-row", style: { marginTop: 14 } }, ...item.tags.map((tag) => h(Pill, { key: tag }, tag))),
      h("div", { className: "key-block" }, h("strong", null, TEXT.eventSummary), h("p", null, item.summary)),
      h("div", { className: "key-block" }, h("strong", null, TEXT.impact), h("p", null, item.impact)),
      item.audience ? h("div", { className: "key-block" }, h("strong", null, TEXT.audience), h("p", null, item.audience)) : null,
      item.note ? h("div", { className: "callout" }, item.note) : null,
      h(
        "div",
        { className: "meta" },
        h("span", { className: "mini-title" }, TEXT.sourceLink),
        h("a", { className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }, TEXT.openArticle)
      )
    );
  }

  function IdeaCard(props) {
    const item = props.item;
    return h(
      "article",
      { className: "card span-6" },
      h("h3", null, item.title),
      h("div", { className: "tag-row", style: { marginTop: 14 } }, ...item.tags.map((tag) => h(Pill, { key: tag }, tag))),
      h("div", { className: "key-block" }, h("strong", null, TEXT.ideaWhat), h("p", null, item.what)),
      h("div", { className: "key-block" }, h("strong", null, TEXT.ideaStack), h("p", null, item.stack)),
      h("div", { className: "key-block" }, h("strong", null, TEXT.ideaMvp), h("p", null, item.mvp))
    );
  }

  function App() {
    return h(
      "div",
      { className: "page" },
      h(
        "header",
        { className: "hero" },
        h("div", { className: "eyebrow mono" }, "Daily Briefing | ", report.date),
        h(
          "div",
          { className: "hero-grid" },
          h(
            "div",
            null,
            h("h1", null, report.title),
            h("p", null, report.summary),
            h(
              "div",
              { className: "snapshot-grid", style: { marginTop: 20 } },
              ...report.stats.map((stat) =>
                h("div", { className: "metric", key: stat.label }, h("strong", { className: "mono" }, stat.value), h("span", null, stat.label))
              )
            )
          ),
          h(
            "div",
            { style: { display: "grid", gap: 14, alignContent: "start" } },
            h(
              "div",
              { className: "toc" },
              h("h2", null, TEXT.readNav),
              h(
                "ul",
                null,
                ...TEXT.sections.map((item, index) =>
                  h("li", { key: item }, h("span", { className: "toc-index mono" }, index + 1), h("span", null, item))
                )
              )
            ),
            h(
              "div",
              { className: "snapshot" },
              h("h2", null, TEXT.quickJudgment),
              h("p", { style: { marginTop: 14, color: "rgba(248, 251, 251, 0.78)", lineHeight: 1.8 } }, report.heroNote)
            )
          )
        )
      ),
      h(
        "main",
        { className: "main" },
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "github",
            title: TEXT.sections[0],
            desc: "\u4f18\u5148\u9009\u62e9\u6700\u8fd1\u4ecd\u6d3b\u8dc3\u3001\u503c\u5f97\u5f00\u53d1\u8005\u5feb\u901f\u7406\u89e3\u3001\u4e14\u80fd\u76f4\u63a5\u6620\u5c04\u5230\u5de5\u7a0b\u843d\u5730\u7684\u9879\u76ee\u3002",
            chips: ["Active", "Open Source", "Builder Focus"],
          }),
          h(
            "div",
            { className: "grid" },
            ...report.githubProjects.map((item) => h(ProjectCard, { key: item.name, item })),
            h(
              "div",
              { className: "summary-card span-12" },
              h("h3", { style: { margin: 0, fontSize: 21 } }, TEXT.projectTrend),
              h("ol", { className: "list" }, ...report.projectTrends.map((trend) => h("li", { key: trend }, trend)))
            )
          )
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "tech",
            title: TEXT.sections[1],
            desc: "\u4f18\u5148\u4fdd\u7559\u5bf9 AI\u3001\u5f00\u53d1\u8005\u5de5\u5177\u3001\u5f00\u6e90\u751f\u6001\u3001\u786c\u4ef6\u3001\u4e91\u8ba1\u7b97\u548c\u673a\u5668\u4eba\u6700\u6709\u5224\u65ad\u4ef7\u503c\u7684\u4e8b\u4ef6\u3002",
            chips: ["AI", "Cloud", "Hardware", "Robotics"],
          }),
          h("div", { className: "grid" }, ...report.techHotspots.map((item) => h(NewsCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "news",
            title: TEXT.sections[2],
            desc: "\u53ea\u4fdd\u7559\u5bf9\u5546\u4e1a\u3001\u8d44\u672c\u5e02\u573a\u3001\u4f9b\u5e94\u94fe\u3001\u56fd\u9645\u5c40\u52bf\u548c\u4ea7\u54c1\u5224\u65ad\u6709\u76f4\u63a5\u5f71\u54cd\u7684\u4fe1\u606f\u3002",
            chips: ["Macro", "Trade", "Energy", "Policy"],
          }),
          h("div", { className: "grid" }, ...report.generalNews.map((item) => h(NewsCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "vibe",
            title: TEXT.sections[3],
            desc: "\u57fa\u4e8e\u4eca\u5929\u7684 GitHub \u548c\u79d1\u6280\u4fe1\u53f7\uff0c\u6311\u51fa\u53ef\u4ee5\u5feb\u901f\u52a8\u624b\u7684 4 \u4e2a\u65b9\u5411\u3002",
            chips: ["MVP Ready", "Actionable"],
          }),
          h("div", { className: "grid" }, ...report.vibeIdeas.map((item) => h(IdeaCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "trend",
            title: TEXT.sections[4],
            desc: "\u628a\u4eca\u5929\u5206\u6563\u7684\u5f00\u6e90\u9879\u76ee\u3001\u79d1\u6280\u52a8\u6001\u548c\u7efc\u5408\u65b0\u95fb\u6536\u675f\u6210\u4e00\u4e2a\u53ef\u6267\u884c\u5224\u65ad\u3002",
            chips: ["Signal", "Decision"],
          }),
          h("div", { className: "summary-card" }, h("p", { style: { fontSize: 15, color: "var(--text)", lineHeight: 1.92 } }, report.totalTrend))
        )
      ),
      h("footer", { className: "footer" }, report.footer)
    );
  }

  ReactDOM.createRoot(document.getElementById("root")).render(h(App));
})();
