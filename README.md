# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**2.0.1**

- [下载最新版 HongguoTV-2.0.1.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v2.0.1/HongguoTV-2.0.1.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

一、播放•【修复】自动下一集重复取流 — 自动切集改为按 mediaId 反查绝对集号，不再重新拉取当前集。•【新增】无感连播 — 双播放器交替待命，下一集提前预加载，切集不闪屏、不掉帧。•【优化】预加载链路 — 修切集逻辑时完整保留 playlist 预加载。•【新增】后台播放 — 新增 onAppBackground() / onAppForeground()，切后台行为可控。•【修复】快速切集空响应 — 连续快速切集不再出现空页面、进不去播放页。•【优化】错误恢复 — 提示改为 "Resume directly"，可原地续播。二、弹幕•【优化】弹幕渲染 — 全 SurfaceView + Choreographer 预排程，消除黑块与整块黑屏。•【修复】弹幕掉帧卡顿 — 弹幕与音频互不拖累，去掉软件画布/普通 View 方案带来的卡顿。•【新增】播放页双弹幕图标 — 放在「选集」前：一个带小勾/小叉表示开关，一个带小螺丝点击直达设置页「弹幕」栏。三、遥控器与焦点•【修复】非当前项按「下」误入 — 焦点不在当前导航项时按「下」直接吞掉。•【优化】内容未就绪焦点兜底 — 用 pendingContent 记住意图，等 contentReady 后再进入，禁用几何搜索兜底。•【优化】海报移动背景抖动 — 焦点动画统一 tween(150)，首页/剧场/排行榜移动海报不再整屏抖。•【新增】历史行焦点链 — 行 →右→继续观看 →右→移除；移除 →左→继续观看 →左→整行，完整可回退。•【修复】搜索键盘落点 — 键盘展开后自动聚焦中间键（G 键）。四、界面与排版•【优化】播放页布局重排 — 选项从右上移到左下、紧邻播放键；去掉快退/快进图标；右上角显示时钟。•【优化】进度条下移 — 控制区间距收窄，更贴近屏幕底部。•【修复】9:16 首帧 — 短剧按 9:16 比例呈现，不再缩成小窗；延时 100ms 稳定呈现。•【新增】刘海屏适配 — 设置 SHORT_EDGES，横屏画面铺进左右刘海，消除黑边。五、追剧与收藏•【优化】追剧页默认历史 — 打开追剧页默认落在「历史」，接着上次看的继续。•【优化】文案统一「收藏」 —「我的追剧」改为「我的收藏」，命名统一。•【新增】已看完角标 — 历史/收藏里看完的剧集带「已看完」标记。六、设置与数据•【新增】进度条常驻开关 —「画面」分组新增开关，开启后屏幕最底部显示一条极细进度线，低对比、不聚焦、不影响观感。•【新增】返回按钮开关 — 全局控制顶部是否显示可点击返回箭头（默认关）。•【新增】清除缓存 — 删除 cache 目录与字节码，保留观看记录和设置。•【新增】清除全部数据 — 清空偏好、缓存、脚本后重启，回到干净初始状态。•【新增】设备身份重置 — 注册信息落盘避免频繁注册触发风控，支持重置。•【优化】网络与切标签加速 — 网络延迟优化，剧场/排行榜切换标签响应更快。七、投播•【优化】投播页文案 — 改为平实提示："整段粘贴红果/抖音的分享文案，电视自动识别。个别特殊的分享链接可能暂时无法识别播放。"八、稳定性•【修复】应用图标设置闪退 — 根因是 painterResource 加载了带 <inset> 的 drawable，改用 webp + padding(d(14))。•【修复】DetailHero 返回按钮 — 补齐 showBack 参数透传。•【修复】LibraryScreen 编译依赖 — 补齐 focusRequester import。
<!-- END APP: hongguoTV -->

<!-- BEGIN APP: redguo -->
### 红果剧场

当前版本：**1.0.2**（内部版本 `2026112201`）

- [下载 32 位安装包 RedGuo-1.0.2-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.2-2026112201/RedGuo-1.0.2-v7a.apk)
- [下载 64 位安装包 RedGuo-1.0.2-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.2-2026112201/RedGuo-1.0.2-v8a.apk)
- [应用内更新清单 update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)
- [红果剧场全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/redguo)

**本次更新说明**

- 修复连续切换几集后必然卡住转圈、返回后重新点开也无法播放的问题：被取消的请求会一直占着网络限流名额不放，名额占满后所有请求排队直到超时；现在取消时立即释放名额，前台排队加了上限，排队超时也会自动重试，不再出现「一直转圈」。
- 修复切集时偶发「Unexpected runtime error」导致备用预热失效、连播不无感的问题：两路播放器统一缓冲参数，不再在切集时翻转内核内部状态。
- 取消双播放器的内存限制：是否预热只由「预开下一集」开关决定，内存紧张的设备也能无感切集。
- 精简为仅安卓版本：移除 iOS / Windows / macOS 平台代码与桌面专属功能（桌面小窗、老板键、窗口置顶、窗口全屏等），安装包只含 ARM 架构，不再提供 x86 模拟器架构与 32+64 整合包。
- 播放调试日记区分音频与视频轨道：AAC 音频走软解属正常现象，不再误读成视频掉软解。
<!-- END APP: redguo -->

## 仓库用途

AppDownload 是应用发布与下载分发仓库，不是 Android 源代码仓库。应用源码、开发过程和功能实现请以对应的源码项目为准。

### 应用目录

- `hongguoTV/`：红果 TV（HongguoTV）Android APK 发布文件与应用内更新清单。
- `redguo/`：红果剧场（RedGuo）Android APK 发布文件与应用内更新清单。

### 下载与更新

1. 普通用户可通过上方最新版 APK 链接下载安装。
2. 应用内更新功能读取固定地址的 `hongguoTV/latest.json`，获取版本信息和下载地址。
3. 历史版本及对应发布说明可在 [Releases](https://github.com/xycvip/AppDownload/releases) 页面查看。

### 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址，避免应用内更新地址频繁变化。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。

## Repository Information

- Repository: `xycvip/AppDownload`
- Project: Third-party HongguoTV Android APK downloads and updates
- Distribution: GitHub Releases and GitHub Raw
- Manifest: `hongguoTV/latest.json`

如需反馈下载或更新问题，请通过本仓库的 Issues 提交，并注明设备型号、Android 版本和遇到的问题。

<!-- HONGGUOTV_STATS_START -->
## 红果TV统计

**累计下载：2,559 次** · **最新版本：2.0.0**

| 历史版本 | 下载量 |
| --- | ---: |
| 2.0.0 | 60 |
| 1.1.50 | 287 |
| 1.1.49 | 804 |
| 1.1.48 | 45 |
| 1.1.47 | 338 |
| 1.1.46 | 234 |
| 1.1.45 | 87 |
| 1.1.44 | 9 |
| 1.1.43 | 41 |
| 1.1.42 | 4 |
| 1.1.41 | 82 |
| 1.1.40 | 5 |
| 1.1.39 | 32 |
| 1.1.38 | 48 |
| 1.1.37 | 35 |

**每日下载趋势**

![红果TV每日下载趋势](stats/downloads.svg)

**仓库访问趋势**

![仓库访问趋势](stats/traffic.svg)

<sub>仅统计红果TV正式版 APK。访问数据需配置 TRAFFIC_TOKEN；每日数据从启用统计后开始归档。</sub>
<!-- HONGGUOTV_STATS_END -->
