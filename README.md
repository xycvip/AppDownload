# AppDownload

应用安装包与版本更新信息的集中分发仓库。

## 最新版本

<!-- BEGIN APP: hongguoTV -->
### 红果 TV

当前版本：**1.1.0**

- [下载最新版 HongguoTV-1.1.0.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.0/HongguoTV-1.1.0.apk)
- [应用内更新清单 latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)
- [红果 TV 全部下载文件与说明](https://github.com/xycvip/AppDownload/tree/main/hongguoTV)

**本次更新说明**

- Refine about dialog update entry
- Fix settings card focus state
- Simplify settings page header
- Show advanced danmaku settings by default
- Show remote key settings directly in settings tab
- Include blocked words in danmaku master switch
- Add sleep timer remote action
- Expose sleep timer in remote key customization
- Rename remote timer action to 定时
- Move sleep timer to playback controls
- Harden video data source bounds and large-file reads
- Validate remote video range payloads and bound cache on seeks
- Pause danmaku animation loop with video playback
- Detect supported video container before MP4 playback
- Improve playback buffering diagnostics and render overlays
- Bound remote video cache during seeks and guard read ranges
- Optimize danmaku frame scheduling and continuous movement
- Report unsupported video containers as non-retryable
- Handle unsupported video formats without pointless retries
- Tie danmaku frame callbacks to view lifecycle
- Adapt playback buffer profile to device memory and network
- Reject unsupported streaming containers before MP4 parsing
- Polish video surface transition and buffering indicator
- Guard remote read-ahead range arithmetic
- 新增官方评论功能
- Balance buffer profile for slow metered connections
- Add persistent player overlay preferences
- Report actual player data reads for speed overlay
- Add configurable video info and live playback speed overlays
- Refine player overlay placement and speed sampling
- Redesign settings as a vertical focusable waterfall layout
- Group danmaku under playback and order five vertical settings sections
- Keep danmaku controls in the playback settings section
- Highlight active settings category on focus
- Unify settings category headings into one card
- Expose grouped theater filter selectors
- Add theater navigation and filter UI
- Render theater filter screen and load catalog
- Fix theater navigation focus mapping
- Complete theater tab focus remapping
- Correct theater focus routing
- Keep unlabeled theater selector groups
- Remap all focus links for theater tab
- Match theater filter row labels to app layout
- Replace theater filters with official App discovery API
- Allow theater session to retain returned filter panel
- Wire theater tab to official multi-filter App catalog
- Reset theater cursors on refresh and require registered device
- Render App-provided non-genre theater filter dimensions
- Align theater filter defaults and API gateway fallback
- Reset dependent theater dimensions and isolate filter scroll state
- Use explicit removal lambda for theater filter reset
- Match official theater genre labels
- Remove duplicate catalog body declaration
- Refresh home content silently whenever home tab is selected
- Preserve full homepage manual refresh action
- Refresh full homepage on tab click and hide refresh button
- Move homepage genre picker to ranking toolbar
- Add responsive full-width random discovery card
- Move random discovery action below AI shelf
- Center and compact random discovery card
- Move view-all cards to end of home shelves
- make AppDownload the only release destination
- release: start HongguoTV 1.1.0 version line
- remove obsolete sync-source-release.yml
- remove obsolete sync-source-release.py
- release: start HongguoTV 1.1.0
<!-- END APP: hongguoTV -->

## 应用目录

- `hongguoTV/`：红果 TV 安装包与应用内更新清单

## 分发规则

- APK 文件名包含版本号，每个应用只保留当前最新 APK。
- 每个应用使用固定的 `latest.json` 更新清单地址。
- APK、更新清单及本说明由对应应用源码仓库的 GitHub Actions 自动更新。
- 本仓库不存放签名私钥、密码或访问令牌。
