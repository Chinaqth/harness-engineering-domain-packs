# HarmonyOS 页面、资源与中文注释策略实施任务

## 计划

- [x] 建立 Domain 与 CatchElf sample 当前行为基线
- [x] 登记 Owner 要求、项目样例、HMRouter 和 ArkUI V2 来源
- [x] 修正 CatchElf sample 的 Dialog 目录、资源引用和中文注释
- [x] 新增 UI 页面/Dialog/路由/资源/注释参考契约
- [x] 更新 Domain 规则、工作流、Skill、评估器和证据模板
- [x] 同步 Domain 3.0.0 版本、注册表、DOMAIN.md 与 README-CH.md
- [x] 运行 sample 构建、Domain 校验和变更记录校验
- [x] 获取独立 Evaluator 结论并更新最终记录

## 验证矩阵

| 验收标准 | 验证方法 | 结果或证据 |
| --- | --- | --- |
| AC-01–AC-04 | 文件审查、引用解析和 Domain 校验 | pending |
| AC-05 | `rg` 扫描 sample 与文件结构审查 | pending |
| AC-06 | registry/manifest 一致性和 `scripts/domain-check.sh` | pending |
| AC-07 | `devecocli build` 的原始结果 | pending |
| AC-08 | 独立 Evaluator 记录 | pending |

## Evaluator 结论

- 结论：Pass（首轮 Fail 作为旧语义历史证据保留）
- Evaluator：独立 Evaluator（未参与实现）
- 日期：2026-08-28
- 证据：`evaluations/end-to-end-evaluation.md`（首轮历史结论）；`evaluations/end-to-end-reevaluation.md`（当前最终结论）

## 残余风险

- 静态扫描不能判断每个字符串是否确为用户可见内容，仍需人工语义审查。
- 中文注释质量不能由“存在注释”完全证明，评估器必须检查其是否说明职责、原因或副作用。
- HMRouter 行为对具体依赖版本敏感；项目必须以锁定版本和实际构建证据为准。
- 当前 plugin 1.2.0/core 1.2.4 且生成 API 17/19 高于 compatible SDK 15，按 Owner 修订作为
  compatibility warning 保留；API 15 运行兼容性未验证。
