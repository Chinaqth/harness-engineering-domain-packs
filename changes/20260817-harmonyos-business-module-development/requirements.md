# 变更需求

- ID: `20260817-harmonyos-business-module-development`
- Owner: `platform-harmony`
- Risk: G1
- Status: done
- Review-By: 2026-08-31

## 问题

现有 HarmonyOS Domain Pack 只提供业务 HAR 与空 provider HAR 的初始化能力，明确排除了
业务实现、路由和 provider 接口实现。它无法指导初始化后的业务模块按统一架构完成开发。

## 目标

- 新增可复用的 HarmonyOS 业务模块开发 Skill，而不扩大初始化 Skill 的既有边界。
- 固化 MVVM、状态管理 V2、网络层、UI 分类、壳工程委托、模块路由和 provider 桥接契约。
- 新增独立 task type、能力与路由，使完整业务模块开发不与空骨架初始化混淆。
- 为上述架构增加可观察的评估标准和中文制品导览。

## 非目标

- 不复制 `ugc` 的业务逻辑、依赖、模块名或绝对路径。
- 不修改 `hmos-init-business-module` 的模板或事务脚本。
- 不规定组织未知的 SDK、API、路由框架、依赖注入框架或网络库。
- 不安装、发布或部署 Runtime 投影。

## 约束与事实来源

- `USER-BUSINESS-MODULE-CONTRACT`：本次请求给出的业务模块规范。
- `PROJECT-UGC-EXEMPLAR`：只读参考工程，用于验证目录与依赖方向，不作为平台权威。
- `HMOS-ARKUI-V2`：现有研究台账中的 Huawei State Management V2 依据。
- `REPO-HARMONYOS-IDENTITY`：现有 Domain 身份、Owner 与生命周期事实。
- 参考工程路径只保留在本变更研究记录中，不写入生产 Skill。

## 验收标准

- [x] 新 Skill 明确输入、目录契约、MVVM 边界、V2 状态、网络层、路由、壳委托、provider 契约、验证和失败关闭条件。
- [x] provider HAR 只声明外部契约和唯一访问桥梁，具体 Service/Component 实现在业务 HAR 中。
- [x] 现有初始化能力继续排除业务实现，新能力使用独立稳定 ID 和 task type。
- [x] 新 Skill 是业务模块路由的主编排入口，ArkUI、ArkTS、Stage/package、初始化和验证能力不得静默覆盖跨层架构决策。
- [x] manifest、registry、capability、route、workflow、evaluator、Skill 清单和中英文说明保持一致。
- [x] `./scripts/domain-check.sh` 通过，且确定性检查未发现 P0/P1 问题。
- [x] 非 Generator 的 Harmony Domain reviewer 完成专业正确性评审。

## 风险、权限与数据影响

这是新增可逆能力和路由元数据的非破坏性 G1 变更。它不改变权限、安全边界、生产配置或
外部系统状态。主要风险是把项目示例误写成平台事实、与初始化 Skill 重叠，或使 provider
依赖方向含糊；通过来源分级、独立 task type 和结构验收控制。

## 自主权预算

- 范围：`engineering.harmonyos` 的新增 Skill 及其直接依赖的路由、能力、工作流、评估和清单元数据。
- 工具与权限：只读参考工程；仅写 Domain Pack 源仓库；不修改参考工程或 Runtime。
- 外部副作用：无。
- 成本：本地文件修改与确定性校验。
- 检查点间隔：每个 artifact 组完成后更新进度。
- 必要证据：来源台账、结构检查、JSON/Skill/registry 校验与 Domain 全量检查。
- 升级条件：若需要改变权限、安全边界、已有稳定 ID 语义或破坏兼容性，升级为 G2 并重新审批。

## 回滚方案

回退本变更新增的 Skill/参考文件和能力/路由条目，将 HarmonyOS manifest 与 registry 版本恢复
为 `2.1.0`，并恢复被更新的工作流、评估器和导览文件；随后重新运行 `domain-check.sh`。
