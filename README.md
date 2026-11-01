# AppDownload

**红果 TV（HongguoTV）Android APK 非官方发布与应用更新分发仓库。**

本仓库集中提供 Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取红果 TV 最新版本，并通过固定的更新清单地址检查新版本。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is an Android APK download and app release repository. It distributes HongguoTV releases, version metadata, and the app's update manifest.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV（HongguoTV）

当前版本：**1.1.9**

- [下载最新版 HongguoTV-1.1.9.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.9/HongguoTV-1.1.9.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)
- [查看所有版本发布记录（Releases）](https://github.com/xycvip/AppDownload/releases)

**本次更新说明**

- 优化搜索功能与搜索结果展示
- 优化视频播放体验及播放设置
- 优化设置选项与操作体验
- 优化界面布局与交互效果
- 完善本地数据备份与恢复
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
- Project: HongguoTV Android APK downloads and releases
- Distribution: GitHub Releases and GitHub Raw
- Manifest: `hongguoTV/latest.json`

如需反馈下载或更新问题，请通过本仓库的 Issues 提交，并注明设备型号、Android 版本和遇到的问题。
