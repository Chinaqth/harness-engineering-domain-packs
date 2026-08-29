# HarmonyOS 网络请求开发策略端到端独立评估

- Evaluator：独立 Evaluator（未参与本次 Domain 生产制品实现，未修改生产 Domain 制品或 Drill 项目）
- Evaluated at：`2026-08-29T20:19:07+0800`
- Verdict：**Pass**
- Evaluated revision：`aacc364ceeab3b4960b788d24c2c44363e2d962d` 加当前未提交的
  `20260829-harmonyos-network-request-policy` 变更
- Environment：macOS，Asia/Shanghai；系统 Python `3.9.6`；Codex bundled Python（含
  `tomllib`）用于完整 Domain 校验
- Evaluation scope：Domain 4.0.0 策略制品及其独立发布就绪性；不包含后续 Domain/Kernel/CLI
  提交、推送、同步和本地安装，因此不对 AC-09 签发完成结论

## Findings

未发现 P0 或 P1 问题。

### P2 — 默认校验入口依赖未声明的 Python 3.11+ 运行时（AC-07）

直接运行 `./scripts/domain-check.sh` 时，系统 `python3` 为 3.9.6，执行到
`scripts/validate_agents.py` 因缺少标准库 `tomllib` 失败。把 PATH 显式指向 Codex bundled
Python 后，同一脚本完整通过：registry、Repository Skill、Project Custom Agent 校验均通过，48
项测试通过。该问题不是本次 HarmonyOS 变更新增，也不否定制品内容，但发布证据必须记录实际 Python
运行时，不能只登记裸命令。最小安全动作是由 Generator 在进度与验收记录中保留 bundled Python
命令；仓库后续可单独声明 Python 最低版本或提供 `tomli` 兼容路径。

### P2 — Change 机器状态与进度仍停留在评估前状态（AC-01–AC-08）

`acceptance.json` 仍为 `in_progress` 且 AC-01–AC-09 全部为 `pending`；`task.md` 未勾选实现与验证，
`progress.md` 仍称“生产制品尚未完成修改”。这在独立结论产生前是可理解的流程中间态，但发布前必须依据
本报告和后续真实同步证据对账。AC-09 只能在三仓库 revision、远端状态、Kernel pin、CLI bundle 和
本地 Runtime 均被实际核验后改为完成。

## Critical journey result

本次变更是执行政策而非产品网络实现，因此关键旅程通过策略表面追踪、负向规则检查和确定性仓库校验
复现；没有虚构模块构建、设备请求、认证或真实服务运行结果。

1. **指定网络工具有效。** `HMOS-RULE-11` 与网络参考契约要求依次取得 affected-module 声明、
   exact target、package entrypoint、public symbol/type export、implementation dependency/SDK/config/
   permission 和 affected configured build 证据；有效候选被优先复用。Workflow、wrapper Skill、业务
   Skill、Evaluator 和证据模板均保留这些状态，没有把静态发现提升为构建通过。
2. **指定工具无效后搜索项目。** 规则明确在候选 unavailable/unsuitable 时搜索授权项目范围内的
   manifests、entrypoints/exports、既有 client/request function、platform-network import、endpoint、
   response/error contract、interceptor 与 repository implementation，并要求记录每个可信候选的选择
   或拒绝理由。仅有相似文件名或 private source path 不能被当作有效工具。
3. **项目无适用工具后最小创建。** 只有项目搜索确认不存在适用工具时，才允许在 `api/` 或项目等价
   边界创建最小 feature-owned transport abstraction 和经当前 SDK/API 基线核验的官方接口 adapter。
   外部依赖、全局共享模块、认证、证书、重试、缓存、响应协议、URL、Toast、路由和日志策略都保持
   fail-closed，缺少单独授权时停止而不是猜测。
4. **确定终止与脱敏。** Rule、Workflow、两层 Skill 和 `HMOS-EVAL-13` 均要求每条请求路径 exactly
   once 地返回类型化 success/failure，并区分 offline、configuration、protocol、business、decode、
   timeout、cancellation 和 SDK exception；pending Promise、错误折叠或 protected-data log 是明确
   fail。模板要求记录生命周期、重叠/陈旧结果、日志与证据脱敏，并禁止从一次成功构建推断运行时路径。

Drill UGC 台账事实经独立静态抽查成立：UGC 模块声明 `common_app` 本地依赖并从公共入口导入
`httpCall`；`common_app` 导出 `HttpCall`，底层实现引用 `@kit.RemoteCommunicationKit`；观察到的
RCP 实现包含未 resolve/reject 的非成功分支以及 Toast/日志副作用，Service 也把多种失败折叠为
`undefined`。生产规则只保留其职责分层和已知失败模式，没有把 `common_app`、`httpCall`、RCP、
认证、路由、Toast、响应协议或服务地址提升为 HarmonyOS 平台要求。

## Acceptance reconciliation

| Criterion | Revision / environment | Journey and expected result | Actual / evidence | Limitations | Result |
| --- | --- | --- | --- | --- | --- |
| AC-01 | dirty tree；local static review | 参考契约定义职责、有效依赖状态和选择顺序 | `network-request-conventions.md` 定义 9 类职责、5 个依赖状态和 supplied → project search → official interface/minimal adapter 顺序 | 尚未以真实新模块执行一次完整开发任务 | satisfied |
| AC-02 | dirty tree；local static review | 硬规则覆盖解析、搜索、创建、终止、敏感数据与验证 | `HMOS-RULE-11` 覆盖全部要求，并为 unresolved tool、pending path、collapsed error 和 sensitive log 定义 fail/blocked handoff | 具体项目政策仍需项目输入 | satisfied |
| AC-03 | dirty tree；local static review | 实现前、中、构建前均应用规则 | `WORKFLOW.md` track 5/6、wrapper Skill 与业务 Skill 分别执行 inventory、resolution ladder、实现边界、pre-build inspection 和 configured build/negative paths | 没有运行产品模块构建，符合本变更非产品实现范围 | satisfied |
| AC-04 | dirty tree；local static review | Evaluator 可检查依赖链、API 边界、终止和负向路径 | `HMOS-EVAL-13` 有明确 pass conditions、required evidence、negative paths 和 fail/blocked 语义 | 后续实际项目仍需行为证据 | satisfied |
| AC-05 | dirty tree；local static review | 模板记录工具决策、依赖解析、职责、结果和验证矩阵 | `delivery-evidence.md` 新增候选/解析/build 表、职责/result/lifecycle/redaction 表，并复用 scenario matrix | 模板质量仍依赖执行者填写完整 | satisfied |
| AC-06 | dirty tree；bundled Python | manifest、registry、DOMAIN、README 与兼容/迁移边界一致 | 四处版本均为 `4.0.0`；README 描述全部 771 个非隐藏生产文件；compatibility 声明允许 pin 3.x 并把 4.0.0 限定于新增或实质修改的请求表面及直接依赖链 | 根 README 不承载单 Domain 版本，未发现需同步项 | satisfied |
| AC-07 | dirty tree；bundled Python | Domain、Skill、Agent、JSON 与 tests 通过 | bundled Python 下 `./scripts/domain-check.sh` 退出码 0；48 tests OK；`git diff --check` 通过；changed Skill/reference 本地链接通过 | 裸系统 Python 3.9.6 失败，见 P2 | satisfied with limitation |
| AC-08 | 本报告 | 独立 Evaluator 给出唯一结论 | 本文件给出 **Pass**；Evaluator 未修改生产 Domain 制品 | Generator 仍须对账 change 状态 | satisfied |
| AC-09 | 未执行 | 三仓库提交、推送、pin/bundle/本地 Runtime 同步 | Evaluator 按任务约束未提交或推送 | 属于本报告之后的发布阶段 | pending / not evaluated |

## Security, permission, compatibility, and rollback observations

- 未访问设备、账号、签名材料、生产服务、凭据或用户数据；未安装网络依赖，也未修改 Drill 项目。
- 搜索范围与创建权限均失败关闭。规则没有授权第三方安装、共享网络基础设施或认证/证书/服务环境
  决策；敏感日志和证据字段被明确要求删除或脱敏。
- Domain 4.0.0 的 major bump 与新增强制策略相称；兼容声明保留 Kernel protocol 1.0，并允许项目继续
  pin 3.x。该政策不要求一次性重写全部遗留网络栈。
- 回滚方案位于 `requirements.md`：逆序回滚 CLI bundle、Kernel pin、Domain 4.0.0，并重新构建 bundle
  后执行 `harness update`。当前仅 Domain dirty tree，尚未产生需远端回滚的提交；后续必须记录三个
  独立 revision，且不得用破坏性 workspace reset 覆盖用户修改。

## Evidence index and reproducibility

1. Evaluated baseline：`git rev-parse HEAD` →
   `aacc364ceeab3b4960b788d24c2c44363e2d962d`；`git status --short` 与 `git diff --check`。
2. 完整确定性校验：
   `PATH=/Users/albertq/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin:$PATH ./scripts/domain-check.sh`
   → registry、Repository Skill、Project Custom Agent 均 passed；`Ran 48 tests ... OK`。
3. 默认环境负向复现：系统 `python3 --version` → `3.9.6`；裸 `./scripts/domain-check.sh` 在
   `validate_agents.py` 导入 `tomllib` 时失败。
4. 版本与清单断言：解析 `domain.json` 和 `registry/domains.json`，并检查 `DOMAIN.md`、
   `README-CH.md` → `4.0.0` 一致；771 个非隐藏生产文件均出现在 README 清单。
5. Skill/reference 链接断言：检查四个变更 Skill/reference Markdown 的本地链接 → 通过。
6. 来源解析断言：change ledger 的四个 source ID、Drill exemplar/dependency 目录，以及继承 ledger
   中的 `HMOS-ARKTS`、`REPO-HARMONYOS-IDENTITY` 均可解析。
7. Drill 静态抽查：`features/ugc/oh-package.json5`、UGC `api/`、`common_app/Index.ets`、
   `common_app/src/main/ets/net/`；未执行 Drill 构建或网络请求。

## Residual risks and next action

- 策略能强制执行顺序，但无法在没有目标项目、SDK、依赖和服务 fixture 的情况下证明某个实际网络
  adapter 的编译或运行行为；每次应用仍必须提交 configured build 与任务要求的负向场景证据。
- 项目专属认证、证书、response envelope、retry/cache/idempotency、服务环境和日志访问仍是明确的
  owner handoff，不应在发布中被补成通用默认值。
- Generator 的最小下一步是：依据本报告更新 `acceptance.json`、`task.md`、`progress.md`，保持
  AC-09 pending；随后按已授权顺序提交并推送 Domain、同步 Kernel pin、更新并推送 CLI bundle、更新
  本地 CLI/Runtime；只有实际 revision 和本地版本核验完成后才关闭 AC-09 与整个 change。
