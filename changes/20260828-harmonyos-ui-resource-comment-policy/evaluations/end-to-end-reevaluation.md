# HarmonyOS 页面、资源与中文注释策略独立复评

## Findings

### P3 — HMRouter 组合与生成 API 仍限制兼容性声明，但不构成本任务的功能失败

CatchElf 当前将 `@hadss/hmrouter-plugin` 锁定为 `1.2.0`，而 core 解析为 `1.2.4`；项目
compatible SDK 为 API 15。独立执行 sample debug 构建时，HMRouter 生成代码对 `onActive`、
`onInactive` 和 `onNewParam` 报告 API 17/19 警告，但构建以退出码 0 完成，普通页面与 Dialog
均生成路由记录，HAR 产物也成功生成。

本地安装的 HMRouter 1.2.4 README 使用“建议”表述 core/plugin 版本一致，并未把版本相等定义为
硬门槛；本变更的需求、Owner 决策和项目配置也没有这种硬门槛。本任务验收范围是 Domain 开发流程、
sample 结构、资源、中文注释、公共导出和配置构建，不要求证明 API 15 设备运行兼容性，也不要求设备
页面/Dialog 交互证据。因此该证据只使“API 15 运行兼容”保持未验证，不能据此虚构已发生的页面、
Dialog 或路由功能失败，也不能阻断不依赖该结论的验收项。

处置：保留为 compatibility warning 和残余风险；未来若任务明确承诺 API 15 运行兼容、项目新增
版本相等硬门槛，或实际必需运行旅程失败，再对相应兼容性或行为标准单独评估。

未发现 P0、P1 或 P2。尤其未发现构建成功被用于豁免目录分类、匿名路由、UI 魔法字面量、缺失资源
或无意义中文注释的情况。

## Verdict

**Pass**

- Evaluator：独立 Evaluator；未参与实现，未修改 Domain、sample 或首轮评估报告。
- Evaluated at：`2026-08-28T21:50:32+0800`。
- Domain baseline：commit `f359d6a8966665abef196af90b905afaa0f701fe` 加当前未提交变更；关键
  制品 SHA-256 见证据索引。
- CatchElf baseline：commit `2e7f43549e8b5f511861139513bfa1803520df66` 加既有
  `build-profile.json5` 修改和未跟踪 `sample/`；sample 关键文件 SHA-256 见证据索引。
- Environment：macOS，Asia/Shanghai；DevEco CLI `1.2.2`；compatible SDK 15；HMRouter core
  `1.2.4`；HMRouter compiler plugin `1.2.0`。

所有关键验收标准均已由当前内容、独立静态检查、Domain 校验或 sample 构建证据支持，且范围内没有
遗留 P0/P1。首轮评估记录保持原样作为历史证据；本报告评估的是 Owner 修订语义及修复后的当前内容。

## Critical journey result

独立复现的关键旅程为：读取 Owner 修订与来源边界；审查 `HMOS-RULE-09/10`、修订后的
`HMOS-EVAL-12` 和 UI reference；核对工作流、执行 Skills 与交付模板；检查 sample 的页面/Dialog
目录、集中路由、公共导出、资源和中文注释；扫描 UI 与路由字面量；运行 Domain 校验；执行 sample
debug 构建；检查生成路由图、HAR 公共声明和 HAR 产物。

观察结果：

- 普通页面位于 `pages/SamplePage.ets`，Dialog 位于 `dialogs/SampleDialog.ets`，旧的
  `pages/SampleDialog.ets` 不存在；Dialog 声明包含 `dialog: true`。
- `SamplePath.ets` 是两个协议字符串的唯一声明位置；页面、Dialog 和 `SamplePageInfo` 复用具名
  常量，没有匿名 `pageUrl`。
- `sample/Index.ets` 仅导出 `SamplePageInfo` 和 `SamplePath`；构建生成的 `Index.d.ets` 保留两项
  导出，证明 HAR 公共入口已闭合。
- 页面与 Dialog 的用户可见文案、应用颜色和字号分别引用 `string.json`、`color.json`、
  `float.json`；资源键均存在且 JSON 可解析。sample 没有本次受影响的额外 qualifier 目录。
- literal 扫描未命中直接 `Text('...')`、十六进制 UI 颜色、数字 `fontSize(...)`、字符串
  `pageUrl`、字符串 `fontColor` 或字符串 `backgroundColor`。
- 两个 UI 组件及其 `build` 方法、路由 metadata namespace 和路由类均有当前且有意义的中文职责
  注释；注释说明结构、资源化或集中路由意图，不是标识符复述或逐行填充。
- 生成路由图含 `page://SamplePage` 和 `dialog://SampleDialog` 两条记录，后者的
  `customData.dialog` 为 `true`。
- `devecocli build --modules sample --build-mode debug` 退出码为 0，输出
  `BUILD SUCCESSFUL` 和 `Build completed successfully`，生成 19,813-byte `sample.har`。
- API 17/19 警告保持可见；未执行设备/UI 交互，且这些场景不属于本任务要求，因此不能从构建推断
  运行时或 API 15 兼容性结论。

## Acceptance reconciliation

| Criterion | Rule / journey | Expected | Actual and evidence | Status / limitations |
| --- | --- | --- | --- | --- |
| AC-01 | 审查 UI reference、来源台账、Owner amendment 和公共入口 | 可复用契约且权威边界明确 | reference 明确 Owner、sample、HMRouter 与平台来源边界；`Index.ets` 和生成 `Index.d.ets` 均导出两项最小路由契约 | pass；未建立额外 consumer fixture，但当前标准未要求 |
| AC-02 | 审查 `HMOS-RULE-09/10` | UI 分类、资源、非 UI 常量、中文注释、证据和失败处理明确 | 两条规则保持结构/资源/注释硬失败，同时把版本/API warning 只限定到依赖它的兼容性声明 | pass |
| AC-03 | 审查 workflow、orchestrator Skill、business-module Skill | 有实现前、实现中、构建前检查点，构建不豁免结构审查 | 基线 inventory、资源先声明、路由集中、同步中文注释、构建前 literal/结构/语义审查均存在 | pass |
| AC-04 | 审查 `HMOS-EVAL-12` 和 delivery template，并实际执行负向扫描 | 资源、目录、路由、注释和负向路径可重复 | evaluator 明确扫描项、失败条件及 warning 边界；独立扫描未命中实际结构/资源/注释失败 | pass；设备场景非任务要求 |
| AC-05 | 检查 sample 源码、资源、公共导出和生成路由图 | sample 符合新约定且无新增 UI 魔法字面量 | 目录、route owner、Dialog flag、资源引用、中文注释与公共导出均符合；扫描无命中 | pass；API 15 兼容保持未验证 |
| AC-06 | 核对 manifest/registry/迁移说明并运行 Domain 校验 | Domain 3.0.0 同步且校验通过 | `domain.json` 与 registry 均为 3.0.0；breaking migration 边界已记录；registry、Skill、Agent 校验与 48 tests 通过 | pass；需使用已记录的 Python 3.9 `tomllib` compatibility path |
| AC-07 | 执行授权 sample debug build 并检查产物 | 构建通过或准确保留失败证据 | exit 0；HAR、路由图和公共声明产出；警告未被隐藏或描述为通过 | pass；不证明安装、设备运行、签名、发布或 API 15 兼容 |
| AC-08 | 独立复评并形成单一结论 | 独立 Evaluator 给出最终技术结论 | 本报告完成独立复评 | pass；`acceptance.json` 在报告写入前仍为 `evaluating` 且 AC-08 为 `pending`，须由 Generator/Owner 后续对账，不改变本次技术结论 |

## Security, permission, compatibility, and rollback observations

- 评估只读取源码、执行已授权确定性检查和 sample 构建，并新增本报告；未修改实现或首轮报告，未访问
  设备、账号、签名材料、生产数据、发布或部署接口。
- 构建内部执行 `ohpm install` 并清理 entry 下若干 useless folder；构建后 Git 状态仍为评估前已有的
  `build-profile.json5` 修改和未跟踪 `sample/`，未观察到新的已跟踪源码变更。
- HMRouter core/plugin 差异和生成 API 17/19 警告不能支持 API 15 运行兼容声明。本任务也没有提出该
  声明；因此它们是 compatibility warning，而不是观察到的功能失败或证据缺失型 blocker。
- `rollback-sample.md` 保存了修改前的 `SamplePage`、`SampleDialog`、`SamplePageInfo`、
  `SamplePath`、`string.json` 和未修改 `float.json` 内容，并为新增 `color.json`、Dialog 移动和
  `Index.ets` 导出提供逐文件逆操作；它明确禁止删除整个未跟踪 sample 或覆盖其他用户文件。该记录
  已修复首轮报告指出的不可恢复基线问题。
- 当前 change 的定向 `validate_change` 结果为 `PASS current change record`。全仓历史 change 债务
  不属于本变更，未被掩盖或修改。

## Evidence index and reproducibility

1. Domain validation：在 Domain 仓库执行
   `PYTHONPATH=/private/tmp/harness-tomllib-compat ./scripts/domain-check.sh`，exit 0；registry、
   Repository Skill、Project Custom Agent 校验通过；48 tests passed。前置 `xargs` 的 signal 13
   信息未阻止后续门槛执行或改变最终退出码。
2. Change validation：通过 workstation `scripts/validate_change.py` 的同一 `validate_change`
   函数定向检查当前 change，exit 0，输出 `PASS current change record`。
3. Sample build：在 CatchElf 根目录执行
   `devecocli build --modules sample --build-mode debug`，exit 0；生成路由 builder、路由图和 HAR，
   同时保留 API 17/19 与其他项目警告。
4. 路由图：`sample/build/default/intermediates/router_map/default/hm_router_map.json`，含普通页面和
   `dialog: true` 的 Dialog 两条记录。
5. 公共声明：
   `sample/build/default/intermediates/loader_out/default/etsFortgz/sample/Index.d.ets`，含
   `SamplePageInfo` 与 `SamplePath` 两项导出。
6. HAR：`sample/build/default/outputs/default/sample.har`，19,813 bytes，SHA-256
   `75c2039128d5c12525bdf621104fa494eb6e43c28e437bcfeb8fff6051cbdbc0`，时间
   `2026-08-28T21:48:20+0800`。
7. 静态检查：`find` 确认 UI 分类；`rg` 扫描直接可见文本、十六进制颜色、数字字号、匿名
   `pageUrl` 和字符串颜色参数无命中；资源引用与资源键逐项对照；JSON 解析成功。
8. Domain 关键内容 SHA-256：`EVALUATOR.md`
   `7e3ebae414c314c52c4a63f12405d8e582f00c5467ddf04b01b4bedba82f0dd8`；`BASE.md`
   `11ff122bbddb797de5ba083913808c6dd1d65df3abfd1963b2f2fa1f879ce6ff`；UI reference
   `d52471fb30c5722d6c63a85552f533b03f802dc4993db1f7cb3215973a43ed83`；Owner decision
   `79bf577cb020044e2ae7ca8b7f87d63841942d082d0c7842e6af678ccd76ae82`；rollback record
   `c70bc4b28ba5935f96a09d7426aa319c78eb9e994f9a6180eef54ad541ed6b24`。
9. Sample 关键内容 SHA-256：`Index.ets`
   `edea7dbddd8873b467b198a6a1579c1d5a965eb0c938905fcd39796686d0eb56`；`SamplePage.ets`
   `fc5bbfbf55f02020be0bc3230b37014a559049ff8593bb2144493e678707ce1d`；`SampleDialog.ets`
   `6185295b1959810e78f2fbbe5687d1e619fcf18dc34210c5211cd6620f233739`；`SamplePageInfo.ets`
   `a444daf18e48bf372f7b5facc8362b9f37adf02649a0c85a37a4eec049218c53`；`SamplePath.ets`
   `67319ef605f38d5414f59dbfbb00737703d7e624aec92f8513e1be339d9fb4a7`。

## Residual risks and next action

- API 15 页面/Dialog 运行兼容性、设备 UI 交互、安装、签名和发布均未验证，不能从本报告或成功构建
  推断；未来只有在任务要求这些声明时才需要对应目标证据。
- HMRouter plugin/core 版本差异以及生成 API 17/19 警告继续由项目 navigation/architecture Owner
  跟踪。对齐版本是可选风险降低动作，不是本变更通过的前置条件。
- 静态扫描不能完全自动判断任意未来字符串的 UI 语义，中文注释质量也仍需人工语义审查；新
  `HMOS-EVAL-12` 已保留这些硬要求。
- 最小下一步：Generator/Owner 将 `acceptance.json`、`task.md`、`progress.md` 与本独立结论对账，
  然后按 G2 流程完成变更记录；不得删除或改写首轮历史评估。
