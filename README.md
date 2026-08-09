# 赛博黑影儿 · Public Skills

面向跑者的公开 Skills：用证据还原训练，用边界约束结论，再给一个低风险、可验证的下一步。

当前版本：`v1.1.0`

发布日期：`2026-08-09`

## 已发布 Skills

### ShadowRunner

`shadowrunner/` 是原创的跑者—创作者决策框架：先判断阶段与瓶颈，核对建议的适用范围，再设计低风险、可回滚、可验证的下一步。

适合训练瓶颈、长期项目、方法筛选和内容表达。它不是真实人物的数字分身，也不提供医疗诊断、伤病判断、个体化训练处方、营养处方或成绩承诺。

示例：

```text
使用 $shadowrunner 分析我最近的跑步瓶颈；先说明还缺什么信息，不要直接给训练剂量。
```

### COROS 训练复盘｜赛博黑影儿

`coros-workout-review/` 会先检查 COROS 连接、授权、同步与数据完整性，再把单次跑步拆成训练结构、关键证据、主要问题和下一步。它已内置赛博黑影儿的阶段—瓶颈、适用域、边际收益和最小可逆验证框架，不依赖另行安装 `shadowrunner/`。

第一版中，ChatGPT Work、ChatGPT 桌面版中的 Codex 与 Codex CLI 统一优先从官方插件目录搜索并连接 COROS；Codex 桌面版的具体入口是“插件 → 浏览目录（Plugins → Browse directory）”。Claude remote connector 与 OpenClaw 也属于推荐/正式路径。高级/兼容路径覆盖 Claude Code、Gemini CLI、Cursor 与 VS Code；Kimi Claw、Cline、Chatbox、Cherry Studio 采用条件、有限或实验引导。对官方尚未证实的连接能力会明确停止，不生成猜测配置。

示例：

```text
使用 $coros-workout-review 检查我的 COROS 连接，并复盘最近一次跑步训练。
```

这是独立社区项目，不代表 COROS，也不暗示 COROS 或任何 AI 客户端为分析结论背书。

## 安装

克隆仓库：

```bash
git clone https://github.com/leeeboo/public-skills.git
mkdir -p "$HOME/.agents/skills"
```

按需链接一个或两个 Skill：

```bash
ln -s "$(pwd)/public-skills/shadowrunner" "$HOME/.agents/skills/shadowrunner"
ln -s "$(pwd)/public-skills/coros-workout-review" "$HOME/.agents/skills/coros-workout-review"
```

如果目标位置已经存在，请先自行备份；不要让软链接覆盖尚未保存的私有版本。Codex/Agents 宿主需要支持以 `SKILL.md` 为入口的本地 Skill。

`shadowrunner` 不需要运行时依赖；`coros-workout-review` 已包含其训练复盘所需的核心方法，不需要额外安装 `shadowrunner/`。它仍需要 COROS 账号，以及支持 COROS 插件或 remote MCP + 浏览器授权的 AI 客户端；它不会要求用户把 COROS 密码或 Token 发进聊天。

## 目录

```text
public-skills/
├── .gitattributes
├── README.md
├── CHANGELOG.md
├── LICENSE
├── NOTICE
├── shadowrunner/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── frameworks.md
│       ├── content-ethics.md
│       └── validation.md
└── coros-workout-review/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── client-connections.md
        ├── connection-diagnostics.md
        ├── review-methodology.md
        └── privacy-safety.md
```

## 公开版边界

发行包只保留原创、通用化的方法框架与公开的产品连接说明。它不包含：

- 会员、付费、私密或受限内容；
- 原始字幕、长篇逐字引文与第三方评论；
- 真实人物的身份、健康、家庭、居住、职业或财务资料；
- 对真实人物的心理画像、人格归因或私生活推断；
- 用户名、UID、Cookie、Token 或平台访问规避细节；
- 任何用户的 COROS 训练、健康、位置或账号数据。

公开版不是私人研究或训练数据的可复现语料包，也不承诺复刻任何真实人物。

## 许可

原创文字与非程序化元数据采用 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)（CC BY-NC-SA 4.0）许可：允许在非商业条件下复制、改编和分享，但需要署名、标明修改，并按相同或兼容许可分享改编内容。

建议署名格式：

```text
赛博黑影儿 · ShadowRunner，CC BY-NC-SA 4.0
原项目：https://github.com/leeeboo/public-skills
修改：是 / 否（如是，请简述）
```

商业使用需要另行取得书面许可。详细范围、未授予的权利与第三方材料边界见 [`LICENSE`](LICENSE) 和 [`NOTICE`](NOTICE)。

`NonCommercial` 判断的是具体使用是否主要面向商业优势或金钱报酬，并不只看使用者是不是营利机构；具体以正式许可文本为准。

> 注意：由于包含“非商业”限制，本项目是公开源码 / source-available 项目，不按 OSI 定义自称开源软件。

## 发布与贡献

- 变更记录见 [`CHANGELOG.md`](CHANGELOG.md)。
- 提交内容只能包含你有权公开和许可的材料。
- 不要提交真实人物隐私、用户训练数据、付费内容、长篇转录、第三方账号数据或未经授权的拟声模板。
- 客户端连接步骤需要附厂商一手来源与核对日期；未经证实的能力必须标为条件或实验支持。
- 新增程序代码时，应单独选择适合软件的许可证，并在文件和 `NOTICE` 中明确许可边界。

## 局限

这些 Skills 是思考与复盘辅助工具，不替代合格教练、医生、营养师、心理健康专业人士或法律意见。模型与设备输出都可能错误；重要决定应核验事实并保留人工判断。
