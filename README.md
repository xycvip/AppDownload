# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.37**

- [下载最新版 HongguoTV-1.0.37.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.0.37/HongguoTV-1.0.37.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 其他功能优化（详情见本次版本提交记录）
- 发布说明改为中文并保留 AppDownload 多应用首页
- 修正中文更新说明脚本的转义格式
- 将红果TV APK 发布到 AppDownload 独立 Release
- 支持从 AppDownload Release 下载更新包
- 修正 Release 资源上传顺序与 URL 编码
- 发布当前 custom 版本
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
