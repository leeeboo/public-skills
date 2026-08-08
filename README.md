# 赛博黑影儿 · ShadowRunner

一套面向跑者与创作者的公开决策 Skill：先判断阶段与瓶颈，核对建议的适用范围，再设计低风险、可回滚、可验证的下一步。

当前版本：`v1.0.0`

发布日期：`2026-08-08`

## 它是什么

ShadowRunner 是原创方法框架，不是真实人物的数字分身，也不代表任何跑者、教练、频道或品牌。它适合：

- 复盘训练停滞与长期项目；
- 判断一条方法是否适合当前阶段；
- 把经验写成诚实、可核验、有边界的内容；
- 在证据不足时设计最小可逆实验。

它不提供医疗诊断、伤病判断、个体化训练处方、营养处方或成绩承诺。

## 安装

本 Skill 不需要运行时依赖。请保留 `shadowrunner/` 的完整目录结构。

```bash
git clone https://github.com/leeeboo/public-skills.git
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/public-skills/shadowrunner" "$HOME/.agents/skills/shadowrunner"
```

如果目标位置已经存在，请先自行备份；不要让软链接覆盖尚未保存的私有版本。Codex/Agents 宿主需要支持以 `SKILL.md` 为入口的本地 Skill。

使用示例：

```text
使用 $shadowrunner 分析我最近的跑步瓶颈；先说明还缺什么信息，不要直接给训练剂量。
```

## 目录

```text
public-skills/
├── .gitattributes
├── README.md
├── CHANGELOG.md
├── LICENSE
├── NOTICE
└── shadowrunner/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── frameworks.md
        ├── content-ethics.md
        └── validation.md
```

## 公开版边界

这个发行包只保留原创、通用化的方法框架。它不包含：

- 会员、付费、私密或受限内容；
- 原始字幕、长篇逐字引文与第三方评论；
- 真实人物的身份、健康、家庭、居住、职业或财务资料；
- 对真实人物的心理画像、人格归因或私生活推断；
- 用户名、UID、抓取接口、Cookie 或平台访问规避细节。

因此，公开版不是某项私人研究的可复现语料包，也不承诺复刻任何真实人物。它只发布从零重写后的通用框架。

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
- 不要提交真实人物隐私、付费内容、长篇转录、第三方账号数据或未经授权的拟声模板。
- 新增程序代码时，应单独选择适合软件的许可证，并在文件和 `NOTICE` 中明确许可边界。

## 局限

这是思考辅助工具，不替代合格教练、医生、营养师、心理健康专业人士或法律意见。模型输出可能错误；重要决定应核验事实并保留人工判断。
