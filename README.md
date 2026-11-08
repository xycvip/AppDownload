# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.38**

- [下载最新版 HongguoTV-1.1.38.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.38/HongguoTV-1.1.38.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- **下载体验优化**：修复自动回退成功回调的默认参数；记录自动回退提示的首帧显示规则；修正线路回退成功回调参数；补充线路回退提示的单元测试；播放线路自动回退成功后等待首帧再提示。
- **播放体验优化**：修复播放恢复代码中的 Context 常量引用；更新播放故障恢复机制说明；完善播放故障恢复：同线路重试后双线路切换；播放失败时清理未展示的线路切换提示；播放线路切换提示延后到实际首帧；区分播放线路与内容平台；修正播放接口验证结果记录；更正播放线路说明与1.1.37验证状态。
- **操作体验优化**：修复启动时焦点默认落在四叶状态灯。
- **体验优化**：限制自动恢复仅处理媒体与网络故障；保留跨线路恢复待显示提示；修正首帧提示的 Activity 接收者引用；接口诊断请求不触发用户线路提示；清理河马平台说明；更新无感连播线路隔离与审计基准；校准1.1.37功能说明与验证记录。
- **问题修复**：完善线路恢复确认与失败回滚；修复线路首选左侧说明不显示。
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
