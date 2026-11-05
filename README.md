# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.18**

- [下载最新版 HongguoTV-1.1.18.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.18/HongguoTV-1.1.18.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 为新版 GET 和旧版 POST 播放请求接入六头签名
- 接入播放专用六头签名算法
- 单击视频区域同时唤起完整播放工具栏
- 清理播放切换中的旧双击任务引用
- 退出播放器时释放中央按钮引用
- 删除不再使用的双击状态
- 移除废弃双击时间记录
- 清理旧双击状态字段
- 清理旧单击延迟任务
- 控制栏收起时隐藏中央按钮
- 同步中央按钮播放状态
- 将中央播放暂停提示改为可点击状态按钮
- 取消双击并接入中央按钮触控
- 调整手机播放器点击交互
- 接入手机播放器中央播放状态反馈图标
- 手机播放器单击切换时显示中央播放状态图标
- 新增手机播放器中央播放状态反馈图标
- 移除播放器快进中状态提示
- 增加手机触屏长按 3 倍速处理
- 接入手机长按倍速手势回调
- 手机播放器增加长按临时倍速手势
- 确保剧场海报卡片布局后补齐向上焦点
- 清理剧场筛选头旧焦点连线残留
- 明确在剧场 ConcatAdapter 组装后统一连接焦点
- 修复剧场筛选头与海报网格布局完成后的焦点连接
- 在剧场筛选头与海报网格组装后连通焦点
- 移除覆盖剧场筛选行焦点映射的错误逻辑
- 修复剧场筛选区焦点上下导航
- 移除搜索导航与首页导航之间的10dp间距
- 精简清理日志设置说明
- 更新无感连播默认设置说明
- 默认开启无感连播
- 清理重复的旧版 JPG 启动图标资源
- Add files via upload
- Delete kotlin-tv/app/src/main/res/drawable-nodpi/tv_banner.webp
- 更新正式版 1.1.17 下载信息
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
