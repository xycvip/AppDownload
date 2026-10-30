# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.41**

- [下载最新版 HongguoTV-1.0.41.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.0.41/HongguoTV-1.0.41.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 清除所有数据完成后立即重新打开应用，取消原有闹钟等待重启流程。
- 调整清除数据后的重启兼容处理，最终采用直接启动全新首页的方式。
- Media3 播放器依赖统一升级至 1.11.1，涵盖 ExoPlayer、HLS 与 UI 模块。
- 优化手机扫码登录二维码尺寸，短屏设备弹窗显示更适配。
- 关于页面补充当前版本号显示，并优化版本信息展示。
- 优化备份恢复选项文案，默认题材切换为短剧。
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
