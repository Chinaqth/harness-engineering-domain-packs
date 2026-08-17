# 实施任务

## 计划

- [x] 建立现有初始化能力与参考 `ugc`/`ugcprovider` 的只读基线
- [x] 新增业务模块开发 Skill 与架构参考
- [x] 新增独立能力、路由和 task type，并更新版本
- [x] 更新工作流、评估器、Domain/Skill 清单和中文导览
- [x] 运行窄检查与 `./scripts/domain-check.sh`
- [x] 更新验收、进度和独立评审交接

## 验证矩阵

| 验收标准 | 验证方法 | 结果或证据 |
| --- | --- | --- |
| Skill 架构契约完整 | 人工结构核对与 `validate_skills.py` | pass；见 `validation.md` |
| 初始化和开发能力边界不重叠 | JSON 引用检查与文本负向断言 | pass；独立 ID 且初始化排除项未扩大 |
| 注册与版本一致 | `validate_registry.py`、`domain-check.sh` | pass |
| 生产清单完整 | `README-CH.md` 清单核对、`domain-check.sh` | pass |

## Evaluator 结论

- 结论：pass
- Evaluator：`/root/eval_business_skill`、`/root/eval_business_capability`、`independent-domain-artifact-evaluator-routes/workflow`
- 日期：2026-08-17
- 证据：`evaluations/` 下五项当前 digest-bound passing evaluation

## 残余风险

无已知 P0/P1。provider-only 或已有业务 HAR 缺少必需 provider 的半状态必须按 Skill 失败关闭，
不能把本次契约误解为已经提供 provider-only 初始化能力。
