# AppDownload

**红果TV Android APK 下载与版本更新仓库，提供最新版安装包、自动更新清单及历史版本信息。**

本仓库由第三方维护，集中提供红果 TV（HongguoTV）Android 应用安装包（APK）、版本信息、应用内更新清单和下载说明。用户可以在这里获取本仓库发布的最新版本，并通过固定的更新清单地址检查新版本。本仓库与红果 TV 官方运营主体无隶属或授权关系。

**项目关键词：** 红果TV、HongguoTV、Hongguo TV、Android、安卓应用、APK 下载、应用更新、版本发布、latest.json。

**English:** AppDownload is a community-maintained, third-party Android APK download and app update repository for HongguoTV. It provides APK releases, version metadata, and the app's update manifest. It is not affiliated with or endorsed by the official HongguoTV operator.

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.19**

- [下载最新版 HongguoTV-1.1.19.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.19/HongguoTV-1.1.19.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 更新播放器方向重启行为说明
- 取消手机播放器方向持久化写入
- 调整手机播放器方向为进程内记忆并在重启后恢复横屏
- 更新播放器方向持久化逻辑说明
- 同步手机播放器方向偏好的字段说明
- 退出播放器时保留已保存的手机方向偏好
- 持久化手机播放器方向选择
- 恢复手机播放器上次选择的屏幕方向
- 将追剧导航默认入口切换为最近观看
- 调整追剧页入口顺序并默认显示最近观看
- 升级 GitHub Actions 运行时并消除 Node.js 20 警告
- 修复弹幕 SP 字体缩放弃用警告
- 修复 APK 安装 Intent 弃用警告
- 移除签名对照测试临时诊断输出
- 修正 F13 哈希消息调度递推
- 增加签名哈希差异诊断
- 增加签名对照测试差异诊断
- 按弹幕备用线路数量修正退避测试断言
- 修正文件传输测试中的查询路径格式
- 修正剧场接口测试以覆盖新版双阶段请求
- 切换追剧分区后恢复对应入口焦点
- 完善追剧入口的遥控器焦点连接
- 将收藏和最近观看归入追剧导航
- 新增追剧导航并合并收藏与最近观看入口
- 调整 v1 首屏请求顺序并修正身份状态识别
- 剧场筛选接口优先使用 v1 并保留旧接口回退
- 诊断日志记录内容接口空响应的HTTP状态和字节数
- 修正剧场身份失效状态码识别
- 增加剧场接口身份恢复与网络故障回归测试
- 修复剧场接口空响应后的设备身份恢复并增加逐域名诊断
- 手机播放方向选择保持至应用退出
- 手机长按三倍速松手不弹出控制栏
- 手机长按三倍速不唤起播放工具栏
- ci: 将手机播放器代码纳入自动编译检查
- fix: 接入手机播放工具栏点击收起回调
- fix: 手机端点击视频空白处收起播放工具栏
- fix: 剧场接口增加六线路故障切换
- ci: 添加核心模块单元测试工作流
- fix: 剧场接口签名绑定注册设备身份
- fix: 弹幕复用注册设备身份并增加线路切换
- 更新正式版 1.1.18 下载信息
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
