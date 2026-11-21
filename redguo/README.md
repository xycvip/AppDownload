# 红果剧场 发布页

红果剧场（RedGuo）Android 客户端安装包与应用内更新清单。包名 `com.x.redguoapp`，同时提供 32 位（armeabi-v7a）与 64 位（arm64-v8a）两个安装包。

<!-- LATEST_RELEASE_START -->
当前版本：**1.0.2**（内部版本 `2026112201`）

- 32 位安装包：[RedGuo-1.0.2-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.2-2026112201/RedGuo-1.0.2-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.2-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.2-2026112201/RedGuo-1.0.2-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.2-2026112201/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.2-2026112201)）
- 完整发布页：[redguo-v1.0.2-2026112201](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.2-2026112201)

## 本次更新说明

- 修复连续切换几集后必然卡住转圈、返回后重新点开也无法播放的问题：被取消的请求会一直占着网络限流名额不放，名额占满后所有请求排队直到超时；现在取消时立即释放名额，前台排队加了上限，排队超时也会自动重试，不再出现「一直转圈」。
- 修复切集时偶发「Unexpected runtime error」导致备用预热失效、连播不无感的问题：两路播放器统一缓冲参数，不再在切集时翻转内核内部状态。
- 取消双播放器的内存限制：是否预热只由「预开下一集」开关决定，内存紧张的设备也能无感切集。
- 精简为仅安卓版本：移除 iOS / Windows / macOS 平台代码与桌面专属功能（桌面小窗、老板键、窗口置顶、窗口全屏等），安装包只含 ARM 架构，不再提供 x86 模拟器架构与 32+64 整合包。
- 播放调试日记区分音频与视频轨道：AAC 音频走软解属正常现象，不再误读成视频掉软解。
<!-- LATEST_RELEASE_END -->

## 历史版本

### 红果剧场正式版 1.0.1

发布版本：**1.0.1**（内部版本 `2026112002`）

- 32 位安装包：[RedGuo-1.0.1-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.1-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.1-2026112002)）
- 完整发布页：[redguo-v1.0.1-2026112002](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.1-2026112002)

**本次更新说明**

优化exo播放体验

### 红果剧场正式版 1.0.1

发布版本：**1.0.1**（内部版本 `2026112002`）

- 32 位安装包：[RedGuo-1.0.1-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.1-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.1-2026112002)）
- 完整发布页：[redguo-v1.0.1-2026112002](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.1-2026112002)

**本次更新说明**

优化exo播放体验

### 红果剧场正式版 1.0.1

发布版本：**1.0.1**（内部版本 `2026112002`）

- 32 位安装包：[RedGuo-1.0.1-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.1-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/RedGuo-1.0.1-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.1-2026112002/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.1-2026112002)）
- 完整发布页：[redguo-v1.0.1-2026112002](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.1-2026112002)

**本次更新说明**

优化exo播放体验

### 红果剧场正式版 1.0.0

发布版本：**1.0.0**（内部版本 `2026112001`）

- 32 位安装包：[RedGuo-1.0.0-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/RedGuo-1.0.0-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.0-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/RedGuo-1.0.0-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.0-2026112001)）
- 完整发布页：[redguo-v1.0.0-2026112001](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.0-2026112001)

**本次更新说明**

初始版本

### 红果剧场正式版 1.0.0

发布版本：**1.0.0**（内部版本 `2026112001`）

- 32 位安装包：[RedGuo-1.0.0-v7a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/RedGuo-1.0.0-v7a.apk)（armeabi-v7a）
- 64 位安装包：[RedGuo-1.0.0-v8a.apk](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/RedGuo-1.0.0-v8a.apk)（arm64-v8a）
- 完整性校验：[SHA256SUMS](https://github.com/xycvip/AppDownload/releases/download/redguo-v1.0.0-2026112001/SHA256SUMS)
- 应用内更新清单：[update.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/redguo/update.json)（[GitCode 发布页](https://gitcode.com/xycvip/redguo/releases/tag/redguo-v1.0.0-2026112001)）
- 完整发布页：[redguo-v1.0.0-2026112001](https://github.com/xycvip/AppDownload/releases/tag/redguo-v1.0.0-2026112001)

**本次更新说明**

初始版本

