# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.35**

- [下载最新版 HongguoTV-1.0.35.apk](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/HongguoTV-1.0.35.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 新增账号接口连通性检测
- 刷新后保留焦点，并显示账号接口状态
- 重新加载后恢复到已选排行榜操作项
- 完善片单刷新操作后的焦点恢复
- 片单刷新失败后恢复焦点
- 清空分类后将焦点返回可用筛选项
- 首页重新加载后保留刷新按钮焦点
- 构建最新定制版安装包
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
