# HarmonyOS 网络请求开发策略实施任务

## 计划

- [x] 分析 Drill UGC `api/` 分层、依赖和工具实现链
- [x] 确认规则、工作流和现有 Skill 的落点
- [x] 建立 G2 变更记录和来源台账
- [x] 新增网络请求参考契约与 `HMOS-RULE-11`
- [x] 更新工作流、Skill、评估器、证据模板、能力描述和 Domain 文档
- [x] 将 Domain 和注册表升级为 4.0.0
- [x] 运行 Skill、JSON、Domain 和 change 校验
- [x] 获取独立 Evaluator 结论并完成验收记录
- [ ] 提交并推送 Domain Pack
- [ ] 同步、提交并推送 Kernel Domain pin
- [ ] 重建、验证、提交并推送 CLI bundle
- [ ] 更新本地 CLI 和受管 Runtime并核验 revision

## 验证矩阵

| 验收标准 | 验证方法 | 结果或证据 |
| --- | --- | --- |
| AC-01–AC-05 | 制品审查、链接与职责一致性检查 | passing；见 `evaluations/end-to-end-evaluation.md` |
| AC-06 | registry/manifest/README/DOMAIN 一致性 | passing；版本一致为 4.0.0 |
| AC-07 | Skill quick validation、JSON、`domain-check.sh` | passing；bundled Python 下 48 tests OK |
| AC-08 | 独立 Evaluator 记录 | Pass；无 P0/P1 |
| AC-09 | 三仓库 revision、bundle manifest 与 `harness version --json` | pending |

## 残余风险

- 静态搜索只能产生网络工具候选，不能替代受影响模块构建。
- 不同 HarmonyOS SDK 对官方网络接口的支持可能不同，必须按项目基线查证。
- 项目专属认证、错误协议、日志和重试策略仍需要项目或任务输入。
