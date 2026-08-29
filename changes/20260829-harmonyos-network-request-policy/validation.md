# 生成者验证记录

## 范围

- Domain Pack：`engineering.harmonyos@4.0.0`
- 参考证据：Drill UGC `api/` 与 `common_app` 网络层（只读）
- 日期：2026-08-29（Asia/Shanghai）
- 权限：Domain/Kernel/CLI 本地编辑、确定性校验、提交推送和本地 CLI/Runtime 更新；不修改参考项目、不访问设备或真实服务。

## 静态与 JSON 检查

执行：

```text
git diff --check
python3 -m json.tool domains/engineering/harmonyos/domain.json
python3 -m json.tool domains/engineering/harmonyos/capabilities.json
python3 -m json.tool registry/domains.json
python3 -m json.tool changes/20260829-harmonyos-network-request-policy/acceptance.json
python3 -m json.tool changes/20260829-harmonyos-network-request-policy/research/sources.json
```

结果：全部通过。生产制品保持英文，`changes/**` 人类可读记录按 Kernel 约定使用中文。

## Skill 校验

系统 Python 和工作区 Python 最初都因缺少 `yaml` 模块无法启动 `skill-creator` 的
`quick_validate.py`，该结果记录为验证环境缺失，不是 Skill 内容失败。随后仅在
`/private/tmp/harness-skill-validate-pyyaml` 安装临时 PyYAML，并执行：

```text
PYTHONPATH=/private/tmp/harness-skill-validate-pyyaml \
  <workspace-python> \
  /Users/albertq/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  domains/engineering/harmonyos/skills/hmos-business-module-development
```

结果：exit 0，`Skill is valid!`。临时依赖不属于仓库或运行时交付内容。

## Domain Pack 校验

系统 Python 3.9 缺少 `tomllib`，因此使用工作区 Python 3.12 置于 `PATH` 前部运行：

```text
PATH=<workspace-python-bin>:$PATH ./scripts/domain-check.sh
```

结果：exit 0；Domain registry、Repository Skill、Project Custom Agent 校验通过，48 个 unittest
全部通过。输出中的 `xargs: grep: terminated with signal 13` 来自前置 `grep -q` 管道提前关闭，
未阻止后续门槛或最终成功退出。

## 当前 change 校验

调用 Kernel `scripts/validate_change.py` 的同一 `validate_change` 函数，仅验证当前 Domain change：

```text
PASS current change record
```

全仓历史 change 状态未被修改。

## 证据边界

- 本轮没有修改或构建 Drill 项目；Drill 只提供结构与失败模式证据。
- 没有实现一个具体产品网络请求，因此没有运行真实成功、业务失败、离线、超时、取消或重叠请求场景。
- Domain 校验和 Skill 校验只证明规范制品结构与仓库确定性门槛，不证明任何产品网络实现。
- 最终 G2 verdict 由独立 Evaluator 给出。

## 独立评估

独立 Evaluator 结论为 Pass，未发现 P0/P1；AC-01–AC-08 satisfied。完整记录见
`evaluations/end-to-end-evaluation.md`。系统 Python 3.9 缺少 `tomllib` 的限制保留为非阻断 P2，不能用
裸系统 Python 的失败替代 bundled Python 3.12 的完整通过证据。

## 发布同步证据

- Domain：`f3d99019d16b681ae3dbc24f948e78508345e311`，已推送 `origin/main`。
- Kernel：`c28afb82b9e4381e2224c9633faac2f7c360061d`，pin 指向上述 Domain revision，完整校验 65 tests
  通过、2 个可选跨仓检查 skipped，已推送 `origin/main`。
- CLI：`0913db122a495563bdf2a2fee6e143a5f5316424`，验证 870 个 Runtime 文件，21 tests 通过，已推送
  `origin/main`。
- 本地：CLI `0.2.4`；`harness update` 发布 51 个受管 Skill projection；`harness version --json`
  报告 bundle `0.2.4+c28afb8.f3d9901`、Kernel `c28afb8`、Domain `f3d9901`。
- 首次 CLI bundle 构建使用系统 Python 3.9 时因缺少 `tomllib` 失败；使用已验证的 bundled Python
  3.12 重跑后全部通过，没有忽略或覆盖失败。
