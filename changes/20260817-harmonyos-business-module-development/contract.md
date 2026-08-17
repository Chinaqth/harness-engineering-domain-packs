# Generator–Evaluator 契约

## 范围与关键旅程

关键旅程是：业务模块实现任务被独立路由，执行者先确认模块/provider 边界，再按 MVVM 和 V2
状态规则实现 API、ViewModel、UI、router、hmdelegate 与 provider 契约，最后以结构、依赖方向、
构建和任务要求的运行证据完成交接。

## Generator 责任

- 只实施已批准范围。
- 保持或加强验收标准。
- 记录可复现证据和已知限制。
- 持续更新 `acceptance.json` 和 `progress.md`。

## Evaluator 责任

- 独立于实现声明进行评估。
- 在隔离环境中复现关键用户旅程。
- 检查安全、权限、兼容性、回滚和证据质量。
- 用证据记录 pass、fail 或 blocked 结论。

## 证据标准

必须有可追溯来源 ID、变更路径、JSON/Skill/registry 校验结果、Domain 全量检查结果，以及对
初始化能力未被扩大的负向核对。项目示例只能证明现存模式，不能证明平台 API 或普遍最佳实践。

## 独立性与职责分离

Generator 可执行确定性校验但不得为自己签发 Domain artifact 专业评估。Evaluator 应由独立
agent 或 Harmony Domain reviewer 执行。

## 结论权

G1 交付可在确定性检查通过后形成待评审候选；正式合并结论由 `platform-harmony` reviewer 所有。

## 升级与争议处理

如果评审发现能力改变了既有权限、兼容性或稳定 ID 语义，暂停并升级为 G2 变更。
