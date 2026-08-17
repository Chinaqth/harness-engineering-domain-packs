# HarmonyOS Engineering Domain 中文导览

本文件是 `engineering.harmonyos` Domain Pack 的中文说明。英文生产制品是唯一权威契约；本导览只忠实解释现有职责和实际行为，不新增规则、权限、版本承诺或组织事实。当前版本为 `2.2.0`，生命周期为 `active`，Owner 为 `platform-harmony`。激活仅授予路由资格，不授予任何操作权限。

## 核心职责与运行方式

本 Domain 覆盖 Stage 模型应用与包设计、ArkTS 实现和静态正确性、ArkUI 界面交付、状态管理 V1→V2 迁移、废弃接口与兼容性分析、业务/provider 模块初始化、MVVM 业务模块开发，以及构建和运行时证据收集。新项目、新增 ArkUI 组件和重写的状态管理界面必须使用 V2；V1 仅作为遗留迁移输入，不得在新代码中引入。执行前必须获得任务所需的 SDK/API、工具链、目标设备、权限和验收基线；缺失的组织事实记录为 `needs-org-input`，不得猜测。

七个用户添加的 Skill 包作为非权威输入保留；另有两个 Domain 自有 Skill 分别负责模块配对初始化和完整业务模块开发。Domain 的九项能力统一绑定 `skills/harmonyos-engineering/SKILL.md` 执行 wrapper，并按 `capabilities.json` 接线到适用 Skill。`hmos-init-business-module` 只执行两个骨架、局部依赖与根清单变更；`hmos-business-module-development` 负责初始化后的 MVVM、V2、API/UI/router/hmdelegate/provider 架构与交付流程。早期七个保留包的逐 Skill 制品评分 Owner 豁免仍作为历史事实保留；任何保留包都不因接线或激活获得政策、版本或平台权威性。

`devecocli` 是 Domain 的组装适配器：统一承接文档检索、兼容性检查、lint、构建、设备发现与运行、UI 检查和日志采集。调用前要验证安装版本、子命令、参数和授权；Skill 中遗留的 `mcp_codegenie-*`、`deveco-mcp` 或示例命令不构成可用性保证，也不能绕过现有权限和证据要求。静态检查、构建、打包、运行和发布是彼此独立的证据类别，某一类成功不证明其他类别通过。

## 权威核心制品

| 路径 | 职责 | 实际行为 |
| --- | --- | --- |
| `DOMAIN.md` | 定义目的、边界、输入、输出、交接、失败模式和成熟度。 | 为所有 HarmonyOS 工作提供稳定专业基线，并明确 Skill 语料的辅助地位。 |
| `domain.json` | 声明 Domain 身份、版本、状态、Owner、兼容性和激活证据。 | 供注册表与生命周期校验使用；当前为 `active`，初始激活证据和 2.2.0 变更验收记录均由 manifest 引用。 |
| `owners.json` | 声明责任归属。 | 将主 Owner 绑定到 `platform-harmony`，不隐含额外审批权。 |
| `capabilities.json` | 组装能力、Workflow、Skill、Evaluator、工具、权限和依赖。 | 九类 HarmonyOS 能力统一绑定 `harmonyos-engineering/SKILL.md` wrapper；初始化与完整业务开发使用独立能力，其余项目验证通过 `devecocli` 组装证据。 |
| `routes.json` | 定义任务类型、识别信号和候选能力。 | 为兼容的 HarmonyOS 请求提供候选路由；Domain 已激活，具备路由资格。 |
| `README-CH.md` | 提供中文导览和完整生产文件清单。 | 解释英文制品，不产生新的规范。 |
| `rules/BASE.md` | 定义可执行的专业不变量。 | 强制新架构使用状态管理 V2，并约束版本基线、权威来源、Stage/ArkTS/ArkUI、V1 迁移、兼容性、工具、证据、权限和交接。 |
| `workflows/WORKFLOW.md` | 定义统一端到端工作流。 | 从任务归类和基线确认，经文档查证、设计/实现/迁移，到 `devecocli` 检查与证据交付。 |
| `evaluators/EVALUATOR.md` | 定义独立验收标准。 | 按证据类别、负向路径、严重度与硬门槛判定结果，不由作者自评。 |
| `templates/delivery-evidence.md` | 提供交付证据记录模板。 | 记录基线、来源、命令、诊断、迁移、运行场景、风险、交接和回滚信息。 |
| `skills/README.md` | 说明 Skill 包的发现和维护约定。 | 列出可加载 Skill，并强调其内容需受 Domain 规则、版本核验和授权约束。 |

## 必需目录

| 目录 | 职责与实际行为 |
| --- | --- |
| `rules/` | 保存 Domain 专业不变量；只能加强、不能削弱 Kernel 约束。 |
| `workflows/` | 保存可重复执行的前置条件、步骤、验证、失败处理与交接。 |
| `evaluators/` | 保存独立验收、负向路径、严重度和 verdict 语义。 |
| `templates/` | 保存不含项目私有事实的可复用交付结构。 |
| `skills/` | 保存能力统一绑定的执行 wrapper、七个按能力接线的非权威输入包，以及两个 Domain 自有业务模块 Skill。 |

## 执行 wrapper、Domain 自有 Skill 与七个保留包

### `harmonyos-engineering`：能力统一绑定的执行 wrapper

这是 Domain 的可执行 Skill 入口。它强制新项目、新增组件和重写状态界面采用状态管理 V2，将 V1 限定为遗留迁移输入；同时执行输入契约、权威来源核验、最小可回滚改动、证据类别分离和失败关闭交接。它不继承保留包的工具可用性、严重度、版本或验收结论；通用业务/provider 配对初始化脚本仅能执行声明的两个骨架、局部依赖与根清单变更，其余包声明必须先获得适用版本的官方文档与项目实证。

以下七个包按 `capabilities.json` 接线到相应能力，但仍不是英文核心制品之上的权威来源。

### `hmos-business-module-development`：HarmonyOS 业务模块完整开发

用于业务 HAR 初始化后的完整功能开发，并作为该 task type 的跨层主编排入口。ArkUI、ArkTS、Stage/package、初始化和验证能力只承担各自子任务，不能静默改写已接受的 MVVM、目录、路由/壳分离、provider 依赖方向或公共接口决策。它要求 View 只负责 `components/`、`dialogs/`、`pages/` 的声明式 UI 与事件转发，ViewModel 负责业务动作、异步编排和可变展示状态，并对新写或重写状态使用 `@ObservedV2` 与有刷新需求的 `@Trace`。网络入口收敛到 `api/`，模块路由收敛到 `router/`，壳工程适配收敛到 `hmdelegate/` 或显式项目映射目录。存在 `<module>provider` 时，provider 只声明 `XxxServiceProvider`、`XxxComponentProvider` 和唯一 `XxxProvider` 工厂/访问点，实际实现位于业务 HAR，外部消费者不得直接依赖业务内部实现路径。

### `hmos-init-business-module`：HarmonyOS 业务模块与 provider 配对初始化

在确认项目根目录、声明的相对模块目录、根 `build-profile.json5`、合法模块 ID、两个目标均不存在及写入授权后，运行包内 Python 脚本创建业务 HAR 和 `providers/<module_id>provider` HAR，登记两个根模块，并在业务包中添加 provider 的相对 `file:` 依赖；未指定业务目录时默认使用 `features/`。Provider 的 `src/main/ets/` 与 `Index.ets` 保持空，不生成 Service、接口、Router 或其他实现，也不复制参考工程的锁文件和依赖缓存；失败时必须验证两个模块、根清单和新建的空 `providers/` 目录均已回滚。

### `hmos-arkts-knowledge-retriever`：ArkTS 语言知识检索

使用索引与检索脚本在保留的 ArkTS 语言指南语料中定位语法、标准库、并发、运行时、工具链和迁移资料；返回本地路径用于追溯。索引和片段只用于发现，版本敏感结论仍须与当前权威文档及实际工具输出核对。

### `hmos-arkui-knowledge-retriever`：ArkUI 知识检索

使用本地索引、加载器和检索器查询保留的 ArkUI 组件、状态管理、布局、交互、导航、渲染、扩展、主题、无障碍、性能、窗口和错误码语料；为其他 Skill 提供可追溯候选依据，但不自行生成或修改业务代码。

### `hmos-arkui-develop-skill`：ArkUI 开发

组织 ArkUI 页面与组件的需求澄清、API 查证、实现、诊断和验证，并使用保留的快速 API、规则、常见错误和检查清单。该包始终受 wrapper 的 V2 架构政策约束；其中任何 V1 示例只能作为迁移候选材料。任何缓存示例都须服从声明的 SDK/API 基线、项目约定和实际编译或运行证据。

### `hmos-arkts-syntax-checker`：ArkTS 语法与构建诊断

指导源文件扫描、诊断分类、限次修复和构建结果记录。Skill 内遗留的工具名和示例不是可直接假定存在的接口；Domain 在执行时通过已验证且获授权的 `devecocli` lint/build 能力或项目提供的等价流程完成适配。

### `hmos-arkts-deprecated-interface-checker`：废弃接口与兼容性检查

组织废弃接口扫描、逐项处置、替代方案查证和复验。内置参考表用于候选定位，不替代目标版本的权威接口文档；Domain 通过 `devecocli check compat`、lint、文档检索和构建证据组装实际检查。

### `hmos-arkui-statemgt-migration`：ArkUI 状态管理 V1→V2 迁移

提供装饰器、数据对象、应用级状态、渲染控制、复用和动画等迁移场景的步骤、参考和测试案例。迁移按行为与依赖分批验证，不能把映射表当作机械替换规则。

## 完整生产文件清单

以下清单按 Skill 包分组。每个路径均相对于本 Domain 根目录；逐项列出是为了让当前仓库校验器和维护者能够核对全部非隐藏生产文件。清单本身只说明文件归属：核心文件按上表职责运行；每个 Skill 的 `SKILL.md` 定义操作指引，`README.md` 提供包内说明，`references/` 保存所述主题的保留参考语料或索引，`scripts/` 保存检索辅助程序，`test-cases/` 保存迁移验证案例。

### 完整生产目录清单

以下路径是当前 Domain 根目录下的全部非隐藏生产目录。每个路径均精确相对于 Domain 根目录并以 `/` 结尾；嵌套目录沿用所属 Skill 的职责说明。`scripts/__pycache__/` 是当前仓库中实际存在的非隐藏目录，仅作为现状清点，不表示应依赖其中的生成缓存。

- `evaluators/`
- `rules/`
- `skills/`
- `skills/hmos-business-module-development/`
- `skills/hmos-business-module-development/references/`
- `skills/hmos-init-business-module/`
- `skills/hmos-init-business-module/agents/`
- `skills/hmos-init-business-module/assets/`
- `skills/hmos-init-business-module/assets/module-template/`
- `skills/hmos-init-business-module/assets/module-template/src/`
- `skills/hmos-init-business-module/assets/module-template/src/main/`
- `skills/hmos-init-business-module/assets/module-template/src/main/resources/`
- `skills/hmos-init-business-module/assets/module-template/src/main/resources/base/`
- `skills/hmos-init-business-module/assets/module-template/src/main/resources/base/element/`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/ets/`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/ets/test/`
- `skills/hmos-init-business-module/assets/module-template/src/test/`
- `skills/hmos-init-business-module/assets/provider-template/`
- `skills/hmos-init-business-module/assets/provider-template/src/`
- `skills/hmos-init-business-module/assets/provider-template/src/main/`
- `skills/hmos-init-business-module/assets/provider-template/src/main/resources/`
- `skills/hmos-init-business-module/assets/provider-template/src/main/resources/base/`
- `skills/hmos-init-business-module/assets/provider-template/src/main/resources/base/element/`
- `skills/hmos-init-business-module/scripts/`
- `skills/harmonyos-engineering/`
- `skills/hmos-arkts-deprecated-interface-checker/`
- `skills/hmos-arkts-deprecated-interface-checker/references/`
- `skills/hmos-arkts-knowledge-retriever/`
- `skills/hmos-arkts-knowledge-retriever/references/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/01-getting-started-with-arkts/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/06-cross-language-interaction/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/08-coding-guide-and-practices/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/08-coding-guide-and-practices/01-coding-style-guide/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/08-coding-guide-and-practices/02-performant-programming-practices/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/01-typescript-to-arkts/`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/02-other-languages-to-arkts/`
- `skills/hmos-arkts-knowledge-retriever/scripts/`
- `skills/hmos-arkts-syntax-checker/`
- `skills/hmos-arkts-syntax-checker/references/`
- `skills/hmos-arkui-develop-skill/`
- `skills/hmos-arkui-develop-skill/references/`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/`
- `skills/hmos-arkui-develop-skill/references/quick-apis/`
- `skills/hmos-arkui-develop-skill/references/quick-rules/`
- `skills/hmos-arkui-knowledge-retriever/`
- `skills/hmos-arkui-knowledge-retriever/references/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/common-attribute/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/media/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/security/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/particle/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/drag/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/router/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/modal/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/12-i18n/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/13-accessibility/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/analysis/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/stability/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/embedded/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/`
- `skills/hmos-arkui-knowledge-retriever/scripts/`
- `skills/hmos-arkui-knowledge-retriever/scripts/__pycache__/`
- `skills/hmos-arkui-statemgt-migration/`
- `skills/hmos-arkui-statemgt-migration/references/`
- `skills/hmos-arkui-statemgt-migration/test-cases/`
- `templates/`
- `workflows/`

### 核心制品

- `DOMAIN.md`
- `README-CH.md`
- `capabilities.json`
- `domain.json`
- `evaluators/EVALUATOR.md`
- `owners.json`
- `routes.json`
- `rules/BASE.md`
- `skills/README.md`
- `skills/harmonyos-engineering/SKILL.md`
- `skills/hmos-business-module-development/SKILL.md`
- `skills/hmos-business-module-development/references/business-module-architecture.md`
- `templates/delivery-evidence.md`
- `workflows/WORKFLOW.md`

### HarmonyOS 业务模块与 provider 配对初始化包文件

- `skills/hmos-init-business-module/SKILL.md`
- `skills/hmos-init-business-module/agents/openai.yaml`
- `skills/hmos-init-business-module/assets/module-template/.gitignore`
- `skills/hmos-init-business-module/assets/module-template/Index.ets`
- `skills/hmos-init-business-module/assets/module-template/build-profile.json5`
- `skills/hmos-init-business-module/assets/module-template/hvigorfile.ts`
- `skills/hmos-init-business-module/assets/module-template/obfuscation-rules.txt`
- `skills/hmos-init-business-module/assets/module-template/oh-package.json5`
- `skills/hmos-init-business-module/assets/module-template/src/main/module.json5`
- `skills/hmos-init-business-module/assets/module-template/src/main/resources/base/element/float.json`
- `skills/hmos-init-business-module/assets/module-template/src/main/resources/base/element/string.json`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/ets/test/Ability.test.ets`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/ets/test/List.test.ets`
- `skills/hmos-init-business-module/assets/module-template/src/ohosTest/module.json5`
- `skills/hmos-init-business-module/assets/module-template/src/test/List.test.ets`
- `skills/hmos-init-business-module/assets/module-template/src/test/LocalUnit.test.ets`
- `skills/hmos-init-business-module/assets/provider-template/.gitignore`
- `skills/hmos-init-business-module/assets/provider-template/Index.ets`
- `skills/hmos-init-business-module/assets/provider-template/build-profile.json5`
- `skills/hmos-init-business-module/assets/provider-template/hvigorfile.ts`
- `skills/hmos-init-business-module/assets/provider-template/obfuscation-rules.txt`
- `skills/hmos-init-business-module/assets/provider-template/oh-package.json5`
- `skills/hmos-init-business-module/assets/provider-template/src/main/module.json5`
- `skills/hmos-init-business-module/assets/provider-template/src/main/resources/base/element/float.json`
- `skills/hmos-init-business-module/assets/provider-template/src/main/resources/base/element/string.json`
- `skills/hmos-init-business-module/scripts/init_business_module.py`

### ArkTS 语言知识检索包文件

- `skills/hmos-arkts-knowledge-retriever/README.md`
- `skills/hmos-arkts-knowledge-retriever/SKILL.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/01-getting-started-with-arkts/arkts-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/advanced-operators.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/classes.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/collection-types.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/concurrency.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/control-flow.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/enumerations.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/error-handling.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/functions.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/generics.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/inheritance.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/initialization.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/interfaces.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/methods.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/properties.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/strings.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/02-basic-syntax/type-casting.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/arkts-json.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/arkts-utils-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/buffer.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/container-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/linear-container.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/nonlinear-container.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/xml-conversion.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/xml-generation.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/xml-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/03-common-library/xml-parsing.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arkts-async-lock-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arkts-collections-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arkts-condition-variable-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arkts-sendable-module.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arkts-sendable.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/arraybuffer-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/ason-parsing-generation.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/async-concurrency-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/batch-database-operations-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/concurrency-faq.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/concurrency-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/concurrent-loading-modules-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/container-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/cpu-intensive-task-development.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/global-configuration-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/independent-time-consuming-task.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/interthread-communication-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/io-intensive-task-development.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/long-time-task-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/long-time-task-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/makeobserved-sendable.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/multi-thread-cancel-task.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/multi-thread-concurrency-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/multi-time-consuming-tasks.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/multithread-develop-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/napi-coerce-to-native-binding-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/napi-define-sendable-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/native-interthread-shared.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/normal-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/resident-task-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/resident-task-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/sendable-constraints.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/sendable-freeze.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/sendable-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/sendablelrucache-recent-list.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/serializable-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/shared-arraybuffer-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/sync-task-development.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/taskpool-async-task-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/taskpool-communicates-with-mainthread.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/taskpool-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/taskpool-vs-worker.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/taskpool-waterflow.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/time-consuming-task-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/transferabled-object.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/worker-and-taskpool.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/worker-communicates-with-mainthread.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/worker-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/worker-invoke-mainthread-interface.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/04-concurrency/worker-postMessage-sendable.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-dynamic-import.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-import-native-module.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-lazy-import.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-module-side-effects.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-runtime-faq.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/arkts-runtime-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/gc-introduction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/js-apis-load-native-module.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/load-module-base-nodeapi.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/05-runtime/module-principle.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/06-cross-language-interaction/arkts-cross-language-interaction.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/arkoptions-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/arkts-bytecode-file-format.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/arkts-bytecode-function-name.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/arkts-bytecode-fundamentals.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/arkts-bytecode-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/bytecode-obfuscation-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/bytecode-obfuscation-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/bytecode-obfuscation-practice.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/bytecode-obfuscation-questions.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/bytecode-obfuscation.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/compilation-tool-chain-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/customize-bytecode-during-compilation.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/es2abc-faq.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/source-obfuscation-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/source-obfuscation-overview.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/source-obfuscation-practice.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/source-obfuscation-questions.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/source-obfuscation.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/07-compilation-toolchain/tool-disassembler.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/08-coding-guide-and-practices/01-coding-style-guide/arkts-coding-style-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/08-coding-guide-and-practices/02-performant-programming-practices/arkts-high-performance-programming.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/01-typescript-to-arkts/arkts-migration-background.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/01-typescript-to-arkts/arkts-more-cases.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/01-typescript-to-arkts/typescript-to-arkts-migration-guide.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/02-other-languages-to-arkts/getting-started-with-arkts-for-java-programmers.md`
- `skills/hmos-arkts-knowledge-retriever/references/arkts-language-guide/09-migration-guide/02-other-languages-to-arkts/getting-started-with-arkts-for-swift-programmers.md`
- `skills/hmos-arkts-knowledge-retriever/references/doc_index.json`
- `skills/hmos-arkts-knowledge-retriever/references/snippet_index.json`
- `skills/hmos-arkts-knowledge-retriever/references/topic_aliases.json`
- `skills/hmos-arkts-knowledge-retriever/scripts/search_docs.py`

### ArkUI 知识检索包文件

- `skills/hmos-arkui-knowledge-retriever/README.md`
- `skills/hmos-arkui-knowledge-retriever/SKILL.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkts-create-custom-components.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkts-declarative-ui-description.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkts-page-custom-components-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkts-page-custom-components-lifecycle.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkts-ui-development-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkui-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/arkui-support-for-aging-adaptation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/ts-appendix-enums.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/ts-custom-component-api.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/ts-custom-component-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/ts-custom-component-lifecycle.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/01-basics/ts-custom-component-parameter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-application-state-management-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-custom-components-access-restrictions.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-custom-components-freeze.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-custom-components-freezeV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-custom-components-new-lifecycle.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-decorator-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-extend-components-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-mvvm-v2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-mvvm.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-state-management-faq-application-and-others.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-state-management-faq-inner-class.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-state-management-faq-inner-component.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-state-management-faq.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-track.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/arkts-two-way-sync.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/advanced/troubleshooting-state-manage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-animateTo.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-application.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-inner-class.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-inner-component.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-inner-object.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-rendering-control-repeat.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration-reusable.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-migration.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-mixusage-before-api-version.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-mixusage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/migration/arkts-v1-v2-update-difference.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/ts-universal-attributes-reuse-id.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/ts-universal-attributes-reuse.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-animatable-extend.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-appstorage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-builder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-builderparam.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-environment.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-link.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-localBuilder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-localstorage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-mutableBuilder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-observed-and-objectlink.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-persiststorage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-prop.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-provide-and-consume.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-require.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-reusable.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-state-management-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-state.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-watch.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/arkts-wrapBuilder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-animatable-extend.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-state-management-environment-variables.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-state-management-v1-parameter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-state-management-watch-monitor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-state-management.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v1/ts-universal-wrapBuilder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-addMonitor-clearMonitor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-applySync-flushUpdates-flushUIUpdates.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-appstoragev2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-binding.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-canBeObserved.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-computed.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-getTarget.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-local.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-makeObserved.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-monitor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-observedV2-and-trace.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-once.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-param.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-persistencev2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-provider-and-consumer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-reusableV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-syncmonitor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-new-type.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/02-state-management/v2/arkts-state-management-introduce.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/arkts-layout-debug.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/arkts-layout-development-create-looping.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/arkts-layout-development-dynamiclayout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/arkts-layout-development-media-query.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/advanced/arkts-list-grid-development-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/arkts-layout-development-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/arkts-layout-development-create-arclist.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/arkts-layout-development-create-grid.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/arkts-layout-development-create-list.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/arkts-layout-development-create-waterflow.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/arkts-layout-development-grid-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-arclist.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-arclistitem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-flowitem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-grid.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-gridcol.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-gridrow.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-lazyvgridlayout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-list.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-listitem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-listitemgroup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/grid-list/ts-container-waterflow.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/arkts-layout-development-flex-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/arkts-layout-development-linear.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/ts-container-column.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/ts-container-flex.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/linear/ts-container-row.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/arkts-layout-development-arcswiper.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/arkts-layout-development-relative-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/arkts-layout-development-stack-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-basic-components-nodecontainer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-alphabet-indexer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-arc-alphabet-indexer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-arcswiper.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-badge.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-counter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-folderstack.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-hyperlink.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-navigator.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-panel.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-refresh.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-relativecontainer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-scroll.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-sidebarcontainer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-stack.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-swiper.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-tabcontent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/other/ts-container-tabs.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-flex-layout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-grid.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-layout-constraints.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-location.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-size.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/03-layout/ts-universal-attributes-z-order.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/arkts-advanced-components-arcbutton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/arkts-common-components-richeditor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ArcButton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ArcSlider.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-Chip.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ChipGroup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ComposeListItem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ComposeTitleBar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-Counter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-Dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-DialogV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-DownloadFileButton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-EditableTitleBar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ExceptionPrompt.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-Filter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-FoldSplitContainer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-FullScreenLaunchComponent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-GridObjectSortComponent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-InnerFullScreenLaunchComponent-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-MultiNavigation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-Popup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ProgressButton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ProgressButtonV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SegmentButton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SegmentButtonV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SelectTitleBar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SelectionMenu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SplitLayout.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SubHeader.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SubHeaderV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-SwipeRefresher.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-TabTitleBar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ToolBar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-ToolBarV2.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-TreeView.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ohos-arkui-advanced-formmenu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ts-basic-components-richeditor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ts-basic-components-richtext.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ts-basic-components-xcomponent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/advanced/ts-container-formlink.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-button.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-progress-indicator.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-radio-button.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-switch.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-symbol.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-text-display.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/arkts-common-components-text-input.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-blank.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-button.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-checkbox.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-checkboxgroup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-divider.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-image.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-imagespan.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-loadingprogress.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-marquee.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-progress.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-radio.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-rating.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-search.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-select.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-slider.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-span.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-symbolGlyph.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-symbolSpan.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-text.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-textarea.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-textinput.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-toggle.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-basic-components-toolbaritem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-image-common.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/basic/ts-text-common.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/common-attribute/ts-universal-attributes-component-id.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/common-attribute/ts-universal-attributes-obscured.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/common-attribute/ts-universal-attributes-restoreId.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/common-attribute/ts-universal-attributes-text-style.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-calendarpicker.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-datapanel.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-gauge.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-qrcode.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-textclock.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-basic-components-texttimer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/display/ts-information-display-common.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/arkts-drawing-customization-on-canvas.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/arkts-geometric-shape-drawing.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/arkts-shape-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-canvasrenderingcontext2d.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-canvas.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-canvasgradient.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-canvaspattern.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-imagebitmap.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-imagedata.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-matrix2d.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-canvas-path2d.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-components-offscreencanvas.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-circle.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-ellipse.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-line.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-path.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-polygon.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-polyline.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-rect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawing-components-shape.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-drawingrenderingcontext.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/drawing/ts-offscreencanvasrenderingcontext2d.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/media/arkts-common-components-video-player.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/media/ts-basic-components-imageanimator.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/media/ts-media-components-video.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-datepicker.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-patternlock.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-stepper.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-stepperitem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-textpicker.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-basic-components-timepicker.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/picker/ts-picker-common.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/security/ts-security-components-pastebutton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/security/ts-security-components-savebutton.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/04-components/security/ts-securitycomponent-attributes.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-animation-smoothing.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-animator.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-component-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-curve-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-spring-curve.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/arkts-traditional-curve.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/curve/ts-animatorproperty.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/particle/arkts-particle-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/particle/ts-particle-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/arkts-attribute-animation-apis.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/arkts-attribute-animation-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/arkts-custom-attribute-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/ts-explicit-animatetoimmediately.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/ts-explicit-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/ts-keyframeAnimateTo.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/property/ts-motion-path-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/arkts-enter-exit-transition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/arkts-page-transition-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/arkts-rotation-transition-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/arkts-shared-element-transition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/arkts-transition-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/ts-page-transition-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/ts-transition-animation-component.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/ts-transition-animation-geometrytransition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/transition/ts-transition-animation-shared-elements.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/ts-universal-attributes-click-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/05-animation/ts-universal-attributes-motionBlur.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/drag/arkts-common-events-drag-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/drag/ts-universal-events-drag-drop.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/arkts-common-events-crown-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/arkts-common-events-focus-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/ts-universal-attributes-focus.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/ts-universal-events-crown.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/ts-universal-events-focus_axis.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/focus/ts-universal-focus-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/arkts-gesture-events-binding.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/arkts-gesture-events-combined-gestures.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/arkts-gesture-events-gesture-judge.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/arkts-gesture-events-multi-level-gesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/arkts-gesture-events-single-gesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-longpressgesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-pangesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-pinchgesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-rotationgesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-swipegesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-basic-gestures-tapgesture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-combined-gestures.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-gesture-settings.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/gesture/ts-gesturehandler.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-capability-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-development-guide-gamepad.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-development-guide-keyboard.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-development-guide-mouse.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-development-guide-touch-screen.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/guide/arkts-interaction-development-guide-touchpad.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-uicommonevent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-uigestureevent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-axis.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-click.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-hover.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-key.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-keyboardshortcut.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-events-touch.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/touch-mouse/ts-universal-mouse-key.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-click.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-cursor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-drag-drop.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-drag-sorting.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-enable.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-foreground-blur-style.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-hit-test-behavior.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-hover-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-monopolize-events.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-on-child-touch-test.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-on-touch-intercept.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-attributes-touch-target.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-events-drag-drop-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/06-interaction/ts-universal-events-show-hide.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-animation-faq.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-animation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-architecture.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-cross-package.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-introduction.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-jump.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-navdestination.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/arkts-navigation-split-mode.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/ts-basic-components-navdestination.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/ts-basic-components-navigation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/navigation/ts-basic-components-navrouter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/router/arkts-router-to-navigation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/router/arkts-routing.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/ts-universal-attributes-modal-transition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/ts-universal-attributes-sheet-transition-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/ts-universal-attributes-sheet-transition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-atomicservicebar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-componentsnapshot.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-componentutils.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-contextmenucontroller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-cursorcontroller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-dragcontroller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-dynamicsyncscene.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-e.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-focuscontroller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-framecallback.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-i.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-marqueedynamicsyncscene.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-measureutils.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-mediaquery.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-overlaymanager.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-promptaction.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-router.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-swiperdynamicsyncscene.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-t.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-textmenucontroller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-uicontext.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-uiinspector.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-apis-uicontext-uiobserver.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-global-interface.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/07-navigation/uicontext/arkts-wrong-uicontext-debug.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-base-dialog-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-common-components-custom-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-contentcover-page.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-create-toast.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-dialog-controller.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-dialog-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-embedded-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/arkts-sheet-page.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-action-sheet.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-alert-dialog-box.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-calendarpicker-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-custom-dialog-box.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-datepicker-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-textpicker-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/dialog/ts-methods-timepicker-dialog.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-menu-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-popup-and-menu-components-menu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-popup-and-menu-components-popup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-popup-and-menu-components-uicontext-menu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-popup-and-menu-components-uicontext-popup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/arkts-popup-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/ts-basic-components-menu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/ts-basic-components-menuitem.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/ts-basic-components-menuitemgroup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/ts-universal-attributes-menu.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/menu/ts-universal-attributes-popup.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/modal/arkts-modal-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/modal/arkts-modal-transition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/ts-universal-attributes-tips.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/08-dialog-menu/ts-universal-attributes-toolbar.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-lazyforeach-repeat-migration-guide.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-new-rendering-control-repeat.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-rendering-control-contentslot.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-rendering-control-foreach.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-rendering-control-ifelse.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-rendering-control-lazyforeach.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/arkts-rendering-control-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-components-contentSlot.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-rendering-control-foreach.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-rendering-control-lazyforeach.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-rendering-control-repeat.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-expand-safe-area.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-filter-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-image-effect-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-image-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-opacity.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-overlay.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-pixelRoundForComponent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-pixelRoundForPage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-point-light-style-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-renderfit.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-sharp-clipping.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-transformation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-use-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/09-rendering/ts-universal-attributes-visibility.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/arkts-user-defined-composition.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/arkts-user-defined-draw.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/arkts-user-defined-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/arkts-user-defined-place-holder.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/custom-component/arkts-user-defined.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/arkts-common-attributes-content-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/arkts-user-defined-extension-attributeModifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/arkts-user-defined-extension-attributeUpdater.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/arkts-user-defined-extension-drawModifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/ts-universal-attributes-attribute-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/ts-universal-attributes-attribute-symbolglyphmodifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/ts-universal-attributes-content-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/ts-universal-attributes-draw-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/modifier/ts-universal-attributes-gesture-modifier.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/arkts-user-defined-arktsNode-builderNode.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/arkts-user-defined-arktsNode-crossLanguage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/arkts-user-defined-arktsNode-frameNode.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/arkts-user-defined-arktsNode-renderNode.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/node/arkts-user-defined-node.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/10-extension/ts-universal-attributes-custom-property.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-blur-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-clip-shape.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-color-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-extend.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-shadow-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-statestyles.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/arkts-style.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/theme_skinning.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-container-with-theme.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-background.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-border-image.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-border.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-foreground-color.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-foreground-effect.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-gradient-color.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-outline.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ts-universal-attributes-polymorphic-style.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/11-theme-style/ui-dark-light-color-adaptation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/12-i18n/arkts-internationalization.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/13-accessibility/arkts-universal-attributes-accessibility.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/13-accessibility/ts-universal-accessibility-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/13-accessibility/ts-universal-accessibility-hover-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/13-accessibility/ts-universal-attributes-accessibility.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/analysis/arkts-inspector-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/analysis/ui-ide-previewer.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/analysis/ui-inspector-profiler.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/analysis/ui-performance-overview.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/stability/arkts-stability-crash-issues.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/stability/arkts-stability-freeze-issues.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/14-performance/stability/arkts-stability-guide.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/arkts-FullScreenComponent.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/ohos-atomicservice-AtomicServiceNavigation.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/ohos-atomicservice-AtomicServiceSearch.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/ohos-atomicservice-AtomicServiceTabs.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/atomic-service/ohos-atomicservice-AtomicServiceWeb.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/embedded/arkts-embedded-components.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/arkts-isolated-components-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/arkts-ui-extension-components-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/ts-basic-components-formcomponent-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/ts-container-ability-component-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/ts-container-embedded-component.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/ts-container-isolated-component-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/15-advanced/system-cability/ts-container-ui-extension-component-sys.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-apis-uicontext-font.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-apis-window-Window.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-apis-window-WindowStage.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-apis-window.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-env-system-property.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-manage-components-visibility.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/16-window/arkts-manage-keyboard.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-bindSheet.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-canvas.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-display.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-drag-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-event.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-focus.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-force-dark.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-internal.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-node-render-monitor.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-node-render.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-node.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-nodeadapter.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-promptAction.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-router.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-scroll.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-snapshot.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-stateManagement.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-styled-string.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-system-resource.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-uiappearance.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-uicontext.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-uiextension.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-video.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-window.md`
- `skills/hmos-arkui-knowledge-retriever/references/knowledges/17-error-code/errorcode-xcomponent.md`
- `skills/hmos-arkui-knowledge-retriever/scripts/__pycache__/document_loader.cpython-313.pyc`
- `skills/hmos-arkui-knowledge-retriever/scripts/__pycache__/document_loader.cpython-314.pyc`
- `skills/hmos-arkui-knowledge-retriever/scripts/__pycache__/retriever.cpython-313.pyc`
- `skills/hmos-arkui-knowledge-retriever/scripts/__pycache__/retriever.cpython-314.pyc`
- `skills/hmos-arkui-knowledge-retriever/scripts/document_loader.py`
- `skills/hmos-arkui-knowledge-retriever/scripts/retriever.py`
- `skills/hmos-arkui-knowledge-retriever/scripts/run.py`

### ArkUI 开发包文件

- `skills/hmos-arkui-develop-skill/README.md`
- `skills/hmos-arkui-develop-skill/SKILL.md`
- `skills/hmos-arkui-develop-skill/references/checklist.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/01-import.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/02-uicontext.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/03-v1v2-mix.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/04-decorator-position.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/05-build-violations.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/06-foreach.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/07-attribute-params.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/08-navigation.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/09-nesting-naming.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/10-type-annotation.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/11-deprecated.md`
- `skills/hmos-arkui-develop-skill/references/common-mistakes/_index.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/01-layout.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/02-basic-components.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/03-data-display.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/04-selectors.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/05-media.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/06-advanced.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/07-security.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/08-state-decorators.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/09-animation.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/10-gesture.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/11-dialog-menu.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/12-navigation.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/13-rendering.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/14-extension.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/15-theme-style.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/16-enums.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/17-resources.md`
- `skills/hmos-arkui-develop-skill/references/quick-apis/_index.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/01-component.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/02-build.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/03-state-v1.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/04-state-v2.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/05-v1v2-mix.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/06-access.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/07-rendering.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/08-animation.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/09-navigation.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/10-dialog.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/11-style.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/12-extension.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/13-interaction.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/14-layout.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/15-visibility.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/16-performance.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/17-particle.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/18-error-code.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/19-uicontext.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/20-import.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/21-reserved-words.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/22-attribute-params.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/23-deprecated.md`
- `skills/hmos-arkui-develop-skill/references/quick-rules/_index.md`
- `skills/hmos-arkui-develop-skill/references/search-strategy.md`
- `skills/hmos-arkui-develop-skill/references/style-guide.md`

### ArkTS 语法与构建诊断包文件

- `skills/hmos-arkts-syntax-checker/README.md`
- `skills/hmos-arkts-syntax-checker/SKILL.md`
- `skills/hmos-arkts-syntax-checker/references/error-fixing-examples.md`
- `skills/hmos-arkts-syntax-checker/references/output-examples.md`

### 废弃接口与兼容性检查包文件

- `skills/hmos-arkts-deprecated-interface-checker/README.md`
- `skills/hmos-arkts-deprecated-interface-checker/SKILL.md`
- `skills/hmos-arkts-deprecated-interface-checker/references/configuration-reference.md`
- `skills/hmos-arkts-deprecated-interface-checker/references/deprecated-api-reference.md`

### ArkUI 状态管理 V1→V2 迁移包文件

- `skills/hmos-arkui-statemgt-migration/README.md`
- `skills/hmos-arkui-statemgt-migration/SKILL.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-animateTo.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-application.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-inner-class.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-inner-component.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-inner-object.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-rendering-control-repeat.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration-reusable.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v1-v2-migration.md`
- `skills/hmos-arkui-statemgt-migration/references/arkts-v2-decorators.md`
- `skills/hmos-arkui-statemgt-migration/test-cases/v1-to-v2-migration-test-cases.md`

## 维护说明

目录内容变化后必须同步更新本清单。保留语料可以继续随 Skill 包存在，但其来源、版本、时效和工具依赖仍需在实际任务中核验。若本导览与英文核心制品、当前权威平台文档或观察到的工具结果冲突，以英文核心制品规定的来源优先级和交接流程处理。
