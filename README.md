# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.28**

- [下载最新版 HongguoTV-1.1.28.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.28/HongguoTV-1.1.28.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- fix: 修复更新弹窗重复添加按钮导致闪退
- ui: 调整版本更新弹窗布局与下载速度显示
- fix: 避免无感连播接管时重复定位导致短暂停顿
- fix: 切换更新弹窗时保持关于页按钮状态
- fix: 无新版时清除暂存的下载线路选择
- fix: 标注三条下载线路并修正速度单位
- fix: 关于软件弹窗固定检查更新按钮
- fix: 保留手动下载线路选择并将速度置顶
- feat: 下载显示实时速度并支持指定线路
- feat: 接入三个下载地址的选择操作
- feat: 更新弹窗增加三个下载地址按钮
- feat: 更新弹窗显示实时下载速度
- feat: 更新下载支持三条手动线路与实时速度
- fix: GitCode主源失败时允许手动线路触发GitHub备用
- fix: GitCode下载失败时先尝试GitHub Release备用
- fix: 兼容更新下载空响应处理
- fix: GitCode下载失败时安全回退AppDownload
- feat: 正式版自动更新改为GitCode优先
- 更新正式版 1.1.27 下载信息
<!-- END APP: hongguoTV -->

## 仓库用途

AppDownload 是应用发布与下载分发仓库，不是 Android 源代码仓库。应用源码、开发过程和功能实现请以对应的源码项目为准。

### 应用目录

- `hongguoTV/`：红果 TV（HongguoTV）Android APK 发布文件与应用内更新清单。

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
