# HarmonyOS 页面、资源与中文注释策略端到端独立评估

- Evaluator：独立 Evaluator（未参与本次实现，未修改 Domain 或 CatchElf sample）
- Evaluated at：`2026-08-28T21:35:59+0800`
- Verdict：**Fail**
- Domain repository baseline：`f359d6a8966665abef196af90b905afaa0f701fe` 加当前未提交变更
- CatchElf repository baseline：`2e7f43549e8b5f511861139513bfa1803520df66` 加当前未提交的
  `build-profile.json5` 与未跟踪 `sample/`
- Environment：macOS，Asia/Shanghai；DevEco CLI `1.2.1`；compile SDK 24；compatible SDK 15；
  HMRouter core `1.2.4`；HMRouter compiler plugin `1.2.0`

## Findings

### P1 — HMRouter core/plugin 版本不一致，并为 sample 生成超出 compatible SDK 的代码（AC-05）

`hvigor/hvigor-config.json5:4` 将 `@hadss/hmrouter-plugin` 固定为 `1.2.0`，而项目
`oh-package-lock.json5:9,20-24` 将 `@hadss/hmrouter` core 解析并锁定为 `1.2.4`。本次新增的
`HMOS-EVAL-12` 在 `evaluators/EVALUATOR.md:390-395` 明确把 mismatched core/plugin version
定义为负向路径，且规定即使构建通过也必须使对应项失败。

独立执行 `devecocli build --modules sample --build-mode debug` 虽然以退出码 0 完成，但编译器对
sample 的两个 HMRouter 生成文件均报告兼容性警告：生成代码调用 `onActive`、`onInactive`
（SDK 17 起）和 `onNewParam`（SDK 19 起），项目 compatible SDK 为 15。该结果说明成功打包不能证明
锁定组合在项目最低兼容基线上安全。当前没有 1.2.0 plugin 与 1.2.4 core 的兼容声明或最低 API
运行证据可以消除此风险。

最小安全动作：由项目路由 Owner 选择并锁定一个有上游兼容依据的 core/plugin 组合，在 API 15
目标上重新生成并构建；若仍支持 API 15，再补充实际页面与 Dialog 路由运行证据。Evaluator 不代替
Owner 修改依赖或兼容基线。

### P1 — sample 声称供调用方使用的路由契约没有 HAR 公共入口（AC-01、AC-05）

`sample/src/main/ets/router/SamplePageInfo.ets:4-10` 明确声明该 namespace “可供调用方使用”，新增
Domain Skill 也要求调用方与声明方复用具名路由常量并有意识地维护 public exports；但是 sample 的
包入口 `sample/Index.ets` 是 0 字节。生成的 HAR 包含内部
`src/main/ets/router/SamplePageInfo.d.ets` 和 `SamplePath.d.ets`，却没有由 `main: Index.ets`
暴露的入口声明。普通依赖方无法通过 `import ... from 'sample'` 复用该集中路由契约，因此关键旅程
在“调用方使用同一 route/page-info owner”处中断，也没有 caller 侧负向扫描或编译证据。

最小安全动作：明确 sample 的公共路由 API，并通过 `Index.ets` 只导出所需的 route/page-info
契约；增加一个依赖方编译检查，证明调用方没有复制匿名路由字面量。

### P1 — 声明的 sample 回滚步骤没有可恢复基线（rollback）

回滚方案要求“以本 change 的逐文件 diff”为依据，将 Dialog 恢复到原位置并恢复 sample 原资源
引用；但 CatchElf 中整个 `sample/` 当前都是未跟踪目录，Git 只能显示 `?? sample/`，无法提供修改前
的文件位置、内容或资源值。`research/sources.json` 只记录了初始状态摘要，没有保存可校验的原始
清单或补丁。因此该 G2 变更的 Domain 文件可以按 diff 回退，但 sample 的“恢复原状”无法按当前证据
安全、确定地执行，也无法证明不会覆盖用户新增 sample 的原始内容。

最小安全动作：由 Generator/Owner 保存 sample 修改前后的受控清单或非破坏性补丁，并把准确的逐文件
恢复步骤写入回滚记录；不得通过删除整个未跟踪 `sample/` 来替代恢复。

### P2 — 默认 Domain 校验环境不可复现，且变更状态记录仍未对账（AC-06、AC-08）

直接运行 `./scripts/domain-check.sh` 时，系统 Python 为 3.9.6，`validate_agents.py` 因缺少
`tomllib` 退出；将 PATH 显式指向工作区 bundled Python 后，registry、Skill、Agent 校验与 48 项测试
全部通过。报告必须保留这一环境前提，不能只登记“Domain 校验通过”。此外 `acceptance.json` 的八项
状态仍全部为 `pending`，`task.md` 与 `progress.md` 仍描述实施未完成。该状态在独立结论产生前可以
理解为流程中间态，但交接前必须与本报告和实际检查结果对账。

## Critical journey result

关键旅程按以下顺序复现：读取 Owner 约定与来源边界；读取页面/Dialog 参考；检查 Domain 规则、
工作流、执行 Skill 与评估器；检查 sample 的目录、路由、资源和中文注释；扫描 UI 与路由字面量；
执行 Domain 校验；执行 sample debug 构建；检查生成路由映射和 HAR。

已观察到的正向结果包括：Dialog 位于 `dialogs/`；普通页面位于 `pages/`；两者都使用
`@ComponentV2`；Dialog 声明包含 `dialog: true`；路由字符串仅在 `SamplePath` 中具名声明；文案、
颜色与字号分别引用 `string.json`、`color.json`、`float.json`；四个主 `.ets` 文件具有有意义的中文
职责注释；静态扫描未发现 `Text('...')`、十六进制颜色、数字字号或匿名 `pageUrl`；生成
`hm_router_map.json` 含普通页面和 Dialog 两条正确记录；`sample.har` 成功产出。

旅程未达到可接受终点：生成集成暴露了 core/plugin 与 compatible SDK 风险，调用方无法从 HAR 主入口
复用集中路由契约，且回滚不可按声明复现。没有访问设备；页面导航以及 Dialog 打开、关闭、dismiss、
重复交互、失败和恢复场景均标记为 `not run / not task-required`，不能从 HAR 构建推断为运行时通过。

## Acceptance reconciliation

| Criterion | Revision / environment | Preconditions and journey | Expected | Actual | Evidence | Limitations | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC-01 | Domain dirty tree；local | 审查 reference、来源台账与调用方契约 | 可复用且权威边界明确 | reference 与来源边界完整，但 sample 的公共入口为空，调用方复用链路未闭合 | `ui-page-dialog-conventions.md`；`research/sources.json`；`sample/Index.ets` | 未建立真实 consumer fixture | failed |
| AC-02 | Domain dirty tree；local | 审查 `HMOS-RULE-09/10` | 范围、证据、失败处理完整 | UI/非 UI、中文注释和失败关闭均有明确条款 | `rules/BASE.md:224-295` | 语义型 literal/comment 仍需人工审查 | satisfied |
| AC-03 | Domain dirty tree；local | 审查 workflow 与两层 Skill | 实现前、中、构建前检查点齐全 | 三阶段检查和“build 不豁免结构错误”均存在 | `WORKFLOW.md`；两份 `SKILL.md`；reference | 未以新 consumer fixture 演练完整开发任务 | satisfied |
| AC-04 | Domain dirty tree；local | 审查 evaluator 的扫描与负向路径 | 可重复资源、目录、路由、注释及负向检查 | `HMOS-EVAL-12` 定义完整；本评估实际命中 mismatch 负向路径 | `EVALUATOR.md:353-397`；本报告命令记录 | 无设备运行时 | satisfied |
| AC-05 | CatchElf dirty tree；local | 目录、literal、资源、注释、route/export 审查 | sample 成为合规参考 | 目录、资源与注释符合；core/plugin mismatch、生成 API 兼容警告和空公共入口不符合完整参考契约 | sample 源文件；版本锁；build 输出；HAR 内容 | sample 整体未跟踪，无法和原始版本做 Git diff | failed |
| AC-06 | Domain dirty tree；bundled Python | 校验版本、registry、迁移边界并运行检查 | 3.0.0 同步且校验可复现 | 版本同步；breaking 范围记录；bundled Python 下 48 tests 通过；系统 Python 3.9.6 下命令失败 | `domain.json`；registry；兼容声明；两次校验输出 | 需要显式记录 Python 运行时；回滚证据不完整 | satisfied with limitations |
| AC-07 | CatchElf dirty tree；DevEco local | 执行授权的 sample debug build | 成功或准确失败证据 | 退出码 0，产出 19,701-byte `sample.har`；同时保留生成 API 与既有依赖警告 | build 命令输出；`sample/build/default/outputs/default/sample.har` | 未运行设备/UI 场景；build 自动执行 ohpm install 步骤 | satisfied with warnings |
| AC-08 | 本报告 | 独立读取、复现并给出唯一结论 | 独立结论与证据 | 已完成，由本报告给出结论 | 本文件 | Generator 仍需对账机器状态 | satisfied |

## Security, permission, compatibility, and rollback observations

- 未访问设备、账号、签名材料、生产数据或发布接口，也未修改实现。唯一新增文件为本评估记录。
- `devecocli build` 是已授权命令，但其内部自动执行 `ohpm install`，并报告清理 entry 下的若干
  “useless folder”；构建后 Git 状态仍只有评估前已存在的 `build-profile.json5` 修改和 `sample/`
  未跟踪项。后续证据应明确这种构建副作用。
- 兼容性最高风险是 plugin 1.2.0/core 1.2.4 与 compatible SDK 15 的组合；sample 生成代码的 API
  17/19 警告是直接构建证据，不应归并进无关模块的既有 ArkTS warnings。
- Domain 3.0.0 与 registry 已同步，且声明旧项目可继续 pin 2.x、新规则仅作用于新增或实质修改面；
  该迁移边界合理。sample 回滚则因缺少变更前基线不可执行。

## Evidence index and reproducibility

1. `PATH=/Users/albertq/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin:$PATH ./scripts/domain-check.sh`
   — exit 0；registry、Skill、Agent 校验通过；48 tests passed。
2. `./scripts/domain-check.sh`（系统 Python 3.9.6）— exit 1；`ModuleNotFoundError: tomllib`。
3. `devecocli build --modules sample --build-mode debug` — exit 0；`BUILD SUCCESSFUL`；同时报告上述
   sample 生成 API 兼容警告以及项目既有依赖/ArkTS warnings。
4. `rg` literal scan — sample 主 `.ets` 中没有十六进制颜色、可见文本构造器字面量、数字字号或匿名
   `pageUrl` 命中。
5. `sample/build/default/intermediates/router_map/default/hm_router_map.json` — 两条 route：
   `page://SamplePage` 与带 `dialog: true` 的 `dialog://SampleDialog`。
6. `sample/build/default/outputs/default/sample.har` — 19,701 bytes，时间
   `2026-08-28T21:33:26+0800`。
7. 关键内容指纹：`EVALUATOR.md` SHA-256
   `2054e6b53340ba9d6a63a3ecc9dd776dd57431bab4cdef15cbd83963d2c0a5d8`；reference
   `b8b48514f2964298671448d6f4df881b15e13ae0f9c60fed23a00dc53ab45844`；空 `sample/Index.ets`
   `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`。

## Summary, residual risks, and next action

AC-02、AC-03、AC-04、AC-06 与 AC-07 的核心交付已得到独立证据，资源/目录/中文注释的基础 sample
改造也成立；但新增评估器自身规定的 HMRouter mismatch 硬失败被真实命中，公共路由契约未从 HAR
入口暴露，sample 回滚也没有可恢复基线。当前不能完成 G2 交付。

最小下一步是：先由路由 Owner 解决或书面证明 core/plugin/compatible-SDK 组合；补齐 sample 的最小
公共路由导出与 consumer 编译证据；保存可执行的 sample 前后回滚单元。随后重跑同一 literal scan、
Domain 校验和 sample build，并重新进行独立评估。现有其他模块警告、设备运行时场景和 UI 交互证据
仍是残余风险，不应被本次成功 HAR 构建解释为已验证。
