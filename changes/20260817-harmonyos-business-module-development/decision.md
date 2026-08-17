# 决策记录

- Status: accepted-for-implementation
- Date: 2026-08-17
- Decision owners: `platform-harmony`（专业评审待确认）

## 背景

现有 `hmos-init-business-module` 只创建业务/空 provider 骨架。用户新增的是初始化之后的完整、
可重复开发流程，包含架构和交付判断，不能仅作为检索知识点。

## 备选方案

1. 只扩充知识文档：无法稳定触发执行流程，也缺少输入、步骤、失败关闭和验证契约。
2. 扩大初始化 Skill：会破坏其已发布的窄边界和事务脚本安全模型。
3. 新增开发 Skill、能力和路由，并引用独立架构规则：职责清晰且兼容。

## 决策

采用方案 3。新 task type 为 `harmonyos-business-module-development`，新能力和 Skill 使用同义
稳定 ID。初始化能力保持不变；完整开发 Skill 是本 task type 的主编排入口，可组合初始化、
ArkTS、ArkUI、Stage/package 和验证能力，但这些子能力不得自行覆盖已接受的跨层架构。

## 后果

HarmonyOS Pack 进行向后兼容的 minor 版本升级；新增 Skill 需要同步 workflow、evaluator、
capability、route、manifest、registry 与 README-CH 清单。

## 重新审视条件

当组织放弃 provider 唯一桥梁、MVVM 或目录契约，或需要把工厂/注册机制绑定到具体框架时重新审视。
