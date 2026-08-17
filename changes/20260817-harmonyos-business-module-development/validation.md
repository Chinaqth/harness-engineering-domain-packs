# 验证记录

## 2026-08-17 确定性检查

运行环境使用 Codex bundled Python，因为系统 `/usr/bin/python3` 为 3.9.6，缺少
`validate_agents.py` 所需的标准库 `tomllib`。

```text
python3 -m json.tool domain.json/capabilities.json/routes.json/registry/domains.json: pass
python3 scripts/validate_skills.py .: pass
python3 scripts/validate_registry.py .: pass
./scripts/domain-check.sh: exit 0
Project Custom Agent validation passed.
Ran 48 tests: OK
```

编排边界复核确认 `hmos-business-module-development` 为该 task type 的主编排 Skill；Skill、
workflow、capability、evaluator、英文清单与中文导览均明确 ArkUI、ArkTS、Stage/package、初始化
和验证为受约束子能力，冲突必须回到架构决策而不能静默覆盖。

全量命令：

```bash
env PATH=/Users/albertq/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin:/usr/bin:/bin:/usr/sbin:/sbin ./scripts/domain-check.sh
```

脚本的英文优先检查管道打印了 `xargs: grep: terminated with signal 13`，这是 `grep -q`
提前关闭消费端时的现有 SIGPIPE 提示；脚本继续执行所有 Python 校验与测试并以 0 退出。

## Change 记录检查

Kernel `validate_change.py` 对整个仓库运行时报告历史 change 记录的既有格式问题；本变更最初
暴露的 `change_id` 和状态同步问题已经修复。由于验证器只支持仓库级扫描，历史问题仍会使
仓库级 change 检查失败，不能将其报告为本变更通过。

## 尚缺证据

无。独立 evaluator 已评审 Skill、capability、route、workflow 与 evaluator artifact。第一轮
Skill P2、capability P1 和 workflow P2 均保留在 iteration-1 记录中；修复后的当前 digest-bound
记录全部通过，且 evaluator 已回读确认标准化 verdict 与原始载荷一致。

| Artifact | Current score | Verdict |
| --- | ---: | --- |
| `skills/hmos-business-module-development/SKILL.md` | 97.35 | pass |
| `capabilities.json` | 96.90 | pass |
| `routes.json` | 98.25 | pass |
| `workflows/WORKFLOW.md` | 98.25 | pass |
| `evaluators/EVALUATOR.md` | 97.55 | pass |
