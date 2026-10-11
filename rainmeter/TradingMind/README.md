# TradingMind — 交易心理盘前提示（Rainmeter 皮肤）

每 15 秒轮播一条交易心理戒律，内容提炼自亚历山大·埃尔德
《以交易为生》第 1–2 章、《以交易为生 II》第 2 章读书笔记。

## 安装

把整个 `TradingMind` 文件夹复制到：

```
%USERPROFILE%\Documents\Rainmeter\Skins\
```

然后在 Rainmeter 管理器中加载 `TradingMind.ini`。

## 操作

- 单击卡片 / 滚轮向下：下一条
- 滚轮向上：上一条
- 鼠标中键 / 底部「暂停」按钮：暂停或继续轮播
- 底部进度条显示距下一条的剩余时间

## 自定义

- 轮播间隔：编辑 `TradingMind.ini` 中 `[Variables]` 的 `RotateSeconds`（秒）
- 增删提示：编辑 `@Resources\Scripts\tips.lua` 顶部的 `tips` 列表，每条为 `{标题, 正文}`
- 配色：`[Variables]` 中的 `BgColor` / `AccentColor` 等（RGBA）

## 编码（重要）

`TradingMind.ini` 和 `tips.lua` 都必须保存为 **UTF-16 LE 带 BOM**
（Windows 记事本“另存为”里的“Unicode”），否则 Lua 中的中文会显示为乱码。
用 VS Code 编辑时，点击右下角编码切到 `UTF-16 LE` 再保存。
