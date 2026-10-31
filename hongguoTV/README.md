# 红果 TV 分发目录

当前版本：**1.1.1**

- APK 安装包：[下载 HongguoTV-1.1.1.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.1/HongguoTV-1.1.1.apk)
- 应用内更新清单：[latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)

## 本次更新说明

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

APK 文件名带版本号。每次成功发布后，工作流会自动更新本说明、APK 和 latest.json。
