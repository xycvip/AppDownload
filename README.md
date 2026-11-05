# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.17**

- [下载最新版 HongguoTV-1.1.17.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.17/HongguoTV-1.1.17.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 更新测试版 0.0.15 下载信息并递增版本号至 0.0.16
- 修复排行榜焦点恢复变量声明顺序导致的编译失败
- 同步更新四叶指示灯尺寸注释
- 调整四叶指示灯尺寸至25sp
- 修复排行榜页面焦点跟踪与恢复
- 保留筛选按钮原有焦点视觉效果
- 在焦点样式回调中记录剧场筛选焦点
- 避免剧场页面重建时焦点恢复冲突
- 修复剧场筛选焦点跟踪与可见区域导航
- 更新远程文件管理IPv4适用范围说明
- 更新远程文件管理网络地址说明
- 允许远程文件服务绑定公网IPv4并接受非局域网客户端
- 远程文件管理支持任意可用IPv4地址
- 更新远程文件管理入口说明
- 允许无局域网连接时打开远程文件管理扫码页面
- 更新一键清理全部调试日志的功能说明
- 更新一键清理全部日志的设置说明
- 调整清理日志为一键清空全部调试日志
- 增加清理全部调试日志文件功能
- 统一无感连播调试文案
- 将实现说明文件更名为无感连播
- 统一功能名称为无感连播
- 文档名称统一为无感连播
- 更新测试版 0.0.14 下载信息并递增版本号至 0.0.15
- 同步播放器手势区域比例说明
- 调整手机播放器上下滑动手势区域为 20/60/20
- 更新手机播放器三分区上下滑动手势说明
- 接入手机播放器上下滑动切集回调
- 手机播放器中间区域上下滑动切换剧集
- 退出播放器时恢复进入前的窗口亮度
- 保存播放器亮度手势前的窗口亮度基准
- 记录手机播放器手势调节前的窗口亮度
- 更新手机播放器手势提示文案
- 接入手机播放器上下滑动亮度音量控制
- 新增手机播放器亮度与音量上下滑动控制
- 为手机播放器触控协调器加入上下滑动手势
- 调整正式版 versionCode 为日期加两位辅助序号
- 明确正式版历史说明与首页同步规则
- 优化正式版README更新说明格式
- 修正正式版历史说明中的 shell 转义
- 更新功能审计中的发布状态与文档同步规则
- 恢复正式版自动更新说明并同步分发仓库总 README
- 更新正式版 1.1.16 下载信息
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
