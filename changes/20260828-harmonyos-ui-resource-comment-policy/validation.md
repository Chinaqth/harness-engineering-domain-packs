# 生成者验证记录

## 范围

- Domain Pack：`engineering.harmonyos@3.0.0`
- 项目参考：`/Users/albertq/zyc-wrok-space/CatchElf/CatchElf-Harmony/sample`
- 日期：2026-08-28（Asia/Shanghai）
- 权限：本地源码编辑、确定性校验和 sample debug 构建；未运行设备、UI、日志、签名或发布操作。

## 静态与结构检查

执行：

```text
git diff --check
python3 -m json.tool <changed-json>
rg -n "Text\(['\"]|#[0-9A-Fa-f]{6,8}|\.fontSize\([0-9]" sample/src/main/ets
find sample/src/main/ets -maxdepth 2 -type f
```

结果：Domain Pack 与 CatchElf diff whitespace 检查通过；变更 JSON 均可解析；sample 的变更
`.ets` 中未发现直接 `Text('...')`、十六进制颜色或数字 `fontSize(...)`；文件清单显示普通页面位于
`pages/SamplePage.ets`，Dialog 位于 `dialogs/SampleDialog.ets`，路由声明位于 `router/`。

## CatchElf sample 构建

先通过 `devecocli build --help` 确认参数，再在 CatchElf 项目根目录执行：

```text
devecocli build --modules sample --build-mode debug
```

结果：exit 0，`BUILD SUCCESSFUL`，`Build completed successfully`。HMRouter 插件为
`SampleDialog` 和 `SamplePage` 生成 builder，并生成 `hm_router_map.json` 后按插件流程清理。

构建保留的非阻塞警告：

- 项目级 `common_ui` 本地依赖可能形成循环引用。
- `@life/zyc_core` 在项目级 `build-profile.json5` 中缺少模块信息。
- 依赖模块存在既有 ESObject、废弃 API、权限和设备能力警告。
- HMRouter 1.2.4 生成代码使用 API 17/19 生命周期接口，而当前 compatible SDK 为 API 15。
- 编译器对 sample 的两个 `@ComponentV2` 输出 `use invalid decorator` 警告，但仍完成 HAR 编译与打包。
- HAR 包含本地依赖，安装该 HAR 包时可能失败。

这些警告不被描述为通过，也不由本次策略变更修复。构建仅证明当前配置下的编译、HMRouter 生成和
HAR 打包成功，不证明设备运行、Dialog 交互、兼容性、签名或发布。

## Domain Pack 校验

第一次执行 `./scripts/domain-check.sh`：注册表和 Skill 校验通过，随后因系统 Python 3.9 缺少
`tomllib` 失败。未修改校验器，也未安装依赖。

系统 pip 已包含 vendored `tomli`。在 `/private/tmp/harness-tomllib-compat/tomllib.py` 建立只用于
验证环境的标准库兼容入口后执行：

```text
PYTHONPATH=/private/tmp/harness-tomllib-compat ./scripts/domain-check.sh
```

结果：exit 0；Domain registry、Repository Skill、Project Custom Agent 校验通过；48 个 unittest
全部通过。输出中的 `xargs: grep: terminated with signal 13` 来自前置 `grep -q` 管道提前关闭，未阻止
脚本完成全部门槛，最终退出码为 0。

## Change 记录校验

全仓执行 `validate_change.py` 时发现 43 条不属于本变更的历史 change 记录问题，以及本次记录最初的
状态不一致。本次状态已修正。随后调用同一校验器的 `validate_change` 函数只评估当前 change，结果为：

```text
PASS current change record
```

历史记录未被擅自批量修改，并保留为仓库既有债务。

## 生成者边界

以上是实现与验证证据，不是 G2 最终 verdict。最终 pass、fail 或 blocked 结论由独立 Evaluator
给出。lint、compat、设备运行和 UI 交互未被本次任务显式要求，分别保持 `skipped` 或未验证状态。

## 独立 Fail 后的范围内修订

独立 Evaluator 首轮 verdict 为 `Fail`，记录见
`evaluations/end-to-end-evaluation.md`。在不修改依赖或兼容基线的原授权范围内完成两项最小修订：

1. `sample/Index.ets` 现在只导出 `SamplePageInfo` 和 `SamplePath`。
2. `rollback-sample.md` 固化 sample 修改前的完整受影响文件内容和逐文件逆操作，不再依赖未跟踪
   目录的 Git diff，也明确禁止通过删除整个 sample 回滚。

修订后再次执行 `devecocli build --modules sample --build-mode debug`，exit 0，构建成功。生成的
`sample/build/default/intermediates/loader_out/default/etsFortgz/sample/Index.d.ets` 明确包含：

```text
export { SamplePageInfo } from './src/main/ets/router/SamplePageInfo';
export { SamplePath } from './src/main/ets/router/SamplePath';
```

HMRouter plugin 1.2.0/core 1.2.4 和 generated API 17/19 versus compatible SDK 15 的独立 P1
在首轮报告中被判为 P1。Domain Owner 随后明确修订评估语义：该证据是 compatibility warning，
不是已经观察到的功能失败；它只使 API 15 运行兼容性保持未验证。本任务没有要求 API 15 运行兼容
结论，也没有授权设备运行，因此不应阻断页面、资源、注释和成功构建的验收。首轮报告保持原样，
修订后的 evaluator、rule、reference 和 Owner 决策等待新的独立评估。
