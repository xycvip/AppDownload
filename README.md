# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.1**

- [下载最新版 HongguoTV-1.1.1.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.1/HongguoTV-1.1.1.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- Improve updater API, Raw and proxy fallback
- Use API Raw and proxy fallback for release versioning
- Use API-first release metadata and avoid global latest takeover
- Keep HongguoTV releases out of repository-wide latest
- 工作流中文化：cleanup-runs.yml
- 工作流中文化：kotlin-native.yml
- 工作流中文化：prepare-custom-update.yml
- 工作流中文化：release.yml
- 工作流中文化：sync-upstream.yml
- 完善工作流中文显示：cleanup-runs.yml
- 完善工作流中文显示：kotlin-native.yml
- 完善工作流中文显示：prepare-custom-update.yml
- 完善工作流中文显示：release.yml
- 完善工作流中文显示：sync-upstream.yml
- Delete .github/workflows/kotlin-native.yml
- 优化红果TV正式发布工作流安全校验
- 增加红果TV发布后远程核验
- 改为基于上一版递增 versionCode
- Remove post-publication remote verification
- Remove duplicate home random button
- Shorten home random pick label
- Improve random discovery card border contrast
- Make settings category navigation switch visible options
- Wire settings category focus navigation
- Preserve requested settings focus category
- Keep all settings expanded and highlight focused category
- Match settings category highlight to top navigation
- Use shared card focus style for settings categories
- Center settings category labels beside their panels
- Unify settings background and refine focus navigation
- Size settings divider to content height
- Fix vertical swipe handoff on homepage shelves
- Allow vertical swipes through theater filter rows
- Fix homepage vertical swipe interception
- Expand vertical swipe area across search results
- Allow skipping tests for requested release  [skip tests]
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
