# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.9**

- [下载最新版 HongguoTV-1.1.9.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.9/HongguoTV-1.1.9.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 优化搜索功能与搜索结果展示
- 优化视频播放体验及播放设置
- 优化设置选项与操作体验
- 优化界面布局与交互效果
- 完善本地数据备份与恢复
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
