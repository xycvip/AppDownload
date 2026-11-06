# 红果 TV 分发目录

<!-- LATEST_RELEASE_START -->
当前版本：**1.1.28**

- APK 安装包：[下载 HongguoTV-1.1.28.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.28/HongguoTV-1.1.28.apk)
- 应用内更新清单：[latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)

## 本次更新说明

- fix: 修复更新弹窗重复添加按钮导致闪退
- ui: 调整版本更新弹窗布局与下载速度显示
- fix: 避免无感连播接管时重复定位导致短暂停顿
- fix: 切换更新弹窗时保持关于页按钮状态
- fix: 无新版时清除暂存的下载线路选择
- fix: 标注三条下载线路并修正速度单位
- fix: 关于软件弹窗固定检查更新按钮
- fix: 保留手动下载线路选择并将速度置顶
- feat: 下载显示实时速度并支持指定线路
- feat: 接入三个下载地址的选择操作
- feat: 更新弹窗增加三个下载地址按钮
- feat: 更新弹窗显示实时下载速度
- feat: 更新下载支持三条手动线路与实时速度
- fix: GitCode主源失败时允许手动线路触发GitHub备用
- fix: GitCode下载失败时先尝试GitHub Release备用
- fix: 兼容更新下载空响应处理
- fix: GitCode下载失败时安全回退AppDownload
- feat: 正式版自动更新改为GitCode优先
- 更新正式版 1.1.27 下载信息
<!-- LATEST_RELEASE_END -->

## 红果TV正式版 1.1.16

- 下载：[HongguoTV-1.1.16.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.16/HongguoTV-1.1.16.apk)
- versionCode：`2026103476`
- SHA-256：`cafcd9cc5200494dc2d2f17573b9c5224e4e8c8bef1d5bf7c8b5bd18683a328d`

### 本次更新
# 红果TV 正式版更新说明

本次版本经过多个测试版本的持续优化，重点改进视频播放体验、第三方片源管理、数据备份恢复及电视端操作体验。

### 【播放体验优化】
- 新增「无缝连播」功能，采用双播放器提前准备下一集，减少切换剧集时的等待和画面中断。
- 优化播放器切集交接、首帧检测及缓冲状态处理。
- 增加备用播放器异常回退机制，提高播放过程中的稳定性。
- 播放控制栏增加视频实际分辨率显示。
- 手机播放器增加横屏、竖屏切换按钮，电视端自动隐藏该按钮。

### 【第三方片源管理】
- 优化第三方片源扫码导入规则，只追加尚未存在的片源，不覆盖已有配置。
- 完善第三方片源、观看历史和收藏的备份与恢复。
- 整机恢复时，第三方片源及其观看历史、收藏按照备份内容完整覆盖，备份中为空的数据也会同步清空。

### 【远程文件管理】
- 增加远程文件删除功能。
- 支持通过手机访问电视设备的公共存储目录。
- 完善文件上传、下载、目录浏览及删除操作。

### 【界面与操作优化】
- 优化电视端导航栏视觉效果，支持与主题联动的磨砂玻璃效果。
- 优化弹窗布局及遥控器焦点移动体验。
- 完善设置页面功能说明和操作体验。
- 更新手机桌面应用图标及电视桌面横幅。

### 【稳定性与问题修复】
- 优化双播放器资源释放、切集状态及缓冲提示。
- 修复播放器备用资源准备和交接过程中的部分异常。
- 完善网络状态、接口请求及播放器运行诊断。
- 修复更新检查可能错误选择旧版本更新清单的问题。
- 优化缓存清理、软件重置及后台资源释放流程。


---

## 红果TV正式版 1.1.17

- 下载：[HongguoTV-1.1.17.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.17/HongguoTV-1.1.17.apk)
- versionCode：2026110501
- SHA-256：f237db0e4c5ac8b71f083e84001d93b8e8e91e6ecc5b62e8eb9653860db4ef7b

### 本次更新
- 更新测试版 0.0.15 下载信息并递增版本号至 0.0.16
- 修复排行榜焦点恢复变量声明顺序导致的编译失败
- 同步更新四叶指示灯尺寸注释
- 调整四叶指示灯尺寸至25sp
- 修复排行榜页面焦点跟踪与恢复
- 保留筛选按钮原有焦点视觉效果
- 在焦点样式回调中记录剧场筛选焦点
- 避免剧场页面重建时焦点恢复冲突
- 修复剧场筛选焦点跟踪与可见区域导航
- 更新远程文件管理IPv4适用范围说明
- 更新远程文件管理网络地址说明
- 允许远程文件服务绑定公网IPv4并接受非局域网客户端
- 远程文件管理支持任意可用IPv4地址
- 更新远程文件管理入口说明
- 允许无局域网连接时打开远程文件管理扫码页面
- 更新一键清理全部调试日志的功能说明
- 更新一键清理全部日志的设置说明
- 调整清理日志为一键清空全部调试日志
- 增加清理全部调试日志文件功能
- 统一无感连播调试文案
- 将实现说明文件更名为无感连播
- 统一功能名称为无感连播
- 文档名称统一为无感连播
- 更新测试版 0.0.14 下载信息并递增版本号至 0.0.15
- 同步播放器手势区域比例说明
- 调整手机播放器上下滑动手势区域为 20/60/20
- 更新手机播放器三分区上下滑动手势说明
- 接入手机播放器上下滑动切集回调
- 手机播放器中间区域上下滑动切换剧集
- 退出播放器时恢复进入前的窗口亮度
- 保存播放器亮度手势前的窗口亮度基准
- 记录手机播放器手势调节前的窗口亮度
- 更新手机播放器手势提示文案
- 接入手机播放器上下滑动亮度音量控制
- 新增手机播放器亮度与音量上下滑动控制
- 为手机播放器触控协调器加入上下滑动手势
- 调整正式版 versionCode 为日期加两位辅助序号
- 明确正式版历史说明与首页同步规则
- 优化正式版README更新说明格式
- 修正正式版历史说明中的 shell 转义
- 更新功能审计中的发布状态与文档同步规则
- 恢复正式版自动更新说明并同步分发仓库总 README
- 更新正式版 1.1.16 下载信息

---

## 红果TV正式版 1.1.18

- 下载：[HongguoTV-1.1.18.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.18/HongguoTV-1.1.18.apk)
- versionCode：2026110502
- SHA-256：c64184f50e953ba26143e9243ee0d27537b4df51017f2ad1344c3d27abda5b8a

### 本次更新
- 为新版 GET 和旧版 POST 播放请求接入六头签名
- 接入播放专用六头签名算法
- 单击视频区域同时唤起完整播放工具栏
- 清理播放切换中的旧双击任务引用
- 退出播放器时释放中央按钮引用
- 删除不再使用的双击状态
- 移除废弃双击时间记录
- 清理旧双击状态字段
- 清理旧单击延迟任务
- 控制栏收起时隐藏中央按钮
- 同步中央按钮播放状态
- 将中央播放暂停提示改为可点击状态按钮
- 取消双击并接入中央按钮触控
- 调整手机播放器点击交互
- 接入手机播放器中央播放状态反馈图标
- 手机播放器单击切换时显示中央播放状态图标
- 新增手机播放器中央播放状态反馈图标
- 移除播放器快进中状态提示
- 增加手机触屏长按 3 倍速处理
- 接入手机长按倍速手势回调
- 手机播放器增加长按临时倍速手势
- 确保剧场海报卡片布局后补齐向上焦点
- 清理剧场筛选头旧焦点连线残留
- 明确在剧场 ConcatAdapter 组装后统一连接焦点
- 修复剧场筛选头与海报网格布局完成后的焦点连接
- 在剧场筛选头与海报网格组装后连通焦点
- 移除覆盖剧场筛选行焦点映射的错误逻辑
- 修复剧场筛选区焦点上下导航
- 移除搜索导航与首页导航之间的10dp间距
- 精简清理日志设置说明
- 更新无感连播默认设置说明
- 默认开启无感连播
- 清理重复的旧版 JPG 启动图标资源
- Add files via upload
- Delete kotlin-tv/app/src/main/res/drawable-nodpi/tv_banner.webp
- 更新正式版 1.1.17 下载信息

---

## 红果TV正式版 1.1.19

- 下载：[HongguoTV-1.1.19.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.19/HongguoTV-1.1.19.apk)
- versionCode：2026110601
- SHA-256：add622a124a9d3b4491775537e47f4d36789a7cf802dccc669b77b0f04639300

### 本次更新
- 更新播放器方向重启行为说明
- 取消手机播放器方向持久化写入
- 调整手机播放器方向为进程内记忆并在重启后恢复横屏
- 更新播放器方向持久化逻辑说明
- 同步手机播放器方向偏好的字段说明
- 退出播放器时保留已保存的手机方向偏好
- 持久化手机播放器方向选择
- 恢复手机播放器上次选择的屏幕方向
- 将追剧导航默认入口切换为最近观看
- 调整追剧页入口顺序并默认显示最近观看
- 升级 GitHub Actions 运行时并消除 Node.js 20 警告
- 修复弹幕 SP 字体缩放弃用警告
- 修复 APK 安装 Intent 弃用警告
- 移除签名对照测试临时诊断输出
- 修正 F13 哈希消息调度递推
- 增加签名哈希差异诊断
- 增加签名对照测试差异诊断
- 按弹幕备用线路数量修正退避测试断言
- 修正文件传输测试中的查询路径格式
- 修正剧场接口测试以覆盖新版双阶段请求
- 切换追剧分区后恢复对应入口焦点
- 完善追剧入口的遥控器焦点连接
- 将收藏和最近观看归入追剧导航
- 新增追剧导航并合并收藏与最近观看入口
- 调整 v1 首屏请求顺序并修正身份状态识别
- 剧场筛选接口优先使用 v1 并保留旧接口回退
- 诊断日志记录内容接口空响应的HTTP状态和字节数
- 修正剧场身份失效状态码识别
- 增加剧场接口身份恢复与网络故障回归测试
- 修复剧场接口空响应后的设备身份恢复并增加逐域名诊断
- 手机播放方向选择保持至应用退出
- 手机长按三倍速松手不弹出控制栏
- 手机长按三倍速不唤起播放工具栏
- ci: 将手机播放器代码纳入自动编译检查
- fix: 接入手机播放工具栏点击收起回调
- fix: 手机端点击视频空白处收起播放工具栏
- fix: 剧场接口增加六线路故障切换
- ci: 添加核心模块单元测试工作流
- fix: 剧场接口签名绑定注册设备身份
- fix: 弹幕复用注册设备身份并增加线路切换
- 更新正式版 1.1.18 下载信息

---

## 红果TV正式版 1.1.20

- 下载：[HongguoTV-1.1.20.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.20/HongguoTV-1.1.20.apk)
- versionCode：2026110602
- SHA-256：f35d342837bc004f04a5f8e893d2ffcc13793cb21cf3fdb89a927c50b444c0ca

### 本次更新
- fix: 明确换源检查状态提示
- fix: 兼容现有Gitee发行版更新清单
- fix: 正式版Gitee下载线路增加缓存规避
- ci: Gitee正式版更新清单使用Gitee APK下载地址
- feat: 正式版换源按钮适配Gitee优先线路
- feat: 正式版更新源改为Gitee优先并保留GitHub回退
- ci: 删除独立Gitee同步工作流，统一由正式版发布工作流执行
- ci: 将Gitee正式版同步合并到发布工作流
- ci: 从源码仓库自动同步正式版到 Gitee
- ci: 正式版同步发布到源码仓库 GitHub Release
- 更新正式版 1.1.19 下载信息

---

## 红果TV正式版 1.1.21

- 下载：[HongguoTV-1.1.21.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.21/HongguoTV-1.1.21.apk)
- versionCode：2026110603
- SHA-256：11ecb3f1a63b16c240a356036cccbf24e1f40ff8923672b40dcd6172eee66505

### 本次更新
- 修正Gitee文件同步步骤环境变量
- 正式版同步Gitee更新清单和说明文件
- 正式版仅发布到 AppDownload 和 Gitee
- 更新正式版 1.1.20 下载信息

---

## 红果TV正式版 1.1.22

- 下载：[HongguoTV-1.1.22.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.22/HongguoTV-1.1.22.apk)
- versionCode：2026110604
- SHA-256：24a7a61e8d2dc9267bee981fc95b6b26c8c979472415729991ef6dd1975ffe45

### 本次更新
- 增强Gitee发行版ID查询兼容
- 修复Gitee已存在发行版ID解析
- 更新正式版 1.1.21 下载信息

---

## 红果TV正式版 1.1.23

- 下载：[HongguoTV-1.1.23.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.23/HongguoTV-1.1.23.apk)
- versionCode：2026110605
- SHA-256：0ab7de01de73abd764a4a302156f73172cb6930b97815b634696dfabadb4df69

### 本次更新
- 新增Gitee网络连接独立检测工作流
- 修正Gitee请求重试函数调用
- 增加Gitee发布网络请求重试
- 更新正式版 1.1.22 下载信息

---

## 红果TV正式版 1.1.24

- 下载：[HongguoTV-1.1.24.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.24/HongguoTV-1.1.24.apk)
- versionCode：2026110606
- SHA-256：4aaeb647d66efb6deecababa0e5a04f55fe6038b0023946c989af163fed8adc0

### 本次更新
- 修复Gitee首次正式版发行版自动创建
- 更新正式版 1.1.23 下载信息

---

## 红果TV正式版 1.1.25

- 下载：[HongguoTV-1.1.25.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.25/HongguoTV-1.1.25.apk)
- versionCode：2026110607
- SHA-256：899880360ad8089a78db0773dd09886af895328cb0f09931e8ca9134092a5bff

### 本次更新
- 修复Gitee更新发行版缺少必填Tag参数
- 更新正式版 1.1.24 下载信息

---

## 红果TV正式版 1.1.26

- 下载：[HongguoTV-1.1.26.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.26/HongguoTV-1.1.26.apk)
- versionCode：2026110608
- SHA-256：c017ab49fc2b73505c3c7682c0ed1b009cacf544e8a6443d80100868467a6f3f

### 本次更新
- 重建正式版工作流末尾Gitee清理与结果步骤
- 修正正式版工作流Gitee清理循环缩进
- 修复正式版工作流末尾Gitee清理代码结构
- 补同步Gitee说明仅保留最新版更新信息
- Gitee说明文档仅保留最新版更新信息
- 正式版发布后清理Gitee旧正式版发行记录
- 修复Gitee正式版附件文件名和MIME类型
- 修复Gitee新建文件POST及重试日志污染
- 修复Gitee新建文件使用POST接口
- 兼容Gitee空数组响应并创建新文件
- 修复Gitee空数组响应时创建新文件
- 修复Gitee补同步说明文件换行
- 修复Gitee补同步工作流路径和换行处理
- 新增Gitee正式版文件补同步工作流
- 修正Gitee文件SHA解析参数
- 修复Gitee文件查询数组响应解析
- 更新正式版 1.1.25 下载信息

---

## 红果TV正式版 1.1.27

- 下载：[HongguoTV-1.1.27.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.27/HongguoTV-1.1.27.apk)
- versionCode：2026110609
- SHA-256：846322b1bcbea4d8e8bea46e94136e53864c56e6eecef176159de7e1e0d0b0ef

### 本次更新
优化使用体验

---

## 红果TV正式版 1.1.28

- 下载：[HongguoTV-1.1.28.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.28/HongguoTV-1.1.28.apk)
- versionCode：2026110610
- SHA-256：77fd2a219e38ee3fe4298624c57ab2664156d5726b5a07c2216abc6ff14d2af6

### 本次更新
- fix: 修复更新弹窗重复添加按钮导致闪退
- ui: 调整版本更新弹窗布局与下载速度显示
- fix: 避免无感连播接管时重复定位导致短暂停顿
- fix: 切换更新弹窗时保持关于页按钮状态
- fix: 无新版时清除暂存的下载线路选择
- fix: 标注三条下载线路并修正速度单位
- fix: 关于软件弹窗固定检查更新按钮
- fix: 保留手动下载线路选择并将速度置顶
- feat: 下载显示实时速度并支持指定线路
- feat: 接入三个下载地址的选择操作
- feat: 更新弹窗增加三个下载地址按钮
- feat: 更新弹窗显示实时下载速度
- feat: 更新下载支持三条手动线路与实时速度
- fix: GitCode主源失败时允许手动线路触发GitHub备用
- fix: GitCode下载失败时先尝试GitHub Release备用
- fix: 兼容更新下载空响应处理
- fix: GitCode下载失败时安全回退AppDownload
- feat: 正式版自动更新改为GitCode优先
- 更新正式版 1.1.27 下载信息

---
