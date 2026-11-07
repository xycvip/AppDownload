# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.36**

- [下载最新版 HongguoTV-1.1.36.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.36/HongguoTV-1.1.36.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- **播放体验优化**：调整播放线路首选项说明文案；将播放线路标签统一改为线路首选；仅保留播放线路切换成功提示；同步播放线路设置文案说明；将播放接口设置文案统一改为播放线路；同步播放接口新名称；更新播放接口名称与设置说明；Ci: 增加播放接口自动回归测试与Debug构建；记录本地播放接口自动选择与会话隔离；覆盖播放接口自动故障切换逻辑；本地播放接口失败自动切换并记忆成功线路；补充播放线路检测请求取消说明；修复播放线路工厂 Kotlin 编译错误；切换播放线路时取消旧接口检测请求；自动与手动播放接口检测支持线路切换取消；为播放接口检测增加可取消请求作用域；记录原生与 Phoenix 播放线路互斥修复；接口检测遵循当前播放线路；切换播放线路时清理旧任务并重启当前播放；隔离单播放器预加载线路缓存；普通播放统一使用当前播放线路；修复播放线路选择与诊断隔离；审计播放接口诊断并补充技术说明；修复播放接口诊断列表编译错误；增加播放接口调试诊断信息；接入 Phoenix 播放接口选择；将 Phoenix 播放接口拆分为独立模块；补齐应用对播放模块的直接依赖；拆分原生播放接口与共享媒体模块。
- **体验优化**：统一 Native 线路优先显示文案；隔离 Phoenix 与原生接口的 CookieJar；记录 PhoenixReadApi 上游来源及签名差异；修正 Phoenix 诊断回调构造参数；补齐共享媒体模块的 CENC 样本诊断属性；将请求加密组件迁入共享媒体模块。
- **界面与体验优化**：统一调试面板 Phoenix 名称；统一诊断中的 Native 名称。
- **问题修复**：Ci: 修复 Android SDK 安装步骤并重跑接口回归；防止诊断回调异常中断自动切换。
- **下载体验优化**：隔离无感连播备用线路缓存。
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
