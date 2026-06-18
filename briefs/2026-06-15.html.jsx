
      const briefDate = "2026-06-15";

      const topSummary = [
        {
          label: "今日摘要",
          title: "Agent 基础设施仍是 GitHub 最强主线",
          body:
            "今天最值得看的开源项目几乎都围绕三层能力展开：代码仓库接入、浏览器执行、以及 agent 前端交互层。市场关注点已经明显从“模型更强”转向“怎样更稳定地接进真实工作流”。",
          tone: "brand",
        },
        {
          label: "科技侧判断",
          title: "AI 竞争正在从模型能力转向资本、入口与工具链控制",
          body:
            "OpenAI 的 IPO 动作、Apple 的 Siri AI、Cloudflare 并购 VoidZero，连起来看不是孤立新闻，而是平台方在争谁能控制分发入口、开发体验和后续商业化节奏。",
          tone: "accent",
        },
        {
          label: "宏观侧判断",
          title: "能源与地缘仍在给科技估值重新定价",
          body:
            "伊朗局势缓和带动油价回落和股市反弹，但 AP 同时提醒供应恢复需要数月。对企业更现实的含义是：成本压力会缓一点，但不会立刻消失。",
          tone: "warn",
        },
      ];

      const githubProjects = [
        {
          name: "OpenHands",
          link: "https://github.com/OpenHands/OpenHands",
          tags: ["AI Coding Agent", "77.1k stars", "GitHub"],
          usage: "开源 AI 开发代理，面向真实代码任务，而不是只做聊天式补全。",
          highlights:
            "仓库首页显示 77.1k stars、9.8k forks，README 直接把定位写成 “AI-Driven Development”。项目规模、贡献密度和多目录结构说明它仍处在高强度迭代期。",
          whyNow:
            "如果你想判断“编程 agent 能不能从 demo 走向稳定工程工具”，OpenHands 仍然是最值得持续跟的样本之一。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "browser-use",
          link: "https://github.com/browser-use/browser-use",
          tags: ["Browser Automation", "98.8k stars", "GitHub"],
          usage: "把网页操作抽象成 agent 可调用的浏览器能力层。",
          highlights:
            "仓库首页描述是 “Make websites accessible for AI agents”，截至 2026-06-15 显示 98.8k stars、11k forks，说明它已经不只是玩具项目，而是这个赛道的流量中心。",
          whyNow:
            "SaaS 后台、数据抓取、运营自动化都离不开浏览器。谁拿下稳定浏览器执行层，谁就更接近真实商业流程。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "microsoft/playwright-mcp",
          link: "https://github.com/microsoft/playwright-mcp",
          tags: ["MCP", "33.9k stars", "Microsoft"],
          usage: "把 Playwright 暴露成 MCP server，让模型用结构化方式操作网页。",
          highlights:
            "截至 2026-06-15 仓库页显示 33.9k stars。它的价值不只是自动化，而是把网页交互从“视觉猜测”推向“可验证执行”。",
          whyNow:
            "MCP 正在从概念热词进入默认工程配置。Playwright MCP 是把 agent 接进网页工作流时最基础、也最具复用性的那层。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "github/github-mcp-server",
          link: "https://github.com/github/github-mcp-server",
          tags: ["Official MCP", "30.7k stars", "GitHub 官方"],
          usage: "GitHub 官方 MCP server，直接把仓库、Issue、PR、Actions 暴露给 agent。",
          highlights:
            "仓库页明确写的是 “GitHub's official MCP Server”，截至 2026-06-15 显示 30.7k stars。平台方亲自下场，意味着 agent 与代码协作接口开始标准化。",
          whyNow:
            "这不是第三方在“接 GitHub”，而是 GitHub 自己定义 AI 协作的接入面。平台层的信号往往比短期热度更重要。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "CopilotKit",
          link: "https://github.com/CopilotKit/CopilotKit",
          tags: ["Generative UI", "35.1k stars", "AG-UI"],
          usage: "为 agent 与生成式 UI 提供前端栈，适合把模型结果直接渲染进业务界面。",
          highlights:
            "仓库页标题直接写 “The Frontend Stack for Agents & Generative UI”，截至 2026-06-15 为 35.1k stars。说明竞争已经进入 agent 前端层，而不只是模型 API 层。",
          whyNow:
            "当越来越多团队不满足于聊天框，能不能把 agent 嵌进工作台、表单、看板，决定了 AI 产品是否真的能被长期使用。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "goose",
          link: "https://github.com/aaif-goose/goose",
          tags: ["Open Agent", "49.4k stars", "Any LLM"],
          usage: "可扩展的开源 agent，强调安装、执行、编辑、测试这一整条闭环。",
          highlights:
            "仓库页定位是 “goes beyond code suggestions”，截至 2026-06-15 显示 49.4k stars。它代表的是本地开发助手与多模型编排结合的路线。",
          whyNow:
            "如果你更关心桌面侧、CLI 侧的 agent 体验，而不是纯 Web 演示，goose 的产品方向很值得观察。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
        {
          name: "bolt.diy",
          link: "https://github.com/stackblitz-labs/bolt.diy",
          tags: ["Self-hosted", "19.5k stars", "Template Repo"],
          usage: "用任意 LLM 生成、运行、编辑并部署全栈应用的自托管方案。",
          highlights:
            "仓库页显示 19.5k stars、10.4k forks。star 未必是今天最高，但 fork 很高，说明“自托管复制闭源产品体验”这条需求很真实。",
          whyNow:
            "很多团队现在要的不是最强模型，而是能不能把生成能力搬回自己的栈里，形成更可控的内部生产流程。",
          source: "来源：GitHub 仓库页，抓取日期 2026-06-15",
        },
      ];

      const githubTrends = [
        {
          title: "趋势一：热门项目继续从“做一个 agent”转向“把 agent 接进真实系统”",
          body:
            "今天入选的项目没有一个只是单纯聊天工具，几乎都在解决仓库读写、网页执行、前端嵌入和本地工作流闭环问题。这说明开发者已经不再为“会说”买单，而是为“能接入、能执行、能交付”买单。",
        },
        {
          title: "趋势二：MCP 已经从协议概念变成工程默认层",
          body:
            "Playwright MCP 和 GitHub MCP 同时高热，不是偶然。MCP 现在扮演的角色越来越像过去的 REST SDK 或 webhook：不是卖点本身，但会决定生态能否大规模复用。",
        },
        {
          title: "趋势三：agent 前端层开始独立成赛道",
          body:
            "CopilotKit 这类项目说明一个现实：模型输出本身不等于产品。谁能把 agent 的状态、动作和结果更自然地放进工作界面，谁就更接近长期留存。",
        },
      ];

      const techNews = [
        {
          title: "OpenAI 已于 2026-06-08 秘密递交 IPO 草案",
          link: "https://www.axios.com/2026/06/08/openai-ipo",
          source: "Axios，2026-06-08",
          tags: ["AI", "资本市场", "平台化"],
          summary:
            "Axios 报道，OpenAI 已秘密递交 IPO 文件，但表示短期仍以产品推进为主。时间点上，它紧跟 Anthropic 之后，也处在 SpaceX 上市窗口附近。",
          impact:
            "这件事的重要性不在“会不会很快上市”，而在 AI 公司竞争已经明显进入资本纪律阶段。之后的模型路线、价格策略和合作节奏都会更受公开市场约束。",
          audience: "关注大模型平台、企业采购、AI 投融资和估值节奏的人。",
        },
        {
          title: "OpenAI 在 IPO 前夕遭多州调查，AI 安全与责任压力继续抬升",
          link: "https://apnews.com/article/a95894407773307fae8ae3ce9742b586",
          source: "AP，2026-06-14",
          tags: ["AI 安全", "监管", "OpenAI"],
          summary:
            "AP 报道，美国多州正调查 ChatGPT 可能带来的用户伤害风险。事件与 IPO 进程叠加，让安全治理从品牌问题变成融资与上市问题。",
          impact:
            "AI 公司后续的竞争不只是能力，还包括可审计性、家长控制、风险处置和法律可解释性。对企业客户来说，这类监管压力会直接影响采购门槛。",
          audience: "企业法务、AI 产品负责人、教育和未成年人产品团队。",
        },
        {
          title: "Apple 在 WWDC 2026 推出 Siri AI，正式补上系统级 AI 助手入口",
          link: "https://www.theverge.com/tech/942416/apple-siri-ai-update-wwdc",
          source: "The Verge，2026-06-09",
          tags: ["Apple", "终端入口", "消费电子"],
          summary:
            "Apple 在 WWDC 2026 发布 Siri AI，把更强的对话、视觉理解和系统级调用放进 iPhone、iPad、Mac 等设备体系。",
          impact:
            "它的重要性不是“Apple 终于有 AI 了”，而是操作系统入口开始重新洗牌。未来大量 AI 应用不会先从网页打开，而会先在系统助手层被分发。",
          audience: "移动产品团队、iOS 开发者、消费电子和入口平台观察者。",
        },
        {
          title: "Cloudflare 收购 VoidZero，把 Vite 工具链拉进 AI-native 开发平台",
          link: "https://www.itpro.com/business/acquisition/cloudflare-snaps-up-voidzero-to-expand-ai-native-developer-tools",
          source: "ITPro，2026-06-05",
          tags: ["开发者工具", "Cloudflare", "前端基础设施"],
          summary:
            "Cloudflare 收购了 VoidZero。后者背后是 Vite、Vitest、Rolldown、Oxc 这套现代前端工具链资产。",
          impact:
            "这说明云平台已经不满足于卖算力或部署，而是在向“开发体验入口”上游延伸。AI 编码时代，工具链与云平台的边界会继续变薄。",
          audience: "前端工程师、云平台团队、构建工具作者。",
        },
        {
          title: "Nvidia 与 Hyundai 继续加码机器人与制造协同",
          link: "https://www.axios.com/2026/06/08/nvidia-jensen-huang-hyundai-robots",
          source: "Axios，2026-06-08",
          tags: ["机器人", "制造业", "Nvidia"],
          summary:
            "Axios 报道，黄仁勋公开强调 Hyundai 在机器人上的实力，并推动双方在移动、制造和机器人方向继续合作。",
          impact:
            "机器人赛道正在从概念展示走向产业协同：算力公司、车厂、制造体系开始共同定义量产路径。物理世界 AI 的落地速度值得重新估计。",
          audience: "机器人创业者、工业自动化团队、智能制造决策者。",
        },
        {
          title: "SpaceX 上市首秀强势，科技资本市场重新奖励“基础设施叙事”",
          link: "https://apnews.com/article/f61ee2e7ec8ca8c95048cef76ed27214",
          source: "AP，2026-06-12",
          tags: ["SpaceX", "IPO", "基础设施"],
          summary:
            "AP 报道，SpaceX 在 2026-06-12 上市首日大涨 19.2%。资本市场对高投入、长周期、基础设施型科技公司的风险偏好明显回升。",
          impact:
            "这会影响整个科技融资预期。AI、航天、算力、网络基础设施这些重资产路线，接下来更容易得到一级和二级市场联动定价。",
          audience: "科技投资人、硬科技团队、基础设施创业者。",
        },
      ];

      const newsHotspots = [
        {
          title: "伊朗战争暂时停火预期推动全球股市大涨、油价回落",
          link: "https://apnews.com/article/f2ee51f1b0686688b3e50068b4b71d70",
          source: "AP，2026-06-15",
          tags: ["中东局势", "能源", "资本市场"],
          summary:
            "AP 报道，围绕结束伊朗战争和重开霍尔木兹海峡的暂时协议预期，带动亚洲股市大涨、原油明显回落。",
          impact:
            "这会立刻影响全球资产价格和风险偏好，但它更像“风险溢价下降”，不是供给恢复完成。企业不要把短期反弹误判成成本问题已经解决。",
        },
        {
          title: "能源专家警告：即便停火，油气供应恢复仍可能需要数月",
          link: "https://apnews.com/article/42bdd71d5afa6fb5ac5d0c3e7857de6c",
          source: "AP，2026-06-15",
          tags: ["供应链", "油气", "风险管理"],
          summary:
            "同样来自 AP 的另一篇报道指出，航运、保险、炼化和油轮调度仍需时间恢复，霍尔木兹恢复通行不等于马上恢复正常供给。",
          impact:
            "这条信息比市场涨跌更有经营价值。制造、物流、跨境贸易公司需要继续把能源和运费波动纳入未来数周预算。",
        },
        {
          title: "美国 2026 年 5 月 PPI 同比上涨 6.5%，批发端通胀再度抬头",
          link: "https://apnews.com/article/137b9d3e10be5244547b3d94a9d6d940",
          source: "AP，2026-06-11",
          tags: ["美国经济", "通胀", "利率"],
          summary:
            "AP 报道，受能源冲击影响，美国 5 月生产者价格指数同比上涨 6.5%，创 2022 年 11 月以来最快增速。",
          impact:
            "这不只是宏观数字。它意味着企业端成本会继续向消费端传导，也会压制市场对宽松货币政策的乐观预期。",
        },
        {
          title: "中国 5 月出口同比增长 19.4%，半导体、汽车与 AI 相关产品需求强劲",
          link: "https://apnews.com/article/33ee2ae323cb9bd8189bf1b13fbe9edf",
          source: "AP，2026-06-09",
          tags: ["中国经济", "出口", "制造业"],
          summary:
            "AP 报道，中国 5 月出口同比增长 19.4%，半导体、计算设备、汽车等高技术和产业链产品是主要拉动力。",
          impact:
            "这说明全球科技投资和高端制造需求并没有明显熄火。对产业判断来说，硬件和 AI 供给链仍然处在景气周期中。",
        },
        {
          title: "美国调整钢铝铜相关关税，对农机和部分工业设备临时下调税率",
          link: "https://apnews.com/article/7ca5a76dbe13db7e732fa48462ccde92",
          source: "AP，2026-06-02",
          tags: ["关税", "制造成本", "贸易政策"],
          summary:
            "AP 报道，美国总统特朗普签署行政令，部分农机、暖通和工业设备税率从 25% 下调到 15%，并调整金属使用规则。",
          impact:
            "这不是全面转向，而是更细颗粒度地重写制造成本结构。依赖跨境零部件和设备采购的企业需要重新核算报价与毛利。",
        },
        {
          title: "欧洲央行先于美联储加息，显示能源驱动的通胀并未过去",
          link: "https://apnews.com/article/2a2c26c580961a979372393706a7f93c",
          source: "AP，2026-06-11",
          tags: ["欧洲", "央行", "通胀预期"],
          summary:
            "AP 报道，欧洲央行因伊朗战争推高油价和通胀而加息，成为主要央行里先行动的一方，美联储后续态度因此更受关注。",
          impact:
            "对跨境业务来说，货币环境并没有转松，反而在能源冲击下重新收紧。估值、融资和消费信心都可能继续承压。",
        },
      ];

      const vibeIdeas = [
        {
          title: "Agent Ops Radar",
          stack: "React + Supabase + GitHub MCP + Playwright MCP",
          what:
            "做一个团队内部的 agent 任务看板，把 PR、Issue、CI、网页自动化步骤和失败原因统一收进一张面板。",
          mvp:
            "先抓 GitHub MCP 的 PR 和 Actions，再接一条 Playwright MCP 执行记录，把失败截图、错误摘要和下一步建议做成日报卡片。",
        },
        {
          title: "Browser Workflow Recorder",
          stack: "React + browser-use + SQLite",
          what:
            "把人工完成的一次后台运营流程录成可复用模板，让 agent 可以在同类任务里自动执行和重试。",
          mvp:
            "先只支持三步：登录后台、抓订单、导出 CSV。把每一步的状态、异常点和重试建议结构化保存。",
        },
        {
          title: "Generative UI Briefing Desk",
          stack: "React + CopilotKit + 任意 LLM API",
          what:
            "做一个一句话生成业务简报界面的工具，让模型不仅给文字，还直接吐出摘要卡片、下一步动作和表单草稿。",
          mvp:
            "第一版只支持输入主题，自动生成三类卡片：今日摘要、风险点、建议动作。数据先写 mock，后续再接真接口。",
        },
        {
          title: "Self-hosted Build Playground",
          stack: "bolt.diy + Docker + GitHub Pages 或 Cloudflare Pages",
          what:
            "搭一个团队可控的 AI 原型工坊，快速生成活动页、产品页和内部小工具页面。",
          mvp:
            "先提供 3 个模板提示词和自动提交到 Git 的能力，让生成结果可以直接发布成静态页面，重点解决“从想法到链接”的最后一公里。",
        },
      ];

      const notes = [
        {
          title: "数据口径",
          body:
            "GitHub 部分优先依据仓库首页可见信息，如 stars、forks、README 定位；新闻优先采用 AP、Axios、The Verge、ITPro 等可追溯来源，时间窗口以 2026-06-02 到 2026-06-15 为主。",
        },
        {
          title: "不确定性说明",
          body:
            "与伊朗停火、油气恢复、IPO 节奏相关的信息都受后续政策与市场动作影响。页面中未能拿到更强官方原始公告的条目，应按“近期判断”理解，而不是永久结论。",
        },
        {
          title: "怎么用这份简报",
          body:
            "这份页面更适合每天 5 到 10 分钟快速判断“现在该看什么、可以做什么”。如果某条信息会直接影响预算、采购或投资决策，建议继续点原文做二次核验。",
        },
      ];

      const trendJudgement =
        "今天几条线索连起来后很清楚：第一，AI 生态的主战场正在从模型能力竞争转向基础设施竞争，重点是仓库接入、浏览器执行、生成式 UI、云上工具链和系统级分发入口；第二，资本市场重新奖励能讲“基础设施故事”的科技公司，但能源与地缘风险仍然决定着估值上限和企业预算弹性。对开发者和产品团队最现实的动作不是再追一个新模型，而是优先掌握那层能把 agent 接进真实工作流的通用基础设施。";

      function Pill({ children, tone }) {
        const className = tone === "warn" ? "pill warn" : tone === "accent" ? "pill accent" : "pill";
        return <span className={className}>{children}</span>;
      }

      function Section({ id, title, desc, count, children }) {
        return (
          <section className="section-shell" id={id}>
            <div className="section-head">
              <div>
                <h2 className="mono">{title}</h2>
                <p>{desc}</p>
              </div>
              {count ? <div className="section-count mono">{count}</div> : null}
            </div>
            {children}
          </section>
        );
      }

      function Card({ item, showAudience = false }) {
        return (
          <article className="card">
            <div className="card-top">
              <div>
                <div className="pill-row">
                  {item.tags.map((tag) => (
                    <span className="mini-tag" key={tag}>
                      {tag}
                    </span>
                  ))}
                </div>
                <a href={item.link} target="_blank" rel="noreferrer">
                  <h3>{item.title || item.name}</h3>
                </a>
              </div>
              <a className="source-link" href={item.link} target="_blank" rel="noreferrer">
                查看链接
              </a>
            </div>

            {item.usage ? (
              <div className="card-block">
                <strong>主要用途</strong>
                <p>{item.usage}</p>
              </div>
            ) : null}

            <div className={`card-block ${item.usage ? "" : "accent"}`}>
              <strong>{item.highlights ? "核心亮点" : "事件摘要"}</strong>
              <p>{item.highlights || item.summary}</p>
            </div>

            <div className="card-block warn">
              <strong>{item.whyNow ? "为什么现在值得看" : "影响判断"}</strong>
              <p>{item.whyNow || item.impact}</p>
            </div>

            {showAudience ? (
              <div className="card-block">
                <strong>适合关注的人群</strong>
                <p>{item.audience}</p>
              </div>
            ) : null}

            <div className="card-footer">
              <span className="source-note">{item.source}</span>
            </div>
          </article>
        );
      }

      function TrendCard({ item, tone }) {
        return (
          <article className="trend-card">
            <div className="pill-row">
              <Pill tone={tone}>趋势观察</Pill>
            </div>
            <h3>{item.title}</h3>
            <p style={{ marginTop: "10px" }}>{item.body}</p>
          </article>
        );
      }

      function IdeaCard({ item }) {
        return (
          <article className="trend-card">
            <div className="pill-row">
              <Pill tone="accent">Vibe Coding</Pill>
              <span className="mini-tag">{item.stack}</span>
            </div>
            <h3>{item.title}</h3>
            <div className="card-block" style={{ marginTop: "14px" }}>
              <strong>可以做什么</strong>
              <p>{item.what}</p>
            </div>
            <div className="card-block accent">
              <strong>MVP 起手思路</strong>
              <p>{item.mvp}</p>
            </div>
          </article>
        );
      }

      function App() {
        return (
          <main className="page">
            <header className="hero">
              <div className="hero-grid">
                <div>
                  <Pill>中文每日简报</Pill>
                  <h1 className="mono">GitHub 热门项目、科技动态与商业信号</h1>
                  <p className="hero-intro">
                    这份日报把 2026 年 6 月 15 日前后最值得开发者和产品团队关注的 GitHub 开源项目、
                    科技动态与宏观新闻放在一页里看。今天的共识很清楚：AI 不再只是比谁模型更强，而是开始比谁更能接进真实工作流、掌握入口、压低成本并形成稳定交付。
                  </p>
                  <div className="hero-meta">
                    <div className="hero-meta-card">
                      <span className="label mono">Date</span>
                      <span className="value mono">{briefDate}</span>
                    </div>
                    <div className="hero-meta-card">
                      <span className="label mono">Coverage</span>
                      <span className="value">7 个 GitHub 项目 + 6 条科技热点 + 6 条新闻热点</span>
                    </div>
                    <div className="hero-meta-card">
                      <span className="label mono">Reader Lens</span>
                      <span className="value">开发者、产品、投资、企业经营</span>
                    </div>
                  </div>
                </div>

                <aside className="hero-side">
                  <h2 className="mono">今日速览</h2>
                  <ul>
                    <li>
                      <strong>GitHub 主线</strong>
                      <p>代码仓库接入、浏览器执行、agent 前端层继续升温，MCP 正在从概念进入默认工程层。</p>
                    </li>
                    <li>
                      <strong>科技主线</strong>
                      <p>OpenAI、Apple、Cloudflare、SpaceX 把 AI 竞争拉进资本市场、操作系统入口和开发者工具链。</p>
                    </li>
                    <li>
                      <strong>新闻主线</strong>
                      <p>油价回落改善市场情绪，但供应恢复仍慢；通胀和关税并未退场，企业预算仍需保守处理。</p>
                    </li>
                  </ul>
                </aside>
              </div>
            </header>

            <nav className="section-nav">
              <a href="#summary">日报摘要</a>
              <a href="#github">GitHub 开源项目观察</a>
              <a href="#tech">每日科技热点</a>
              <a href="#news">每日新闻热点</a>
              <a href="#ideas">Vibe Coding 建议</a>
            </nav>

            <section className="summary-grid" id="summary">
              {topSummary.map((item) => (
                <article className="summary-card" key={item.title}>
                  <Pill tone={item.tone}>{item.label}</Pill>
                  <h3 style={{ marginTop: "12px" }}>{item.title}</h3>
                  <p style={{ marginTop: "12px" }}>{item.body}</p>
                </article>
              ))}
            </section>

            <Section
              id="github"
              title="GitHub 开源项目观察"
              desc="优先选择最近仍活跃、定位清楚、容易让开发者快速理解，且能映射到真实工作流的开源项目。今天的共同点是：它们都在把 agent 从“会说”推进到“会做”。"
              count="7 个值得关注项目"
            >
              <div className="card-grid">
                {githubProjects.map((item) => (
                  <Card item={item} key={item.name} />
                ))}
              </div>

              <div className="muted-line">项目之间的趋势观察</div>
              <div className="trend-grid" style={{ marginTop: "12px" }}>
                {githubTrends.map((item, index) => (
                  <TrendCard item={item} tone={index % 2 === 0 ? "brand" : "accent"} key={item.title} />
                ))}
              </div>
            </Section>

            <Section
              id="tech"
              title="每日科技热点"
              desc="聚焦 AI、开发者工具、开源生态、硬件、云平台和企业软件入口。每条都补一层“为什么重要”，而不是只复述新闻。"
              count="6 条科技热点"
            >
              <div className="card-grid">
                {techNews.map((item) => (
                  <Card item={item} key={item.title} showAudience />
                ))}
              </div>
            </Section>

            <Section
              id="news"
              title="每日新闻热点"
              desc="只保留对商业、科技、消费、产业和资本市场判断有帮助的综合新闻，尽量避开低信息密度内容。"
              count="6 条新闻热点"
            >
              <div className="card-grid">
                {newsHotspots.map((item) => (
                  <Card item={item} key={item.title} />
                ))}
              </div>
            </Section>

            <Section
              id="ideas"
              title="Vibe Coding 项目建议"
              desc="这些建议都尽量贴近今天的热点主线，重点不是做概念展示，而是快速做出一个能跑、能演示、能继续接接口的 MVP。"
              count="4 个可执行方向"
            >
              <div className="idea-grid">
                {vibeIdeas.map((item) => (
                  <IdeaCard item={item} key={item.title} />
                ))}
              </div>
            </Section>

            <Section
              id="trend"
              title="今日总趋势判断"
              desc="把 GitHub、科技新闻和综合新闻放在一起看，能更清楚地看到今天真正发生的结构性变化。"
            >
              <div className="footer-panel" style={{ marginTop: 0 }}>
                <Pill>总趋势判断</Pill>
                <h2 className="mono" style={{ marginTop: "12px", fontSize: "1.4rem", letterSpacing: "-0.03em" }}>
                  AI 竞争进入基础设施阶段，能源与利率继续决定科技投入节奏
                </h2>
                <p>{trendJudgement}</p>
              </div>
            </Section>

            <Section
              id="notes"
              title="说明与使用建议"
              desc="这部分用于说明信息口径、不确定性和后续接入真实接口时应该保持的原则。"
            >
              <div className="note-grid">
                {notes.map((item) => (
                  <article className="note-card" key={item.title}>
                    <Pill tone="accent">Notes</Pill>
                    <h3 style={{ marginTop: "12px" }}>{item.title}</h3>
                    <p style={{ marginTop: "10px" }}>{item.body}</p>
                  </article>
                ))}
              </div>
              <p className="muted-line">
                标注规则：本页所有 GitHub star 数和仓库定位均以 2026-06-15 抓取到的仓库首页为准；新闻按最近可查来源整理。
                若后续官方口径变化，应以原始来源的最新公告为准。
              </p>
            </Section>
          </main>
        );
      }

      ReactDOM.createRoot(document.getElementById("root")).render(<App />);
    