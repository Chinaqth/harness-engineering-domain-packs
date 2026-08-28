# HarmonyOS 页面、资源与中文注释策略变更需求

- ID: `20260828-harmonyos-ui-resource-comment-policy`
- Owner: `platform-harmony`（用户以 Domain Owner 身份明确批准本次约定）
- Risk: G2
- Status: done
- Review-By: 2026-09-11

## 问题

现有 HarmonyOS Domain 已规定页面、弹窗、组件的职责分类和 MVVM 边界，但没有把 HMRouter
页面/弹窗声明、资源化和中文逻辑注释串成一条可执行、可评估的交付流程。CatchElf 新增的
`sample` HAR 展示了基础路由结构，但仍存在弹窗位于 `pages/`、用户可见字符串未使用资源、
缺少 `color.json` 和中文职责注释等问题，不能未经治理直接成为规范样例。

## 目标

1. 建立页面、Dialog 页面、组件、路由路径和页面信息的结构契约。
2. 禁止新增用户可见字符串、颜色和可复用 UI 度量值魔法字面量，并使用
   `src/main/resources/base/element/` 下的 `string.json`、`color.json` 和 `float.json`。
3. 要求新增或实质修改的类、组件、ViewModel、公共方法和复杂业务方法包含有意义的中文注释。
4. 把上述要求落实到 Domain 规则、工作流、执行 Skill、评估器和交付证据，而非只写成建议。
5. 修正 CatchElf `sample`，使其成为与新契约一致的可构建参考实现。

## 非目标

- 不把 HMRouter 宣称为 HarmonyOS 平台标准，也不固定所有项目必须采用该第三方框架。
- 不规定具体产品视觉品牌、颜色值、文案或路由名称。
- 不强制把协议标识、日志模板、正则、枚举判别值等非 UI 字符串写入 `string.json`；此类值使用具名 ArkTS 常量。
- 不要求逐行注释、翻译既有未修改代码或为显而易见的访问器制造无信息注释。
- 不修改 CatchElf 中除 `sample` 参考模块外的用户变更。

## 约束与事实来源

- `OWNER-UI-RESOURCE-COMMENT-CONTRACT`：用户明确批准的 Domain Owner 约定。
- `PROJECT-CATCHELF-SAMPLE`：CatchElf `sample` HAR 的本地项目事实，仅作为项目参考证据。
- `HMROUTER-UPSTREAM`：OpenHarmony SIG `ohrouter` 仓库及本地安装的 `@hadss/hmrouter@1.2.4` README；支持普通页面、Dialog 页面、字符串常量 `pageUrl` 和 HAR/HSP/HAP。
- `HMOS-ARKUI-V2`：既有 HarmonyOS Domain 研究台账中的 ArkUI V2 主来源。
- 新增规则不得削弱 Kernel 的权限、证据、独立评估或失败关闭约束。

## 验收标准

- [x] AC-01：存在可复用的页面/Dialog/路由/资源/中文注释参考契约，并明确 HMRouter 与项目样例的权威边界。
- [x] AC-02：Domain 硬规则对 UI 分类、资源化、非 UI 常量和中文注释给出适用范围、证据及失败处理。
- [x] AC-03：工作流和执行 Skill 包含实现前、实现中、构建前检查点，且构建成功不能替代结构与资源审查。
- [x] AC-04：独立评估器包含可重复的资源扫描、目录/路由检查、注释检查和负向路径。
- [x] AC-05：CatchElf `sample` 使用 `dialogs/`、资源引用和中文职责注释，不新增 UI 魔法字面量。
- [x] AC-06：版本和注册表保持同步，提供重大版本迁移说明，Domain 校验通过。
- [x] AC-07：CatchElf 的授权 sample 构建通过，或保留准确的不可用/失败证据。
- [x] AC-08：独立 Evaluator 对 G2 变更给出 pass、fail 或 blocked 结论。

## 风险、权限与数据影响

这是已激活 Domain 的强制策略变更，会使先前可接受的硬编码 UI 和无中文职责注释在新版本下失败，
因此按 breaking policy 处理并计划将 `engineering.harmonyos` 从 2.2.0 升级到 3.0.0。变更只写入
Domain Pack 和 CatchElf `sample`；不安装依赖、不访问设备、签名材料、账号或生产数据，不发布或部署。

## 自主权预算

- 范围：HarmonyOS Domain 生产制品、注册表、单一 G2 change 记录，以及 CatchElf `sample`。
- 工具与权限：只读上游资料；授权的本地文件编辑、Domain 校验和 `devecocli build`。
- 外部副作用：无。
- 成本：不新增依赖，不产生付费外部操作。
- 检查点间隔：每个制品组完成后检查 diff；最终校验前再次检查范围。
- 必要证据：来源台账、变更清单、资源/目录扫描、构建输出、Domain 校验和独立评估。
- 升级条件：需要改变路由框架、公共 API、依赖、其他业务模块或发布流程时停止并重新审批范围。

## 回滚方案

以本 change 的逐文件 diff 为最小恢复依据：回退 Domain 3.0.0 相关规则、工作流、评估器、Skill、
参考和注册表同步修改；CatchElf 中将 Dialog 文件恢复到原位置并恢复 sample 原资源引用。不得使用
破坏性工作区重置，也不得覆盖 `build-profile.json5` 等既有用户修改。
