# 红果 TV 分发目录

<!-- LATEST_RELEASE_START -->
当前版本：**1.1.46**

- APK 安装包：[下载 HongguoTV-1.1.46.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.46/HongguoTV-1.1.46.apk)
- 应用内更新清单：[latest.json](https://raw.githubusercontent.com/xycvip/AppDownload/main/hongguoTV/latest.json)

## 本次更新说明

【播放与播放器】
- 调整双线路播放优先级，优化主线路与兼容线路切换逻辑
- 优化播放设备注册及会话身份处理
- 改进播放接口异常响应时的兼容处理  【演员榜与排行榜】
- 调整排行榜页面，新增演员榜入口
- 增加剧星榜、星光榜相关页面及演员作品列表功能
- 优化排行榜页面导航、焦点和交互体验  【分享与推送播放】
- 优化抖音短剧分享链接解析
- 增强剧名识别能力，减少作者名称、营销文案和无关话题干扰
- 增加短剧详情识别，改进剧名获取及候选匹配流程
- 优化分享链接无法直接识别时的后续处理  【界面与交互】
- 优化排行榜及目录页面布局和焦点处理
- 弹幕默认显示行数调整为2行
- 优化页面操作及使用体验
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

## 红果TV正式版 1.1.29

- 下载：[HongguoTV-1.1.29.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.29/HongguoTV-1.1.29.apk)
- versionCode：2026110611
- SHA-256：8b0cd5e8851abf2427c387cbb944ea72caab9cad2281be3bd0f76b018c19af75

### 本次更新
- fix: 增强B播放器接管后的初始缓冲
- fix: 正式版不再发布到源码仓库
- revert: 恢复导航栏首页名称
- ui: 修改导航栏首页文案
- 更新正式版 1.1.28 下载信息

---

## 红果TV正式版 1.1.30

- 下载：[HongguoTV-1.1.30.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.30/HongguoTV-1.1.30.apk)
- versionCode：2026110612
- SHA-256：ab9a747ed315b5ce69c98124210b84ab41b99979e702d4888830b4bdb3b8b19d

### 本次更新
- ui: 总榜名称调整为综合榜
- fix: 明确排行榜首排海报向上焦点
- fix: 统一排行榜分页来源名称
- fix: 统一排行榜来源名称
- feat: 增加总榜入口并调整榜单顺序
- feat: 默认打开红果综合总榜
- feat: 接入红果综合热播总榜
- fix: 完善GitHub手动下载源备用清单
- fix: 修复GitCode下载源回退判断
- 更新正式版 1.1.29 下载信息

---

## 红果TV正式版 1.1.31

- 下载：[HongguoTV-1.1.31.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.31/HongguoTV-1.1.31.apk)
- versionCode：2026110701
- SHA-256：f2ec71127901871e31cf0d34b34c3acfbbd22fea6d23dd8bb451d16527667771

### 本次更新
- **问题修复**：修复正式版发布脚本 heredoc 缩进。
- **排行榜优化**：片库和排行榜题材标签改为亮橘色。
- **界面与体验优化**：首页题材标签文字改为亮橘色。
- **体验优化**：首页海报标题下显示作品题材；海报标题下显示作品题材；修正正式版发布说明脚本转义；优化正式版中文发布说明生成。

---

## 红果TV正式版 1.1.32

- 下载：[HongguoTV-1.1.32.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.32/HongguoTV-1.1.32.apk)
- versionCode：2026110702
- SHA-256：d271edbc6da8c4e5e7872b3dd70b8830a0237f039a9b1658641ee8ff5524e0d2

### 本次更新
- **体验优化**：完善 GitCode APK 验证结构检查；覆盖 GitCode APK 正式附件地址；按 GitCode API 返回地址读取更新清单；覆盖 GitCode 新版附件地址格式；修正 GitCode Release 附件地址解析。
- **下载体验优化**：覆盖 GitCode Release 清单下载地址。
- **操作体验优化**：返回键支持从搜索导航返回首页。

---

## 红果TV正式版 1.1.33

- 下载：[HongguoTV-1.1.33.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.33/HongguoTV-1.1.33.apk)
- versionCode：2026110703
- SHA-256：4d8807ef0f922584b3c9181f17ede41fb4fe6c811f832261006cbcb8689e6fb4

### 本次更新
优化使用体验

---

## 红果TV正式版 1.1.34

- 下载：[HongguoTV-1.1.34.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.34/HongguoTV-1.1.34.apk)
- versionCode：2026110704
- SHA-256：f2500e9dddc9d5880df058af6a1c6a9ae745c248803f01e4e25ca095312e3bac

### 本次更新
- **体验优化**：显式允许 GitCode 文件 CDN 域名；Ci: GitCode清单诊断改为请求原始地址。
- **下载体验优化**：GitCode下载保留原始地址并允许其子域名；Ci: 增加 GitCode APK 原始地址下载校验。

---

## 红果TV正式版 1.1.35

- 下载：[HongguoTV-1.1.35.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.35/HongguoTV-1.1.35.apk)
- versionCode：2026110705
- SHA-256：3a49864828bedc0d0d590cace77d5b3755abae8f79f4467122f972cb58aa6f29

### 本次更新
优化使用体验

---

## 红果TV正式版 1.1.36

- 下载：[HongguoTV-1.1.36.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.36/HongguoTV-1.1.36.apk)
- versionCode：2026110706
- SHA-256：8e430a192292739b247f10c5d976e7fed217c070e56c8695aaf5d85f3b5319ea

### 本次更新
- **播放体验优化**：调整播放线路首选项说明文案；将播放线路标签统一改为线路首选；仅保留播放线路切换成功提示；同步播放线路设置文案说明；将播放接口设置文案统一改为播放线路；同步播放接口新名称；更新播放接口名称与设置说明；Ci: 增加播放接口自动回归测试与Debug构建；记录本地播放接口自动选择与会话隔离；覆盖播放接口自动故障切换逻辑；本地播放接口失败自动切换并记忆成功线路；补充播放线路检测请求取消说明；修复播放线路工厂 Kotlin 编译错误；切换播放线路时取消旧接口检测请求；自动与手动播放接口检测支持线路切换取消；为播放接口检测增加可取消请求作用域；记录原生与 Phoenix 播放线路互斥修复；接口检测遵循当前播放线路；切换播放线路时清理旧任务并重启当前播放；隔离单播放器预加载线路缓存；普通播放统一使用当前播放线路；修复播放线路选择与诊断隔离；审计播放接口诊断并补充技术说明；修复播放接口诊断列表编译错误；增加播放接口调试诊断信息；接入 Phoenix 播放接口选择；将 Phoenix 播放接口拆分为独立模块；补齐应用对播放模块的直接依赖；拆分原生播放接口与共享媒体模块。
- **体验优化**：统一 Native 线路优先显示文案；隔离 Phoenix 与原生接口的 CookieJar；记录 PhoenixReadApi 上游来源及签名差异；修正 Phoenix 诊断回调构造参数；补齐共享媒体模块的 CENC 样本诊断属性；将请求加密组件迁入共享媒体模块。
- **界面与体验优化**：统一调试面板 Phoenix 名称；统一诊断中的 Native 名称。
- **问题修复**：Ci: 修复 Android SDK 安装步骤并重跑接口回归；防止诊断回调异常中断自动切换。
- **下载体验优化**：隔离无感连播备用线路缓存。

---

## 红果TV正式版 1.1.37

- 下载：[HongguoTV-1.1.37.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.37/HongguoTV-1.1.37.apk)
- versionCode：2026110707
- SHA-256：09f049189c268965e41eb46573c96b98dcfd3ea8a6837f2dd206cc19d1aab604

### 本次更新
- **播放体验优化**：修正播放线路设置说明标题；修正播放线路首选项显示文案；升级河马接口验证：自动发现剧集并测试播放解析。

---

## 红果TV正式版 1.1.38

- 下载：[HongguoTV-1.1.38.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.38/HongguoTV-1.1.38.apk)
- versionCode：2026110801
- SHA-256：9d8df049fcf77b820c30063baa2cbca321fc958eec0f3ed271b6c644f1d503c2

### 本次更新
- **下载体验优化**：修复自动回退成功回调的默认参数；记录自动回退提示的首帧显示规则；修正线路回退成功回调参数；补充线路回退提示的单元测试；播放线路自动回退成功后等待首帧再提示。
- **播放体验优化**：修复播放恢复代码中的 Context 常量引用；更新播放故障恢复机制说明；完善播放故障恢复：同线路重试后双线路切换；播放失败时清理未展示的线路切换提示；播放线路切换提示延后到实际首帧；区分播放线路与内容平台；修正播放接口验证结果记录；更正播放线路说明与1.1.37验证状态。
- **操作体验优化**：修复启动时焦点默认落在四叶状态灯。
- **体验优化**：限制自动恢复仅处理媒体与网络故障；保留跨线路恢复待显示提示；修正首帧提示的 Activity 接收者引用；接口诊断请求不触发用户线路提示；清理河马平台说明；更新无感连播线路隔离与审计基准；校准1.1.37功能说明与验证记录。
- **问题修复**：完善线路恢复确认与失败回滚；修复线路首选左侧说明不显示。

---

## 红果TV正式版 1.1.39

- 下载：[HongguoTV-1.1.39.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.39/HongguoTV-1.1.39.apk)
- versionCode：2026110901
- SHA-256：ebc5aa01e5bc86542b8f625ba627b5b53a6a1ff6d101921a25643b81e7ae3708

### 本次更新
- **问题修复**：修复 P/N 自动切换与无感连播逻辑。
- **体验优化**：Align Native playback profile with Phoenix；Align Native registration device profile with Phoenix；Correct registration URL resolution assertion；Update Phoenix registration tests for aligned playback profile；Pass playback device profile into Phoenix registration URL；Align Phoenix registration device parameters with playback profile；仅在注册被服务端拒绝时暂停重注册；将 Phoenix 设备身份轮换次数对齐 Xanerix；按 Xanerix 注册身份管理机制重写 Phoenix 会话；按 Xanerix 注册协议重写 Phoenix 设备注册；Match guoapp playback query canonical encoding；Align Phoenix query and fallback handling with guoapp；Rewrite Phoenix playback flow to match guoapp。
- **播放体验优化**：修复 Phoenix P 播放入口缺失导入；完整恢复 0.0.42 Phoenix P 播放实现；将 0.0.42 Native 播放实现完整移植到 Phoenix；按可用内存阈值启用备用播放器；移除播放线路切换通知前缀。
- **下载体验优化**：延长 Gradle Wrapper 下载超时时间。

---

## 红果TV正式版 1.1.40

- 下载：[HongguoTV-1.1.40.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.40/HongguoTV-1.1.40.apk)
- versionCode：2026110902
- SHA-256：1bb87febd0c58033a1d4c0b3751ab234dfc6b2e2c61eee659ab0123799d1f552

### 本次更新
更新内容  - 新增 Phoenix 播放线路，支持双线路自动切换。 - 优化新线路播放，支持清晰度选择。 - 新增无感连播，实现集数切换时无缝衔接。 - 优化无感连播开启条件，可用内存需达到或超过 300MB。 - 新增清晰度自动选择：高清优先、兼容优先。 - 新增弹幕多种颜色自定义功能。 - 新增动态四叶草状态图标，直观显示当前接口状态。 - 优化接口自检，进入设置页面即可显示接口状态。

---

## 红果TV正式版 1.1.41

- 下载：[HongguoTV-1.1.41.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.41/HongguoTV-1.1.41.apk)
- versionCode：2026110903
- SHA-256：f67946c7e1bbd2fa320f4c3e6a6f934365767af24412a932a698b811b975e50b

### 本次更新
更新内容
- 新增 Phoenix 播放线路，支持双线路自动切换。
- 优化新线路播放，支持清晰度选择。
- 新增无感连播，实现集数切换时无缝衔接。
- 优化无感连播开启条件，可用内存需达到或超过 300MB。
- 新增清晰度自动选择：高清优先、兼容优先。
- 新增弹幕多种颜色自定义功能。
- 新增动态四叶草状态图标，直观显示当前接口状态。
- 优化接口自检，进入设置页面即可显示接口状态。

---

## 红果TV正式版 1.1.42

- 下载：[HongguoTV-1.1.42.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.42/HongguoTV-1.1.42.apk)
- versionCode：2026111101
- SHA-256：95a9520b106b5cad233032b45f320488dc5f1a7ac00d9a5249ad9c190a125718

### 本次更新
新增手机推送红果/抖音App分享链接播放

---

## 红果TV正式版 1.1.43

- 下载：[HongguoTV-1.1.43.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.43/HongguoTV-1.1.43.apk)
- versionCode：2026111102
- SHA-256：5d03b6dc82efc4194cb47a76a15cd5049d3e2b1ccee4f9e9ca2342110c4bf273

### 本次更新
优化使用体验

---

## 红果TV正式版 1.1.44

- 下载：[HongguoTV-1.1.44.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.44/HongguoTV-1.1.44.apk)
- versionCode：2026111103
- SHA-256：d6c186cb425b8e31fe428aef9d77b55ef5ba947669417a42e88fdadf8a2f985f

### 本次更新
优化使用体验

---

## 红果TV正式版 1.1.45

- 下载：[HongguoTV-1.1.45.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.45/HongguoTV-1.1.45.apk)
- versionCode：2026111104
- SHA-256：65bc346db10ed4ed7c66a4febe30253787d5686ed0d25611c94265b174721fb8

### 本次更新
修复双线路

---

## 红果TV正式版 1.1.46

- 下载：[HongguoTV-1.1.46.apk](https://github.com/xycvip/AppDownload/releases/download/hongguotv-v1.1.46/HongguoTV-1.1.46.apk)
- versionCode：2026111301
- SHA-256：889f8c9c4048860ad8486e0e4b5eff2e41dd7e1897870b8624af3b95a569981c

### 本次更新
【播放与播放器】
- 调整双线路播放优先级，优化主线路与兼容线路切换逻辑
- 优化播放设备注册及会话身份处理
- 改进播放接口异常响应时的兼容处理  【演员榜与排行榜】
- 调整排行榜页面，新增演员榜入口
- 增加剧星榜、星光榜相关页面及演员作品列表功能
- 优化排行榜页面导航、焦点和交互体验  【分享与推送播放】
- 优化抖音短剧分享链接解析
- 增强剧名识别能力，减少作者名称、营销文案和无关话题干扰
- 增加短剧详情识别，改进剧名获取及候选匹配流程
- 优化分享链接无法直接识别时的后续处理  【界面与交互】
- 优化排行榜及目录页面布局和焦点处理
- 弹幕默认显示行数调整为2行
- 优化页面操作及使用体验

---
