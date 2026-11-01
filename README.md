# 联想拯救者 R7000P 2025 · Hackintosh EFI

联想拯救者 **R7000P 2025 / 83LT / R7000P ADR10** 的个人 OpenCore 配置快照。

**快照日期：2026-11-01（America/Los_Angeles）。这是一份持续调试中的配置，不是全功能完美 EFI。**

本机已通过 Kingston 启动 U 盘进入 macOS；本仓库保留该 EFI 的二进制与配置，仅对公开副本去除了机器身份信息。原始序列号、MLB、SystemUUID、ROM 已清空或置零，**使用前必须填写自己的 SMBIOS 身份信息**。不要把仓库副本直接覆盖正在使用的 EFI。

## 硬件与系统

| 项目 | 本机配置 |
|---|---|
| 电脑 | Lenovo Legion / 联想拯救者 R7000P 2025，83LT / R7000P ADR10 |
| BIOS | RLCN32WW |
| CPU | AMD Ryzen 9 8940HX；BIOS 关闭一半核心，当前开放 **8核16线程** |
| 内存 | 16GB |
| 独立显卡 | NVIDIA GeForce RTX 5060 Laptop，8GB，`10DE:2D59` |
| 核显 | AMD Radeon 610M，`1002:164E`；本仓库不声称已获得核显加速 |
| 内屏 | MNG007DA6-2 / CSW1659，2560×1600，60/240Hz，EDID 首选60Hz |
| 外接显示器 | AOC Q24G4，2560×1440，实际识别过180Hz |
| 有线网卡 | Realtek RTL8168；EFI 使用 RealtekRTL8111.kext |
| 无线网卡 | MediaTek MT7925；Wi-Fi / 蓝牙未完成运行验证 |
| macOS | Tahoe 26.7.2，构建25G332，Darwin25.6.0，x86_64 |
| SMBIOS | MacBookPro16,2 |
| OpenCore | 1401 Windows 2.6.6 生成的**自定义 OpenCore 1.0.9** |
| 当前引导 | Kingston USB，卷标1401，活动配置 `EFI/OC/config.plist`；未确认迁入内置盘 |

**不要用其他版本的 OpenCore 二进制或旧 EFI 混合覆盖此配置。** 版本来源来自本机交接记录；二进制完整性参见 `EFI-SHA256SUMS.txt`，文件校验不能替代实际启动验证。

## 已验证与待验证

| 项目 | 状态与证据边界 |
|---|---|
| 进入系统 | 用户确认安装 NVIDIA 2.6.6 后可以进入；Mac 端已读取实际系统信息 |
| CPU 核心数 | `sysctl` 读取8个物理核心、16个逻辑线程；没有 `cpus=1` 或其他 `cpus` 限制 |
| CPU 名称 | 内核已正确识别 Ryzen 9 8940HX；系统信息曾显示8-Core Intel Xeon W；当前快照新增 `revpatch=sbvmm,cpuname`，**尚未重启验证名称修正** |
| NVIDIA kext | `kmutil showloaded --list-only` 确认 NVRM、NVAccel、NVRMFB、NVRMAGDC 均加载2.6.6 |
| Metal | `system_profiler SPDisplaysDataType` 报告 Metal3、8GB显存；不等于所有 Metal 应用都已测试 |
| 双屏 | 内屏与 Q24G4 均在线；分别报告过240Hz和180Hz，部分配置操作后会回到60Hz；未做长期高刷稳定性验证 |
| 原生 HiDPI | 加入 `nvfbhidpi=1` 后出现1920×1080、2048×1152 HiDPI模式，但实际切换被 WindowServer 以“Mode not available”拒绝；60/180Hz均未成功 |
| HiDPI 串流 | BetterDisplay4.3.7 虚拟1920×1080 HiDPI、60Hz，工具报告串流开启；**用户实际清晰度和长期运行尚未确认**。BetterDisplay5.2.1在本机启动崩溃 |
| TSC | ForgedInvariant1.5.0加入后，用户确认恢复环境与系统可继续启动；历史出现过 Non-monotonic time |
| USB | USBToolBox1.2.0 + 按本机 Windows 实测生成的 UTBMap；USB-C高速数据与翻转方向未完整验证 |
| 键盘/触控板 | PS/2键盘和 VoodooI2C 路径保留；PS/2鼠标/触控板插件停用；触控板全部手势未完整验证 |
| OpenCore菜单输入 | 曾偶发完全不响应；已调整键盘支持设置，是否完全解决仍待观察 |
| 声音/睡眠/唤醒/电源管理 | 未完成实测，不承诺可用 |
| 网络/蓝牙 | 硬件与 kext 清单已记录；连接、吞吐量和蓝牙运行未完整验证 |

## 关键配置

### 内核启动与时钟

- `Booter → Quirks → DevirtualiseMmio = true`。
- `MmioWhitelist` 保留启用的 **`0xFF000000`**。移除此设置曾出现 `CR2=0xFF00004C` 的早期内核崩溃。
- AMD 核心补丁按 **8个物理核心**配置；不要擅自添加 `cpus=1`。
- Lilu之后加载 ForgedInvariant1.5.0。
- `ResizeAppleGpuBars=0`，`ResizeGpuBars=-1`；不随意强制调整BAR。

### NVIDIA显示路径

使用 [NullMoth NVIDIA macOS Driver](https://github.com/nullmoth/nvidia-macos-driver) **原版2.6.6**。

本机安装包SHA256：

```text
dbb0f5c2a18ccc97dfdf57ca14488b0ea713c15608f684a0a4283e88c676ab6e
```

这套驱动通过已安装macOS的后台安装流程完成。**驱动不包含在 EFI 中，也不应重复放入 EFI 注入。** 四个 kext 安装在 `/Library/Extensions`，已确认进入 AuxiliaryKernelExtensions.kc；Metal插件位于 `/Library/GPUBundles`。仅复制本仓库 EFI 并不能完成 NVIDIA 驱动安装。

- 保留 WhateverGreen 与 `gfxrst=4`；不能将其误当作核显驱动删除。
- 当前没有 NootedRed、NootRX，也没有 EFI EDID 注入。
- `Kernel → Block` 启用 `com.apple.iokit.IONDRVSupport`，`Strategy=Exclude`，`MinKernel=25.0.0`；这是**驱动已安装后的显示路径**。
- 若恢复环境因此无显示，应在备份现配置后恢复**安装NVIDIA之前**的恢复环境配置。仓库不包含该历史未脱敏备份，不要把 HiDPI 参数修改前的备份误当作恢复环境配置。
- 内屏历史已有60Hz报告，没有证据证明高刷新率就是此前黑屏根因。

### 安全与NVRAM（记录本机现状）

- `csr-active-config` Data：`430A0000`。
- `SecureBootModel=Disabled`；Lilu和AMFIPass启用。
- `NVRAM → Delete` 包含 `boot-args`，避免旧参数覆盖配置。
- 不随意执行 Reset NVRAM，优先定向处理变量。

当前配置中的完整启动参数：

```text
-v debug=0x100 keepsyms=1 -amfipassbeta -vi2c-force-polling revpatch=sbvmm,cpuname nvfb=1 nvaccel=1 nvfbheads=4 -nvkmsnosmooth amfi_get_out_of_my_way=0x1 amfi=0x80 ipc_control_port_options=0 gfxrst=4 nvfbhidpi=1
```

CPU名称修正只改变显示名称相关补丁，不改变核心数或电源管理。系统信息的2.4GHz不是实时频率监测结果。

### USB与菜单输入

- UTBMap 匹配AMD控制器 `1022:15B6 / 15B7 / 15B8`，根端口数量分别4/4/1。
- 使用 UTBMap 替代 UTBDefault；不要声称USB-C全部测试通过。
- 菜单设置：`KeySupport=true`、`KeySupportMode=Auto`、`KeyFiltering=true`、`KeyForgetThreshold=5`、`TimerResolution=0`、Builtin菜单、`PollAppleHotKeys=false`、`Timeout=10`。
- EFI包含 ResetNvramEntry.efi 不代表建议日常使用该工具。

## 使用与维护

1. 先备份自己可用的完整 EFI，保留当前可启动U盘。对照硬件、BIOS、核心数、USB映射和系统版本，不要跨机器直接套用。
2. 在公开副本 `EFI/OC/config.plist → PlatformInfo → Generic` 中填写自己的 `SystemSerialNumber`、`MLB`、`SystemUUID` 和6字节 `ROM`。不要使用他人真实身份信息，也不要将填写后的文件推送到公开仓库。
3. 保持该自定义OpenCore的二进制、kext和配置配套；本仓库不是纯上游OpenCore的替换包。
4. 明确区分恢复环境配置和已安装NVIDIA驱动后的配置。没有系统侧驱动时，当前 `IONDRVSupport` 屏蔽设置不保证提供可用画面。
5. 每次只改一个问题，保留可回滚配置；不要无备份重写整套EFI或重新安装系统。
6. 进入系统后分别检查实际加载、显示状态和功能，不能把plist格式校验、路径校验或文件SHA256校验说成完整运行验证。

只读检查示例：

```sh
sysctl machdep.cpu.brand_string hw.physicalcpu hw.logicalcpu
kmutil showloaded --list-only | grep -E 'com.nullmoth.(NVRM|NVAccel|NVRMFB|NVRMAGDC)'
system_profiler SPDisplaysDataType
nvram boot-args
```

HiDPI的显示覆盖文件及BetterDisplay设置属于**系统侧配置**，不在此EFI快照内；安装EFI不会自动复现当前串流方案。

## 仓库内容

- `EFI/`：当前U盘EFI公开副本，机器身份信息已脱敏。
- `EFI-SHA256SUMS.txt`：公开副本全部EFI文件的SHA256；其中config.plist因脱敏与本机原始文件不同。
- [组件与版本清单](docs/COMPONENTS.md)：实际启用/停用的kext、ACPI、UEFI驱动。
- [验证记录](docs/VALIDATION.md)：本次快照的检查范围与局限。
- [隐私处理](docs/PRIVACY.md)：公开副本移除项目及使用前要求。
- `scripts/check_snapshot.py`：只读验证公开快照的身份占位、引用路径和校验和。

## 来源与许可

本仓库是个人硬件配置与第三方组件的组合快照。OpenCore、各kext、图标/资源及自定义构建保留各自上游版权和许可，本仓库不为第三方二进制另行授予统一许可，也不表示得到联想、Apple、NVIDIA或相关上游项目背书。

- [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg)
- [AMD Vanilla内核补丁](https://github.com/AMD-OSX/AMD_Vanilla)
- [Lilu](https://github.com/acidanthera/Lilu) / [WhateverGreen](https://github.com/acidanthera/WhateverGreen) / [RestrictEvents](https://github.com/acidanthera/RestrictEvents)
- [USBToolBox](https://github.com/USBToolBox/kext) / [VoodooI2C](https://github.com/VoodooI2C/VoodooI2C)
- [NullMoth NVIDIA驱动](https://github.com/nullmoth/nvidia-macos-driver)
- [BetterDisplay](https://github.com/waydabber/BetterDisplay)
