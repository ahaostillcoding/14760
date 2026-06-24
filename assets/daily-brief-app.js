(() => {
  const report = window.DAILY_REPORT;
  if (!report) {
    throw new Error("DAILY_REPORT is missing");
  }

  const h = React.createElement;

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
        h(
          "div",
          null,
          h("h2", null, props.title),
          h("p", { className: "section-desc" }, props.desc)
        ),
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
        h(
          "div",
          null,
          h("h3", null, item.name),
          h("p", { className: "card-subtitle" }, item.source)
        ),
        h(
          "div",
          { className: "stat" },
          h("strong", null, item.stars),
          h("span", null, "GitHub Stars")
        )
      ),
      h("div", { className: "tag-row", style: { marginTop: 14 } }, ...item.tags.map((tag) => h(Pill, { key: tag }, tag))),
      h("div", { className: "key-block" }, h("strong", null, "主要用途"), h("p", null, item.purpose)),
      h("div", { className: "key-block" }, h("strong", null, "核心亮点"), h("p", null, item.highlight)),
      h("div", { className: "key-block" }, h("strong", null, "为什么现在值得看"), h("p", null, item.whyNow)),
      h(
        "div",
        { className: "meta" },
        h("span", { className: "mini-title" }, "来源链接"),
        h("a", { className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }, "查看项目")
      )
    );
  }

  function NewsCard(props) {
    const item = props.item;
    return h(
      "article",
      { className: "card span-4" },
      h(
        "div",
        { className: "card-header" },
        h(
          "div",
          null,
          h("h3", null, item.title),
          h("p", { className: "card-subtitle" }, item.source)
        )
      ),
      h("div", { className: "tag-row", style: { marginTop: 14 } }, ...item.tags.map((tag) => h(Pill, { key: tag }, tag))),
      h("div", { className: "key-block" }, h("strong", null, "事件摘要"), h("p", null, item.summary)),
      h("div", { className: "key-block" }, h("strong", null, "影响判断"), h("p", null, item.impact)),
      item.audience ? h("div", { className: "key-block" }, h("strong", null, "适合关注的人群"), h("p", null, item.audience)) : null,
      item.note ? h("div", { className: "callout" }, item.note) : null,
      h(
        "div",
        { className: "meta" },
        h("span", { className: "mini-title" }, "来源链接"),
        h("a", { className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }, "打开原文")
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
      h("div", { className: "key-block" }, h("strong", null, "可以做什么"), h("p", null, item.what)),
      h("div", { className: "key-block" }, h("strong", null, "适合技术栈 / 组件"), h("p", null, item.stack)),
      h("div", { className: "key-block" }, h("strong", null, "MVP 思路"), h("p", null, item.mvp))
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
                h(
                  "div",
                  { className: "metric", key: stat.label },
                  h("strong", { className: "mono" }, stat.value),
                  h("span", null, stat.label)
                )
              )
            )
          ),
          h(
            "div",
            { style: { display: "grid", gap: 14, alignContent: "start" } },
            h(
              "div",
              { className: "toc" },
              h("h2", null, "阅读导航"),
              h(
                "ul",
                null,
                ...[
                  "GitHub 开源项目观察",
                  "每日科技热点",
                  "每日新闻热点",
                  "Vibe Coding 项目建议",
                  "今日总趋势判断",
                ].map((item, index) =>
                  h(
                    "li",
                    { key: item },
                    h("span", { className: "toc-index mono" }, index + 1),
                    h("span", null, item)
                  )
                )
              )
            ),
            h(
              "div",
              { className: "snapshot" },
              h("h2", null, "一句话判断"),
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
            title: "模块一 | GitHub 开源项目观察",
            desc: "优先选择最近仍活跃、适合开发者快速理解并能直接映射到工程落地的项目。",
            chips: ["Active", "Open Source", "Builder Focus"],
          }),
          h(
            "div",
            { className: "grid" },
            ...report.githubProjects.map((item) => h(ProjectCard, { key: item.name, item })),
            h(
              "div",
              { className: "summary-card span-12" },
              h("h3", { style: { margin: 0, fontSize: 21 } }, "项目趋势观察"),
              h("ol", { className: "list" }, ...report.projectTrends.map((trend) => h("li", { key: trend }, trend)))
            )
          )
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "tech",
            title: "模块二 | 每日科技热点",
            desc: "优先保留对 AI、基础设施、开发者工具、硬件和自动驾驶最有判断价值的事件。",
            chips: ["AI", "Cloud", "Hardware", "Robotics"],
          }),
          h("div", { className: "grid" }, ...report.techHotspots.map((item) => h(NewsCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "news",
            title: "模块三 | 每日新闻热点",
            desc: "只保留对商业、资本市场、供应链、国际经营和政策判断有直接影响的内容。",
            chips: ["Macro", "Trade", "Energy", "Policy"],
          }),
          h("div", { className: "grid" }, ...report.generalNews.map((item) => h(NewsCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "vibe",
            title: "模块四 | Vibe Coding 项目建议",
            desc: "基于今天的 GitHub 和科技信号，挑出本周就能开干的 4 个方向。",
            chips: ["MVP Ready", "Actionable"],
          }),
          h("div", { className: "grid" }, ...report.vibeIdeas.map((item) => h(IdeaCard, { key: item.title, item })))
        ),
        h(
          "section",
          { className: "section" },
          h(SectionHeader, {
            id: "trend",
            title: "模块五 | 今日总趋势判断",
            desc: "把今天分散的开源项目、科技动态和综合新闻，收束成一个可执行判断。",
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
