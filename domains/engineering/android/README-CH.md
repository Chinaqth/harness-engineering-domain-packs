# Android Engineering Domain 目录说明

本文件帮助中文使用者理解 `engineering.android` Domain Pack 中各文件和目录的职责。英文生产制品是权威契约；本文件只做中文导览，不新增规则、权限或组织政策。当前 Domain 仍为 `draft`，其中部分文件是等待自主补全流程完善的骨架。

## 顶层文件

| 路径 | 作用 | 会做什么事情 |
| --- | --- | --- |
| `DOMAIN.md` | 描述 Android Engineering 的目标、边界、输入、输出、Owner 和成熟度。 | 帮助维护者判断该 Domain 的职责与交接边界；当前内容仍提示需要完成激活工作。 |
| `domain.json` | 保存 `engineering.android` 的身份、版本、生命周期、适用性、兼容性和激活证据。 | 供注册表校验；当前状态为 `draft`，不会参与生产路由。 |
| `routes.json` | 保存任务选择条件与候选 Capability。 | 完成后供未来的路由解析器判断 Android 任务是否应选择本 Domain；当前列表为空。 |
| `capabilities.json` | 组装 Android Workflow、Skill、Tool、Evaluator、权限和依赖。 | 完成后描述 Android 能力的执行与验证依赖；当前列表为空。 |
| `owners.json` | 记录主 Owner 与 Reviewer。 | 指定 `platform-android` 负责专业正确性；Reviewer 尚待组织确认。 |
| `README-CH.md` | 提供当前目录的中文导览。 | 解释实际文件和目录，不替代英文权威契约。 |

## 子目录

| 路径 | 作用 | 会做什么事情 |
| --- | --- | --- |
| `rules/`、`rules/BASE.md` | Android 专业规则目录及当前骨架。 | 完成后约束 Android 工作，同时保持 Kernel 规则优先。 |
| `workflows/`、`workflows/WORKFLOW.md` | Android 工作流目录及当前骨架。 | 完成后定义可重复的 Android 交付步骤、输出、检查与失败处理。 |
| `evaluators/`、`evaluators/EVALUATOR.md` | Android验收契约目录及当前骨架。 | 完成后规定结果证据、负向路径和通过标准。 |
| `skills/` | Android 自有 Skill 目录。 | 完成后保存执行 Android 工作流所需的指导与确定性工具；当前没有生产 Skill。 |
| `templates/` | Android 可复用模板目录。 | 完成后保存标准化的 Android 专业制品结构；当前没有生产模板。 |

## 后续更新

运行 `$complete-domain-pack` 后，必须根据最终实际文件重新生成本说明，逐项解释新增的规则、工作流、Evaluator、Skill 和模板。
