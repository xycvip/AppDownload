# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.0.39**

- [下载最新版 HongguoTV-1.0.39.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.0.39/HongguoTV-1.0.39.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- 优化开机推荐等待逻辑：8 秒仅限制内容开始播放前，开始播放后不再超时中断，返回键始终有效。
- 修复红果账户页面返回行为，账户内按返回键保持在红果账户标签。
- 统一全应用弹窗样式，覆盖多层弹窗、扫码登录、备份确认及选集面板。
- 手机端轻触播放画面即可唤起完整播放菜单。
- 排行榜首次打开默认显示短剧榜。
- 设置页默认聚焦启动推荐开关，并清晰显示开启或关闭状态。
- 清除所有数据后自动重新启动应用。
- 调整遥控器默认按键：上键上一集、下键下一集、确认键播放或暂停、菜单键打开播放菜单。
- 备份与恢复覆盖遥控器自定义、弹幕屏蔽词、按剧弹幕记忆及片头片尾跳过等播放偏好。
- 备份恢复新增重置播放偏好选项，并明确区分当前与备份中的播放偏好设置。
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
