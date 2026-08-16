# OpenWeatherMap One Call API 4.0 环境补全

这条路径只用于补充一次活动的温度和湿度上下文，不把 OpenWeatherMap 的结果伪装成跑者身上的实测值。优先使用活动详情或 FIT 中可信的环境字段；只有字段缺失、明显无效，或用户明确标记为不可信时，才考虑补全。

## 配置 API Key

配置完全可选。只有复盘所需的温湿度缺失或不可信、且用户愿意启用第三方天气补全时，才进入配置引导。先问用户是否需要配置；拒绝或暂不配置时不要劝说，直接进入“人工温湿度兜底”。

使用宿主的密钥管理器或本机环境变量配置：

```text
OPENWEATHERMAP_API_KEY=<用户自己的 OpenWeatherMap API key>
```

- 引导用户时一次只给一个动作：打开 [OpenWeather API Keys](https://home.openweathermap.org/api_keys) 创建或复制自己的 key；再到当前客户端的 secret / 环境变量设置中，把变量名设为 `OPENWEATHERMAP_API_KEY`；最后只让用户回复“已配置”，不要让用户回传 key。
- API key 只能存在于本机密钥管理器、客户端 secret 或进程环境中；不要写入 `SKILL.md`、仓库、聊天记录、截图、命令参数或日志。
- 不要求用户把 key 粘贴到聊天里。当前客户端无法安全保存 secret 时，说明“暂时不能启用天气补全”，不要改用明文配置。
- 设置 key 不等于授权发送活动位置和时间。第一次为某次活动查询前，仍需取得这次天气查询的明确同意。
- One Call API 4.0 的套餐、计费和请求额度以 OpenWeather 官方账户页面为准；不要承诺免费或无限调用。

## 人工温湿度兜底

key 未配置、用户拒绝配置、当前客户端无法安全保存 secret、用户拒绝本次第三方查询，或 API 最终失败时，只问一句：

> 这次运动时大约多少摄氏度、湿度大约多少？不清楚可以直接说不知道。

- 这项信息也不强制；用户不知道时保留环境未知并继续复盘。
- 用户回答只能标为“用户提供的环境信息”，不能写成 COROS、FIT 或天气 API 实测。
- 不要求用户为了回答而提供地点、路线、坐标或活动截图，也不根据当前天气反推历史温湿度。

## 允许发送的最小输入

天气查询前，只准备以下信息：

1. 活动开始时间（UTC Unix timestamp 或可转换为 UTC 的带时区时间）；
2. 活动持续时间，用于限定匹配窗口；
3. 用户提供的城市 / 地区，或已经被用户同意使用的**粗略位置**。

位置必须先粗化到约 `0.1°` 纬度 / 经度，再发送给 OpenWeatherMap；这大约是 11 km 级别的环境上下文，不是路线定位。不要从 FIT 读取或上传完整 GPS、路线、起终点、坐标序列、活动 ID、训练名称、姓名或任何其他 COROS 字段。

如果只有精确 FIT GPS，没有用户同意的粗略位置，就停止天气查询并把环境记为未知。不能为了补天气而下载、上传或解析完整路线。

## One Call API 4.0 调用

历史活动使用 `timeline/1h`，不要调用 `/current` 代替历史天气：

```text
GET https://api.openweathermap.org/data/4.0/onecall/timeline/1h
    ?lat=<粗化后的纬度>
    &lon=<粗化后的经度>
    &start=<活动开始时间的 UTC Unix timestamp>
    &units=metric
    &appid=<从 OPENWEATHERMAP_API_KEY 读取>
```

请求执行规则：

- 只请求覆盖本次活动的最小时间窗；默认一次请求，不为填满指标墙而分页。
- 只读取 `data[].dt`、`data[].temp` 和 `data[].humidity`；其他天气字段按需且最小化读取。
- `units=metric` 时温度使用摄氏度，湿度使用百分比；仍需核对响应中的字段和单位。
- API key 不得出现在用户可见的 URL、输出、异常文本或日志中。若宿主只能把 URL 全量记录，停止调用。
- 401 / 403 视为 key、权限或套餐问题；429 视为额度限制；5xx 或超时视为服务暂时不可用。最多重试一次，随后进入人工温湿度兜底，再继续 COROS / FIT 复盘路径。

技能目录提供了一个只从环境变量读取 key、并默认粗化位置的辅助脚本。宿主允许本地执行时优先使用它：

```bash
python coros-workout-review/scripts/openweather4.py \\
  --lat <粗化后的纬度> \\
  --lon <粗化后的经度> \\
  --start 2026-08-16T01:00:00Z \\
  --duration-minutes 120
```

脚本只返回最小温湿度记录，不返回完整 OpenWeather 响应或位置；使用 `--dry-run` 可在没有 key 时检查请求参数。

## 合并与呈现

- FIT 中的温度 / 湿度只要可信，就保留为主数据；OpenWeatherMap 不自动覆盖可信的设备值。
- 只有缺失、非数值、单位无法确认、超出合理范围，或用户明确标记为不可信时，才用 API 结果补空缺或并列展示。
- 保留来源标签：`FIT / COROS`、`OpenWeatherMap One Call API 4.0` 或“用户提供的环境信息”。发现差异时报告差异，不挑一个看起来更“准确”的值覆盖另一个。
- 以活动时间窗内最近的小时记录为匹配依据；没有足够接近的记录、返回字段缺失或响应只覆盖部分活动时，对应字段仍记为未知。
- 输出写成“外部天气上下文 / 约略位置估计”，不能写成“跑者当时实际体感”或确定的疲劳原因。它只能帮助解释环境这一候选因素，不能单独改变风险筛查、训练阶段或训练处方边界。

## 官方文档

- [OpenWeather One Call API 4.0](https://openweathermap.org/api/one-call-4)
- [OpenWeather One Call API 3.0 与 4.0 迁移入口](https://openweathermap.org/api/one-call-3)
- [OpenWeather API Key 账户入口](https://home.openweathermap.org/api_keys)
