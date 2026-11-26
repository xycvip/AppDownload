# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**2.1.0**

- [下载最新版 HongguoTV-2.1.0.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v2.1.0/HongguoTV-2.1.0.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

【播放体验】
- 修复单播放器切集同步与弹幕生命周期
【页面与操作】
- 精简首页大海报设置说明
- 简化弹幕帧率设置说明
- 修复首页导航下移导致 被滚出屏幕
- 修复 焦点相关导入
- 修复首页 遥控器两层焦点导航 (#24)
【网络与稳定性】
- 修复首页 与热门片单内容重复
- 修复首页 获焦后被滚出屏幕
- 修复桌面图标入口与二次启动初始化卡顿
【其他功能】
- 修正首页 去重计算顺序
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

**累计下载：2,882 次** · **最新版本：红果TV正式版 2.1.0**

| 历史版本 | 下载量 |
| --- | ---: |
| 红果TV正式版 2.1.0 | 22 |
| 红果TV正式版 2.0.3 | 93 |
| 红果TV正式版 2.0.2 | 86 |
| 红果TV正式版 2.0.1 | 57 |
| 红果TV正式版 2.0.0 | 117 |
| 红果TV正式版 1.1.50 | 290 |
| 红果TV正式版 1.1.49 | 808 |
| 红果TV正式版 1.1.48 | 45 |
| 红果TV正式版 1.1.47 | 338 |
| 红果TV正式版 1.1.46 | 234 |
| 红果TV正式版 1.1.45 | 87 |
| 红果TV正式版 1.1.44 | 9 |
| 红果TV正式版 1.1.43 | 41 |
| 红果TV正式版 1.1.42 | 4 |
| 红果TV正式版 1.1.41 | 82 |

**每日下载趋势**

![红果TV每日下载趋势](stats/downloads.svg)

**仓库访问趋势**

![仓库访问趋势](stats/traffic.svg)

<sub>仅统计红果TV正式版 APK。访问数据需配置 TRAFFIC_TOKEN。</sub>
<!-- HONGGUOTV_STATS_END -->
