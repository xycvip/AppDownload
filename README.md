# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.16**

- [下载最新版 HongguoTV-1.1.16.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.16/HongguoTV-1.1.16.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

本次版本经过多个测试版本的持续优化，重点改进视频播放体验、第三方片源管理、数据备份恢复及电视端操作体验。

### 【播放体验优化】
- 新增「无缝连播」功能，采用双播放器提前准备下一集，减少切换剧集时的等待和画面中断。
- 优化播放器切集交接、首帧检测及缓冲状态处理。
- 增加备用播放器异常回退机制，提高播放过程中的稳定性。
- 播放控制栏增加视频实际分辨率显示。
- 手机播放器增加横屏、竖屏切换按钮，电视端自动隐藏该按钮。

### 【第三方片源管理】
- 优化第三方片源扫码导入规则，只追加尚未存在的片源，不覆盖已有配置。
- 完善第三方片源、观看历史和收藏的备份与恢复。
- 整机恢复时，第三方片源及其观看历史、收藏按照备份内容完整覆盖，备份中为空的数据也会同步清空。

### 【远程文件管理】
- 增加远程文件删除功能。
- 支持通过手机访问电视设备的公共存储目录。
- 完善文件上传、下载、目录浏览及删除操作。

### 【界面与操作优化】
- 优化电视端导航栏视觉效果，支持与主题联动的磨砂玻璃效果。
- 优化弹窗布局及遥控器焦点移动体验。
- 完善设置页面功能说明和操作体验。
- 更新手机桌面应用图标及电视桌面横幅。

### 【稳定性与问题修复】
- 优化双播放器资源释放、切集状态及缓冲提示。
- 修复播放器备用资源准备和交接过程中的部分异常。
- 完善网络状态、接口请求及播放器运行诊断。
- 修复更新检查可能错误选择旧版本更新清单的问题。
- 优化缓存清理、软件重置及后台资源释放流程。
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
