# Generator–Evaluator 契约

## 范围与关键旅程

关键旅程是：开发者接到包含网络请求的 HarmonyOS 业务模块任务，先验证指定依赖和工具类，再搜索
项目既有网络能力；只有不存在适用工具时才创建最小官方 SDK 适配层。随后按 endpoint、repository、
service、transport 和 request/response 职责实现，并验证成功及失败路径能够确定结束。

## Generator 责任

- 只实施批准的 Domain、Kernel pin、CLI bundle 和本地 Runtime 范围。
- 将样例事实与可复用专业规则明确分开。
- 不把静态文件发现描述为构建验证。
- 不自动安装或引入第三方网络依赖。
- 持续更新 `acceptance.json`、`progress.md` 和验证记录。
- 不给自己编写的 G2 制品签发最终 verdict。

## Evaluator 责任

- 独立读取当前 diff 和来源台账。
- 检查有效依赖的分级证据是否可执行且失败关闭。
- 检查工具选择顺序、创建边界、分层职责、结果终止和敏感信息规则的一致性。
- 运行确定性 Domain 校验并给出 pass、fail 或 blocked 结论。
- 不把参考项目的具体工具名称提升为 HarmonyOS 平台要求。

## 证据标准

- 区分 Owner 规则、项目样例、官方 SDK 事实、静态解析、构建和运行时证据。
- 每个工具选择记录候选、选择/拒绝原因、依赖链、适用基线和验证状态。
- 未运行的模块构建、设备请求、认证和真实服务交互不得描述为通过。

## 结论权

最终技术评估结论属于独立 Evaluator；策略范围、例外、远端推送和风险接受属于用户与
`platform-harmony` Owner。
