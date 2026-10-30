# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.42**

- [下载最新版 HongguoTV-1.0.42.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.0.42/HongguoTV-1.0.42.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 题材选择记住手动切换的短剧、漫剧和 AI 剧，冷启动仍默认短剧。
- 题材类型标签按屏幕宽度自适应分配空间与间距。
- 搜索热搜推荐改为短剧与漫剧混合展示，不再清一色 AI 剧。
- 修复清除所有数据：停止后台任务、等待写入完成，再清空本机设置与记录后重启。
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
