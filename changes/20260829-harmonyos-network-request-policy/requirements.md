# HarmonyOS 网络请求开发策略变更需求

- ID: `20260829-harmonyos-network-request-policy`
- Owner: `platform-harmony`（用户明确批准按已分析方案实施）
- Risk: G2
- Status: evaluating
- Review-By: 2026-09-12

## 问题

现有 HarmonyOS Domain 规定网络入口收敛在业务模块 `api/` 边界，但没有要求开发者在生成代码前
验证网络工具依赖是否真实可解析，也没有定义“指定依赖不可用 → 搜索项目既有工具 → 创建最小适配
层”的失败关闭回退流程。直接复制某个样例的包名、工具类或认证行为会生成无法构建或违反项目架构
的代码。

## 目标

1. 把网络工具的依赖声明、目标解析、入口导出、实现链和构建验证定义为分级证据。
2. 优先复用任务指定且有效的网络工具；不可用时搜索项目既有网络能力。
3. 项目不存在适用工具时，在最小业务边界内基于当前 SDK 已验证支持的官方网络接口创建适配层。
4. 保留 endpoint、repository、service、transport、request/response 等职责抽象，不复制样例的项目专属名称、认证、路由、提示、响应协议或服务地址。
5. 要求每条请求路径确定地成功或失败结束，并分离传输、协议、业务、解析、取消和超时结果。
6. 将规则落实到工作流、执行 Skill、评估器和交付证据。

## 非目标

- 不强制所有项目使用 `common_app`、`httpCall`、RCP 或任何固定第三方网络库。
- 不自动安装外部依赖，不擅自新增共享基础设施模块。
- 不规定产品 API 地址、认证协议、后端响应字段、重试次数、缓存策略或证书策略。
- 不修改 Drill UGC 样例；该项目只作为结构与失败模式证据。
- 不新增独立网络请求 route、capability 或 Skill。

## 约束与事实来源

- `OWNER-HMOS-NETWORK-REQUEST-CONTRACT`：用户批准的依赖探测、项目搜索和最小创建回退策略。
- `PROJECT-DRILL-UGC-NETWORK-EXEMPLAR`：Drill UGC 与 `common_app` 的本地网络分层和依赖链，仅作为项目结构证据。
- `HMOS-ARKTS`：既有 HarmonyOS Domain 研究台账中的 ArkTS 与 SDK 权威来源边界。
- `REPO-HARMONYOS-IDENTITY`：既有 HarmonyOS Domain 仓库身份与所有权事实。
- 新规则不得削弱 Kernel 权限、安全、隐私、证据、审批或失败关闭约束。

## 验收标准

- [x] AC-01：存在可复用的网络请求参考契约，定义分层职责、有效依赖证据和选择顺序。
- [x] AC-02：新增 Domain 硬规则，覆盖依赖解析、项目搜索、最小创建、结果终止、敏感信息和验证要求。
- [x] AC-03：工作流和现有执行 Skill 在实现前、实现中、构建前应用该规则。
- [x] AC-04：评估器能检查工具选择证据、依赖链、API 边界、错误终止和负向场景。
- [x] AC-05：证据模板包含网络工具决策、依赖解析、入口清单、结果契约和验证矩阵。
- [x] AC-06：Domain 与注册表升级到 `4.0.0`，兼容性说明和迁移边界一致。
- [x] AC-07：Domain 全量校验和相关 Skill 校验通过。
- [x] AC-08：独立 Evaluator 对 G2 变更给出 pass、fail 或 blocked 结论。
- [ ] AC-09：Domain、Kernel pin 和 CLI bundle 按顺序提交、推送并同步到本地 Runtime。

## 风险、权限与数据影响

这是已激活 Domain 的新增强制策略；先前仅满足“网络代码位于 `api/`”的交付可能无法满足新的依赖
解析和错误终止要求，因此按 breaking policy 将 `engineering.harmonyos` 从 `3.0.0` 升级到
`4.0.0`。用户明确授权提交和推送 Domain、同步 Kernel/Domain、更新 CLI 仓库及本地 CLI。
不修改参考项目、不安装第三方网络依赖、不访问设备、账号、生产服务或签名材料。

## 自主权预算

- 范围：HarmonyOS Domain 生产制品、本 change、Domain 注册表、Kernel Domain pin、CLI bundle 和本地受管 Runtime。
- 工具与权限：本地文件编辑、确定性校验、Git 提交/推送、已有同步脚本、CLI bundle 构建与本地全局安装/更新。
- 外部副作用：向三个已配置 Git 远端推送提交；更新用户级 Harness Runtime 和受管 Skill 投影。
- 成本：不新增付费服务或第三方依赖。
- 升级条件：需要修改产品源码、安装新网络依赖、改变 Kernel 协议或修改 CLI 行为时停止并重新确认范围。

## 回滚方案

按三个仓库的独立提交逆序回滚：先回滚 CLI bundle，再回滚 Kernel pin，最后回滚 Domain 4.0.0
制品。重新构建 CLI bundle并执行 `harness update` 恢复前一组已验证 revision。不得使用破坏性工作区
重置，也不得覆盖不属于本变更的用户修改。
