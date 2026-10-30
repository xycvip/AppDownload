# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.38**

- [下载最新版 HongguoTV-1.0.38.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.0.38/HongguoTV-1.0.38.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 优化竖屏视频评论面板宽度与显示间距，避免遮挡视频画面。
- 修复关闭评论后遥控器按键误控制播放的问题，恢复控件焦点操作。
- 美化未登录评论操作的登录提示弹窗，统一弹窗样式。
- 新增上、下、确认、菜单键功能自定义，可设置上一集、下一集、播放菜单、评论、播放/暂停、选集或无操作。
- 修复手机端触屏无法唤起播放进度条的问题，支持左右滑动快退快进。
- 设置中的“关于软件”统一显示名称。
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
