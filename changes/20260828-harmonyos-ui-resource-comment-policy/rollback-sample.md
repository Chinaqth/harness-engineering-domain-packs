# CatchElf sample 可恢复基线与回滚步骤

## 目的与边界

CatchElf 的 `sample/` 在本次任务开始时是未跟踪目录，Git 无法提供修改前 diff。本文固化本次实际
修改的原始内容和准确逆操作，使回滚不依赖删除整个 sample，也不会覆盖 `build-profile.json5` 或
其他用户文件。原始内容来自 2026-08-28 修改前的只读检查记录。

## 本次实际修改面

1. 修改 `sample/src/main/ets/pages/SamplePage.ets`。
2. 将原 `sample/src/main/ets/pages/SampleDialog.ets` 改为
   `sample/src/main/ets/dialogs/SampleDialog.ets` 并修改内容。
3. 仅为 `SamplePageInfo.ets` 和 `SamplePath.ets` 增加中文职责注释。
4. 修改 `sample/src/main/resources/base/element/string.json`。
5. 新增 `sample/src/main/resources/base/element/color.json`。
6. 修改原本为空文件的 `sample/Index.ets`，导出最小路由公共契约。
7. `float.json`、模块 manifest、包依赖、构建配置和测试文件未由实现阶段修改。

## 准确回滚步骤

回滚需由获授权的项目 Owner 逐项执行并在执行后重新构建；不要删除整个 `sample/`。

1. 将 `sample/src/main/ets/pages/SamplePage.ets` 恢复为下方“原始 SamplePage”。
2. 删除本次新增的 `sample/src/main/ets/dialogs/SampleDialog.ets`，并在
   `sample/src/main/ets/pages/SampleDialog.ets` 写入下方“原始 SampleDialog”。
3. 将 `SamplePageInfo.ets`、`SamplePath.ets`、`string.json` 恢复为下方对应原始内容。
4. 删除本次新增的 `sample/src/main/resources/base/element/color.json`。
5. 将 `sample/Index.ets` 恢复为空文件。
6. 确认 `float.json` 仍保持下方记录的原始内容，并执行项目批准的 sample 构建。

## 原始 SamplePage

路径：`sample/src/main/ets/pages/SamplePage.ets`

```ets
import { HMRouter } from '@hadss/hmrouter';
import { matchSize } from 'common_app';
import { SamplePath } from '../router/SamplePath';

@HMRouter({pageUrl: SamplePath.SamplePage})
@ComponentV2
export struct SamplePage {
  build() {
    Column() {
      Text('SamplePage')
    }
    .size(matchSize)
  }
}
```

## 原始 SampleDialog

路径：`sample/src/main/ets/pages/SampleDialog.ets`

```ets
import { HMRouter } from '@hadss/hmrouter';
import { matchSize } from 'common_app';
import { SamplePath } from '../router/SamplePath';

@HMRouter({ pageUrl: SamplePath.SampleDialog, dialog: true })
@ComponentV2
export struct SampleDialog {
  build() {
    Column() {
      Text('SampleDialog')
    }
    .size(matchSize)
  }
}
```

## 原始 SamplePageInfo

路径：`sample/src/main/ets/router/SamplePageInfo.ets`

```ets
import { PageInfo } from '@life/zyc_core/src/main/ets/router/params/PageInfo';
import { SamplePath } from './SamplePath';

export namespace SamplePageInfo {
  export const SamplePage: PageInfo = new PageInfo(SamplePath.SamplePage)

  export const SampleDialog: PageInfo = new PageInfo(SamplePath.SampleDialog)
}
```

## 原始 SamplePath

路径：`sample/src/main/ets/router/SamplePath.ets`

```ets
export class SamplePath {
  static readonly SamplePage: string = 'page://SamplePage'
  static readonly SampleDialog: string = 'dialog://SampleDialog'
}
```

## 原始 string.json

路径：`sample/src/main/resources/base/element/string.json`

```json
{
  "string": [
    {
      "name": "page_show",
      "value": "page from package"
    }
  ]
}
```

## 原始 float.json（实现阶段未修改）

路径：`sample/src/main/resources/base/element/float.json`

```json
{
  "float": [
    {
      "name": "page_text_font_size",
      "value": "50fp"
    }
  ]
}
```

## 恢复验证

恢复后至少检查：Dialog 仅存在于原 `pages/` 路径；`color.json` 不存在；`Index.ets` 为空；上述
原始文件逐字一致；`devecocli build --modules sample --build-mode debug` 的实际结果被记录。回滚只
恢复本次修改，不处理或掩盖 HMRouter 版本、compatible SDK 或其他既有构建警告。
