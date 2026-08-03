# Harness Engineering Domain Packs

面向企业职能能力的私有事实来源，通过 Harness Engineering 路由协议向不同项目提供可复用、可治理的专业能力。

[English README](README.md)

## 项目概括

这个仓库把产品、设计、iOS、Android、Web、后端、质量、安全、运维等长期存在的企业职能，转化为可版本化、可治理的 Domain Pack。

一个 Domain Pack 定义某项职能在什么情况下适用、拥有哪些能力、提供哪些工作流和 Skill、需要哪些工具与权限，以及如何评估其产出。这样，专业实践可以独立于 Harness 底座和任何单一产品项目演进。

仓库提供注册表、Schema、模板、治理规则、验证机制和注册工作流，保证新增职能先建立稳定身份，再在自动完善和校验通过后激活。

### 这个仓库是什么

- 企业职能身份和生命周期的权威目录；
- 专业工作流、规则、Skill、工具、模板和评估器的复用来源；
- Domain Owner、Harness 底座和接入项目之间的版本化契约；
- 用户级 Domain 运行时投影的受控发布源。

### 这个仓库不是什么

- Harness Kernel 或企业全局政策仓库；
- 产品项目，不能存放项目专属架构、命令或秘密；
- 已经运行的生产 Router；
- 一组没有 Owner 的提示词；
- 因 Domain 已激活就自动获得部署、发布或生产权限的捷径。

## 底座、Domain Pack 与具体项目

企业能力被划分为三个版本化范围：

| 范围 | 事实来源 | 职责 |
| --- | --- | --- |
| Harness Kernel | `harness-engineering-workstation` | 跨职能工作流、风险、授权、路由协议、证据和治理 |
| Domain Packs | 当前仓库 | 职能身份、路由、能力、专业工作流、规则、Skill、工具和评估器 |
| 产品项目 | 各产品仓库 | 架构、命令、本地 Owner、启用的 Pack 版本、更严格约束和任务记录 |

上下文越靠近任务越具体：

```text
Harness Kernel
  -> Domain Pack
       -> 项目 Domain Overlay
            -> Task Envelope 和 Routing Plan
```

Domain Pack 和项目 Overlay 可以细化上层规则，但不能削弱 Kernel 的安全、隐私、授权、证据和审批约束。

参见 [Domain Pack 架构](docs/ARCHITECTURE.md) 和 [Domain Pack 治理](docs/GOVERNANCE.md)。

## Domain Pack 工程思想

### 1. 身份必须稳定

已发布的 Domain、Route 和 Capability ID 不允许静默修改。破坏性语义变化需要通过版本、废弃和迁移完成。

### 2. 先有所有权，再谈激活

注册只建立草稿身份和明确 Owner；完善流程补齐角色、能力与自动化证据，并在通过后自动激活。

### 3. 发现阶段保持轻量

路由先读取注册表和 Route 元数据。只有能力被选中后，才加载完整工作流、Skill、规则和评估器。

### 4. 专业知识必须可复用

Domain Pack 保存职能级实践。项目路径、命令、架构和例外留在项目 Overlay 中。

### 5. 激活由完善结果驱动

`active` Pack 必须通过 Schema，并具备有效 Route、Capability、Workflow、Evaluator、Owner、兼容性声明和可解析依赖。Reviewer 与单独激活证据不再构成生命周期卡点。

### 6. 能力缺失必须显式暴露

Agent 或未来 Router 都不能为了路由成功而虚构未注册职能或能力。

## 生命周期与运行模型

| 状态 | 含义 | 路由行为 |
| --- | --- | --- |
| `draft` | 已注册但未完成 | 对维护者可见，不能接收生产任务 |
| `active` | 已拥有并通过自动验证 | 项目启用精确兼容版本后可被选择 |
| `deprecated` | 仅用于迁移期兼容 | 只允许明确固定版本的消费者使用 |
| `retired` | 不再可用 | 保留审计和迁移历史 |

标准生命周期：

```text
出现可复用职能需求
  -> 注册稳定身份和 Owner
  -> 完成 Route 和 Capability
  -> 增加 Workflow、Skill、Tool 和 Evaluator
  -> 记录兼容性与自动评估证据
  -> 运行确定性验证
  -> 自动激活
  -> 获得单独授权后发布
  -> 持续观察、版本升级、废弃或退役
```

成功注册后的初始状态始终是 `draft`；自动完善通过后，在同一流程中变为 `active`。

## 目录和文件职责

### 入口、架构与治理

| 路径 | 职责 | 何时读取或更新 |
| --- | --- | --- |
| `README.md` | 英文项目概览和操作指南 | 贡献者首次进入仓库 |
| `README-CH.md` | 中文项目概览和操作指南 | 中文贡献者首次进入仓库 |
| `AGENTS.md` | 强制规则和任务路由入口 | Agent 开始 Domain 工作 |
| `docs/ARCHITECTURE.md` | 分层边界、Pack 契约、路由和发布方式 | 修改结构或集成方式 |
| `docs/GOVERNANCE.md` | 所有权、生命周期、激活、版本和注册表评审 | 注册、激活或修改 Pack |
| `changes/README.md` | Domain 仓库的变更记录要求 | 规划重要仓库变更 |

### 注册表、Schema 与 Domain 内容

| 路径 | 职责 |
| --- | --- |
| `registry/domains.json` | Domain 身份、版本、状态、Owner 和路径的排序权威目录 |
| `schemas/domain-pack.schema.json` | Domain 身份、适用性、兼容性、生命周期和激活契约 |
| `schemas/route.schema.json` | 任务类型、信号、优先级和能力引用契约 |
| `schemas/capability.schema.json` | Workflow、Skill、Tool、Evaluator、权限和依赖契约 |
| `schemas/owners.schema.json` | 主 Owner 和 Reviewer 契约 |
| `schemas/registry.schema.json` | 注册表条目契约 |
| `domains/_template/` | 标准草稿 Pack 骨架 |
| `domains/<domain-path>/` | 一个已注册专业职能的版本化源码 |

### 注册、验证与交付

| 路径 | 职责 |
| --- | --- |
| `.agents/skills/register-domain-pack/` | 引导式、可回滚的新 Domain 草稿注册 |
| `.agents/skills/complete-domain-pack/` | 仅根据 Domain ID 自动研究、生成、评分和完善内容 |
| `.codex/agents/` | 项目级 Builder、Researcher、Author 和独立 Evaluator 角色 |
| `scripts/validate_registry.py` | Schema、生命周期、引用、身份、所有权和依赖验证 |
| `scripts/domain-check.sh` | 完整仓库检查 |
| `tests/test_registration.py` | 注册编码、幂等、暂存和回滚行为 |
| `tests/test_registry_validation.py` | 注册表、Schema、生命周期、证据和依赖拒绝路径 |
| `.github/workflows/domain-check.yml` | 在推送和 Pull Request 中运行完整检查 |
| `.github/pull_request_template.md` | 要求所有权、生命周期、兼容性、证据和回滚信息 |

## Domain Pack 文件契约

每个职能使用统一结构：

```text
domains/<domain-path>/
├── DOMAIN.md
├── README-CH.md
├── domain.json
├── routes.json
├── capabilities.json
├── owners.json
├── rules/
├── workflows/
├── evaluators/
├── templates/
└── skills/
```

| 文件或目录 | 职责 |
| --- | --- |
| `DOMAIN.md` | 人类可读的目标、边界、输入、输出和成熟度 |
| `README-CH.md` | 中文目录导览，逐项说明每个生产文件和目录的作用及实际行为 |
| `domain.json` | 稳定身份、版本、生命周期、Owner、适用性、兼容性和激活证据 |
| `routes.json` | 任务类型、仓库信号、优先级和候选能力 |
| `capabilities.json` | Workflow、Skill、Tool、Evaluator、权限和依赖 |
| `owners.json` | 主 Owner 和可选 Reviewer |
| `rules/` | 细化但不能削弱 Kernel 的专业规则 |
| `workflows/` | 可重复的专业交付流程 |
| `evaluators/` | Domain 专属验收与证据契约 |
| `templates/` | 可复用的职能制品 |
| `skills/` | Domain 自有 Skill 源码 |

## 快速开始

### 1. 阅读入口规则

阅读 [AGENTS.md](AGENTS.md)、[架构](docs/ARCHITECTURE.md) 和 [治理](docs/GOVERNANCE.md)。

### 2. 注册一个草稿职能

调用仓库 Skill：

```text
使用 $register-domain-pack 注册 iOS Engineering 职能。
```

或者先预览确定性注册脚本：

```bash
python3 .agents/skills/register-domain-pack/scripts/register_domain_pack.py \
  --root . \
  --id engineering.ios \
  --display-name "iOS Engineering" \
  --owner "ios-platform-team" \
  --description "Owns reusable iOS application delivery and evaluation." \
  --dry-run
```

确认身份和 Owner 后再移除 `--dry-run`。注册只创建符合 Schema 的 `draft`；完善流程负责生成专业内容并在校验通过后自动启用路由。

### 3. 完成 Pack

当使用者知道注册职能、但不了解其专业内容时，委托自动完善流程：

```text
启动 domain_pack_builder sub-agent，并使用 $complete-domain-pack
根据 engineering.android 的注册身份自动完善内容并激活。
```

请在权威 Domain Packs 源码仓库中运行这条内容生产流程。它的 Custom Agent 位于项目级
`.codex/agents/`，不会由 Harness CLI 投射成产品仓库中的运行时职能。

Domain ID 是唯一必需输入。只读 Researcher 会查找当前权威公开资料并记录组织特定缺口，
随后由相互分离的 Author、Artifact Evaluator 和 Pack Evaluator 生成并评估全部生产制品。
每个制品必须获得大于 90 分且绑定来源的当前独立评估，通过全部硬门禁，并且不存在 P0
或 P1 问题。

配套 Skill 包括：

- `$author-domain-artifact`：生成一个明确声明的制品；
- `$evaluate-domain-artifact`：生成与内容摘要绑定的独立评估；
- `$evaluate-domain-pack`：完成最终内容与激活就绪评估。

结果必须达到 `content_state=content-complete` 和 `state=activation-ready`，随后自动把
Registry 与 Manifest 同步为 `active`。内部 Reviewer、权限和未公开项目政策是下游任务
输入，不阻塞 Domain 生命周期，但依赖这些输入的任务操作和声明仍须 fail-closed。

### 4. 验证

```bash
./scripts/domain-check.sh
```

### 5. 发布或采用

完善流程已经把注册表和 Manifest 同步为 `active`。获得仓库适用的 Git 发布授权后发布不可变版本，再由项目 Overlay 启用。

## 多场景用例流程

### 场景 A：注册一个新部门或专业职能

| 阶段 | 工作流如何运行 | 涉及文件 |
| --- | --- | --- |
| 确认需要 | 判断职能是否长期存在且可跨项目复用 | `docs/ARCHITECTURE.md`、Owner 信息 |
| 选择身份 | 确定稳定点分 ID、显示名称、Owner 和长期职责 | 注册契约和注册表搜索 |
| 注册 | 原子地暂存标准 Pack 和注册表条目 | `$register-domain-pack`、模板、注册表 |
| 验证草稿 | 检查 Schema、结构、所有权和回滚行为 | `scripts/domain-check.sh` |
| 交接 | Domain Owner 接收可见但不可路由的草稿 | `DOMAIN.md`、`domain.json`、`owners.json` |

### 场景 B：为已有 Domain 增加能力

| 阶段 | 工作流如何运行 | 涉及文件 |
| --- | --- | --- |
| 定义专业结果 | 明确输入、输出、支持的任务类型和证据 | `DOMAIN.md`、变更记录 |
| 建模路由 | 增加 Route 信号与能力引用，不扩大无关范围 | `routes.json`、`capabilities.json` |
| 增加执行内容 | 提供 Workflow、Skill、Tool、Template 和权限 | 对应目录与能力文件 |
| 增加评估 | 定义合格评估者如何证明结果 | `evaluators/`、`capabilities.json` |
| 验证和版本化 | 解析依赖并选择正确语义版本影响 | Schema、治理、完整检查 |

### 场景 C：修改一个 active Workflow

| 阶段 | 工作流如何运行 | 涉及文件 |
| --- | --- | --- |
| 评估兼容性 | 判断行为、输入、输出、权限或证据是否变化 | 治理文档、当前 Manifest |
| 保存意图 | 记录原因、迁移需要和回滚方式 | 变更记录和决策证据 |
| 修改受控内容 | 只更新受影响的 Workflow、Skill、Rule 或 Evaluator | 被选中的 Domain 文件 |
| 重新评估 | 运行检查并复现代表性 Domain 旅程 | 测试、评估契约、激活证据 |
| 发布 | 更新正确版本并保持注册表和 Manifest 一致 | `domain.json`、注册表 |

### 场景 D：废弃或退役能力

| 阶段 | 工作流如何运行 | 涉及文件 |
| --- | --- | --- |
| 查找消费者 | 找到固定版本项目和依赖能力 | 注册表、依赖引用、项目 Overlay |
| 定义迁移 | 指明替代能力，或解释为什么没有替代 | Domain 文档和变更记录 |
| 修改生命周期 | 需要迁移窗口时先废弃，再退役 | 注册表和 Manifest |
| 验证安全性 | 确保 active Route 不再选择不可用能力 | Route、Capability、测试 |
| 保留证据 | 保存审计和恢复历史 | Git 历史和长期变更记录 |

### 场景 E：产品项目接入 Domain

| 阶段 | 工作流如何运行 | 事实来源 |
| --- | --- | --- |
| 发布 | Domain Owner 发布不可变 active Pack | 当前仓库 |
| 启用 | 产品 Owner 固定获批版本和本地 Owner | 产品 `.harness/domains.json` |
| 细化 | 项目增加路径、命令、信号、禁用能力和更严格约束 | 项目 Overlay |
| 路由 | Harness 合并 Task Envelope、注册表版本和 Overlay | Harness CLI 或未来 Router |
| 执行和评估 | 只加载被选中内容，保持项目与 Domain 证据可追踪 | Routing Plan、Pack Workflow、项目测试 |

## 项目验证

运行完整检查：

```bash
./scripts/domain-check.sh
```

检查覆盖：

- 英文优先的仓库语言策略；
- 可疑凭据文件名；
- JSON Schema；
- 注册表排序、身份、目录、Owner、版本和生命周期一致性；
- Route、Capability 唯一性和引用；
- Workflow、Skill、Evaluator、Template 和依赖是否存在；
- active Pack 的所有权、兼容性、Evaluator、Route、Capability 与引用完整性；
- 注册编码、暂存、幂等和回滚行为。

## 当前状态与下一步

仓库底座已经完成，验证套件通过。当前没有已注册或 active 的业务 Domain。

下一项生产里程碑建议注册一个有明确 Owner 的草稿——`engineering.ios`——自动补齐专业内容并激活，发布不可变版本，再在一个试点项目 Overlay 中启用。
