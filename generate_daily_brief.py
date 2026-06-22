from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


REPO = Path(__file__).resolve().parent
BRIEFS_DIR = REPO / "briefs"
REPORT_DATE = "2026-06-22"

SWITCHER_DAYS = [
    {"date": "2026-06-22", "href": "/14760/"},
    {"date": "2026-06-18", "href": "/14760/briefs/2026-06-18.html"},
    {"date": "2026-06-17", "href": "/14760/briefs/2026-06-17.html"},
    {"date": "2026-06-16", "href": "/14760/briefs/2026-06-16.html"},
    {"date": "2026-06-15", "href": "/14760/briefs/2026-06-15.html"},
    {"date": "2026-06-12", "href": "/14760/briefs/2026-06-12.html"},
]

REPORT = {
    "date": REPORT_DATE,
    "title": "每日 GitHub + 科技新闻热点简报",
    "summary": (
        "今天最值得盯住的，不是又多了几个 AI 概念，而是 AI 正在同时穿透开发流程、"
        "电力与算力基础设施、终端入口和全球经营约束。GitHub 热门项目继续向 agent 执行、"
        "协议标准化、运行时和评测工程集中；科技与综合新闻则共同说明，真正能持续受益的玩家，"
        "会是那些能把 AI 接进真实流程、真实供给和真实监管框架里的团队。"
    ),
    "stats": [
        {"value": "8", "label": "GitHub 项目"},
        {"value": "6", "label": "科技热点"},
        {"value": "6", "label": "新闻热点"},
        {"value": "4", "label": "Vibe 建议"},
    ],
    "githubProjects": [
        {
            "name": "langgenius/dify",
            "url": "https://github.com/langgenius/dify",
            "stars": "146k",
            "source": "GitHub 仓库页",
            "tags": ["Agent Workflow", "LLMOps", "RAG", "Low-code"],
            "purpose": "面向生产环境的智能体应用开发平台，把知识库、工作流编排、模型接入和上线交付串成闭环。",
            "highlight": "它的优势不是单点功能，而是把“从 Demo 到可维护系统”的路径压短，适合团队快速验证和交付 AI 应用。",
            "whyNow": "企业现在更关心怎么把 AI 系统做成稳定产品，Dify 正好踩中这条最务实的落地链路。",
        },
        {
            "name": "OpenHands/OpenHands",
            "url": "https://github.com/OpenHands/OpenHands",
            "stars": "77.9k",
            "source": "GitHub 仓库页",
            "tags": ["AI Coding", "Agent", "Developer Tools"],
            "purpose": "让 AI 直接操作代码库、终端和任务流程，而不是停留在聊天式建议层。",
            "highlight": "项目核心价值在执行闭环和长任务延续能力，越来越接近“可托管开发代理”而不是代码补全插件。",
            "whyNow": "AI 编程的竞争重点，已经从会不会写代码，转向能不能持续完成复杂工程任务。",
        },
        {
            "name": "daytonaio/daytona",
            "url": "https://github.com/daytonaio/daytona",
            "stars": "72.4k",
            "source": "GitHub 仓库页",
            "tags": ["Sandbox", "Runtime", "Infra", "AI Code"],
            "purpose": "为 AI 生成代码提供安全、弹性、可隔离的运行环境。",
            "highlight": "它把执行层抽象成可调度资源，这对 agent、批处理开发任务和云端代码运行都非常关键。",
            "whyNow": "大家开始意识到，最稀缺的并不是 prompt，而是稳定、可观测、可隔离的执行环境。",
        },
        {
            "name": "modelcontextprotocol/servers",
            "url": "https://github.com/modelcontextprotocol/servers",
            "stars": "87.5k",
            "source": "GitHub 仓库页",
            "tags": ["MCP", "Protocol", "Integrations"],
            "purpose": "MCP 生态里最直观的服务端集合，帮助模型统一接入工具、数据和外部系统。",
            "highlight": "它的重要性不在某个单独 server，而在于它证明了 AI 工具接入层正在快速标准化。",
            "whyNow": "谁掌握协议和工具生态，谁就更有机会占住下一轮 AI 平台层入口。",
        },
        {
            "name": "continuedev/continue",
            "url": "https://github.com/continuedev/continue",
            "stars": "34.2k",
            "source": "GitHub 仓库页",
            "tags": ["IDE", "Coding Agent", "Open Source"],
            "purpose": "开源 AI 编程代理，嵌入 IDE 使用，强调团队可控性和自定义能力。",
            "highlight": "团队可以按自己的模型、规则和上下文策略定义开发体验，不必完全依赖闭源路线。",
            "whyNow": "企业对 AI 开发栈的可控性要求持续上升，Continue 是开源团队助手路线的代表样本。",
        },
        {
            "name": "marimo-team/marimo",
            "url": "https://github.com/marimo-team/marimo",
            "stars": "21.5k",
            "source": "GitHub 仓库页",
            "tags": ["Python", "Notebook", "Reactive", "Data App"],
            "purpose": "响应式 Python notebook，可做实验、查数据、导出脚本，也能直接部署成应用。",
            "highlight": "它把 notebook、脚本和轻应用三者之间的边界打薄，非常适合 AI 实验快速产品化。",
            "whyNow": "越来越多团队需要把探索式工作流尽快变成可共享工具，marimo 很适合做这座桥梁。",
        },
        {
            "name": "promptfoo/promptfoo",
            "url": "https://github.com/promptfoo/promptfoo",
            "stars": "22.4k",
            "source": "GitHub 仓库页",
            "tags": ["AI Eval", "Security", "CI/CD", "Red Team"],
            "purpose": "对 prompts、agents 和 RAG 系统做评测、回归测试与安全扫描。",
            "highlight": "它把 AI 评测真正工程化了，能直接进入 CI，并覆盖越权、幻觉和提示注入等风险点。",
            "whyNow": "模型能力趋同后，能不能稳定评测和控风险，正在变成团队是否敢上线 AI 的分水岭。",
        },
        {
            "name": "google/adk-python",
            "url": "https://github.com/google/adk-python",
            "stars": "20.2k",
            "source": "GitHub 仓库页",
            "tags": ["Agent SDK", "Python", "Google"],
            "purpose": "Google 的开源、代码优先 Python 工具包，用于构建、评估和部署复杂 AI agents。",
            "highlight": "它的信号价值大于单一功能，说明大厂也在把 agent 框架推向更开放、可组合的开发范式。",
            "whyNow": "当多家平台都在争夺 agent 开发层，开发者最该关注的是 API 形态、可迁移性和生态黏性。",
        },
    ],
    "projectTrends": [
        "热门项目继续从“模型更强”转向“系统更完整”：协议、运行时、评测和 IDE 工作流正在成为新焦点。",
        "开源 AI 编程工具不再只拼补全体验，而是拼多步骤执行、上下文延续、团队治理和可运维性。",
        "Python 数据实验工作流正在快速产品化，notebook 与轻应用之间的边界会继续被压薄。",
    ],
    "techHotspots": [
        {
            "title": "美国监管层要求电网运营商加速为 AI 数据中心接电",
            "source": "AP News · 2026-06-18",
            "url": "https://apnews.com/article/506e3d206871111f15c3c62fc5368be5",
            "tags": ["AI", "Data Center", "Power Grid", "Cloud"],
            "summary": "美国联邦能源监管机构要求区域电网运营商简化大型用电项目接网流程，直接回应 AI 数据中心的电力饥渴问题。",
            "impact": "这件事重要，因为算力瓶颈已经从 GPU 延伸到电力和并网审批。未来云计算竞争不只是买芯片，更是拿电、拿地和拿建设周期。",
            "audience": "云基础设施团队、数据中心投资人、AI 平台公司、能源与园区从业者。",
        },
        {
            "title": "Nvidia 联合 Coherent 在德州推进 AI 光互连制造",
            "source": "AP News · 2026-06-16",
            "url": "https://apnews.com/article/9bf560fa2365e4d6b57804438cda579e",
            "tags": ["Nvidia", "Manufacturing", "Optics", "AI Infra"],
            "summary": "Nvidia 与 Coherent 推进价值 20 亿美元的设施升级，生产用于高速 AI 芯片互连的光学组件，并主打更低功耗、更高带宽。",
            "impact": "市场关注点正在从 GPU 本身向互连和系统级效率扩散。谁能解决芯片之间怎么更快、更省电地协同，谁就能吃到下一段基础设施红利。",
            "audience": "芯片产业链、AI Infra 创业者、硬件投资人、服务器与网络设备团队。",
        },
        {
            "title": "黄仁勋称 AI 时代需要“新的社会规范”",
            "source": "AP News · 2026-06-16",
            "url": "https://apnews.com/article/8334abcbc6ed8d3d7889b640ec6fa05b",
            "tags": ["AI", "Policy", "Nvidia", "Society"],
            "summary": "黄仁勋在接受 AP 采访时强调，社会需要更积极地使用 AI，也需要新的制度与行为规范来消化它带来的就业和治理变化。",
            "impact": "这反映出行业主旋律已经从“AI 能不能用”转向“AI 用到什么边界、怎么治理”。对企业来说，合规与组织设计会越来越接近产品能力本身。",
            "audience": "企业管理层、政策研究者、AI 产品经理、人力与组织负责人。",
        },
        {
            "title": "Microsoft Build 2026 把焦点压到企业级 agent 栈",
            "source": "Tom's Guide · 2026-06-02",
            "url": "https://www.tomsguide.com/news/live/microsoft-build-2026",
            "tags": ["Microsoft", "GitHub Copilot", "Agent", "Developer Tools"],
            "summary": "微软在 Build 2026 上集中展示 GitHub Copilot app、Microsoft IQ、企业长任务 agent 和新型 AI 开发硬件。",
            "impact": "这说明大厂已经把竞争从单模型能力拉到完整 agent 平台，包括上下文层、执行层和企业治理层。开发者工具会更深度绑定平台生态。",
            "audience": "企业开发平台团队、Copilot 用户、ISV、AI 工具创业者。",
        },
        {
            "title": "Google 向 Pixel 推送 Android 17 与新一轮 Gemini 功能",
            "source": "The Verge · 2026-06-17",
            "url": "https://www.theverge.com/tech/950651/android-17-release-pixel-drop-google-bubble-screen-reaction",
            "tags": ["Google", "Android 17", "Gemini", "Consumer AI"],
            "summary": "Android 17 与 6 月 Pixel Drop 一起上线，带来新的多任务交互和 Gemini 视频、音乐等生成能力扩展。",
            "impact": "消费电子侧的 AI 正在从“单点助手”走向操作系统级入口。谁控制设备端的原生工作流，谁就更容易把模型能力沉淀为用户习惯。",
            "audience": "移动产品团队、终端厂商、开发者工具厂商、消费 AI 创业者。",
        },
        {
            "title": "Uber 为 robotaxi 时代开始重资产建设补能与运维节点",
            "source": "Axios · 2026-06-17",
            "url": "https://www.axios.com/2026/06/17/why-uber-is-spending-big-on-robotaxi-depots-and-charging-infrastructure",
            "tags": ["Robotaxi", "Uber", "Autonomous Driving", "Infrastructure"],
            "summary": "Uber 正为 robotaxi 网络建设充电、维护和调度基础设施，明显偏离其过去更轻资产的平台模式。",
            "impact": "自动驾驶商业化已经进入基础设施阶段，不再只是算法竞赛。真正的护城河会落在调度、补能、维修和城市落地能力上。",
            "audience": "自动驾驶公司、出行平台、车队运营商、城市基础设施投资方。",
        },
    ],
    "generalNews": [
        {
            "title": "美伊在瑞士继续谈判，停火与航运安排仍待进一步确认",
            "source": "AP News · 2026-06-22",
            "url": "https://apnews.com/article/2edf9268aae550883252080014013963",
            "tags": ["Iran", "Oil", "Shipping", "Geopolitics"],
            "summary": "美国与伊朗代表团继续围绕核问题、霍尔木兹海峡通行和资产解冻等细节谈判，但政治表态仍强硬，协议执行细节并未完全落定。",
            "impact": "这直接影响能源、航运和风险资产定价。市场虽然会交易停火预期，但真正决定企业预算的仍是执行条款和持续稳定性。",
            "note": "待进一步确认：谈判仍在进行，后续正式文本和执行机制可能继续变化。",
        },
        {
            "title": "G7 再度把乌克兰援助与对俄制裁拉回核心议程",
            "source": "AP News · 2026-06-18",
            "url": "https://apnews.com/article/d2748517274f3c0da4641b08d16df255",
            "tags": ["G7", "Ukraine", "Sanctions", "Defense"],
            "summary": "G7 领导人承诺继续向乌克兰提供防空、能源和财政支持，并强化对俄罗斯的经济压力。",
            "impact": "这意味着欧洲能源、国防与供应链不确定性并没有退场，只是从中东风险重新切回东欧风险。",
        },
        {
            "title": "“China Shock 2.0” 正成为欧洲产业政策的新压力源",
            "source": "AP News · 2026-06-16",
            "url": "https://apnews.com/article/edd7a75a090afca912b4650bcceb562d",
            "tags": ["China", "Europe", "Trade", "Manufacturing"],
            "summary": "中国出口外溢继续冲击欧洲制造业，而且已扩展到高端设备、新能源链条和工业品领域。",
            "impact": "欧洲的本地制造、补贴和贸易保护只会更强。对中国企业和跨国品牌来说，欧洲业务的政治与合规成本会继续上升。",
        },
        {
            "title": "美联储按兵不动，但点阵图显著转向鹰派",
            "source": "AP News · 2026-06-16",
            "url": "https://apnews.com/article/103325df845d2d6bde63dfa4b8093d35",
            "tags": ["Fed", "Rates", "Markets", "Capital"],
            "summary": "美联储维持利率不变，但多位官员转向支持年内加息，市场因此重新评估风险资产定价。",
            "impact": "对高投入、长回报周期的 AI 与硬科技赛道来说，这意味着融资窗口并没有真正放松，资本成本仍会压制扩张节奏。",
        },
        {
            "title": "美国上诉法院允许 10% 全球关税暂时继续执行",
            "source": "AP News · 2026-06-11",
            "url": "https://apnews.com/article/a95ef7309d89018477a3265ebf93d620",
            "tags": ["Tariffs", "Trade", "Supply Chain", "Policy"],
            "summary": "美国法院允许特朗普政府在诉讼期间继续征收 10% 全球关税，最终合法性仍可能打到更高法院。",
            "impact": "对跨境供应链企业而言，短期最关键的不是关税是否永久存在，而是政策不确定性本身已经足够推高定价与备货压力。",
        },
        {
            "title": "伊朗战事即使降温，油价和消费端涨价也不会立刻回落",
            "source": "AP News · 2026-06-17",
            "url": "https://apnews.com/article/9c413bc111efcfa9bac53b20e9057738",
            "tags": ["Oil", "Inflation", "Logistics", "Consumer"],
            "summary": "AP 采访的能源与供应链专家普遍认为，即便停火推进，燃油、食品和航空票价等价格压力仍会持续一段时间。",
            "impact": "这对企业经营判断很重要，因为宏观风险不是新闻停了就结束，库存、保险、运力和合同重定价都会滞后传导。",
        },
    ],
    "vibeIdeas": [
        {
            "title": "MCP Connector Radar",
            "tags": ["MCP", "React", "Node.js"],
            "what": "做一个 MCP 连接器观察站，展示不同 server 的能力边界、权限类型、最近更新和典型使用场景。",
            "stack": "React、Vite、普通 CSS、GitHub API、静态 JSON；需要时再补 SQLite。",
            "mvp": "先收录 30 个常见 MCP server，完成搜索、标签过滤和一键复制配置片段。",
        },
        {
            "title": "Agent Runtime Ops Board",
            "tags": ["Daytona", "OpenHands", "Charts"],
            "what": "做一个 agent 运行看板，跟踪任务耗时、失败率、重试次数和单次执行成本。",
            "stack": "React、Recharts、Node.js；需要持久化时接 Supabase/Postgres。",
            "mvp": "先用 mock 数据覆盖 3 类任务，做任务列表、趋势图和失败原因面板。",
        },
        {
            "title": "Prompt Security Regression Lab",
            "tags": ["promptfoo", "CI", "Security"],
            "what": "把 promptfoo 包成团队内部小工具，持续检查越权、泄漏、幻觉和回归风险。",
            "stack": "TypeScript、Node.js、promptfoo、GitHub Actions。",
            "mvp": "先支持 YAML 配置上传、单次评测运行和历史结果对比，再接入 PR 检查。",
        },
        {
            "title": "Notebook to App Studio",
            "tags": ["marimo", "Python", "Data App"],
            "what": "做一个把 marimo notebook 快速打包成轻应用的模板站，降低数据实验产品化门槛。",
            "stack": "Python、marimo、FastAPI、轻量静态前端。",
            "mvp": "先做两个模板：数据查询助手和日报生成器，并写清本地运行与静态部署说明。",
        },
    ],
    "totalTrend": (
        "今天背后的共同趋势非常集中：AI 正在从“模型热度竞争”进入“基础设施与约束条件竞争”。"
        "GitHub 热门项目里，协议、运行时、评测和团队级开发代理越来越重要，说明开发者真正关心的是怎么把 AI 变成可持续交付能力；"
        "科技新闻里，电网、光互连、终端系统和 robotaxi 运维都在提醒我们，下一轮价值分配会落在真实执行层；"
        "宏观与国际新闻则继续告诉市场，能源、利率、关税和地缘政治没有退场。最值得下注的方向，不是讲故事最热的 AI，"
        "而是那些能在真实成本、真实供给和真实监管之下稳定工作的产品与基础设施。"
    ),
    "footer": (
        "数据说明：GitHub 项目部分基于 GitHub 仓库页公开元数据；科技与新闻热点优先引用 AP News、Axios、The Verge 等可信媒体。"
        "标注“待进一步确认”的项目，表示执行细节或正式文本仍可能变化。"
    ),
}


def make_switcher_js() -> str:
    days_json = json.dumps(SWITCHER_DAYS, ensure_ascii=False, indent=2)
    return dedent(
        f"""\
        (function () {{
          var days = {days_json};

          var path = window.location.pathname.replace(/index\\.html$/, "");
          var currentDate = "{REPORT_DATE}";

          for (var i = 0; i < days.length; i += 1) {{
            if (path === days[i].href.replace(/index\\.html$/, "")) {{
              currentDate = days[i].date;
              break;
            }}
          }}

          var nav = document.createElement("nav");
          nav.className = "brief-switcher";

          var label = document.createElement("span");
          label.className = "brief-switcher-label";
          label.textContent = "切换简报日期";

          var buttons = document.createElement("div");
          buttons.className = "brief-switcher-buttons";

          for (var j = 0; j < days.length; j += 1) {{
            var item = days[j];
            var link = document.createElement("a");
            link.className = "brief-switcher-button" + (item.date === currentDate ? " is-active" : "");
            link.href = item.href;
            link.textContent = item.date;
            buttons.appendChild(link);
          }}

          nav.appendChild(label);
          nav.appendChild(buttons);

          var spacer = document.createElement("div");
          spacer.className = "brief-switcher-spacer";

          document.body.insertBefore(nav, document.body.firstChild);
          document.body.insertBefore(spacer, nav.nextSibling);
        }})();
        """
    )


def make_html(asset_prefix: str) -> str:
    report_json = json.dumps(REPORT, ensure_ascii=False, indent=2)
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="zh-CN">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{REPORT["title"]}</title>
            <meta name="description" content="{REPORT["date"]} 中文日报：GitHub 开源项目观察、科技热点、新闻热点、Vibe Coding 建议与总趋势判断。" />
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
            <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet" />
            <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
            <style>
              :root {{
                --bg: #f3eee6;
                --bg-2: #e4d9c8;
                --panel: rgba(255, 251, 246, 0.94);
                --panel-strong: #fffdfa;
                --text: #17212a;
                --muted: #617080;
                --line: rgba(23, 33, 42, 0.1);
                --brand: #0f6863;
                --brand-soft: rgba(15, 104, 99, 0.1);
                --accent: #b96c35;
                --accent-soft: rgba(185, 108, 53, 0.12);
                --warn: #93463b;
                --warn-soft: rgba(147, 70, 59, 0.11);
                --shadow: 0 24px 64px rgba(18, 28, 36, 0.12);
                --radius-xl: 30px;
                --radius-lg: 24px;
                --radius-md: 18px;
              }}

              * {{ box-sizing: border-box; }}
              html {{ scroll-behavior: smooth; }}
              body {{
                margin: 0;
                color: var(--text);
                font-family: "Noto Sans SC", system-ui, sans-serif;
                background:
                  radial-gradient(circle at top left, rgba(15, 104, 99, 0.16), transparent 24%),
                  radial-gradient(circle at top right, rgba(185, 108, 53, 0.14), transparent 22%),
                  linear-gradient(180deg, #fcf8f2 0%, var(--bg) 52%, var(--bg-2) 100%);
              }}
              a {{ color: inherit; text-decoration: none; }}
              .page {{ width: min(1240px, calc(100% - 28px)); margin: 0 auto; padding: 24px 0 84px; }}
              .mono {{ font-family: "Manrope", sans-serif; }}
              .hero {{
                position: relative;
                overflow: hidden;
                padding: 34px;
                border-radius: var(--radius-xl);
                border: 1px solid rgba(255, 255, 255, 0.68);
                background:
                  linear-gradient(135deg, rgba(15, 104, 99, 0.98), rgba(14, 30, 39, 0.98)),
                  linear-gradient(145deg, rgba(185, 108, 53, 0.28), transparent 48%);
                color: #f8fbfb;
                box-shadow: var(--shadow);
              }}
              .hero::after {{
                content: "";
                position: absolute;
                inset: auto -70px -90px auto;
                width: 310px;
                height: 310px;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(255, 255, 255, 0.18), transparent 66%);
              }}
              .eyebrow {{
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.1);
                font-size: 13px;
                letter-spacing: 0.04em;
              }}
              .hero-grid {{
                display: grid;
                grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.92fr);
                gap: 24px;
                margin-top: 20px;
              }}
              .hero h1 {{ margin: 0 0 14px; font-size: clamp(34px, 5vw, 56px); line-height: 1.03; }}
              .hero p {{ margin: 0; max-width: 760px; color: rgba(248, 251, 251, 0.84); font-size: 16px; line-height: 1.8; }}
              .snapshot, .toc, .section, .card, .summary-card {{
                border-radius: var(--radius-lg);
                border: 1px solid var(--line);
                background: var(--panel);
                backdrop-filter: blur(16px);
              }}
              .snapshot, .toc, .card, .summary-card {{ padding: 20px; }}
              .snapshot h2, .toc h2, .section h2 {{ margin: 0; font-size: 20px; }}
              .snapshot-grid {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 12px;
                margin-top: 16px;
              }}
              .metric {{
                padding: 14px;
                border-radius: 18px;
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.08);
              }}
              .metric strong {{ display: block; font-size: 26px; line-height: 1; }}
              .metric span {{ display: block; margin-top: 8px; font-size: 13px; color: rgba(248, 251, 251, 0.7); }}
              .toc ul {{ margin: 12px 0 0; padding: 0; list-style: none; display: grid; gap: 10px; }}
              .toc li {{ display: flex; align-items: center; gap: 12px; color: var(--muted); }}
              .toc-index {{
                width: 26px;
                height: 26px;
                border-radius: 50%;
                display: inline-grid;
                place-items: center;
                background: var(--brand-soft);
                color: var(--brand);
                font-size: 12px;
                font-weight: 800;
              }}
              .main {{ display: grid; gap: 22px; margin-top: 22px; }}
              .section {{ padding: 24px; box-shadow: var(--shadow); }}
              .section-head {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }}
              .section-desc {{ margin: 10px 0 0; color: var(--muted); font-size: 15px; line-height: 1.78; }}
              .chip-row, .tag-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
              .chip, .tag {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 8px 12px;
                border-radius: 999px;
                font-size: 12px;
                font-weight: 700;
              }}
              .chip {{ background: var(--brand-soft); color: var(--brand); }}
              .tag {{ background: rgba(23, 33, 42, 0.06); color: var(--muted); }}
              .grid {{ display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 16px; margin-top: 20px; }}
              .span-4 {{ grid-column: span 4; }}
              .span-6 {{ grid-column: span 6; }}
              .span-12 {{ grid-column: span 12; }}
              .card-header {{ display: flex; justify-content: space-between; gap: 14px; align-items: flex-start; }}
              .card h3 {{ margin: 0; font-size: 21px; line-height: 1.34; }}
              .card-subtitle {{ margin: 6px 0 0; color: var(--muted); font-size: 13px; }}
              .stat {{
                min-width: 92px;
                padding: 10px 12px;
                border-radius: 16px;
                background: var(--accent-soft);
                color: var(--accent);
                text-align: right;
              }}
              .stat strong {{ display: block; font-size: 17px; }}
              .stat span {{ font-size: 12px; }}
              .summary-card {{ background: linear-gradient(160deg, rgba(15, 104, 99, 0.08), rgba(185, 108, 53, 0.06)); }}
              .card p, .summary-card p, .card li {{ margin: 0; color: var(--muted); font-size: 14px; line-height: 1.75; }}
              .key-block {{ margin-top: 16px; padding: 14px; border-radius: 16px; background: rgba(23, 33, 42, 0.04); }}
              .key-block strong, .mini-title {{ display: block; margin-bottom: 8px; color: var(--text); font-size: 13px; }}
              .list {{ margin: 14px 0 0; padding-left: 18px; display: grid; gap: 8px; }}
              .meta {{ margin-top: 16px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; justify-content: space-between; }}
              .source-link {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 10px 14px;
                border-radius: 999px;
                background: var(--panel-strong);
                border: 1px solid var(--line);
                color: var(--text);
                font-weight: 700;
                transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
              }}
              .source-link:hover {{
                transform: translateY(-2px);
                border-color: var(--brand);
                box-shadow: 0 12px 24px rgba(15, 104, 99, 0.12);
              }}
              .callout {{
                margin-top: 14px;
                padding: 12px 14px;
                border-radius: 14px;
                background: var(--warn-soft);
                color: var(--warn);
                font-size: 13px;
                line-height: 1.7;
              }}
              .footer {{ margin-top: 24px; padding: 18px 20px; color: var(--muted); font-size: 13px; line-height: 1.8; }}
              @media (max-width: 1100px) {{
                .hero-grid, .snapshot-grid {{ grid-template-columns: 1fr; }}
                .span-4, .span-6 {{ grid-column: span 12; }}
              }}
              @media (max-width: 720px) {{
                .page {{ width: min(100% - 18px, 1240px); padding-top: 16px; }}
                .hero, .section {{ padding: 20px; }}
                .snapshot, .toc, .card, .summary-card {{ padding: 16px; }}
                .section-head, .card-header {{ flex-direction: column; }}
                .stat {{ text-align: left; }}
                .hero h1 {{ font-size: 34px; }}
              }}
            </style>
            <link rel="stylesheet" href="{asset_prefix}switcher.css" />
            <script defer src="{asset_prefix}switcher.js"></script>
          </head>
          <body>
            <div id="root"></div>
            <script>
              (() => {{
                const report = {report_json};

                function Pill({{ children, tone = "default" }}) {{
                  return React.createElement("span", {{ className: tone === "chip" ? "chip" : "tag" }}, children);
                }}

                function SectionHeader({{ id, title, desc, chips = [] }}) {{
                  return React.createElement(
                    "div",
                    {{ id }},
                    React.createElement(
                      "div",
                      {{ className: "section-head" }},
                      React.createElement(
                        "div",
                        null,
                        React.createElement("h2", null, title),
                        React.createElement("p", {{ className: "section-desc" }}, desc)
                      ),
                      React.createElement(
                        "div",
                        {{ className: "chip-row" }},
                        chips.map((chip) => React.createElement(Pill, {{ key: chip, tone: "chip" }}, chip))
                      )
                    )
                  );
                }}

                function ProjectCard({{ item }}) {{
                  return React.createElement(
                    "article",
                    {{ className: "card span-6" }},
                    React.createElement(
                      "div",
                      {{ className: "card-header" }},
                      React.createElement(
                        "div",
                        null,
                        React.createElement("h3", null, item.name),
                        React.createElement("p", {{ className: "card-subtitle" }}, item.source)
                      ),
                      React.createElement(
                        "div",
                        {{ className: "stat" }},
                        React.createElement("strong", null, item.stars),
                        React.createElement("span", null, "GitHub Stars")
                      )
                    ),
                    React.createElement(
                      "div",
                      {{ className: "tag-row", style: {{ marginTop: 14 }} }},
                      item.tags.map((tag) => React.createElement(Pill, {{ key: tag }}, tag))
                    ),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "主要用途"), React.createElement("p", null, item.purpose)),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "核心亮点"), React.createElement("p", null, item.highlight)),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "为什么现在值得看"), React.createElement("p", null, item.whyNow)),
                    React.createElement(
                      "div",
                      {{ className: "meta" }},
                      React.createElement("span", {{ className: "mini-title" }}, "来源链接"),
                      React.createElement("a", {{ className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }}, "查看项目")
                    )
                  );
                }}

                function NewsCard({{ item }}) {{
                  return React.createElement(
                    "article",
                    {{ className: "card span-4" }},
                    React.createElement(
                      "div",
                      {{ className: "card-header" }},
                      React.createElement(
                        "div",
                        null,
                        React.createElement("h3", null, item.title),
                        React.createElement("p", {{ className: "card-subtitle" }}, item.source)
                      )
                    ),
                    React.createElement(
                      "div",
                      {{ className: "tag-row", style: {{ marginTop: 14 }} }},
                      item.tags.map((tag) => React.createElement(Pill, {{ key: tag }}, tag))
                    ),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "事件摘要"), React.createElement("p", null, item.summary)),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "影响判断"), React.createElement("p", null, item.impact)),
                    item.audience
                      ? React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "适合关注的人群"), React.createElement("p", null, item.audience))
                      : null,
                    item.note ? React.createElement("div", {{ className: "callout" }}, item.note) : null,
                    React.createElement(
                      "div",
                      {{ className: "meta" }},
                      React.createElement("span", {{ className: "mini-title" }}, "来源链接"),
                      React.createElement("a", {{ className: "source-link", href: item.url, target: "_blank", rel: "noreferrer" }}, "打开原文")
                    )
                  );
                }}

                function IdeaCard({{ item }}) {{
                  return React.createElement(
                    "article",
                    {{ className: "card span-6" }},
                    React.createElement("h3", null, item.title),
                    React.createElement(
                      "div",
                      {{ className: "tag-row", style: {{ marginTop: 14 }} }},
                      item.tags.map((tag) => React.createElement(Pill, {{ key: tag }}, tag))
                    ),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "可以做什么"), React.createElement("p", null, item.what)),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "适合技术栈 / 组件"), React.createElement("p", null, item.stack)),
                    React.createElement("div", {{ className: "key-block" }}, React.createElement("strong", null, "MVP 思路"), React.createElement("p", null, item.mvp))
                  );
                }}

                function App() {{
                  return React.createElement(
                    "div",
                    {{ className: "page" }},
                    React.createElement(
                      "header",
                      {{ className: "hero" }},
                      React.createElement("div", {{ className: "eyebrow mono" }}, "Daily Briefing · ", report.date),
                      React.createElement(
                        "div",
                        {{ className: "hero-grid" }},
                        React.createElement(
                          "div",
                          null,
                          React.createElement("h1", null, report.title),
                          React.createElement("p", null, report.summary),
                          React.createElement(
                            "div",
                            {{ className: "snapshot-grid", style: {{ marginTop: 20 }} }},
                            report.stats.map((stat) =>
                              React.createElement(
                                "div",
                                {{ className: "metric", key: stat.label }},
                                React.createElement("strong", {{ className: "mono" }}, stat.value),
                                React.createElement("span", null, stat.label)
                              )
                            )
                          )
                        ),
                        React.createElement(
                          "div",
                          {{ style: {{ display: "grid", gap: 14, alignContent: "start" }} }},
                          React.createElement(
                            "div",
                            {{ className: "toc" }},
                            React.createElement("h2", null, "阅读导航"),
                            React.createElement(
                              "ul",
                              null,
                              ["GitHub 开源项目观察", "每日科技热点", "每日新闻热点", "Vibe Coding 项目建议", "今日总趋势判断"].map((item, index) =>
                                React.createElement(
                                  "li",
                                  {{ key: item }},
                                  React.createElement("span", {{ className: "toc-index mono" }}, index + 1),
                                  React.createElement("span", null, item)
                                )
                              )
                            )
                          ),
                          React.createElement(
                            "div",
                            {{ className: "snapshot" }},
                            React.createElement("h2", null, "一句话判断"),
                            React.createElement(
                              "p",
                              {{ style: {{ marginTop: 14, color: "rgba(248, 251, 251, 0.78)", lineHeight: 1.8 }} }},
                              "这份日报最重要的信号是：AI 的决定性竞争点，正在从模型能力本身，转向协议、运行环境、供电、互连、终端入口和合规执行。"
                            )
                          )
                        )
                      )
                    ),
                    React.createElement(
                      "main",
                      {{ className: "main" }},
                      React.createElement(
                        "section",
                        {{ className: "section" }},
                        React.createElement(SectionHeader, {{
                          id: "github",
                          title: "模块一 · GitHub 开源项目观察",
                          desc: "优先选择最近仍活跃、增长明显，并且适合开发者快速理解的工程化与基础设施项目。",
                          chips: ["Active", "Open Source", "Builders First"],
                        }}),
                        React.createElement(
                          "div",
                          {{ className: "grid" }},
                          report.githubProjects.map((item) => React.createElement(ProjectCard, {{ key: item.name, item }})),
                          React.createElement(
                            "div",
                            {{ className: "summary-card span-12" }},
                            React.createElement("h3", {{ style: {{ margin: 0, fontSize: 21 }} }}, "项目趋势观察"),
                            React.createElement(
                              "ol",
                              {{ className: "list" }},
                              report.projectTrends.map((trend) => React.createElement("li", {{ key: trend }}, trend))
                            )
                          )
                        )
                      ),
                      React.createElement(
                        "section",
                        {{ className: "section" }},
                        React.createElement(SectionHeader, {{
                          id: "tech",
                          title: "模块二 · 每日科技热点",
                          desc: "优先保留对 AI、云基础设施、终端入口、机器人和开发者工具真正有判断价值的事件。",
                          chips: ["AI", "Cloud", "Hardware", "Robotics"],
                        }}),
                        React.createElement("div", {{ className: "grid" }}, report.techHotspots.map((item) => React.createElement(NewsCard, {{ key: item.title, item }})))
                      ),
                      React.createElement(
                        "section",
                        {{ className: "section" }},
                        React.createElement(SectionHeader, {{
                          id: "news",
                          title: "模块三 · 每日新闻热点",
                          desc: "只保留对商业、产业、资本市场、供应链和国际经营环境有实质影响的信息。",
                          chips: ["Macro", "Trade", "Energy", "Policy"],
                        }}),
                        React.createElement("div", {{ className: "grid" }}, report.generalNews.map((item) => React.createElement(NewsCard, {{ key: item.title, item }})))
                      ),
                      React.createElement(
                        "section",
                        {{ className: "section" }},
                        React.createElement(SectionHeader, {{
                          id: "vibe",
                          title: "模块四 · Vibe Coding 项目建议",
                          desc: "基于今天的 GitHub 和科技信号，挑出这周就能启动的 4 个可执行方向。",
                          chips: ["MVP Ready", "Actionable"],
                        }}),
                        React.createElement("div", {{ className: "grid" }}, report.vibeIdeas.map((item) => React.createElement(IdeaCard, {{ key: item.title, item }})))
                      ),
                      React.createElement(
                        "section",
                        {{ className: "section" }},
                        React.createElement(SectionHeader, {{
                          id: "trend",
                          title: "模块五 · 今日总趋势判断",
                          desc: "把今天分散的开源项目、科技动态和宏观新闻，收束成一个更可执行的判断。",
                          chips: ["Signal", "Decision"],
                        }}),
                        React.createElement("div", {{ className: "summary-card" }}, React.createElement("p", {{ style: {{ fontSize: 15, color: "var(--text)", lineHeight: 1.92 }} }}, report.totalTrend))
                      )
                    ),
                    React.createElement("footer", {{ className: "footer" }}, report.footer)
                  );
                }}

                ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
              }})();
            </script>
          </body>
        </html>
        """
    )


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    BRIEFS_DIR.mkdir(exist_ok=True)
    write_text(REPO / "switcher.js", make_switcher_js())
    write_text(REPO / "index.html", make_html("./"))
    write_text(BRIEFS_DIR / f"{REPORT_DATE}.html", make_html("../"))


if __name__ == "__main__":
    main()
