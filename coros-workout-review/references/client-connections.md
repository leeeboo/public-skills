# COROS 客户端连接指南

核对日期：2026-08-09。界面会变化；实际菜单与本文不同时，只查对应厂商的官方文档，不照猜测继续。

## 目录

- [统一连接卡](#统一连接卡)
- [支持等级](#支持等级)
- [ChatGPT 与 Codex 插件目录](#chatgpt-与-codex-插件目录)
- [Claude 网页版与桌面版](#claude-网页版与桌面版)
- [OpenClaw](#openclaw)
- [Kimi Claw](#kimi-claw)
- [Claude Code](#claude-code)
- [Gemini CLI](#gemini-cli)
- [Cursor](#cursor)
- [VS Code 与 GitHub Copilot](#vs-code-与-github-copilot)
- [Cline、Chatbox 与 Cherry Studio](#clinechatbox-与-cherry-studio)
- [其他 AI 客户端](#其他-ai-客户端)
- [官方来源](#官方来源)

## 统一连接卡

这张连接卡只适用于没有现成 COROS 插件、且支持 remote MCP 的其他客户端。ChatGPT Work、ChatGPT 桌面版中的 Codex 与 Codex CLI 必须先走插件目录，不得先使用本节参数。

| 项目 | 值 |
|---|---|
| 名称 | `coros` |
| 服务器 URL | `https://mcp.coros.com/mcp` |
| 连接类型 | Remote MCP |
| 传输 | 自动检测；必须指定时先试 Streamable HTTP |
| 认证 | 浏览器中的 COROS 授权 |
| Skill 使用方式 | 只读 |

连接时执行这些规则：

- 只在 COROS 官方授权页输入账号、密码和验证码。
- 不把密码、Cookie、OAuth code、Bearer token 或授权回调地址粘贴进聊天。
- 如果客户端只能使用静态 Token，而不能完成浏览器 OAuth，不把它列为正式支持。
- 保存配置不等于连接成功。最后必须能列出一条活动摘要，才算完成。
- 连接后优先只开放活动记录、活动详情和分圈工具。FIT 下载、GPS、睡眠、健康、月经、个人资料和设备信息保持关闭；COROS 连接本身不下载 FIT/GPS。天气补全若收到用户本地 FIT，只在本地读取最小环境字段，健康字段仍只有用户明确需要时才按最小范围开启。

## 支持等级

| 客户端 | v1 等级 | 零技术程度 | 路径 |
|---|---|---:|---|
| ChatGPT Work（网页/桌面） | 推荐 | 高 | 插件 / Plugins → 搜索 COROS |
| ChatGPT 桌面版中的 Codex | 推荐 | 高 | 插件 → 浏览目录 / Plugins → Browse directory → 搜索 COROS |
| Codex CLI | 推荐 | 中 | `/plugins` → marketplace → COROS |
| Codex IDE 扩展 | 间接支持 | 中低 | 无插件目录；改用桌面版或 CLI |
| Claude Web / Desktop | 推荐 | 高 | 图形化 Custom Connector |
| OpenClaw | 正式支持 | 中 | Control UI；首次用 probe 验证 |
| Kimi Claw | 条件支持 | 中低 | 先检查其 OpenClaw 是否暴露 MCP；不盲写配置 |
| Claude Code | 高级支持 | 低 | CLI |
| Gemini CLI | 高级支持 | 低 | CLI，支持 OAuth |
| Cursor | 兼容 | 低 | `mcp.json` |
| VS Code + Copilot | 兼容 | 中低 | Add Server 引导或 `mcp.json` |
| Cline / Chatbox | 有限支持 | 中 | HTTP 可配，但通用 OAuth 未充分证实 |
| Cherry Studio | 实验 | 中 | 当前官方远程字段与 OAuth 文档不足 |

“条件支持”不是“不支持”，而是必须先检查当前版本的实际能力，不能承诺一键完成。

## ChatGPT 与 Codex 插件目录

这是所有受支持 OpenAI 客户端的首选路径。**不要开启 Developer Mode，不要进入 Settings → MCP servers，也不要手动粘贴 MCP URL。**

### ChatGPT Work

1. 在 ChatGPT 网页版或桌面版的切换器中打开 **Work**。
2. 打开 **插件 / Plugins**。
3. 搜索 `COROS`；中文界面也可再搜索 `高驰`。
4. 打开 COROS 条目，查看开发者、权限、隐私政策和支持范围，再选择 `+` 或 **Install / Connect**。
5. 在弹出的 COROS 官方页面登录并授权。
6. 安装完成后新开聊天，通过 `@COROS` 或工具选择器调用。
7. 发送：“只列出我最近一条跑步的日期、距离和时长，不要显示地点。”

ChatGPT Work 的第一轮只说：

```text
请打开左侧的「插件」，搜索 COROS。看到结果后回复“找到了”；不要发送账号或密码。
```

### ChatGPT 桌面版中的 Codex

1. 在 ChatGPT 桌面版中选择 **Codex**。
2. 打开 **插件 / Plugins**。
3. 选择 **浏览目录 / Browse directory**。
4. 搜索 `COROS`；中文界面也可再搜索 `高驰`。
5. 打开 COROS 条目并选择 `+` 安装；按提示在 COROS 官方页面完成连接与授权。
6. 安装完成后新开一个 Codex 聊天，再发送最小验证问题。

Codex 桌面版的第一轮只说：

```text
请打开左侧的「插件」，点击「浏览目录」（Browse directory），再搜索 COROS。看到结果后回复“找到了”；不要发送账号或密码。
```

### Codex CLI

1. 在 Codex CLI 中输入 `/plugins`。
2. 进入可用 marketplace，搜索或浏览 `COROS`。
3. 打开条目并安装；需要连接时按提示完成 COROS 官方授权。
4. 安装后新开一个 CLI session，再执行最小验证。

Codex IDE 扩展当前不提供插件目录。不要把 IDE 扩展误称为 Codex 桌面版，也不要在用户没有选择高级路径时直接给 MCP URL；优先建议改用 ChatGPT 桌面版中的 Codex 或 Codex CLI。

通过条件：返回的是本人真实活动，且没有要求再次登录。

若搜索不到、无法安装或 Connect 变灰：

- 确认使用最新版 ChatGPT 网页或桌面版；
- 查看条目是否受套餐、地区、当前界面或工作区角色限制；
- 若提示 `Disabled by admin`，只能请工作区管理员启用；
- Business / Enterprise / Edu 管理员需要同时检查 Workspace settings 中的 Plugins 与底层 Apps 权限；
- 确认插件是否已安装但未启用，并在安装后新开聊天或 CLI session；
- 不要因此退回 Developer Mode 或手动 MCP。先解释套餐、区域、工作区策略或界面限制；用户明确选择高级替代方案后，再推荐 Claude 或其他支持 OAuth 的 remote MCP 客户端。

OpenAI 在 2026-07-09 将 App Directory 迁移到 Plugin Directory。**Plugin Directory** 是功能名称；Codex 桌面版当前的入口按钮是 **浏览目录 / Browse directory**，不是“插件市场 / Plugin Marketplace”。COROS 2026-07-02 的帮助页仍保留旧的 ChatGPT Developer Mode 步骤；本 Skill 以较新的 ChatGPT 插件流程和用户当前可见界面为准。

## Claude 网页版与桌面版

操作：

1. 打开 **Customize / 自定义 → Connectors**；部分桌面版显示为 **Settings → Connectors**。
2. 选择 **Add custom connector**。
3. 名称填 `coros`，URL 填 `https://mcp.coros.com/mcp`。
4. 选择 Add / Save。
5. 在浏览器打开的 COROS 页面完成授权。
6. 在新聊天的 **Search and tools** 中启用 COROS 工具。
7. 发送最小验证问题：“只列出最近一条跑步的日期、距离和时长，不显示地点。”

Team / Enterprise 通常需要 Owner 先在组织设置中添加 Custom Web Connector，成员再分别完成自己的 COROS 授权。

不要把 remote URL 写进 `claude_desktop_config.json`；那个文件主要用于本地 MCP，COROS 远程服务走 Connectors 图形入口。

## OpenClaw

### 图形路径

1. 打开 OpenClaw Control UI。
2. 进入 **Settings → MCP → Add server**；也可在对话中用 **+ → Connectors → Add MCP server…**。
3. 名称填 `coros`。
4. Transport 选择 **Streamable HTTP**。
5. URL 填 `https://mcp.coros.com/mcp`，选择 Add server。
6. 若出现认证提示，在浏览器完成 COROS 授权。

保存后需要真实探测。OpenClaw 官方目前提供的明确验证命令是：

```bash
openclaw mcp doctor coros --probe
```

输出能确认服务器可达并列出 tools 才算成功。若提示需要 OAuth：

```bash
openclaw mcp login coros
```

只打开命令打印的授权 URL，在 COROS 页面操作。不要把回调 URL、code 或 token 发给聊天助手。

### 高级命令路径

只在图形入口不存在或用户主动选择时使用：

```bash
openclaw mcp add coros --url https://mcp.coros.com/mcp --transport streamable-http
openclaw mcp doctor coros --probe
```

撤销：在 **Settings → MCP** 禁用或移除 `coros`。若配置已保存但运行中的 Agent 看不到工具，先按官方方式 publish / reload / restart 当前 Gateway，不要反复添加同名服务器。

## Kimi Claw

Kimi 官方把 Kimi Claw 定义为在 Kimi 中创建、部署或连接自己的 OpenClaw 实例。官方帮助中心当前没有给出 Kimi Claw 专用的 COROS/MCP 添加页面或 remote MCP 配置格式，因此按条件路径处理。

### 非技术路径

1. 打开 `https://kimi.com/bot`，进入目标 Kimi Claw。
2. 打开 **Settings**，查找明确标为 **MCP / Connectors / COROS** 的入口。
3. 如果入口存在，并且字段与 OpenClaw 的 Add server 一致，按上面的 OpenClaw 图形路径填写。
4. 如果入口不存在，停止；不要把 Kimi Code 的 `/mcp-config` 或别处的 JSON 猜着套进 Kimi Claw。

三个入口都没有时，明确告诉用户“当前版本未确认支持，配置到此停止”；不要索取日志、账号或凭据。

### 有人协助时的检查路径

Kimi Claw 提供 Settings 中的 Terminal。以下步骤只交给用户主动找到的协助者执行，非技术用户不需要自行操作。先只做只读检查：

```bash
openclaw mcp status --verbose
```

- 命令存在且输出当前 OpenClaw 的 MCP 状态：继续使用 OpenClaw 的官方 CLI 路径。
- 命令不存在、无权限或输出不属于当前运行实例：停止，并请 Kimi 官方支持确认；不要直接编辑未知配置文件。

Kimi Claw 无响应时，只按官方顺序刷新，再用 **Settings → Restart Kimi Claw**；仍失败才考虑 **Repair Kimi Claw**。Repair 可能影响状态，执行前提醒用户阅读界面说明。

如果用户可以接受命令行，也可改用 Kimi Code CLI。Kimi Code 的 `/mcp-config` 与 `mcp.json` 是另一个产品的能力，不代表 Kimi Claw 原生支持。

## Claude Code

```bash
claude mcp add --transport http coros https://mcp.coros.com/mcp
claude mcp login coros
claude mcp list
```

在 Claude Code 中也可用 `/mcp` 查看认证和工具状态。若 OAuth 回调无法回到远程终端，按 Claude Code 官方页面给出的 callback 方案处理；不要把回调地址公开发送。

## Gemini CLI

Gemini 的普通聊天界面不等于 Gemini CLI。当前正式路径是 CLI：

```bash
gemini mcp add coros https://mcp.coros.com/mcp --transport http
```

启动或重启 Gemini CLI 后：

```text
/mcp list
/mcp auth coros
```

完成浏览器授权后，`/mcp list` 应显示 Connected。必要时使用 `/mcp reload`。无浏览器的远程 SSH 环境不适合这条零技术路径。

等价配置使用 `httpUrl`，不要写成其他客户端的字段：

```json
{
  "mcpServers": {
    "coros": {
      "httpUrl": "https://mcp.coros.com/mcp"
    }
  }
}
```

## Cursor

Cursor 的官方主路径是配置文件，适合有人协助的用户。全局配置为 `~/.cursor/mcp.json`，项目配置为 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "coros": {
      "url": "https://mcp.coros.com/mcp"
    }
  }
}
```

重开 Cursor，在 Chat 的 Available Tools 中确认 `coros`。若自动打开 OAuth，完成浏览器授权。不要额外猜 `auth` 字段。

## VS Code 与 GitHub Copilot

优先使用命令面板：

1. 运行 **MCP: Add Server**。
2. 选择 HTTP 服务器，输入 `https://mcp.coros.com/mcp`。
3. 选择 Global 或 Workspace；完全不懂技术时选 Global，避免把个人连接配置提交进项目。
4. 首次启动确认信任，在 Chat 的 Configure Tools 中查看 COROS 工具。
5. 故障时运行 **MCP: List Servers → coros → Show Output**。

手动 JSON 使用 VS Code 自己的顶层键 `servers`：

```json
{
  "servers": {
    "coros": {
      "type": "http",
      "url": "https://mcp.coros.com/mcp"
    }
  }
}
```

不要复制 Cursor 的 `mcpServers` 顶层结构。

## Cline、Chatbox 与 Cherry Studio

这些客户端可以显示或配置远程 MCP，但当前官方资料不足以保证 COROS 的通用浏览器 OAuth 能完整工作，因此只做有限或实验支持。

### Cline

路径：Cline 侧栏 → MCP Servers → Remote Servers。若手动配置，Cline 的精确类型是 `streamableHttp`：

```json
{
  "mcpServers": {
    "coros": {
      "url": "https://mcp.coros.com/mcp",
      "type": "streamableHttp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

如果客户端没有自动打开 COROS OAuth，停止。不要要求用户复制 Bearer Token。

### Chatbox

路径：**Settings → MCP → Add custom MCP → Remote (http/sse)**，填 URL 后先点 Test。只有 Test 能完成授权并通过，才保存并在新的 Work Mode 对话中启用。Test 卡在认证时停止。

### Cherry Studio

路径通常是 **Settings → MCP 服务器 → 添加服务器**。只有当前版本明确显示 HTTP / Streamable HTTP 和浏览器授权时才继续；否则标记为暂不兼容，不使用本地桥接规避。

## 其他 AI 客户端

不要按品牌名猜兼容。先用下面的五项检查做标准化判断：

1. 是否明确支持 **remote MCP**，而不只是本地 stdio；
2. 是否支持 **Streamable HTTP** 或能自动识别远程 MCP 传输；
3. 是否能对受保护的 MCP 服务器发起 **浏览器 OAuth**；
4. 是否允许用户查看并限制单个工具权限；
5. 是否有工具列表、Test、Probe 或日志，可证明保存后的连接真的可用。

五项都能由客户端官方文档或当前界面确认时，使用“统一连接卡”，然后做最小活动查询。第 1、2 或 3 项缺失时标记“不兼容”；第 4、5 项缺失时标记“实验”，不代替用户写全局配置。

询问客户端客服或查官方文档时，可直接使用这段问题：

```text
该客户端是否支持连接带 OAuth 2.0 浏览器授权的远程 Streamable HTTP MCP 服务器？
服务器 URL 由用户提供，连接后需要能查看工具列表并限制单个工具权限。
```

拿到肯定答案仍要做真实的只读查询；“支持 MCP”不自动等于支持 COROS 的认证方式。

## 官方来源

- [COROS MCP 官方指南](https://support.coros.com/hc/en-us/articles/50841795180948-COROS-MCP-A-Guide-to-Connecting-Your-Training-Data-to-AI)
- [OpenAI：Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256)
- [OpenAI：Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)
- [OpenAI：Codex MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Claude：Remote MCP custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code：MCP](https://code.claude.com/docs/en/mcp)
- [OpenClaw：Connect MCP servers](https://docs.openclaw.ai/tools/mcp)
- [Kimi Claw 官方概览](https://www.kimi.com/help/kimi-claw/overview)
- [Kimi Claw：无响应排查](https://www.kimi.com/help/kimi-claw/slow-no-response)
- [Kimi Code CLI：MCP](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/mcp.html)
- [Gemini CLI：MCP servers](https://geminicli.com/docs/tools/mcp-server/)
- [Cursor：Model Context Protocol](https://docs.cursor.com/context/model-context-protocol)
- [VS Code：MCP servers](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [GitHub MCP Server：Cline 远程 MCP 配置](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-cline.md)
- [Chatbox：Work Mode / MCP](https://releases.chatboxai.app/en/guide/work-mode/configuration)
- [Cherry Studio：MCP 配置](https://docs.cherry-studio-ai.com/advanced-basic/mcp/config)
