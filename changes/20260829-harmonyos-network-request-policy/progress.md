# HarmonyOS 网络请求开发策略进度与交接

- Change ID: `20260829-harmonyos-network-request-policy`
- Updated: 2026-08-29
- Current phase: done
- Last verified revision: Domain `f3d9901`；Kernel `c28afb8`；CLI `0913db1`
- Environment: macOS，Domain、Kernel、CLI 本地工作区

## 当前状态

已完成 Drill UGC 网络分层与依赖链分析及 Domain 4.0.0 生产制品修改。Owner 已批准按规则、工作
流、Skill 和评估闭环实施，并授权三个仓库的提交推送及本地 CLI/Runtime 更新。确定性 Domain 与
Skill 校验通过；独立 Evaluator 结论为 Pass，未发现 P0/P1。Domain、Kernel pin、CLI bundle 与本地
Runtime 已完成首轮同步，AC-09 通过。

## 已完成

- 确认 UGC 通过本地 `common_app` 包导出 `httpCall`，再选择 HarmonyOS RCP 实现。
- 确认样例中的 endpoint、repository、service、transport 抽象可复用。
- 识别样例中 pending Promise、错误折叠、UI/Router 耦合和敏感日志风险。
- 确认新增规则属于 breaking Domain policy，目标版本为 4.0.0。
- 新增网络请求参考契约、`HMOS-RULE-11`、`HMOS-EVAL-13`，并更新工作流、两个执行 Skill、
  架构参考、证据模板、能力描述、Domain 文档、注册表与中文清单。
- `git diff --check`、JSON、Skill quick validation、Domain 全量校验和当前 G2 change 校验通过。
- 独立 Evaluator 完成关键旅程审查，AC-01–AC-08 satisfied；系统 Python 3.9 缺少 `tomllib` 记为
  非阻断 P2，完整校验使用 bundled Python 3.12。
- Domain `f3d9901`、Kernel `c28afb8`、CLI `0913db1` 已推送至各自 `origin/main`。
- 本地 CLI 版本为 `0.2.4`；Runtime bundle 为 `0.2.4+c28afb8.f3d9901`，并发布 51 个受管 Skill
  projection 到 Codex 与 Kimi。

## 待办

- 无。发布证据提交后再执行一次最终 pin、bundle 与 Runtime 同步，使最终 Domain revision 被消费。

## 阻塞项

- 当前无阻塞项。
