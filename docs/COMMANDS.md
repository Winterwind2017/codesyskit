# IDE command inventory

Generated from `system.commands` in CODESYS V3.5 SP22 Patch 2 (`recon/commands.json`).

**832 unique commands** (of 870 enumerated; duplicates share a GUID) across **90 families**.

Every row is also reachable at runtime: `codesyskit commands --filter <text>` lists them
and `codesyskit execute <name|guid>` runs one, judged from the engine log.

## Families

| family | commands | examples |
| --- | --- | --- |
| `network` | 78 | 修复POU, 修改文本, 切换网络注释状态, 删除IL行 |
| `(no token)` | 73 | Toggle child index visibility (DEBUG), 上传跟踪, 上移, 下移 |
| `visual` | 68 | Trim visual element texts, 上对齐, 下对齐, 使垂直间距相等 |
| `script` | 61 | ..., A, B, C |
| `online` | 54 | 下载, 下载源代码到连接设备上, 二进制, 从[]断开连接 |
| `cfc` | 52 | EN/ENO, R (复位), REF= (引用赋值), S (置位) |
| `frame` | 34 | 1   (Window 1), 10   (Window 10), 2   (Window 2), 3   (Window 3) |
| `ladder` | 31 | Auto Declare for Ladder..., EN, ENO, 上升沿 |
| `view` | 30 | CODESYS 视角, HMI 视角, HMI功能, 书签 |
| `sfc` | 26 | 初始步, 在...之后插入关联动作, 在...之后插入宏, 在...之后插入步 |
| `project` | 19 | 为活动应用程序生成代码, 从XML导入..., 从XML导入..., 以XML导出... |
| `CAS` | 17 | Assign Server Applications on Download, Check Device Identification, Checkout from Server..., Compare with Server |
| `recipes` | 16 | 从设备上传配方., 保存配方..., 写入配方, 加载和写入变量... |
| `textlist` | 16 | 创建全局文本列表, 创建系统文本列表, 删除语言, 导入/导出文本列表 |
| `edit` | 15 | 全选, 删除, 剪切, 在工程中查找 |
| `devicecommunication` | 14 | 从设备中删除应用程序, 删除所选设备, 发送Echo服务..., 扫描网络 |
| `file` | 13 | 保存存档..., 保存工程, 保存工程并安装到库存储库中, 关闭工程 |
| `breakpoints` | 11 | 使能断点, 新建断点..., 显示当前语句, 禁用断点 |
| `redundancy` | 11 | 交换PLC路径, 写入设置, 切换到主动, 切换到待机 |
| `text` | 11 | 将文件作为文本插入..., 展开所有折叠, 折叠所有折叠, 查看定义指南 |
| `browse` | 10 | 在经典视图中浏览交叉引用, 显示交叉引用, 显示全局交叉参考, 显示声明交叉引用 |
| `device` | 9 | 从CSV导入映射..., 导出映射到CSV..., 扫描设备..., 插入设备... |
| `libman` | 9 | 下载缺失的库..., 信任证书, 占位符..., 导出库... |
| `Composer` | 8 | 不同的参数值, 使用在线值, 扫描, 更新所有实例 |
| `project_diff` | 8 | 使用右块, 使用右线, 使用左块, 使用左线 |
| `AlarmConfig` | 7 | 导入报警, 导出报警存储至CSV文件, 导出警告, 添加信息列 |
| `bookmark` | 7 | 上一个书签, 上一个书签(活动编辑器), 下一个书签, 下一个书签(活动编辑器) |
| `object` | 7 | 实现接口..., 添加对象, 添加对象..., 添加文件夹... |
| `installation` | 6 | CODESYS 安装程序..., OPC UA信息模型存储库.., 可视元素库, 可视化样式库... |
| `coredump` | 5 | 从核心转储加载设备日志, 关闭核心转储, 创建PLC崩溃报告, 创建核心转储 |
| `refactor` | 5 | 对变量重新排序..., 更新引用引脚, 添加变量..., 清除''... |
| `csttoolbox` | 4 | 从选定内容创建新项目, 创建文件夹, 编辑项目, 进入快速插入模式 |
| `help` | 4 | CODESYS帮助, 反馈..., 帮助安装第三方软件包, 用户调查 |
| `print` | 4 | 打印..., 打印预览..., 文档..., 页面设置... |
| `staticanalysis` | 4 | 查看标准指标, 计算并导出标准指标, 运行静态分析, 运行静态分析 |
| `tabulardeclaration` | 4 | 上移, 下移, 插入, 编辑声明标题... |
| `text_editor_base` | 4 | 使能在线监控, 切换增量搜索的字段, 取消注释选定的行, 注释掉选定的行 |
| `usermgmt` | 4 | Change user, 权限..., 注销用户, 用户登录... |
| `watchlist` | 4 | 将所有的强制添加到监视列表中, 添加查看, 解除和恢复所有所选值, 解除强制并保持所有所选值 |
| `VisualManagerEditor` | 3 | 停用未使用的的可视化, 可视化标签视图, 设置颜色变量为完全不透明 |
| `VisualManagerTextlistSettings` | 3 | 删除语言, 复制语言设置, 粘贴语言设置 |
| `messages` | 3 | 下一个消息, 前一个消息, 转到源代码处 |
| `trace` | 3 | 保存跟踪..., 加载跟踪..., 导出符号跟踪配置 |
| `` | 2 | (DEBUG) Delete all hidden/transient devices, 通配符选择 |
| `AlarmInstance` | 2 | 创建, 改变报警组 |
| `gw_config_form` | 2 | 添加接口..., 添加配置设置... |
| `iec6113110` | 2 | 导入IEC-61132-10..., 导出IEC61131-10... |
| `localize` | 2 | 创建本地化模板..., 本地化工程... |
| `memory_tools` | 2 | 查看内存使用情况, 检查活动应用程序的内存 |
| `plcopenxml` | 2 | 导入 PLCopenXML..., 导出PLCopenXML... |
| `security_agent` | 2 | 加密向导, 设备安全设置 |
| `softmotion` | 2 | 使能运动控制, 禁用运动控制 |
| `tools` | 2 | 授权存储库..., 授权管理器... |
| `Clear` | 1 | 列表重新排序并清除间隙 |
| `CommunicationManager` | 1 | 导出条件 Ids |
| `Installer集成` | 1 | 安装所需的附加组件 |
| `None` | 1 | 导出安装配置... |
| `OPC UA` | 1 | 导出OPC UANodeSet |
| `PROFINET` | 1 | 设置 PROFISAFE F 源地址 |
| `Restore` | 1 | 从配方中恢复变量值 |
| `Save` | 1 | 保存当前值到配方 |
| `TCIEntryPoint0` | 1 | TCIEntryPoint0 |
| `TCIEntryPoint1` | 1 | TCIEntryPoint1 |
| `TCIEntryPoint2` | 1 | TCIEntryPoint2 |
| `TCIEntryPoint3` | 1 | TCIEntryPoint3 |
| `TCIEntryPoint4` | 1 | TCIEntryPoint4 |
| `VariableListView` | 1 | 切换到树视图 |
| `autodeclare` | 1 | 自动声明... |
| `communication` | 1 | 发布 |
| `compile` | 1 | 显示离线代码更改的细节 |
| `databreakpoints` | 1 | 新建数据断点... |
| `datasourceseditor` | 1 | 转到映射 |
| `debug` | 1 | 添加查看 |
| `devices` | 1 | 导入DBC文件... |
| `enum` | 1 | 添加文本列表支持 |
| `export` | 1 | 生成EtherCAT XML |
| `forcelist` | 1 | 监视全部强制 |
| `imagepool` | 1 | 插入图片 |
| `inputassistant` | 1 | 输入助手... |
| `manage` | 1 | 管理本地化... |
| `nwl` | 1 | 显示语言模式... |
| `parallel` | 1 | 切换并行模式 |
| `security_manager` | 1 | 安全界面 |
| `targetsettings` | 1 | 目标设置文档导出 |
| `text_list_enum` | 1 | 清除文本列表支持 |
| `toggle` | 1 | 切换本地化 |
| `var_config` | 1 | 添加所有实例路径 |
| `var_persistent` | 1 | 添加所有实例路径 |
| `visu` | 1 | 多样可视化元素 |
| `window` | 1 | 重置窗口布局 |

## Full list

| family | name | guid | tokens |
| --- | --- | --- | --- |
| `` | (DEBUG) Delete all hidden/transient devices | `4dcad734-fc5c-43c5-a2b5-596f2ff5219b` | `-` |
| `` | Toggle child index visibility (DEBUG) | `4c0128e7-9ce6-4846-8abb-36a2be3676af` | `-` |
| `` | 上传跟踪 | `9e374088-6236-44fc-b420-2597cc030bb8` | `-` |
| `` | 上移 | `e8bad280-939d-4bd4-98ea-54b8578e7c95` | `-` |
| `` | 下移 | `09b29d04-49f8-4e81-b74d-edbaf9249105` | `-` |
| `` | 下载缺失的设备描述 | `a3cb0388-da1d-40d7-8455-de494fb0e527` | `-` |
| `` | 下载跟踪 | `1781907e-cf91-424e-a5b3-8a5b34a10194` | `-` |
| `` | 中心视图到断点 | `e4a50f87-08d7-45e5-ba05-d9b0800ae85e` | `-` |
| `` | 之后添加步 | `1a10a0d9-deee-4a5b-9460-8e7b8534bd44` | `-` |
| `` | 从已选FB创建模块 | `0c5ba7cf-2156-4b7c-bd4f-e365013d6f16` | `-` |
| `` | 仿真 | `b74a8b9c-0335-4303-a2cc-27034ba12fb6` | `-` |
| `` | 停止跟踪 | `33e0e114-0372-4ae2-b97f-2049c5f7b9e6` | `-` |
| `` | 光标 | `f9eb11a8-6afb-4b0c-b1df-163281879cd7` | `-` |
| `` | 关闭子序列后添加步 | `ad75e779-432d-442f-92c5-43077c17c7d6` | `-` |
| `` | 切换断点 | `4be620f9-7ed8-4b72-96a8-aa252c4c07a5` | `-` |
| `` | 创建丢失的文本列表条目 | `3df3488f-3f58-42c1-8d92-7f920fcd6603` | `-` |
| `` | 创建宏模块 | `8ba25795-3425-47e0-97db-c52fd683749b` | `-` |
| `` | 创建扩展板块 | `c359b64c-3121-4ec9-ac63-7935f9d6be9a` | `-` |
| `` | 创建持久性管理器 | `6e9bb326-c01b-45ee-8df8-e686fe123def` | `-` |
| `` | 创建数据日志管理器 | `542f125b-ccd7-4a60-8f01-6b63e6504d84` | `-` |
| `` | 创建遗漏的全部图像池. | `f8fd87a8-01c0-43ed-9dac-7d48838cb776` | `-` |
| `` | 删除生成的对象 | `0acf1e77-4472-44ae-84ad-d348012ffd22` | `-` |
| `` | 删除自动生成的I/O | `cb199140-b2ad-4780-b313-d59fb5f087e1` | `-` |
| `` | 前往目标 | `185c9b2f-890c-4e9d-8aa2-769c5442ee8d` | `-` |
| `` | 压缩 | `83cf72a4-f49b-471d-b729-e5848575a8b3` | `-` |
| `` | 在异常处停止执行 | `63406a8b-dd43-4fb3-8f16-c270c15f5558` | `-` |
| `` | 在线列表 ... | `29a319fe-0fd4-4858-89f8-df002919ee6f` | `-` |
| `` | 在线配置模式... | `e4e9aa66-6467-45be-a112-9086f990f4bc` | `-` |
| `` | 复位触发器 | `f8dd345d-8324-432d-9243-5e4506bd20d2` | `-` |
| `` | 对所有选择模块进行签名 | `97e0dafc-9997-4dbf-ba07-932df6c9844c` | `-` |
| `` | 导出设备... | `f78aa927-46c8-46a5-8925-776cc25877ff` | `-` |
| `` | 导出设备描述文件 | `cfc96d6c-103f-441f-a6df-263f1df0fbfe` | `-` |
| `` | 将光标固定到值 | `f9ace0fc-064e-4be6-afe6-1d1720edf388` | `-` |
| `` | 将所有变量移至单独的图表中 | `fb328d82-b7c7-405f-b2ad-4bd1dfe3c8e3` | `-` |
| `` | 将所有变量移至第一个图图标中 | `1caf4463-d319-486b-bd77-d55d051bc7f6` | `-` |
| `` | 将模块程序库添加到项目中 | `d1479a9d-ba1c-4f99-ae10-924504b5d862` | `-` |
| `` | 开始跟踪 | `32f81dc9-4d2d-4059-aa2f-fa56e4a0e3ab` | `-` |
| `` | 引用模块实例 | `88da4a12-ae27-4a2c-a89a-9884427899fc` | `-` |
| `` | 拉伸 | `14b3a241-26e3-449f-95b7-c23a64508063` | `-` |
| `` | 映射I/O | `bd2b5bd3-d4a7-4106-8048-b1080bf254f2` | `-` |
| `` | 显示所有引用(调试) | `55f525eb-fa9b-402d-bbfb-47ce9394c46b` | `-` |
| `` | 显示消息视图(从状态栏) | `c68c34e5-e785-4a83-8c66-2d1ebc96b6e9` | `-` |
| `` | 显示隐藏插槽 | `71a572d0-95b0-4bd7-8e62-98e3185ba148` | `-` |
| `` | 更新模块实例 | `ec0a0269-2ad0-447c-b553-8f799aeb97e6` | `-` |
| `` | 检查所有池对象并扫描 | `bcb37658-15e5-4cf7-90cb-ca5609d41d17` | `-` |
| `` | 检查未知条目 | `981c0825-b7de-4ec2-8e82-1ae092b5c28c` | `-` |
| `` | 添加变量 | `863ff542-ae52-4596-aff3-3783f9d69685` | `-` |
| `` | 添加子模块实例 | `c503703d-87b9-4bc2-9135-687336c7e898` | `-` |
| `` | 添加注释 | `09b025b6-2bd0-4153-8f5b-affa3eda88fb` | `-` |
| `` | 添加顶层模块实例 | `aeec5feb-245f-4bc9-a5a8-bcb56d19ca8c` | `-` |
| `` | 激活断点到下一步 | `511263bb-d091-40aa-b85d-3e97d17e84b6` | `-` |
| `` | 生成,建立并登录 | `b91a3aa4-5445-480c-96c9-8e10b03378e1` | `-` |
| `` | 确认诊断 | `c9272719-e5f3-46ba-aeff-c953c48ad586` | `-` |
| `` | 确认诊断子树 | `da0d023d-78ee-440a-8afd-e5461b6dbb57` | `-` |
| `` | 禁用LogicalIO同步 | `6cd8e674-51d8-4302-a5a8-3d66f065cbfc` | `-` |
| `` | 禁用设备 | `53bb412d-8007-4439-9af9-5708da68aa48` | `-` |
| `` | 移除生成的 InstRefs | `7355c454-85ac-4055-bad1-97b67b96f942` | `-` |
| `` | 统计 | `4b20a9fa-177b-4bc6-ba10-59ef28b9a7ca` | `-` |
| `` | 自动滚动 | `16566b26-64e0-42d2-918a-fa565ec3429a` | `-` |
| `` | 自动调整 | `abaaa310-da09-42b9-8cd7-5581d0e31c5f` | `-` |
| `` | 自动调整 | `dddddddd-f3fe-404b-b680-683bf0f956f0` | `-` |
| `` | 设置引用 | `9732ea69-46ec-47a9-807e-c952d98426f6` | `-` |
| `` | 设置跳转引用 | `4df7182d-b5a8-46aa-9452-e43f8838ea3f` | `-` |
| `` | 读取PLC参数文件到配置 | `f34abcf8-4944-41fc-a57e-d9a5efc1d00e` | `-` |
| `` | 跳转到定义 | `e7f85b26-3f14-44e0-9d95-d5690bbf2658` | `-` |
| `` | 进入模块FB | `8165a51a-a9d1-488f-b918-3862a2aac4d3` | `-` |
| `` | 进入模块实例 | `fae24103-e3d8-46c8-a23e-b1464cafd019` | `-` |
| `` | 选择映射的设备 | `27a23832-a3e3-459a-9629-d7d87c2dab7f` | `-` |
| `` | 选择模块实例 | `3efc87a9-b0fb-43ff-aad3-fb71a32a781c` | `-` |
| `` | 通配符选择 | `2f1a1d38-b8d9-4b73-824c-1737e859aa65` | `-` |
| `` | 配置 | `aad586d7-8313-431d-a91c-052e5310b96f` | `-` |
| `` | 重置视图 | `296fd49a-40da-42d6-8a78-e37a440c4cc2` | `-` |
| `` | 重置顶层的文本. | `e559831b-9a4c-498d-b8f7-1a14b7bd1234` | `-` |
| `` | 隐藏可选空插槽 | `b54e8177-8d3d-4b20-ac21-dd29f8d7c016` | `-` |
| `` | 鼠标缩放 | `f0762521-cc64-46a7-8af0-1badae2ac571` | `-` |
| `AlarmConfig` | 导入报警 | `1714ccd5-eccb-4dcc-b9a5-f2619b03bb06` | `importAlarms` |
| `AlarmConfig` | 导出报警存储至CSV文件 | `38716407-76e2-4154-b993-0275057cd204` | `AlarmStorageCsvExport` |
| `AlarmConfig` | 导出警告 | `7003635c-e8d3-4184-8a1b-4442522a3f9e` | `exportAlarms` |
| `AlarmConfig` | 添加信息列 | `6676bf55-d697-4f23-98f6-9458ca36e91e` | `AddMessageColumn` |
| `AlarmConfig` | 添加锁存变量列 | `d883c5f7-2e05-4b16-b0c9-ca36f1da2b80` | `AddLatchVarColumn` |
| `AlarmConfig` | 移除信息列 | `55ff7ef1-f578-4a3b-aebe-769818f63c3f` | `RemoveMessageColumn` |
| `AlarmConfig` | 移除锁存变量列 | `b418f669-2194-4f06-a388-a4b262893cd0` | `RemoveLatchVarColumn` |
| `AlarmInstance` | 创建 | `fa3bd639-8f34-4b6b-ac68-7d86402305bd` | `ToggleCreateAlarmCommand` |
| `AlarmInstance` | 改变报警组 | `33206d5b-b4f3-4bc2-b19a-9bd3446c4bbe` | `ChangeAlarmGroup` |
| `CAS` | Assign Server Applications on Download | `81818e3b-0e99-4840-bfa4-6dd3cc4c91ab` | `assignserverbootappsondownloadenabled` |
| `CAS` | Check Device Identification | `8bcfbc76-bc7e-4629-ada3-3703d11b5c9e` | `checkdeviceidentification` |
| `CAS` | Checkout from Server... | `9b9de1de-8476-4dd5-a649-f28c4f660520` | `checkoutfromserver` |
| `CAS` | Compare with Server | `33964a9c-98ad-4c83-9271-d92f47628ed9` | `comparetoserver` |
| `CAS` | Connect Edge Gateway | `dec140d6-1ac2-4707-a34a-69f00b024300` | `connectedgegateway` |
| `CAS` | Connect Project to Server... | `d8b9d886-eeb7-4434-bdca-0f9484710293` | `connecttoserver` |
| `CAS` | Create BootAppArchive (testing only) | `11879d1b-1ef4-4f78-b5ec-6806da5c2ade` | `createbootapplicationarchive` |
| `CAS` | Delete Cached Credentials | `3145a569-79f9-4e08-954c-9fb6e1618d75` | `deletelocallystoredusercredentials` |
| `CAS` | Disable URL handler (requires admin permissions) | `9d803c94-1a32-4afe-8435-415bcbc4a280` | `disableurlhandler` |
| `CAS` | Disconnect project | `40d8a9c3-04fa-4997-8f77-8175c78ad3cb` | `disconnectproject` |
| `CAS` | Enable URL handler (requires admin permissions) | `8806e7c0-6c96-494c-8d99-1f61499d3c5d` | `enableurlhandler` |
| `CAS` | Logout | `8457ddcc-247e-427b-a408-b814e3ff921a` | `logout` |
| `CAS` | Logout from 'current server' | `6a5a9d93-3c0d-4123-b11c-5c2211806da5` | `logoutfromcurrentserver` |
| `CAS` | Select a Gateway | `69cd1837-1546-4689-aa44-f881366fce2a` | `selectgateway` |
| `CAS` | Synchronize | `b5742453-9036-4d18-ad69-ae508b4ffbec` | `synchronize` |
| `CAS` | Synchronize Remote Gateways | `b762daf0-08b2-46f0-b8ca-7ab0ba44ea2e` | `synchronizeremotegateways` |
| `CAS` | Update from Server... | `9526eae9-ca19-4cba-9971-7a22871f861e` | `updatefromserver` |
| `Clear` | 列表重新排序并清除间隙 | `e6fd1bfd-16e8-4b72-8674-cbf23a018243` | `-` |
| `CommunicationManager` | 导出条件 Ids | `0b21fe6a-6da4-48ac-8447-3d9100e60413` | `OPC UA Server,SymbolSet,Alarm Groups,ExportConditionIds` |
| `Composer` | 不同的参数值 | `43f6f72b-cf2b-4f2d-85ef-6d05e91d6e1f` | `ShowDifferingOnlineValues` |
| `Composer` | 使用在线值 | `b92ee892-f3da-4a88-9f71-a9a2cca2a387` | `UseOnlineValues` |
| `Composer` | 扫描 | `32b0eb92-ce70-43b8-83d8-1aeacd8181e2` | `ReadModules` |
| `Composer` | 更新所有实例 | `d7716e93-8620-433e-bcb4-e0e2c5fb9ed9` | `UpdateAll` |
| `Composer` | 检查模块树 | `4b18da15-770b-4a6b-b463-455e9ab67d72` | `CheckTree` |
| `Composer` | 生成 | `917acb80-e8a4-4c60-b3c5-c6289b9b9687` | `Generate` |
| `Composer` | 生成器配置... | `dd6b0770-eadf-4a04-be59-e7fbbe928da8` | `GeneratorConfig` |
| `Composer` | 获取授权信息 | `b6b3663e-ec3f-4f7a-b31f-1d88921f35b0` | `GetLicenseInfo` |
| `Installer集成` | 安装所需的附加组件 | `4a7684a8-e0f8-4b99-92a5-0cdea133bc87` | `Install Add-ons` |
| `None` | 导出安装配置... | `9bc6ecef-a7ca-49cf-9076-ea56f12344ee` | `installationconfigurationexport` |
| `OPC UA` | 导出OPC UANodeSet | `151c6053-ab75-47dc-b8f8-cb54b759c8b8` | `Node Set Export` |
| `PROFINET` | 设置 PROFISAFE F 源地址 | `94604712-e56f-4519-8450-b15918bb6979` | `SetFSourceAddress` |
| `Restore` | 从配方中恢复变量值 | `9fbe59ca-5228-4342-9118-b73cbb065ea4` | `values` |
| `Save` | 保存当前值到配方 | `88b99e55-2d0d-4385-8329-104da9403895` | `acutal,values` |
| `TCIEntryPoint0` | TCIEntryPoint0 | `a72f722e-5b29-4449-a6ea-d6280c2a2ed4` | `command` |
| `TCIEntryPoint1` | TCIEntryPoint1 | `1f74e700-bb1e-46e7-8ea1-7e57b79bc8fc` | `command` |
| `TCIEntryPoint2` | TCIEntryPoint2 | `f6c593be-2a58-4000-a0eb-ab9d9d708836` | `command` |
| `TCIEntryPoint3` | TCIEntryPoint3 | `23a896fd-d307-4fe3-9117-500f9efaddbb` | `command` |
| `TCIEntryPoint4` | TCIEntryPoint4 | `cbeb757c-ccc6-4e1b-be49-d3bf443901ed` | `command` |
| `VariableListView` | 切换到树视图 | `d15fc5a3-4cf4-4004-b76e-6f950cd9e81b` | `SwitchToTreeView` |
| `VisualManagerEditor` | 停用未使用的的可视化 | `ae0dd382-4634-442d-96bb-5af683fbabe3` | `Visualizations,DeactivateUnusedVisualizations` |
| `VisualManagerEditor` | 可视化标签视图 | `fb3a809b-309b-471b-885b-ed83bd7c525c` | `VariableList` |
| `VisualManagerEditor` | 设置颜色变量为完全不透明 | `b047c96d-79cc-4186-87db-155d942507e8` | `setcolorvariablesfullopaque` |
| `VisualManagerTextlistSettings` | 删除语言 | `dd791567-8ac4-4c9a-912e-a382320b8d7a` | `deletelanguage` |
| `VisualManagerTextlistSettings` | 复制语言设置 | `5c2f7c99-f95e-4d18-84fd-f30cc8f4a356` | `copylanguagesetting` |
| `VisualManagerTextlistSettings` | 粘贴语言设置 | `b1279d33-fc9a-41fe-872e-2abd59a51799` | `pastelanguagesetting` |
| `autodeclare` | 自动声明... | `a0d49995-418d-4935-bf03-7803e7d1ec06` | `-` |
| `bookmark` | 上一个书签 | `f08f50f2-4ba5-47c6-90df-9b7ed495e34a` | `previousglobal` |
| `bookmark` | 上一个书签(活动编辑器) | `d349ba1c-bd27-4ede-88f2-e0f7bc0a4def` | `previous` |
| `bookmark` | 下一个书签 | `8cd4adb4-ed58-4f39-b44a-e8067dbde106` | `nextglobal` |
| `bookmark` | 下一个书签(活动编辑器) | `407ec07a-080d-498b-9e03-b1e79c7a1034` | `next` |
| `bookmark` | 切换书签 | `487bb961-3672-4ece-ae9d-32afb6fc5f9a` | `toggle` |
| `bookmark` | 清除所有书签 | `f6c56795-bf5e-4973-8291-71ba66597c16` | `clearallglobal` |
| `bookmark` | 清除所有书签(活动编辑器) | `80c4e466-e5cf-47ff-8c13-05966527a04c` | `clearall` |
| `breakpoints` | 使能断点 | `54cbcd5f-8edb-4261-90c2-9d3b83758b58` | `enable` |
| `breakpoints` | 新建断点... | `48764ee6-13fc-4fbb-9d39-a0acc26fbf41` | `new` |
| `breakpoints` | 显示当前语句 | `0d232328-c966-41a2-9869-b86ed063b225` | `showcurrentstatement` |
| `breakpoints` | 禁用断点 | `79f0a788-5e37-4f60-8c12-a320b09194c1` | `enable` |
| `breakpoints` | 编辑断点... | `8de52f68-1388-4fc5-b2e1-d640c4c5a3d6` | `edit` |
| `breakpoints` | 设置下一条语句 | `d7690922-1594-4dfa-8260-8a14213cf7f2` | `setnextstatement` |
| `breakpoints` | 设置或清除断点 | `16992649-ce8c-42ab-8650-1fc941f95afe` | `toggle` |
| `breakpoints` | 跳入 | `12289edb-4f13-400c-9e9d-35aa46946c51` | `stepinto` |
| `breakpoints` | 跳出 | `417b5c5c-2bb4-4eb6-b19d-4513281bacb0` | `stepout` |
| `breakpoints` | 跳过 | `0e79e9b0-7516-456f-b201-c056a02c4876` | `stepover` |
| `breakpoints` | 运行到光标处 | `3040e1af-a3d0-444f-8905-db5643f7bfbc` | `runtocursor` |
| `browse` | 在经典视图中浏览交叉引用 | `94201411-71c8-4a93-a861-a2887db6bc1e` | `legacycrossreferences` |
| `browse` | 显示交叉引用 | `2d499d13-af93-43b4-afda-e98349935b51` | `crossreferences` |
| `browse` | 显示全局交叉参考 | `41fb3bef-9268-4671-9964-193fe5427dca` | `globalcrossreferences` |
| `browse` | 显示声明交叉引用 | `da4f9f18-e708-412d-8fb0-a8bbd6bd242f` | `declarationcrossreferences` |
| `browse` | 显示调用树 | `3f4567d6-13e3-463c-8c7c-6edfefe488a4` | `calltree` |
| `browse` | 跳转到 类型 的定义处 | `deffdeff-2ce9-4e58-9701-4925710616c0` | `gotodefinitionoftype` |
| `browse` | 转到定义 | `d19a9182-fc62-4ea5-bd01-cad58e092281` | `gotodefinition` |
| `browse` | 转到实例 | `017b821e-e365-4bb6-9585-e45ba4d33dba` | `gotoinstance` |
| `browse` | 转到实现 | `224c5075-a190-4d7c-af49-f2351e2e8b4a` | `gotoimplementation` |
| `browse` | 转到引用 | `ba061b2b-1f0a-40c8-88bf-f139afdc3191` | `gotoreference` |
| `cfc` | EN/ENO | `67e38578-22ca-42a3-a6cd-de9d32b71362` | `eneno` |
| `cfc` | R (复位) | `ae8b8369-9a02-4114-b1dd-dc5d4f5fe820` | `setreset,reset` |
| `cfc` | REF= (引用赋值) | `4c60a44c-2aa9-477d-b20e-af08a6fd1eb5` | `setreset,ref` |
| `cfc` | S (置位) | `818368cb-9be2-4fd4-b5c2-7b38820b304e` | `setreset,set` |
| `cfc` | 上移 | `780b7875-6e64-4843-8edc-8fce2808a6c5` | `moveup` |
| `cfc` | 下移 | `9ceabf91-60be-4711-a0be-ce7e75a0fd4b` | `movedown` |
| `cfc` | 从输入助手插入块 | `8a5014f3-8888-4842-8344-02726d3dddf2` | `insert,boxfrominputassitant` |
| `cfc` | 从输入助手插入带有EN/ENO的块 | `0665ceda-b7df-46bb-bdb1-e9eca57cb91c` | `insert,boxenenofrominputassitant` |
| `cfc` | 使用归属成员作为输入 | `dd8275f0-be78-4432-81d9-54cd01e71b3a` | `useattributedmemberasinput` |
| `cfc` | 准备强制运算块 | `5ea86f85-21ab-427f-b927-654b649463ad` | `prepareforce` |
| `cfc` | 创建控制点 | `af46eb34-b5d0-4226-a30a-cd4b08aad3ab` | `createcheckpoint` |
| `cfc` | 创建组 | `edc96a5c-81ef-4c64-8808-7d879543a929` | `createelementgroup` |
| `cfc` | 取反 | `6d149712-6c0a-4585-a2f4-12cd3e9f2b35` | `negate` |
| `cfc` | 取消组 | `c162f204-c7e0-4e1c-bc04-95d7aab64d09` | `ungroupelements` |
| `cfc` | 复位引脚 | `e254a5b9-46b4-4e09-95d2-1cba49fb7929` | `resetpins` |
| `cfc` | 将准备的参数值保存到当前工程中 | `59be6273-9882-4656-b832-92a1f57bbfe1` | `incurparametervalues` |
| `cfc` | 将所有对象的预处理参数保存至项目 | `904eb0a0-5cb0-45fb-b0ad-e3e84ff04cc0` | `incurparametervaluesallobjects` |
| `cfc` | 开关S/R/Ref/None | `ecdd86f5-af74-46fa-990e-2bffdc0e8f3b` | `setreset,switchtonext` |
| `cfc` | 强制功能块输入... | `730a3273-d2f8-48a7-8fab-b2ff64d83e52` | `forcevalue` |
| `cfc` | 折叠所有内联监视字段 | `1a7d20d1-686a-4049-9bc1-f514d1ab7ed5` | `expandallwatches` |
| `cfc` | 折叠所有内联监视字段 | `6941cf71-174f-416f-9123-9f3c38bec1ce` | `collapseallwatches` |
| `cfc` | 按拓扑排序 | `31a3f1e1-57d8-4c4c-8777-e78117f272df` | `order,topology` |
| `cfc` | 按照数据流排序 | `48ecdf88-05ec-4b1f-8c25-4259cbfdcd75` | `order,dataflow` |
| `cfc` | 插入有EN/ENO的块 | `52ef591b-8274-4529-b92f-a8d5185a42ab` | `insert,BoxWithEnEno` |
| `cfc` | 插入跳转 | `87e69d23-3e1c-4753-9b54-ffca17ac1f97` | `insert,jump` |
| `cfc` | 插入输入 | `4b0036ce-653c-41ef-adec-e74aa72b5f36` | `insert,input` |
| `cfc` | 插入输出 | `8e8c2f88-3999-44e8-8f9e-7b59dd637b6e` | `insert,output` |
| `cfc` | 插入运算块 | `5ba54744-a0a0-4c7a-91fb-bfc657225352` | `insert,emptybox` |
| `cfc` | 无 | `b67d035f-4f87-4e69-bcb8-ed7807df818d` | `setreset,none` |
| `cfc` | 显示执行顺序 | `a332a8e0-b119-4b72-9b6f-705014f6082b` | `activate_execution_overlay` |
| `cfc` | 显示语言模型... | `2ab34d33-e8d6-48f6-85a0-22954b4efde9` | `viewlanguagemodel` |
| `cfc` | 添加输入引脚 | `ffa7cb58-c0bc-4ac1-8d6a-6670891945b9` | `addinputpin` |
| `cfc` | 添加输出引脚 | `d308ab34-8d2b-4dfd-abf5-de7fc3da39b1` | `addoutputpin` |
| `cfc` | 清除控制点 | `4cf0815a-85e8-4a9c-aee6-fb7621c1eb83` | `clearcheckpoints` |
| `cfc` | 移除控制点 | `28e7cac5-babe-4996-af04-ea8159a8c4c3` | `removecheckpoint` |
| `cfc` | 移除未使用的引脚 | `c812f0ee-5f4e-4de8-bbea-0c620eff4a96` | `removeunusedpins` |
| `cfc` | 编辑参数... | `ec69198b-62cc-4fc8-bf25-9d9b5fe0cf5e` | `editparameters` |
| `cfc` | 编辑工作表... | `607b5a49-16bf-4948-812d-33b24ccd20ea` | `editworkingsheet` |
| `cfc` | 编辑页面尺寸... | `26d06a2d-442e-42a1-af76-0343579319cc` | `editpagesize` |
| `cfc` | 置尾 | `ce0330c5-aca3-4d2c-92d6-19bf906fa145` | `sendtoback` |
| `cfc` | 置首 | `e10d8193-fce7-4685-a814-98845abd5655` | `sendtofront` |
| `cfc` | 解锁连接 | `89b3df8c-9456-4b60-a1dc-36eb3a1ae2ff` | `unlockconnection` |
| `cfc` | 设置反馈的开始 | `2dfc6860-e72f-46c0-9764-8fa22b4f62e7` | `set_start_feedback` |
| `cfc` | 设置执行顺序... | `dcf1cb68-c372-4898-afe5-abedc50ba9c8` | `setexecutionorder` |
| `cfc` | 路由所有连接 | `08ea4856-29fd-40ad-a1dd-090070662cf3` | `routeallconnections` |
| `cfc` | 返回 | `aeffd87a-9b55-41cb-9778-b46d205cdc31` | `insert,return` |
| `cfc` | 连接所选引脚 | `8ba75516-d455-48d6-a26b-3007a11baf2b` | `connectselectedpins` |
| `cfc` | 连接标记 | `46ae2ab9-c159-427a-a903-99c241109a94` | `connectionmark` |
| `cfc` | 选择下面的所有内容 | `f367e02e-6e77-4c32-88fa-d8d91256e516` | `selecteverythingbelow` |
| `cfc` | 选择全部 | `f851aae4-d6b6-4337-a73f-19e44b67c39b` | `selectAll` |
| `cfc` | 选择连接的引脚 | `9ab88d68-4791-4f8b-92d3-d7252e4895f8` | `selectconnectedpins` |
| `cfc` | 隐藏命名空间 | `c4263ef4-9c5f-4b23-92b0-2694cdf59161` | `hide_namespaces` |
| `communication` | 发布 | `7403e5af-0dcf-424a-ba08-e76783c2ea3d` | `publish_symbol` |
| `compile` | 显示离线代码更改的细节 | `6ff9ffdb-8572-4b73-96f3-9f9404d11bcf` | `ShowCompileChangeDetails` |
| `coredump` | 从核心转储加载设备日志 | `777fa26b-dbe6-434e-a72d-00ca7ff0907f` | `loadlog` |
| `coredump` | 关闭核心转储 | `7b3bd753-4e10-4dfa-a71a-a4b2e640a5bc` | `close` |
| `coredump` | 创建PLC崩溃报告 | `c06cef7e-739c-4e19-9c3f-66792bea703b` | `create_plc_crash_report` |
| `coredump` | 创建核心转储 | `98e47539-7806-42d2-80a2-3a052944d468` | `create` |
| `coredump` | 加载核心转储 | `09378f3a-5156-4ef1-85ae-9d06b5e5a6ef` | `load` |
| `csttoolbox` | 从选定内容创建新项目 | `b3334122-912a-419f-8ac4-7b1cc423c0fc` | `csttoolboxcreateitem` |
| `csttoolbox` | 创建文件夹 | `a9a10f09-7b17-4913-ad05-40139c218506` | `csttooltoxcreatefolder` |
| `csttoolbox` | 编辑项目 | `964e0f61-db40-4f38-96de-dd33f6aa4ade` | `csttoolboxedititem` |
| `csttoolbox` | 进入快速插入模式 | `7ea5e51b-7446-42c0-bc39-3eeba915effa` | `csttoolboxquickinsert` |
| `databreakpoints` | 新建数据断点... | `a7189c5b-c8da-42c5-8e21-903286a5d471` | `new` |
| `datasourceseditor` | 转到映射 | `cb7c20d0-19b8-45f5-ae50-0f2f806efeab` | `gototypedefinition` |
| `debug` | 添加查看 | `5728f0bb-f39a-4892-a23a-5ee1b76ae095` | `addwatch` |
| `device` | 从CSV导入映射... | `6aa1fb55-612d-4295-af34-77ffd904fa44` | `importcsv` |
| `device` | 导出映射到CSV... | `e898828e-47a5-4e5c-bc0f-4008ff1999eb` | `exportcsv` |
| `device` | 扫描设备... | `73b2ca6f-8b4e-45cb-9533-eaa108aaf7f7` | `scan` |
| `device` | 插入设备... | `99c26731-71f6-42cd-8184-434991a5bbc2` | `insert` |
| `device` | 插入设备... | `3c9bacd6-cc7d-4ae7-90a6-d35fe7685028` | `plug` |
| `device` | 更新设备... | `361c88a2-559e-4893-9fc5-c2fc635dcbc4` | `replace` |
| `device` | 添加占位符 | `18dc3ab3-034f-471c-962d-b0ed59341e54` | `addplaceholder` |
| `device` | 添加设备... | `b3ffc7be-394a-4e9c-8e85-2fe445849ef6` | `add` |
| `device` | 编辑IO映射 | `778be21d-a863-415b-a19b-cb8c432980db` | `simplemapping` |
| `devicecommunication` | 从设备中删除应用程序 | `f6818f3a-4bb9-43e5-98b9-f122ee191717` | `removeapplications` |
| `devicecommunication` | 删除所选设备 | `6245bbb6-d3ff-447d-a4ac-f4fc9c2b0b64` | `deletedevice` |
| `devicecommunication` | 发送Echo服务... | `a3e5a0d0-32d6-49de-8823-2aec8e7f1a24` | `send_echo_service` |
| `devicecommunication` | 扫描网络 | `ddee7c46-285a-447d-a1f2-7957e324dea5` | `scannetwork` |
| `devicecommunication` | 按照名称扫描设备 | `35628516-e52e-47c3-a189-cb21fd417380` | `resolvename` |
| `devicecommunication` | 改变设备名称... | `a101e9ea-181f-4f34-b417-59e36089bf09` | `changedevicename` |
| `devicecommunication` | 添加网关... | `6fe816a8-5b43-48b0-9020-5061d0a97647` | `addgateway` |
| `devicecommunication` | 添加设备... | `4879aa57-2806-4e89-b881-2a9a021a0e8c` | `adddevice` |
| `devicecommunication` | 移除设备应用 | `03178cc9-c563-4066-9d26-3f374adbbae4` | `removeapplication` |
| `devicecommunication` | 编辑网关... | `284b1a83-0ed5-48ba-9b3d-12d1616d2f5d` | `editgateway` |
| `devicecommunication` | 设置激活路径 | `9f63b399-3ea1-4e38-afc2-a7b042bc29df` | `setactivepath` |
| `devicecommunication` | 通过IP扫描设置 | `7393b1f2-ee94-46ae-b58f-d93a24c2b847` | `resolveipaddress` |
| `devicecommunication` | 通过地址扫描设备 | `a7b4adcf-98fe-4f29-aacd-f23422cde222` | `resolveaddress` |
| `devicecommunication` | 配置本地网关... | `cd05dc11-af96-4815-b6bc-ae2739f9be9f` | `connectgateway` |
| `devices` | 导入DBC文件... | `b5913c86-3868-4e4e-9313-f5ff06b79ad5` | `import_dbc_network` |
| `edit` | 全选 | `1c36ca5e-e26d-4edc-9ab7-c7d87690c328` | `selectall` |
| `edit` | 删除 | `c5aaecf0-f55a-4864-871e-4584d1ccc9af` | `delete` |
| `edit` | 剪切 | `586fb001-60ca-4dd1-a2f9-f9319ee13c95` | `cut` |
| `edit` | 在工程中查找 | `bb8cc53c-9f28-46ea-a8df-0db140c2b325` | `find,project` |
| `edit` | 复制 | `e76b8e0b-9247-41e7-93d5-80fe36af9449` | `copy` |
| `edit` | 工程内替换 | `0d375192-1cd8-4207-8f2a-3640f4f2d031` | `replace,project` |
| `edit` | 恢复 | `871b29a1-9e9f-47f9-a5ce-d56c40976743` | `redo` |
| `edit` | 撤消 | `9eccaf22-3293-4165-943e-88c2c40b4a58` | `undo` |
| `edit` | 替换 | `1b03871f-4700-48c4-904f-adcaa4a5bc6d` | `replace` |
| `edit` | 查找 | `6e684418-bfb4-4ff0-ab89-385aa724bb03` | `find` |
| `edit` | 查找下一个 | `ed3f69cc-af4f-431b-9f41-9edad09e4734` | `findnext` |
| `edit` | 查找下一个(选择的) | `fee78da4-bcd3-47db-885d-286af5c6dab7` | `findnextselected` |
| `edit` | 查找前一个 | `e62ddd24-032b-4928-84ab-f4fa9fe6da02` | `findprevious` |
| `edit` | 查找前一个(选择的) | `f7e547e5-2c17-4988-af2a-4b8ba566e8ea` | `findpreviousselected` |
| `edit` | 粘贴 | `73a7678b-2707-44f6-963b-8a4b3c05a331` | `paste` |
| `enum` | 添加文本列表支持 | `592ad39b-097b-47f2-83e6-b59e8c590c3d` | `convert_to_text_list_enum` |
| `export` | 生成EtherCAT XML | `4f4611ee-4a7f-4d83-b59b-ad0469b2e32b` | `xml` |
| `file` | 保存存档... | `8184767e-1ae4-4071-a04d-a7e9d5a678f1` | `archive,save` |
| `file` | 保存工程 | `0e1415d3-e28c-46ec-93b1-10a1d470f9df` | `save` |
| `file` | 保存工程并安装到库存储库中 | `aa561b90-e851-48a8-9fed-bc7669c5e1d3` | `saveandinstall` |
| `file` | 关闭工程 | `7b7d5056-5cd3-4132-9e49-d64781bf4a7c` | `close` |
| `file` | 将工程另存为编译库... | `82d40622-dcc1-414c-ade2-2068c2c1808a` | `saveascompiledlibrary` |
| `file` | 工程信息... | `4581a3ae-8888-4afa-8c65-4db81cb66597` | `projectinfo` |
| `file` | 工程另存为... | `6d0d9cc5-67a2-46fd-9d29-fdfa326321e5` | `saveas` |
| `file` | 工程设置... | `f97dfcb1-28a0-4af5-ac78-d20e8f17249a` | `projectsettings` |
| `file` | 打开工程... | `9d09e965-6254-46fd-9c21-b27fd2e97b52` | `open` |
| `file` | 新建工程... | `142063ff-039a-46ff-afd8-16c0c4afaacd` | `new` |
| `file` | 精简项目 | `b741d3f6-484f-4c17-9fb0-762c5dc8e866` | `compact` |
| `file` | 解压存档... | `82cfec92-88b8-4c43-803d-839d2905e589` | `archive,extract` |
| `file` | 退出 | `caa0ef1f-6563-49ae-b0e0-80095fb233ef` | `exit` |
| `forcelist` | 监视全部强制 | `d2cc2ad7-fc8d-49a4-aeed-c8cf9f5a8ccf` | `watchallforces` |
| `frame` | 1   (Window 1) | `2da43148-03ab-46bc-a4df-48dcc4c838f9` | `window0` |
| `frame` | 10   (Window 10) | `b3b523d5-cc57-45a4-ac2d-d1d2d640f1d9` | `window9` |
| `frame` | 2   (Window 2) | `5888f929-8a48-465a-89ac-c30e3d3aa095` | `window1` |
| `frame` | 3   (Window 3) | `42c24446-d49a-4333-90fd-035bbc0e07ae` | `window2` |
| `frame` | 4   (Window 4) | `82c8af46-39b0-454d-a717-ca5225442809` | `window3` |
| `frame` | 5   (Window 5) | `fc7d0415-bfd8-4a33-8d27-b1b132836f09` | `window4` |
| `frame` | 6   (Window 6) | `ec945740-b20b-42c7-bb5a-5fc6850df60f` | `window5` |
| `frame` | 7   (Window 7) | `8581325c-3240-4c5e-9368-ae0b18dc6a4f` | `window6` |
| `frame` | 8   (Window 8) | `e2067782-932d-4db2-8c06-c2283edfd1ee` | `window7` |
| `frame` | 9   (Window 9) | `cfd7252f-7a73-4980-a75d-1cf80d9889f4` | `window8` |
| `frame` | 上一个子窗口 | `1be534fc-2cba-43d3-a9a6-f925d9b6fe5c` | `previouspane` |
| `frame` | 上一个编辑器 | `5df425b5-cad5-4277-9613-fec44ae43f52` | `previouseditor` |
| `frame` | 下一个窗格 | `7b061d57-120e-4897-b840-7e3251ec70a2` | `nextpane` |
| `frame` | 下一个编辑器 | `488224f9-d71a-47a6-8d7b-aa9116ab3b7a` | `nexteditor` |
| `frame` | 停靠 | `09018b75-686e-4371-bf94-a4c6939fdff5` | `dock` |
| `frame` | 全屏 | `d156c692-3203-40a4-958b-fe14bd80edad` | `togglefullscreen` |
| `frame` | 关于... | `ec181567-c559-445f-b629-77e6752d12da` | `about` |
| `frame` | 关闭所有编辑器 | `7053192d-1cfa-40ad-b4b2-6e838c362b6a` | `closealleditors` |
| `frame` | 关闭所有非活动应用程序的编辑器 | `0172e873-4b9e-407e-8707-045498e24c3d` | `closealleditorsofinactiveapplications` |
| `frame` | 关闭编辑器 | `6c40286f-cfb5-414f-b204-04a8cc91f403` | `closeeditor` |
| `frame` | 关闭除此之外的编辑器 | `e689224f-106c-4145-b788-b2f66ac66a20` | `closealleditorsbutthis` |
| `frame` | 切换第一窗格 | `edc5891d-22c6-460f-9d58-6f7d30d5f928` | `togglefirstpane` |
| `frame` | 切换第二窗格 | `a43ebcfc-17a2-40c1-82b5-0cfeec258f4e` | `togglesecondpane` |
| `frame` | 在导航器中选择对象 | `40456f7f-b524-4d0b-a554-44504113965c` | `selectobjectinnavigator` |
| `frame` | 在导航器中选择父对象 | `64f5ee05-fa53-4dd3-9f90-70b813442f4c` | `selectparentobjectinnavigator` |
| `frame` | 导入与导出选项... | `73c3e5ee-5d7e-425f-880d-04934c7cb323` | `options,import_export` |
| `frame` | 属性... | `748e63e2-68e6-4364-b7dc-8c09a4891a15` | `properties` |
| `frame` | 新建垂直序列组 | `53e779a9-4d53-4999-a7b8-e5a88a5a6b34` | `newverttabgroup` |
| `frame` | 新建水平序列组 | `6123d86d-029c-402e-8a33-fc823e57d02b` | `newhorztabgroup` |
| `frame` | 浮动 | `7fec924d-b521-4a4f-9d1a-07d23c774f33` | `float` |
| `frame` | 窗口... | `9561d563-8bf4-42f5-bcea-82dbab9f85fa` | `windows` |
| `frame` | 自动隐藏 | `51c48cf0-0e09-4533-aa10-502150eb4d9d` | `autohide` |
| `frame` | 自定义... | `98f9e1bd-125f-4590-96a9-24150e53c5bf` | `customize` |
| `frame` | 选项... | `3e80809e-1bbe-4f49-8667-74991e16fe82` | `options` |
| `gw_config_form` | 添加接口... | `4ce6d9ee-fa9f-4674-885f-0b095c6ad30c` | `add_main_net` |
| `gw_config_form` | 添加配置设置... | `3dcff463-8241-4096-9a2c-4447417832e9` | `add_setting` |
| `help` | CODESYS帮助 | `c77b06ec-960b-41b7-b53a-66fd0b835665` | `contents` |
| `help` | 反馈... | `3ad5e516-3892-4c78-8d6d-c5a6a9240859` | `usersurvey,feedback` |
| `help` | 帮助安装第三方软件包 | `5afc9df7-ca9c-48e8-b580-b62fc3321ce8` | `additional` |
| `help` | 用户调查 | `d783654d-7cdb-45e5-9416-565b4c4b3b35` | `usersurvey` |
| `iec6113110` | 导入IEC-61132-10... | `eb1e1cad-288f-4f19-8ad1-9e006f0154e8` | `import` |
| `iec6113110` | 导出IEC61131-10... | `3d32bd12-9ebb-4153-94c6-415c4537dfb4` | `export` |
| `imagepool` | 插入图片 | `19a6b56e-424a-40bf-a954-0e3da6ae917e` | `insertimage` |
| `inputassistant` | 输入助手... | `1c74f00c-6a9b-47b9-99be-e74b1d767545` | `-` |
| `installation` | CODESYS 安装程序... | `7d20f8e2-a557-47ff-abab-70d417887ac3` | `packagemanager` |
| `installation` | OPC UA信息模型存储库.. | `e50b347d-4ec8-470c-8257-e4f13227569c` | `informationmodelrepository` |
| `installation` | 可视元素库 | `3841219e-e84b-4c48-bc1d-1384b84a4dc6` | `visualelementrepository` |
| `installation` | 可视化样式库... | `90fc44e5-75a1-474f-9385-e829baab7b53` | `visualizationstylesrepository` |
| `installation` | 库存储... | `c748310a-0784-46c2-8475-0439c495869b` | `libraryrepository` |
| `installation` | 设备存储库... | `9790ad8b-5ecd-4840-8cce-be68aaf1d5e9` | `devicerepository` |
| `ladder` | Auto Declare for Ladder... | `c89df5c4-a431-4d10-9dc4-ae705685e78f` | `autodeclare` |
| `ladder` | EN | `81a1ac72-15bb-4172-8841-778300e73a2b` | `modify,toggleen` |
| `ladder` | ENO | `056ffe1d-0155-4bd3-be79-ba1324a37145` | `modify,toggleeno` |
| `ladder` | 上升沿 | `18921635-ef44-448d-ae86-818e5bfdc9b6` | `modify,toggleedgerising` |
| `ladder` | 下降沿 | `dce67817-6078-4ce7-b57c-cbd8bc9100c7` | `modify,toggleedgefalling` |
| `ladder` | 关闭平行分支 | `98361014-f6e0-4a1f-84f7-0dae5abaa0ee` | `modify,closebranch` |
| `ladder` | 切换插入有或没有 EN/ENO的新块 | `c43b24ad-1da3-4e82-a3df-d6774b7e1a22` | `insertblockswithenenotogglecommand` |
| `ladder` | 否定 | `12043cee-b272-48a7-bb63-21d4df9e3e0a` | `modify,setnegation` |
| `ladder` | 增加输入引脚 | `0148723d-9411-4536-96b7-b5200cef41a2` | `insert,addinputpin` |
| `ladder` | 复位 | `7970e6d1-5e4b-431e-814e-148b35a7ad7b` | `modify,togglestoragereset` |
| `ladder` | 已作评论 | `e918a4a3-6f30-4959-abf6-12e6409132d3` | `modify,toggleoutcommented` |
| `ladder` | 开关置位/复位修改器 | `6f4f8870-625e-4cc2-8869-99f178e660a9` | `modify,switchstorage` |
| `ladder` | 开关边缘检测 | `e42ee942-525e-4ff0-b2dd-2242e68d41ef` | `modify,switchedgedetection` |
| `ladder` | 打开并行分支 | `9f910a89-bc41-40a9-b0b7-027a96800f7d` | `modify,openbranch` |
| `ladder` | 插入 ST块 | `a853bd84-48f5-4e14-bf9e-8a9cda277bbd` | `insert,structuredtextblock` |
| `ladder` | 插入 块 | `ab199a90-ba8f-4aa9-bc70-77d4cb8388cb` | `insert,block` |
| `ladder` | 插入 线圈 | `49f35960-e385-4606-8697-5e5cac11778f` | `insert,coil` |
| `ladder` | 插入 网络 | `65e894b7-f128-4736-93cb-d9c24e5712ab` | `insert,network` |
| `ladder` | 插入 触点 | `ce9b8bd1-189c-42fa-9ccf-7157036ea2e2` | `insert,contact` |
| `ladder` | 插入 跳转 | `c7a37c40-f284-4fc8-9323-8cf4b99b0ee9` | `insert,jump` |
| `ladder` | 插入 输入 | `f1ed1127-d15c-4bc8-8e9e-0b3312837116` | `insert,invariable` |
| `ladder` | 插入 输出 | `016a0fd2-eb81-4071-acd6-ac1165847345` | `insert,outvariable` |
| `ladder` | 插入 返回 | `5f269ab4-43a8-4bc6-bf8c-729abbf19a18` | `insert,return` |
| `ladder` | 无边缘检测 | `b526f3d2-4226-442d-8a99-09ca0ff8a2e3` | `modify,edgenone` |
| `ladder` | 更新参数 | `992fc6f5-ecc1-4fbe-910f-6ddd3e7999c8` | `modify,updateparameters` |
| `ladder` | 没有 | `94c889b8-63aa-42f4-80a9-5d812c3005a1` | `modify,storagenone` |
| `ladder` | 移除未使用的插针 | `0e7bf2b1-7831-4d3b-87bc-66e1c8dbaa49` | `modify,Removeunusedfbcallparameters` |
| `ladder` | 设置 | `2a65e2ed-4dce-4954-a7b0-0033e9ac9fed` | `modify,togglestorageset` |
| `ladder` | 设置输出连接 | `5595b245-a4eb-451f-966f-a4e56a823ba2` | `modify,setoutputconnection` |
| `ladder` | 转换为新的梯形图 | `39487d94-5276-477d-9866-fc22dab08063` | `legacyconversion` |
| `ladder` | 通过变量链接 | `ffdd8aa4-7bba-4b8b-93dc-3648d99e2d10` | `modify,linkviavariable` |
| `libman` | 下载缺失的库... | `0ae00f1a-9483-402b-96bd-54b568fd2520` | `opendownloadmissinglibrariesdialog` |
| `libman` | 信任证书 | `8eaf44e7-f2ac-4cbe-bf6c-3fd93388f9d8` | `trustcertificate` |
| `libman` | 占位符... | `c8d936b4-32b6-47ca-bafd-ead29338deb4` | `placeholders` |
| `libman` | 导出库... | `4ff87f84-9524-45e9-a19f-a6b3c55c59fa` | `export` |
| `libman` | 尝试重新加载库 | `73d6ea58-232c-47dd-ad9e-7f608518ec27` | `reload` |
| `libman` | 属性... | `074427ab-e05a-4680-92c4-86b069ae881c` | `properties` |
| `libman` | 库参数... | `44444444-53d1-4baa-8ad2-b428e2ce831b` | `openparameterdialog` |
| `libman` | 添加库... | `4f2952df-747f-4c91-9f8d-46f87680faa2` | `add` |
| `libman` | 添加没有占位符解析的库... | `2271ea68-3562-4f41-bd93-557fd37592d8` | `addwithoutplaceholder` |
| `localize` | 创建本地化模板... | `a8e7e21b-fb2b-41fb-954e-f52a8347971a` | `createfile` |
| `localize` | 本地化工程... | `05446ccf-ca2d-4812-8901-12c42b85b7f9` | `project` |
| `manage` | 管理本地化... | `7c7cff1c-730f-4273-8cd2-ff3fe8d1d6c1` | `localization` |
| `memory_tools` | 查看内存使用情况 | `16139e35-ad35-4f9d-82f3-aac94786b446` | `view_memory_usage` |
| `memory_tools` | 检查活动应用程序的内存 | `3372a6bc-1a2e-4c87-b229-e2e28c0d2818` | `check_active_application` |
| `messages` | 下一个消息 | `126cbd4c-05da-4ac8-94e8-8b6f8bff23a7` | `next` |
| `messages` | 前一个消息 | `213cee13-e457-468b-9313-4279fc8e7134` | `prev` |
| `messages` | 转到源代码处 | `15d4c1ab-a1f4-44f4-bb71-a46b8b7355db` | `gotosourcepos` |
| `network` | 修复POU | `c88fce6e-76b5-41d3-982d-07e7aeabfff5` | `repair` |
| `network` | 修改文本 | `1675e063-0eb0-400c-9d13-eb22410abcc3` | `changetext` |
| `network` | 切换网络注释状态 | `147c903a-e420-40b4-9146-8a8b043e907e` | `togglenetworkoutcomment` |
| `network` | 删除IL行 | `ed36be20-2e35-46de-a1e9-939c104be5b5` | `deleteilline` |
| `network` | 删除未使用的FB调用参数 | `8ee67f5c-1758-405c-b94c-60b2577d2364` | `removeunusedfbparams` |
| `network` | 取反 | `f749f995-845e-440c-985b-d5d96480aec2` | `negate` |
| `network` | 在上面插入分支 | `7906b723-7ca2-4353-85ca-ecd91011b1db` | `insertbranchabove` |
| `network` | 在下方插入 IL 行 | `e0a53b0f-161c-4119-93d8-ffbeec57ee63` | `insertilline` |
| `network` | 在下面插入分支 | `d9f255d2-cd6f-4fc5-b720-d780965f1a91` | `insertbranchbelow` |
| `network` | 插入ADD功能块 | `8d411c80-2911-41e8-ae58-f57ab45b3cce` | `insertcustombox0` |
| `network` | 插入CTD功能块 | `00b6ddb3-c26d-4034-a42c-6fe999305614` | `insertcustombox13` |
| `network` | 插入CTUD功能块 | `18c9ff01-8217-498f-be41-130608f3711e` | `insertcustombox14` |
| `network` | 插入CTU功能块 | `b4b8fad8-b5fa-4899-a513-fb9459b60bc2` | `insertcustombox12` |
| `network` | 插入CustomBox20功能块 | `fa03ba14-0b13-4df5-b5a5-aab8c45d165b` | `insertcustombox20` |
| `network` | 插入CustomBox21功能块 | `2c5bb3fe-b457-4c00-9b46-80c1542ca4ae` | `insertcustombox21` |
| `network` | 插入CustomBox22功能块 | `136b3fae-c2b5-470a-9438-3ffdc341da61` | `insertcustombox22` |
| `network` | 插入CustomBox23功能块 | `13b4c840-3b4f-4ddc-aaf7-c12c02860901` | `insertcustombox23` |
| `network` | 插入CustomBox24功能块 | `59c4d9d8-687d-42c0-ad7c-b8cc23bb9184` | `insertcustombox24` |
| `network` | 插入CustomBox25功能块 | `903b5b63-be4a-4653-b6e5-5bb1b3091eba` | `insertcustombox25` |
| `network` | 插入CustomBox26功能块 | `f777d452-8ff8-4aba-b4b0-cbc4a27fb72b` | `insertcustombox26` |
| `network` | 插入CustomBox27功能块 | `ca9f10e2-c53d-40d3-a92c-6e2f6e077b6d` | `insertcustombox27` |
| `network` | 插入CustomBox28功能块 | `a86fc6e8-0b02-4644-938b-d30ffd4a1657` | `insertcustombox28` |
| `network` | 插入CustomBox29功能块 | `3d0fd931-0da6-4198-9ba9-c9259d483f5e` | `insertcustombox29` |
| `network` | 插入CustomBox30功能块 | `db016884-1ba9-418c-98a5-6b49d9f06f6d` | `insertcustombox30` |
| `network` | 插入CustomBox31功能块 | `ab2e1fdd-efcd-44e3-becc-a781eeb4fd06` | `insertcustombox31` |
| `network` | 插入DIV功能块 | `ebad8acf-6fe7-4255-8db6-d01fe7459583` | `insertcustombox3` |
| `network` | 插入EQ功能块 | `8d0e714d-8f1f-408d-8cde-738e23699403` | `insertcustombox6` |
| `network` | 插入F_TRIG功能块 | `9e917516-ca6b-499b-83dd-5b3f82a09ae4` | `insertcustombox18` |
| `network` | 插入GE功能块 | `b9678884-1ee9-4179-adcb-f6d501330f73` | `insertcustombox7` |
| `network` | 插入GT功能块 | `95bac5f2-356c-4d79-8e6a-b72b6962cbd1` | `insertcustombox8` |
| `network` | 插入LE功能块 | `a49bd0ff-9522-4ea3-b9dc-ee263bc53822` | `insertcustombox5` |
| `network` | 插入LT功能块 | `1344c07c-4910-4b89-aacd-2be569a5a21f` | `insertcustombox4` |
| `network` | 插入MUL功能块 | `a7bd4d8e-9307-4ab3-a391-8516f3c33989` | `insertcustombox2` |
| `network` | 插入NE功能块 | `d5f6ceb4-e426-4d77-9f84-26ecbf415139` | `insertcustombox9` |
| `network` | 插入RS功能块 | `acd2ef91-4eb2-4130-b350-0556dffc8438` | `insertcustombox11` |
| `network` | 插入R_TRIG功能块 | `e5eb885d-1461-45c3-84bb-cd73e5cacafb` | `insertcustombox19` |
| `network` | 插入SR功能块 | `06e97d7f-15d7-4d95-a80c-da4479909d1e` | `insertcustombox10` |
| `network` | 插入SUB功能块 | `7c44f816-1be6-4338-a1c7-08bc2d5ef85e` | `insertcustombox1` |
| `network` | 插入TOF功能块 | `ee6c0373-e4de-4b29-b7db-b5f5585f5282` | `insertcustombox16` |
| `network` | 插入TON功能块 | `73f6fd46-20c7-4e90-b578-2115eb66740e` | `insertcustombox15` |
| `network` | 插入TP功能块 | `79cdbf56-bb69-4c8c-a5cd-7fbeb0f25505` | `insertcustombox17` |
| `network` | 插入串联右触点 | `8c389d15-902b-4694-825e-1eb9ec36a1a0` | `insertcontactright` |
| `network` | 插入分支 | `d56fefd5-f979-4f09-8d4e-51f1b6ecb70a` | `insertbranch` |
| `network` | 插入取反并联触点(下方) | `6429bc1b-164b-48ae-adc1-c41d837d5dbf` | `insertnegatedcontactparallelbelow` |
| `network` | 插入取反触点 | `3aed1635-6d8a-4d26-b062-256e61aaf943` | `insertnegatedcontact` |
| `network` | 插入复位线圈  | `a8c3e6b3-3a14-4a9b-a3ea-f47ae446c824` | `insertresetcoil` |
| `network` | 插入带EN/ENO的运算块 | `fa85edd6-a520-4f44-8427-0ed1d370952b` | `insertboxeneno` |
| `network` | 插入带有EN/ENO的功能块 | `3e1a1cde-f53d-4761-a144-aeb0d3089786` | `insertemptyboxeneno` |
| `network` | 插入平行块(下方) | `01f3425e-f0d3-4f45-be69-1228a9f2219a` | `insertboxparallel` |
| `network` | 插入并联触点(上方) | `57f76100-3afa-4631-8d4c-244c02d4eed2` | `insertcontactparallel` |
| `network` | 插入并联触点(向下) | `df2a16c4-c74a-42d9-931c-2a009269c353` | `insertcontactparallelbelow` |
| `network` | 插入执行块 | `133c60c9-905c-48d2-a19f-e99a38954ba9` | `insertexecutebox` |
| `network` | 插入标号 | `e37fc81a-2694-408e-aea7-95a6440346da` | `insertlabel` |
| `network` | 插入空运算块 | `5ba28864-e061-472b-86eb-6e056f990f09` | `insertemptybox` |
| `network` | 插入线圈 | `8049e5bc-5777-440a-991a-ceb553ee83e5` | `insertcoil` |
| `network` | 插入网络 | `30e83ee9-fc64-4a97-894a-c861b60334d1` | `insertnetwork` |
| `network` | 插入网络(在下方) | `31d4a564-01c1-4c05-b3c5-1855409261a0` | `insertnetworkbelow` |
| `network` | 插入置位线圈  | `e9d08357-25be-4b20-a312-198f879462b6` | `insertsetcoil` |
| `network` | 插入触点 | `0f4655b0-906c-4c58-8c20-47417af9a4a4` | `insertcontact` |
| `network` | 插入跳转 | `075b228e-f28a-4cb0-8d71-818e86cb9213` | `insertjump` |
| `network` | 插入转换操作符 | `e73ed671-b674-4513-8b07-2ec380ab02b9` | `insertconversionbox` |
| `network` | 插入输入 | `971eeac5-e8e6-45ae-8c70-1c657e4ef38b` | `insertinput` |
| `network` | 插入输出 | `03d27e8b-f285-4463-a986-f5e9b262338d` | `insertassign` |
| `network` | 插入运算块 | `1a674948-25a4-4420-8669-3660b1b9b51d` | `insertbox` |
| `network` | 插入返回 | `855887f9-51c7-4517-a9e1-c844e9dc040f` | `insertreturn` |
| `network` | 显示为功能块图 | `13e3c3bf-8a66-4bf3-afde-69e6a3b09c53` | `viewasfbd` |
| `network` | 显示为指令表 | `f2d9d994-7393-43c4-9283-538c8f219761` | `viewasil` |
| `network` | 显示为梯形图逻辑 | `e3245d0e-49bc-4272-9d6a-a49c7c65fbd9` | `viewasladder` |
| `network` | 更新参数 | `e52c8a1c-6cd3-4215-a65c-3ca0b0fcf8dc` | `updatefbparams` |
| `network` | 添加/删除 EN/ENO | `c149bb3a-494f-48fa-a3bb-0de28140fbe8` | `adden` |
| `network` | 粘贴到上方 | `60574203-d998-4709-8af5-996bb8133f65` | `pasteabove` |
| `network` | 粘贴到下方 | `1b56dd12-8853-4946-bfb2-acd130c29e79` | `pastebelow` |
| `network` | 粘贴在右侧(之后) | `182eeb9a-1b55-4e6d-b1d7-bc7319d0f196` | `pasteright` |
| `network` | 置位/复位 | `eb93457f-ca4e-4454-9227-26fba297a10d` | `set` |
| `network` | 设置分支开始/结束点 | `8559f03a-8929-4ce9-8c8e-0289960b9342` | `setbranchpoint` |
| `network` | 设置输出连接 | `97ff5a07-94e9-4e01-b9f1-b40929fb83ad` | `setoutput` |
| `network` | 转到... | `cfe30982-951a-4e58-a2ce-14a8e547cb60` | `goto` |
| `network` | 边缘检测 | `bbefd975-2bce-4e70-959f-8ff2d29e9d96` | `trigger` |
| `nwl` | 显示语言模式... | `7391dd33-08d9-4644-94bd-bd9895bcf41d` | `viewlanguagemodel` |
| `object` | 实现接口... | `33a0dd76-f43a-4e2c-bbc6-113810643a0a` | `implementinterfaces` |
| `object` | 添加对象 | `a960311a-5fd0-4db6-8368-bd1caf82e967` | `addlist` |
| `object` | 添加对象... | `c03a1a6f-d66e-4bca-8866-e281f901cce6` | `add` |
| `object` | 添加文件夹... | `10de7ed7-34fe-4ac3-97d1-97ed66e7874e` | `addfolder` |
| `object` | 用...编辑对象 | `27d7527d-cfe3-485a-83b4-fa64b7b7a29e` | `editwith` |
| `object` | 编辑对象 | `42f6acb9-bd6e-42e7-94bb-6e2a03973b83` | `edit` |
| `object` | 编辑对象(离线) | `72a2f7c2-a650-4feb-ada4-a8a9beff1291` | `editoffline` |
| `online` | 下载 | `cc9ad1e5-fe78-4dc6-a4be-b1991bf068ea` | `downloadactiveapp` |
| `online` | 下载源代码到连接设备上 | `42545c70-5715-41de-b98d-cc3fec79f536` | `sourcedownload` |
| `online` | 二进制 | `5f5ed4ad-72e1-4d7c-b638-2dc19ecfa5bc` | `display,bin` |
| `online` | 从[]断开连接 | `99ff1305-c130-43dc-9fe6-ac5ecb436359` | `disconnectDevice` |
| `online` | 从设备上删除应用程序 | `ec0de984-12e7-462c-b2f4-1dd7c5ac7537` | `removeapplicationfromdevice` |
| `online` | 仿真 | `515e05ec-aece-47d7-98a6-5c582ba392fb` | `simulate_active_app` |
| `online` | 停止 | `fd2ae898-05a5-478c-9b31-20c0c112cab1` | `stopactiveapp` |
| `online` | 停止 | `d8ee4c28-e09b-4ace-ad55-600a8a3c906f` | `stopMultiapp` |
| `online` | 写入值 | `975591c7-7bc5-46ee-9b49-2940d6c13003` | `writeactiveapplication` |
| `online` | 写入所有值[所选应用] | `e0e61d96-c56d-4129-a041-8a9768426da7` | `writeselectedaplication` |
| `online` | 冷复位 | `c25ccb8f-a743-4cbb-9ff9-697838f49e62` | `resetcoldactiveapp` |
| `online` | 切换流控制模式 | `3e908575-08b7-4d45-a7e0-3a74a456c403` | `flowcontrolactiveapp` |
| `online` | 创建启动应用 | `cf46872e-7cf6-484e-acee-f8b9da763449` | `createbootproject` |
| `online` | 删除设备用户... | `81fc1dbd-081a-4027-ae70-182c55192798` | `removeonlineuser` |
| `online` | 十六进制 | `b8b0b06c-daf4-4fa8-9ec2-5826bd8e15c6` | `display,hex` |
| `online` | 十进制 | `6a2e1650-7459-4a0f-8e38-45ee2e80cd95` | `display,dec` |
| `online` | 单循环 | `285207b7-3503-4338-9c8d-b73c42d99ee3` | `singlecycleactiveapp` |
| `online` | 可操作 | `12434183-b7b6-4e9b-b754-81e2c13b2dd2` | `modeoperational` |
| `online` | 启动 | `b534bc77-e731-47a3-8a5e-93c57ed3e2a2` | `startactiveapp` |
| `online` | 启动 | `a8c25d44-4b83-4d05-8bcb-574e64eae4a1` | `startMultiapp` |
| `online` | 在线修改 | `f6b049e7-6c27-4736-9a45-4cc93c3e8c9d` | `onlinechangeactiveapp` |
| `online` | 在线修改 | `c6fccd24-b0db-4eab-a4b4-c9068340fac2` | `onlinechangeselectedapp` |
| `online` | 复位原点 | `ecc6fbeb-d37f-4171-887b-c07635bb6302` | `resetoriginactiveapp` |
| `online` | 复位原点设备[<无>] | `ec20a2f0-fa6f-488d-8b1b-3fe5fafac6b5` | `resetorigindevice` |
| `online` | 多重下载... | `fe09b175-5f71-413a-b5ed-253520184b64` | `multidownload` |
| `online` | 对全部在线应用强制值 | `4344c8cf-1db3-4bf8-a609-6ac6f7c6aeaa` | `forcevalues` |
| `online` | 对所有在线应用中写入值 | `dcea4a16-b0ea-476b-9e44-1eb7569ca360` | `writevalues` |
| `online` | 对所有在线应用中释放全部强制变量 | `311e81c3-c31a-48f9-b48b-0f6b6ea99713` | `unforcevalues` |
| `online` | 已锁定 | `c39db5b0-9e3e-463c-9fbe-ea760895a195` | `modelocked` |
| `online` | 强制值 | `dcda7402-d805-460d-ab87-48c4a3d31c37` | `forceactiveaplication` |
| `online` | 强制所有值[所选应用] | `92bd0446-3916-48cc-a50b-9e445ea4f21d` | `forceselectedaplication` |
| `online` | 打开日志页面... | `d0b4ff00-397f-48ac-82b6-2c2fd4b63579` | `open_logger_page` |
| `online` | 改变设备用户密码... | `b2d833cc-c429-4305-8a62-4effeea604e5` | `changepasswordonlineuser` |
| `online` | 文件上传 | `b099ed07-d6d3-4e2b-aed2-bf15b59c2f35` | `fileUpload` |
| `online` | 文件下载 | `ede62c94-9e06-4d0e-b713-01c9c66351eb` | `fileDownload` |
| `online` | 注销当前在线用户 | `ab1f8435-ce2e-4a75-af9e-26e3dfbd9e2c` | `logoffuser` |
| `online` | 添加设备用户... | `0de2be1f-b649-4b00-a3e9-aa1ac6209806` | `addonlineuser` |
| `online` | 源代码上传... | `5637cd44-cb3d-4f7c-ba9a-80e81482cd7b` | `sourceupload` |
| `online` | 源代码下载... | `9904594c-7a74-4da7-9efb-1918cad98b3f` | `sourcedownloadex` |
| `online` | 热复位 | `d887b9d2-d1ed-4dd9-9aba-dd796ec80b4b` | `resetwarmactiveapp` |
| `online` | 登录 | `c7a2dcea-d175-45b1-a85b-4d589bcdbcbe` | `loginactiveapp` |
| `online` | 登录 | `d796bf41-64f2-400d-bff7-6ac496ba2ffc` | `loginmultiapp` |
| `online` | 眨眼 | `b5b39990-da62-4568-9c64-d27a0c89680f` | `wink` |
| `online` | 自动选择任务 | `5571fe23-fea9-40af-9c96-896b038cc42e` | `flowcontrol_autoselecttask` |
| `online` | 调试 | `f1957746-e8f9-43d4-91f0-5edd7c57e38e` | `modedebug` |
| `online` | 连接到[] | `f112e292-5944-49c0-bf7f-e67658573eb9` | `connectDevice` |
| `online` | 退出 | `ad6955d2-2713-4828-9d6c-1c0cf20abdbe` | `logoutMultiapp` |
| `online` | 退出 | `87cf633b-c70d-4e11-b40a-61bd7008fc78` | `logoutactiveapp` |
| `online` | 选择活跃应用 | `1389e61c-be22-4df5-a5ce-9dc3e72421de` | `activeapplicationselector` |
| `online` | 选择该任务 | `92006760-db8c-4c05-ad5b-5be5f3497fa9` | `flowcontrol_selectthistask` |
| `online` | 释放值 | `e2427937-56d2-4699-a2e8-1007d9620ce4` | `unforceactiveapplication` |
| `online` | 释放强制列表 | `e7ee1ac1-2e71-4465-aa6b-3a808cd4d78d` | `releaseforcelistactiveapp` |
| `online` | 释放所有值[所选应用] | `fcd3d68c-509a-4c36-8925-d9422c68c437` | `unforceselectedaplication` |
| `online` | 重命名安全在线设备 | `d7ddca02-efaf-461f-8f9a-2239e4fa955e` | `renamesafetydevice` |
| `parallel` | 切换并行模式 | `305efbbe-d6bb-4e36-a849-aa2bad95d840` | `togglemode` |
| `plcopenxml` | 导入 PLCopenXML... | `9d207f52-78c1-4325-9e6a-1ba7cef5c42a` | `import` |
| `plcopenxml` | 导出PLCopenXML... | `b1550f09-29a6-4547-b460-f5619f66b82c` | `export` |
| `print` | 打印... | `7d2665c9-3f4a-4df1-a514-899fb70df440` | `print` |
| `print` | 打印预览... | `4dae020b-79a4-4cde-af3d-0fd1d276e887` | `printpreview` |
| `print` | 文档... | `06af8574-32ba-4ef2-a9fa-da024e0a9311` | `document` |
| `print` | 页面设置... | `85e0c017-3844-4550-9668-09cc4baf5611` | `pagesetup` |
| `project` | 为活动应用程序生成代码 | `331bbd71-97ed-4035-99a4-f64c3b78c698` | `generatecodeactiveappinlib` |
| `project` | 从XML导入... | `97f08523-ff6e-4c15-a0c3-c0084fc5fe55` | `import` |
| `project` | 从XML导入... | `10d76368-2418-4935-b52e-4eea72cedbe8` | `import2` |
| `project` | 以XML导出... | `2b5ca59b-ba1d-457d-8f49-0016a3f0e4d7` | `export` |
| `project` | 工程环境... | `a19fda3a-9040-47ba-a191-9f80a46388a6` | `checkavailableversions` |
| `project` | 提交接受的更改 | `11d3f774-3adc-40ff-aa18-b08c3e43d6cc` | `commit_accepted_changes` |
| `project` | 检查库兼容性 | `5b1db5f4-dc0d-4484-aeea-8c41e9b26a6c` | `checklibrarycompatibility` |
| `project` | 检查所有应用对象 | `f165bf3d-e77a-4ab8-b1bd-3b6aa9233459` | `checkallapplicationobjects` |
| `project` | 检查所有池对象 | `b2948d00-e68d-4a5e-a0f2-fa9b53753969` | `checkall` |
| `project` | 比较... | `2aca1cfd-c5b0-420f-904e-96ee3754d8f4` | `compare` |
| `project` | 清除 | `83524479-d23b-4e4c-96f4-3e89898e7277` | `cleanactiveapp` |
| `project` | 清除全部 | `024a0dc9-987d-42be-add4-5775c60d128a` | `cleanall` |
| `project` | 生成hex文件 | `a5283c89-09b8-4e4b-a920-cc80f1f2adb8` | `generatehexfileactiveapp` |
| `project` | 生成代码 | `095eb048-7e69-4a49-8c7c-3b3efb494bc5` | `generatecodeactiveapp` |
| `project` | 生成反汇编文件 | `b27f0b92-83ec-43a4-b7ea-ad705ba57c21` | `generatedisassemblyactiveapp` |
| `project` | 生成运行时系统文件... | `5ec8443b-9818-42dd-a488-c56ceaa16835` | `generateextlibm4` |
| `project` | 编译 | `a0da4287-64ed-459e-81f0-98ab3667a58f` | `buildactiveapp` |
| `project` | 设置激活的应用 | `7e8c3a96-bbf1-441a-b6a2-aa0a08954a76` | `setactiveappl` |
| `project` | 重新编译 | `50dc8f97-9e21-4b15-a504-ea2549ab61e0` | `rebuildactiveapp` |
| `project_diff` | 使用右块 | `0b271de3-7b2f-4b95-bf51-9d3371bf18ae` | `merge_use_right_block` |
| `project_diff` | 使用右线 | `e6ebe2f4-2a33-4ff8-8fb8-278b081ad5c1` | `merge_use_right` |
| `project_diff` | 使用左块 | `ef9c68ad-c6be-462f-ae43-8d4f42a601b6` | `merge_use_left_block` |
| `project_diff` | 使用左线 | `87c1e27e-e098-470a-a100-8dd8fc28a3f3` | `merge_use_left` |
| `project_diff` | 先用右块后用左块 | `7904315e-1408-4411-a230-1924d3222cfe` | `merge_use_right_before_left_block` |
| `project_diff` | 先用左块后用右块 | `fd775e4d-84b2-4cba-b84d-5410fb85a70d` | `merge_use_left_before_right_block` |
| `project_diff` | 切换第三个合并视图 | `bc552c28-d901-4099-8da0-85986b92f6ec` | `toggle_three_way_merge_view` |
| `project_diff` | 反对更改 | `cca37f67-1d64-473f-b86c-a13f0419688c` | `toggle_oppose_changes` |
| `recipes` | 从设备上传配方. | `d64adc74-f199-4eb8-b126-c4d453c7d673` | `uploadrecipesfromdevice` |
| `recipes` | 保存配方... | `11513c0b-4303-46ac-aa82-4d1fc0e6423a` | `saverecipe` |
| `recipes` | 写入配方 | `2c0ea133-3bf5-459c-a209-b227ea2d0675` | `writerecipe` |
| `recipes` | 加载和写入变量... | `8daee6ac-3dff-452d-9601-c8f369702979` | `loadwriterecipe` |
| `recipes` | 加载配方... | `6cc1e0eb-87fc-4b01-a7b5-504b10ba4145` | `loadrecipe` |
| `recipes` | 插入变量 | `f3b0f291-8fb5-4790-b008-5fbaaf7049eb` | `insertvariable` |
| `recipes` | 更新结构变量 | `714fa2c5-b677-45b2-85d8-3144aba5d531` | `updatestructuredvariables` |
| `recipes` | 添加到配方定义. | `381acf35-b8ec-4fae-9cb7-b2346d0cb042` | `addvariablestorecipedefinition` |
| `recipes` | 添加变量 | `cd43ae46-1b40-4df0-a033-231619868692` | `addvariable` |
| `recipes` | 添加同级 | `ffab8ae9-5702-4169-822e-a5045f3b4e0a` | `recipevariableaddsibling` |
| `recipes` | 添加子级 | `09340be0-b3f1-4215-948f-ea57ae40298c` | `recipevariableaddchild` |
| `recipes` | 添加新配方 | `237b4c62-b131-4961-b2dc-5574cd16584d` | `addrecipe` |
| `recipes` | 移除变量 | `ddf7742b-f688-48f5-99c6-3bc539440733` | `removevariables` |
| `recipes` | 移除配方 | `0be2aee7-875a-47b9-858f-62611d759911` | `removerecipes` |
| `recipes` | 读取并保存配方... | `370d5925-eb68-4491-9822-74c6fc685be4` | `readsaverecipe` |
| `recipes` | 读取配方 | `bfe30ca3-69e4-4181-809e-b2b584628b51` | `readrecipe` |
| `redundancy` | 交换PLC路径 | `73baa0a0-13bf-4c1d-a22c-2d6729011122` | `swapcomsettings` |
| `redundancy` | 写入设置 | `98f771a1-2f58-4923-afcb-f385ad179726` | `writesettings` |
| `redundancy` | 切换到主动 | `3ab9b46e-1191-43ef-8cb5-00c897c83bd2` | `switchsimulationtoactive` |
| `redundancy` | 切换到待机 | `f650dc12-df2f-407a-bca5-52c2ac549c40` | `switchactivetopassive` |
| `redundancy` | 切换到模拟 | `942f2075-e08c-4de6-b652-04964787131f` | `switchpassivetosimulation` |
| `redundancy` | 切换到独立 | `70680993-7873-4a54-a149-53ec0d3b1f06` | `switchsimulationtostandalone` |
| `redundancy` | 创建证书 | `2d6bf955-9317-49c5-a906-4f3b1521239a` | `createcertificates` |
| `redundancy` | 同步 | `9da0ad37-7598-445d-8f26-45e6452146dc` | `synchronize` |
| `redundancy` | 移除证书 | `cb6fcb27-521c-42ae-8824-e4c199651638` | `removecertificates` |
| `redundancy` | 设置PLC2的活动路径 | `a128faa3-7fd6-4de9-ab26-e034ff8474b9` | `setactivepathplc2` |
| `redundancy` | 读取设置 | `60075872-eaaf-4a8a-81ea-fd6b07c92f3d` | `readsettings` |
| `refactor` | 对变量重新排序... | `80a9336e-d2c1-4d25-b814-dc2fdaf9e53b` | `reorderVariables` |
| `refactor` | 更新引用引脚 | `569a419b-0526-4edf-a1fb-951c50a978a1` | `globalupdatepins` |
| `refactor` | 添加变量... | `541c9eec-d74b-4cb7-b311-0093247ca835` | `addvariable` |
| `refactor` | 清除''... | `fa5b07c7-638a-4b09-b56c-bd0f8d1d8741` | `removevariable` |
| `refactor` | 重命名''... | `eea6d3f9-7b35-4843-8d5b-911b5e6d2dab` | `rename` |
| `script` | ... | `ade5b54c-58ed-4855-a7b1-3f6b0ad17cdc` | `executewithletter` |
| `script` | A | `69a25ff7-1630-4169-9a82-3e2776426487` | `executewithletter` |
| `script` | B | `c53c2b61-976b-49f7-a24a-90b99addca7d` | `executewithletter` |
| `script` | C | `82357d9d-824a-4056-a0af-3ec60e9bb6ec` | `executewithletter` |
| `script` | D | `61d39ae4-2048-4df2-8101-225ac3022235` | `executewithletter` |
| `script` | E | `dc4b5558-f1fa-49da-a2fc-81029bb50a98` | `executewithletter` |
| `script` | F | `9de3537c-95db-4140-9987-7b20186f0c53` | `executewithletter` |
| `script` | G | `734c40ed-5686-4e09-9e35-1555d736d622` | `executewithletter` |
| `script` | H | `fb344cf3-02aa-4d8f-8f07-348189c78995` | `executewithletter` |
| `script` | I | `60943ab6-ea7a-4d4a-a145-2b9d3a7a6b20` | `executewithletter` |
| `script` | J | `04e26429-5ced-4180-a2ae-9bc3aa6645f2` | `executewithletter` |
| `script` | K | `4bd3469a-dc77-4433-ac1e-0fd2f73c9db1` | `executewithletter` |
| `script` | L | `5fd900c0-1dae-48b8-8d98-598f5ffc67b5` | `executewithletter` |
| `script` | M | `abf0377c-b942-43b8-a2c4-0ae3eb3e70a9` | `executewithletter` |
| `script` | N | `36852754-42b0-4bc3-8946-aac1fd5c0c07` | `executewithletter` |
| `script` | O | `83090639-60f6-461c-aa76-16991219d4b9` | `executewithletter` |
| `script` | P | `a9b65152-0c1c-458c-bef7-655dc955aea8` | `executewithletter` |
| `script` | Q | `30332ba1-5bdc-46e2-b395-b7cbd7c938cf` | `executewithletter` |
| `script` | R | `424fae55-05cd-429a-af63-0c2a1a7a0347` | `executewithletter` |
| `script` | S | `4cd726c9-2a74-46e7-8429-4994b005fcd5` | `executewithletter` |
| `script` | Script0 (unavailable) | `d5d3f463-e55c-4c4e-b557-e56beb397207` | `execute0` |
| `script` | Script1 (unavailable) | `747a61d0-23b7-4d36-86e8-d40be44756bd` | `execute1` |
| `script` | Script10 (unavailable) | `d53e26f4-dae3-460b-9a05-be4b6d89d70c` | `execute10` |
| `script` | Script11 (unavailable) | `58301487-e584-47d8-be33-1b61298c6cb5` | `execute11` |
| `script` | Script12 (unavailable) | `c2712d76-7b36-41f1-ac7a-28ca2fedcc28` | `execute12` |
| `script` | Script13 (unavailable) | `3bd716d8-22e3-412d-8907-ef769dc637d7` | `execute13` |
| `script` | Script14 (unavailable) | `4819c37a-fec8-4195-bb13-6dc3fa3e5322` | `execute14` |
| `script` | Script15 (unavailable) | `d355a0ea-d59e-4c1e-8424-0697c9974a04` | `execute15` |
| `script` | Script16 (unavailable) | `ea88ff69-1e93-446d-a4db-58718b3f507c` | `execute16` |
| `script` | Script17 (unavailable) | `ac633e0f-4b35-4ba7-9397-c17dae2fab17` | `execute17` |
| `script` | Script18 (unavailable) | `b0b9ca45-b3a2-43be-aaba-ffe94dbcb67f` | `execute18` |
| `script` | Script19 (unavailable) | `0e6ddc68-3c42-41b6-9d09-74bd95b46912` | `execute19` |
| `script` | Script2 (unavailable) | `133280df-960a-4ec7-b767-e4d562515ed0` | `execute2` |
| `script` | Script20 (unavailable) | `a49611f9-5849-4207-8b30-42edb411fc8c` | `execute20` |
| `script` | Script21 (unavailable) | `cf8f02cd-5116-4d79-be09-f3421e2a7157` | `execute21` |
| `script` | Script22 (unavailable) | `0a0efe72-fbc8-4100-9355-aab9e39275cf` | `execute22` |
| `script` | Script23 (unavailable) | `e59343ce-24ea-4fe9-b6b2-d4ac4afbe2f3` | `execute23` |
| `script` | Script24 (unavailable) | `ebbf03a2-9997-4cc1-93a5-3601cf2995e0` | `execute24` |
| `script` | Script25 (unavailable) | `e27ecef9-c8c6-47a5-85ed-00ea1d10a2cf` | `execute25` |
| `script` | Script26 (unavailable) | `0d29f393-3fa0-4bb2-9742-1144a3f12ad8` | `execute26` |
| `script` | Script27 (unavailable) | `222e3ddc-2e90-413b-93ff-eb154a91b26d` | `execute27` |
| `script` | Script28 (unavailable) | `50ebb99c-6df0-4ae6-8006-5415f0a1b5fc` | `execute28` |
| `script` | Script29 (unavailable) | `06e8d918-19cb-471a-9e61-5e852e108cb7` | `execute29` |
| `script` | Script3 (unavailable) | `58af3c0b-9ff8-4e3b-ba41-32e3134b1d1a` | `execute3` |
| `script` | Script30 (unavailable) | `0cbc7dbe-6956-482a-ad0f-663aa78bad74` | `execute30` |
| `script` | Script31 (unavailable) | `24baca81-1add-4779-855c-140a89b4c679` | `execute31` |
| `script` | Script4 (unavailable) | `53f7102b-1b30-4540-b848-be06df03b179` | `execute4` |
| `script` | Script5 (unavailable) | `e287d6b7-9e9b-4db2-88be-101cff9c1d3f` | `execute5` |
| `script` | Script6 (unavailable) | `2817fd46-e7f6-43cc-a4e2-3ded0b0bf4fe` | `execute6` |
| `script` | Script7 (unavailable) | `a841f175-9c71-4206-857b-07eddca0ab9a` | `execute7` |
| `script` | Script8 (unavailable) | `16895bb3-b3fa-4cec-8ca8-184312c210f4` | `execute8` |
| `script` | Script9 (unavailable) | `f1b3b408-f152-4ea4-a504-8405cdfe73e1` | `execute9` |
| `script` | T | `2f5c43ea-5ae9-4953-be64-2852757a64f4` | `executewithletter` |
| `script` | U | `1da7a098-c6a1-4e65-8661-376fcffdfe35` | `executewithletter` |
| `script` | V | `c19800a9-d11c-42e3-b0fe-2fd55c2eb8b0` | `executewithletter` |
| `script` | W | `43ffc3ce-a574-40a6-9016-6ff50f80fe78` | `executewithletter` |
| `script` | X | `9f778172-f7be-41de-9be0-cf8a964344e0` | `executewithletter` |
| `script` | Y | `be9982e1-c23f-4080-973b-28f2124f89ac` | `executewithletter` |
| `script` | Z | `5210847c-98b3-4a56-93d3-234e03996c5c` | `executewithletter` |
| `script` | 使能脚本跟踪 | `016de37c-8107-4b72-ad6b-f84775a45d44` | `tracing` |
| `script` | 执行脚本文件... | `974e36d0-d2ed-4dcc-9505-2e4f2fb9c70d` | `execute` |
| `security_agent` | 加密向导 | `cfff31b1-17da-4bbc-8b48-490a41862347` | `show_encryption_wizard` |
| `security_agent` | 设备安全设置 | `7de26209-6771-4abc-9ac9-f21121e79f07` | `configure_runtime_security_settings` |
| `security_manager` | 安全界面 | `f3812737-3d28-455f-81e0-f85fcd212aba` | `show_security_screen` |
| `sfc` | 初始步 | `acef1039-3caa-49e0-b712-7194fd005368` | `setinitstep` |
| `sfc` | 在...之后插入关联动作 | `f0830a30-cc43-4de5-ac6a-2e0462076faa` | `insertactionassociationafter` |
| `sfc` | 在...之后插入宏 | `12b42af1-741b-416d-a24c-0c643592f72f` | `insertmacroafter` |
| `sfc` | 在...之后插入步 | `65c3faca-ef86-4694-a171-3d9f28dc8b6f` | `insertstepafter` |
| `sfc` | 在...之后插入步转移 | `351754c0-5b83-4218-80e1-f0e80e657f72` | `inserttransstepafter` |
| `sfc` | 在...之后插入跳转 | `bb80384b-5f04-4f43-a475-aee2d3d45b1e` | `insertjumpafter` |
| `sfc` | 在...之后插入转移 | `bbc7bc6a-e9c3-4e40-b88f-bddb6c9befb0` | `inserttransafter` |
| `sfc` | 在...之后粘贴 | `88c0076a-6560-476c-9cba-078604d44473` | `pasteafter` |
| `sfc` | 在激活和非激活之间切换 | `252d50a1-391f-406c-848b-6d8e85641a99` | `toggle_step_active` |
| `sfc` | 并行分支 | `d62daf72-21c9-4c8d-ad23-6b70ccd4bee1` | `parallel` |
| `sfc` | 插入关联动作 | `2a4fa2c6-c583-4de4-89e6-9932798859c6` | `insertactionassociation` |
| `sfc` | 插入分支 | `85936005-4d28-49ff-95c2-41e58bd3945d` | `insertbranch` |
| `sfc` | 插入右分支 | `dd65dd13-00b0-45ed-91b8-64211859e1f5` | `insertbranchright` |
| `sfc` | 插入宏 | `059bd758-bf2b-4bd8-8eaf-6043f98ccb49` | `insertmacro` |
| `sfc` | 插入步 | `59f1042a-27fb-453d-893b-a88e39a18c51` | `insertstep` |
| `sfc` | 插入步转移 | `940b1721-68ab-4786-825a-819566daa5b3` | `inserttransstep` |
| `sfc` | 插入跳转 | `05badf67-3260-4987-b35d-7e91e65405d1` | `insertjump` |
| `sfc` | 插入过渡 | `5bd1ab71-27dc-403e-9c56-2e9579ae5fc2` | `inserttrans` |
| `sfc` | 添加入口动作 | `376046e4-f3b0-4824-aa09-0359e558c665` | `addentryaction` |
| `sfc` | 添加出口动作 | `f8889734-074a-4c26-b8dd-7e32f6578c1b` | `addexitaction` |
| `sfc` | 移除 | `2a53ee11-e83b-4e1f-a402-a87f5ae7acab` | `duplicationremove` |
| `sfc` | 设定 | `1e3e7143-9a10-4082-88fc-3bfd4ff4491a` | `setduplicate` |
| `sfc` | 进入宏 | `1360e7e6-4106-42ad-8635-9b46fdfc20ac` | `zoommacroin` |
| `sfc` | 退出宏 | `2c92dd9c-ce1a-4e30-a1c1-a7e44f512cad` | `zoommacroout` |
| `sfc` | 选择分支 | `db8a975d-3aa8-432c-92f8-069d3395a48b` | `alternative` |
| `sfc` | 隐藏嵌入对象 | `dcd1ee27-6f0f-482f-b8a3-cf4d7d051887` | `toggleshowembeddedobjects` |
| `softmotion` | 使能运动控制 | `005ef395-b0c2-4be1-85b0-7092652805f2` | `enable` |
| `softmotion` | 禁用运动控制 | `b742d820-248b-408f-b239-d79997d5309d` | `disable` |
| `staticanalysis` | 查看标准指标 | `4a787366-a156-403a-803c-b2826128b709` | `standardmetrics` |
| `staticanalysis` | 计算并导出标准指标 | `eeeeeeee-7d19-4230-b8cd-8c1bb00b6f50` | `exportstandardmetrics` |
| `staticanalysis` | 运行静态分析 | `ae97b6f4-dc9a-480e-aac8-6061e684f3c0` | `run` |
| `staticanalysis` | 运行静态分析 | `92e3b5d4-f999-4135-a1a8-a823423a370e` | `runforlibrary` |
| `tabulardeclaration` | 上移 | `4cbeebb2-181f-40eb-83ee-4073f5323fa1` | `moveup` |
| `tabulardeclaration` | 下移 | `77d89f0d-5e4e-49b7-af9a-82140f4b0055` | `movedown` |
| `tabulardeclaration` | 插入 | `7dbc3c49-db16-4208-91d5-8c4aa3b20ac2` | `insert` |
| `tabulardeclaration` | 编辑声明标题... | `b40d9966-fab5-4b1f-9f87-087d8fcac68c` | `editheader` |
| `targetsettings` | 目标设置文档导出 | `e8b67168-ae63-459e-93f4-deb66ce956ac` | `exportdoc` |
| `text` | 将文件作为文本插入... | `c1e88c90-0294-491c-9e36-73710f679b18` | `insertfile` |
| `text` | 展开所有折叠 | `047e2304-dd4f-4dae-a3f4-15ce8f817b63` | `expandallfolds` |
| `text` | 折叠所有折叠 | `d72f221d-3ad3-4682-9f72-1ad877b1085c` | `collapseallfolds` |
| `text` | 查看定义指南 | `59eecf81-1a83-40cb-b08a-6b135e1ece73` | `viewindentationguides` |
| `text` | 查看空白 | `59b7c9f4-8d9b-404c-910c-866e372f6237` | `viewwhitespace` |
| `text` | 覆盖模式 | `012502ca-abfb-41cb-90fa-ebd2dcad1813` | `toggleinsertmode` |
| `text` | 转到匹配的括号 | `8199691f-d4b1-4de8-9d2a-9b10f2bb9bb5` | `gotomatchingbracket` |
| `text` | 转到行... | `dfbfd10a-9d9c-4aff-a296-e7d3bdf07193` | `gotoline` |
| `text` | 转换为大写 | `e6e57377-ecd1-4991-a5f0-c835cfc526b8` | `makeuppercase` |
| `text` | 转换为小写 | `74516663-f8b7-4c49-83e1-54bb800e8eec` | `makelowercase` |
| `text` | 选择要匹配括号 | `3879487e-90c3-4b9b-a3c6-086bade55040` | `selecttomatchingbracket` |
| `text_editor_base` | 使能在线监控 | `35a166ee-6a30-44f3-a37a-94f7a096a080` | `toggle_inline_monitoring` |
| `text_editor_base` | 切换增量搜索的字段 | `08c97f66-b323-4d64-a6eb-565b6b30fb7a` | `toggle_incrementalsearch` |
| `text_editor_base` | 取消注释选定的行 | `012e6601-fc48-457f-8280-19f59b6c4a51` | `comment_in_selected_lines` |
| `text_editor_base` | 注释掉选定的行 | `5e0619de-d6f4-4f62-a9a0-9c60d44a311d` | `comment_out_selected_lines` |
| `text_list_enum` | 清除文本列表支持 | `85ce4cc9-aa5d-44f5-a06e-76e6ce4516db` | `convert_to_enum` |
| `textlist` | 创建全局文本列表 | `3b079581-ec53-400c-88cb-79e702354d5b` | `createglobaltextlist` |
| `textlist` | 创建系统文本列表 | `82c0c3fc-24fa-48cc-9895-a528315b4e66` | `createsystemtextlist` |
| `textlist` | 删除语言 | `a36e8f54-4cd8-44c5-b8b4-e537ac822bef` | `removelanguage` |
| `textlist` | 导入/导出文本列表 | `d75434a7-7d1a-4add-8f10-7cff82d18cf6` | `import_export` |
| `textlist` | 导入Unicode.txt文本列表 | `96ffc394-37e6-4438-a5d6-d77983a6354b` | `import` |
| `textlist` | 导入全部Unicode.txt文本列表文件 | `79f702f4-a03f-4a0d-b7ea-d0f50c0f3113` | `importalltxtfiles` |
| `textlist` | 导出全部.txt文本列表文件 | `91cc8d4f-eb03-48ec-b54d-6d6fd92c2623` | `exportalltxtfiles` |
| `textlist` | 导出全部.xml文本列表文件 | `78599c10-e4de-4521-9653-257f02f520fb` | `exportallxmlfiles` |
| `textlist` | 导出全部Unicode.txt文本列表文件 | `71775307-438e-4d4e-896a-a9f3082a9aa2` | `exportallunicodetxtfiles` |
| `textlist` | 导出全部Unicode.xml文本列表文件 | `5fe4c666-c36b-4885-aa1f-a814604143ad` | `exportallunicodexmlfiles` |
| `textlist` | 插入文本 | `bf3179be-a7d9-4214-8fa7-56af10e7fe9e` | `inserttext` |
| `textlist` | 更新可视化文本ID | `808087ad-caff-4c87-9d7a-ec417b14f904` | `updatetextids` |
| `textlist` | 检查可视化文本ID | `297b936c-ba12-438c-ae3f-d65e24b1e369` | `checktextids` |
| `textlist` | 添加语言 | `1a26a308-9a8a-4e4e-94d9-bc40e2b92caf` | `addlanguage` |
| `textlist` | 移除未使用的文本列表记录. | `8f79c0ea-8087-42bc-b1ea-7a68481cbdea` | `remove_unused_items` |
| `textlist` | 重命名语言 | `83bf10ba-df48-4ee3-a7dd-abccf2fcdc3f` | `renamelanguage` |
| `toggle` | 切换本地化 | `d026b784-b5cb-48ff-8df0-7aa7c396b318` | `localization` |
| `tools` | 授权存储库... | `2ce5552c-3f08-4fe4-bd85-e76d04c89a27` | `licenserepository` |
| `tools` | 授权管理器... | `6b980099-a6e4-429b-9f64-c2c5191f2440` | `licensemanager` |
| `trace` | 保存跟踪... | `28015cfa-91cb-47ad-9e91-22fad58bd53b` | `save` |
| `trace` | 加载跟踪... | `7169b8a8-aff7-42f4-a23d-b86de0bca6d8` | `load` |
| `trace` | 导出符号跟踪配置 | `d704adf2-6117-406e-8841-7c553cb078d9` | `ExportSymbolicConfig` |
| `usermgmt` | Change user | `aa65559b-3bcb-40b3-a6fe-871e3baa8191` | `changeuser` |
| `usermgmt` | 权限... | `7a979090-1138-4b26-aabc-9a10983d6b4d` | `permissions` |
| `usermgmt` | 注销用户 | `70c28e64-65d9-498b-a80a-2f9ccbc09e5a` | `logout` |
| `usermgmt` | 用户登录... | `c0130d68-f78b-4e12-9c50-ac27371eea79` | `login` |
| `var_config` | 添加所有实例路径 | `6ca69045-2e11-409d-b160-81ef1d7705f8` | `addallinstpaths` |
| `var_persistent` | 添加所有实例路径 | `76fad7fd-c8ab-417e-9a60-67fca40baeda` | `addallinstpaths` |
| `view` | CODESYS 视角 | `76cbcb67-3dda-4b8b-9854-641d25f19ac4` | `setstandardperspective` |
| `view` | HMI 视角 | `89fca65b-a68e-45e2-b53a-ea24d078d1d2` | `sethmiperspective` |
| `view` | HMI功能 | `b9dca5dc-1772-4d17-828e-ef23a5b53fc8` | `hmifeaturesview` |
| `view` | 书签 | `da81b3d6-010f-447e-b96c-dc8f921d0317` | `bookmarks` |
| `view` | 交叉引用列表 | `5ed0375d-1278-4af6-b4c8-29beaff95f43` | `crossref` |
| `view` | 元素属性 | `79d46924-f2b6-454d-8c0e-500222a234f0` | `elementproperties` |
| `view` | 可定制工具箱 | `ce77ea7e-c7b3-4e01-901a-0187de446bdb` | `csttoolbox` |
| `view` | 可视化 | `321f5799-b306-4556-b7b7-dca9429a0436` | `hmivisualizationsview` |
| `view` | 可视化工具箱 | `b987ba7b-0844-488f-a750-11d0a500a655` | `visutoolbox` |
| `view` | 在线更改内存预留设置 | `ca5b4f8a-6be8-4ed3-9494-e1d99e716c8b` | `allocationplus` |
| `view` | 工具箱 | `e5a57296-ac20-41b8-86ca-0e997a2ddae9` | `toolbox` |
| `view` | 所有的应用列表 | `cb65a30d-212c-4492-9881-4edbd0cc60bb` | `applicationlistcommand` |
| `view` | 打开内存扫描 | `fdd09f02-cdd1-4e32-8604-b204dc87fac1` | `memory_scan` |
| `view` | 数据源 | `36c3ebca-445e-4946-8011-026e62be9790` | `hmidatasourcesview` |
| `view` | 断点 | `8008cd5a-234d-49f6-b2fc-9f6c5d6c87a7` | `breakpoints` |
| `view` | 显示内存视图 | `41a4faad-6d1b-4430-bead-3dea6008058d` | `memory` |
| `view` | 显示模块引用窗口 | `75ff31ca-b1fa-4947-9f5b-d32fc87657d6` | `modulereferences` |
| `view` | 模块 | `5a8291aa-370e-4dfb-8253-52c5a5ad5c65` | `modules` |
| `view` | 消息 | `ac4e98fe-8ff9-4055-8002-93a451800bac` | `messages` |
| `view` | 监视 1 | `eecbee66-648b-4e9c-a738-4e5c09ab7c50` | `watch1` |
| `view` | 监视 2 | `7cae844f-6685-43cb-9575-a7206be83f31` | `watch2` |
| `view` | 监视 3 | `325b3dcf-24ee-459c-ac41-f8bb1a158d23` | `watch3` |
| `view` | 监视 4 | `6bbe615c-8fe4-493f-87da-976a7461e568` | `watch4` |
| `view` | 程序组织单元 | `92d4ebf6-b699-42ee-ac5e-3c533024eb69` | `pous` |
| `view` | 经典交叉引用列表 | `356e4a32-5638-4565-915a-de143fe91bfc` | `legacycrossref` |
| `view` | 编程 | `a37956b2-67c2-44fa-82b9-c062cddb36db` | `hmiprogrammingview` |
| `view` | 设备 | `954125ec-3a22-4054-84fb-10609b9f1f5c` | `devices` |
| `view` | 调用堆栈 | `e4b1fa4f-62fd-4972-9242-43f6828a3ebb` | `callstack` |
| `view` | 调用树 | `0a1c8a75-99da-47fe-a1f1-2eb258f623df` | `calltree` |
| `view` | 起始页 | `86b061d8-a4f4-4e58-9177-16ed9001c9ff` | `startpage` |
| `visu` | 多样可视化元素 | `984b26ee-e427-4c2f-836f-32a02f9a95e7` | `mulitplyelements` |
| `visual` | Trim visual element texts | `21cf650f-3a94-4390-9953-024d662930da` | `trimvisualelementtexts` |
| `visual` | 上对齐 | `bd93da1c-7d70-46c1-be3c-d48071d3d6a2` | `aligntop` |
| `visual` | 下对齐 | `bde710de-7a41-45a7-b4d5-082472669f11` | `alignbottom` |
| `visual` | 使垂直间距相等 | `55ca4c71-6007-4fae-ac3d-7fbb8884f9a3` | `makeverticalspacingequal` |
| `visual` | 使水平间距相等 | `5c240f3d-b7b9-44e8-9c77-b52385d1fc9e` | `makehorizontalspacingequal` |
| `visual` | 使用新的跟踪元素替代旧的跟踪元素 | `3ac8548f-0329-415b-a538-f3ae25496ebf` | `replacetraceelement` |
| `visual` | 保持相同大小 | `04afcb66-352f-495e-83b4-bed29eeb4ecf` | `makesamesize` |
| `visual` | 保持相同宽度 | `c48e34a3-bcae-44e0-9241-1289b50c587b` | `makesamewidth` |
| `visual` | 保持相同的高度 | `dd45c127-14d2-47e3-90ec-d0ffb009a6f5` | `makesameheigth` |
| `visual` | 全选 | `04f25b75-8ebf-41f2-86b5-8a7b4153c1d2` | `selectall` |
| `visual` | 减少垂直间距 | `4d512295-a029-4280-8a6a-631fcb039ec2` | `decreaseverticalspacing` |
| `visual` | 删除垂直间距 | `9cfbb0ff-e581-455c-99db-60b82eeae22b` | `removeverticalspacing` |
| `visual` | 删除水平间距 | `f91bb024-d4c8-49af-8174-d61dfbb3fc0d` | `removehorizontalspacing` |
| `visual` | 取消组 | `cdb9d5f2-91f6-4e67-b031-a27f5d6abc7e` | `ungroupelements` |
| `visual` | 可视元素列表 | `929e7f56-d41d-4b3b-a6c3-d21507aace8b` | `showelementlist` |
| `visual` | 右对齐 | `55c24226-d2d4-440f-a29a-17fec9cfc21d` | `alignright` |
| `visual` | 在<无>中更新框架参数 | `219bb226-08d1-428d-95ce-fc83379c8839` | `updateframeparameterscurrent` |
| `visual` | 在可视化视图中合并语言模型 | `c48013da-64ff-4095-847c-ceb603e76efd` | `mergelanguagemodel` |
| `visual` | 垂直居中对齐 | `c5f3a3e1-0cb7-4410-acc2-b823d593f198` | `alignverticalcenter` |
| `visual` | 增加垂直间距 | `8d2938fa-9778-4534-ba80-625f5025f330` | `increaseverticalspacing` |
| `visual` | 增加水平距离 | `0346538f-3106-42fa-b8f0-b0277244a346` | `increasehorizontalspacing` |
| `visual` | 复位到默认 | `dd306b9b-15c6-4f44-8b86-57063c94ec04` | `resettaborder` |
| `visual` | 大小格 | `dec2e780-98e8-4f46-9bdc-d02b70de060e` | `sizetogrid` |
| `visual` | 对齐线 | `86eccc46-ac99-4a66-b012-a386332a65ff` | `assistpositionsnap` |
| `visual` | 将一个置尾 | `83c320b9-49ca-4fbc-846a-1f685656c6ae` | `sendonetoback` |
| `visual` | 将一个置首 | `88a3e153-32c6-4cf6-bc37-ec58877a4852` | `bringonetofront` |
| `visual` | 左对齐 | `c2b51fc7-2f6a-4035-9e17-15a524fe49c0` | `alignleft` |
| `visual` | 开放式框架配置 | `0042d1d1-ef6f-42f2-840d-baf6bd55545f` | `frameselection` |
| `visual` | 插入元素控制XYChart... | `1eae6b5d-df41-48c2-a1f7-ac1528947c01` | `xychartwizard` |
| `visual` | 插入元素控制跟踪... | `f2cd205f-eb42-4261-a439-1ea69934332a` | `tracewizard` |
| `visual` | 插入用于滚动报警的元素... | `c4ad8f39-d56b-401c-a801-6af1b2293254` | `alarmbannerwizard` |
| `visual` | 插入用于趋势控制的元素... | `543524b5-7950-4c6f-9589-e5913ae3d403` | `trendwizard` |
| `visual` | 更新全部框架参数 | `071b20a3-cd40-446d-896d-857833e0e46c` | `updateframeparametersall` |
| `visual` | 更新工具箱 | `9ef5e7a1-8c81-456e-966d-73dd73379102` | `updatetoolbox` |
| `visual` | 水平居中对齐 | `66bca50b-1c93-4879-9832-b975e60d7742` | `alignhorizontalcenter` |
| `visual` | 没有辅助 | `70332b79-fa7a-4dc4-956e-0d3b964c3f8c` | `assistpositionno` |
| `visual` | 没有选择 | `85a0df4a-d8eb-4790-8f05-70b0b54458ed` | `selectnone` |
| `visual` | 添加一个子类别节点 | `56997173-c88d-4cd7-a7d9-8be53787fd47` | `addcategoryaschildhierarchicalpropertiesnode` |
| `visual` | 添加一个子节点 | `32931f24-f0b5-4506-abf7-e03dcfa1b210` | `addchildhierarchicalpropertiesnode` |
| `visual` | 添加一个类别节点 | `f9fc6a36-951e-42c3-9cbd-743ebbc2dc8a` | `addcategoryhierarchicalpropertiesnode` |
| `visual` | 添加可视元素开发库 | `8de1b44e-6065-4fd8-8e10-490ea0168f7c` | `insertvisuelementplaceholders` |
| `visual` | 添加可视化元素 | `db667872-2795-444c-9846-2b4e579026c4` | `addelement` |
| `visual` | 添加所有标准属性节点 | `afdc7226-c9a5-49ee-b71a-c7bbe297e485` | `addallstandardpropertieshierarchicalpropertiesnode` |
| `visual` | 添加接口描述 | `25769029-caf9-40cd-bfd8-a71de641e77a` | `addhierarchicaldescriptionnode` |
| `visual` | 添加标准属性节点 | `4fe79058-bd27-457a-b060-d3939399b324` | `addstandardpropertyhierarchicalpropertiesnode` |
| `visual` | 添加节点 | `6442ceef-6a51-4822-b791-d366755bd7a5` | `addhierarchicalpropertiesnode` |
| `visual` | 激活热键用法 | `e4c98a2e-d47a-4e78-9fc5-3e63abfac7ff` | `activatekeyboardusage` |
| `visual` | 点击参考可视化 | `fd8c7961-b799-47f5-84ae-23b396ba8b97` | `gotoreferencedvisu` |
| `visual` | 热键编辑器 | `5417f0ca-4f99-40ee-976f-f065b5b4e5e3` | `showhotkeys` |
| `visual` | 用新的元素替换旧的跟踪元素,以实现项目的所有可视化 | `782e71ea-2b8d-400e-a630-404a21fc699b` | `replacealltraceelement` |
| `visual` | 界面编辑器 | `37463fcb-a66a-4c0e-b7d6-409ca3093de0` | `showinterface` |
| `visual` | 移动到位置... | `83f433cf-0e9d-4aa5-84cb-28fd5885c5b9` | `movetotaborder` |
| `visual` | 移动到内容区域 | `8c240874-f956-4b77-8158-c3991459254c` | `movetocontentarea` |
| `visual` | 移除不支持的可视化高亮属性 | `9b42b33d-28dc-4634-b160-ed979d93ad43` | `removenotsupportedtargetvisulightproperties` |
| `visual` | 组 | `42bea518-f57d-4e91-9d13-60e3f161cd70` | `groupelements` |
| `visual` | 编辑趋势记录 | `0cadca12-2cbe-435d-bb5a-51e7bd41abee` | `trendrecordingconfig` |
| `visual` | 网格 | `29f0a073-0672-4c1b-b9f9-3c60cf7f2432` | `assistpositiongrid` |
| `visual` | 置尾 | `6332a20e-28fe-4a3b-9034-85d4916ce35f` | `sendtoback` |
| `visual` | 置首 | `85b7c280-5694-4dcb-919e-04d29148d982` | `bringtofront` |
| `visual` | 背景 | `df2eb79b-29da-4c1c-84af-cc6d606890cc` | `backgroundbitmapcolor` |
| `visual` | 节点向上移动 | `6d28aba9-b063-48b7-97da-f0ea1d848d82` | `moveselectednodeuphierarchicalpropertieseditorcommand` |
| `visual` | 节点向下移动 | `c75ae092-3907-4e33-baac-d3399c740031` | `moveselectednodedownhierarchicalpropertieseditorcommand` |
| `visual` | 通过插入元素确认报警... | `31468817-3cf4-4002-8383-a935452d6a05` | `alarmtablewizard` |
| `visual` | 配置XYChart设置... | `aa1e3c42-c4b6-40c9-b80c-f68616d33baa` | `xychartconfig` |
| `visual` | 配置趋势的显示设置 | `7cf1acce-5a50-479b-8c25-8c1e2e1088fa` | `trendconfig` |
| `visual` | 配置跟踪... | `c2737c84-cead-4248-9229-7325cbc9141e` | `traceconfig` |
| `visual` | 重置框架大小 | `41d4057b-4228-41de-a57a-b6529b96fc38` | `frameresize` |
| `visual` | 降低水平间距 | `6ee794bf-fb33-47ee-a62e-206dd85e5992` | `decreasehorizontalspacing` |
| `watchlist` | 将所有的强制添加到监视列表中 | `8ee117eb-a14c-48f2-aef6-e44c5b2a6931` | `addallforces` |
| `watchlist` | 添加查看 | `88888888-30f6-49b9-808d-245fe8ca7d76` | `addchildnodetowatch` |
| `watchlist` | 解除和恢复所有所选值 | `2187ff0a-d565-452b-a410-c261bd0109ca` | `unforce_all_selected_restore_values` |
| `watchlist` | 解除强制并保持所有所选值 | `0aacf5ae-1d29-4140-9922-144527cdb752` | `unforce_all_selected_keep_values` |
| `window` | 重置窗口布局 | `1ce18f41-c205-4cb3-a28d-0b8fc7a794ad` | `resetwindowlayout` |
