# 快照验证记录

日期：2026-11-01，America/Los_Angeles。

## 当前运行证据

- 实际读取macOS26.7.2 / 25G332。
- 实际读取CPU品牌 AMD Ryzen9 8940HX、8个物理核心、16个逻辑线程。
- 实际读取四个NullMoth2.6.6 kext已加载，RTX5060 Laptop8GB，Metal3报告。
- 内屏与Q24G4均识别在线；刷新率在不同调试阶段分别出现过60/240Hz、60/180Hz。
- `nvfbhidpi=1` 已进入当前启动参数；原生HiDPI模式出现，但切换失败，日志包含 `CGXCompleteDisplayConfiguration: Mode ... not available`。
- BetterDisplay虚拟屏1920×1080 HiDPI60Hz和串流开启状态已通过工具读取，未取得用户视觉效果确认。

## 当前快照与运行系统的差别

快照包含稍后追加的 `revpatch=sbvmm,cpuname`；该修改已校验只有这一项参数变化，尚未重启验证。运行系统当时仍报告8-Core Intel Xeon W的展示名称，内核AMD品牌识别正确。

公开副本只清理机器身份信息与密码字段；其余主config配置和EFI组件均来自当前U盘。历史备份config未发布。

## 静态检查

- plist可解析。
- 所有启用的ACPI、UEFI驱动、kext路径，以及kext可执行文件和Info.plist引用存在。
- 对全部EFI文件记录SHA256；除主config脱敏、历史备份剔除外，保持源文件内容。
- 原始SMBIOS身份信息的文本和二进制残留扫描通过。

这些静态检查不能证明跨机器可启动，也不能替代本机长时间稳定性、睡眠、音频、网络、USB-C、高刷或Metal应用测试。未运行不匹配的上游ocvalidate来宣称自定义OpenCore全量校验通过。
