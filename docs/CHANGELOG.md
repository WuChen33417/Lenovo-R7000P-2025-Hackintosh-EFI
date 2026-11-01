# 版本记录

## v2.0.0 — Wi-Fi / 蓝牙 / 扬声器可用版本

2026-11-01。用户确认本机三项功能成功驱动。

- 新增MtkWlan0.12.1、MtkWlanNative0.4.15，Wi-Fi原生菜单参数及示例自动连接清理。
- 新增MtkBt0.2.4、BlueToolFixup2.7.2、LegionBtFix0.3.0，以及蓝牙两项定向NVRAM值。
- 新增AppleALC1.9.8、SimpleHDA1.0.0、ALC287 layout13；系统卷未做根补丁。
- CPU名称修正已验证；补充板载ALC287和蓝牙USB硬件ID。
- 保留既有OpenCore、AMD8核补丁、MMIO/TSC、NVIDIA2.6.6、USB映射。
- 指针实验nvcursor=0已撤回，第二版不包含该参数；外屏指针偏大仍为已知问题。
- 明确隔空投送缺少AWDL支持，以及睡眠、麦克风、耳机、高刷长期稳定性等验证边界。

## v1.0.0 — NVIDIA启动基线

首个公开快照，提交fdb01967b047729b46e0947b8968b5173a77a969。

- R7000P2025 / 83LT，Ryzen9 8940HX（8核16线程），RTX5060 Laptop。
- 自定义OpenCore1.0.9，macOS26.7.2，NullMoth2.6.6系统侧驱动已加载。
- 保留DevirtualiseMmio、0xFF000000白名单、ForgedInvariant、USBToolBox与UTBMap等关键修正。
- 尚未加入第二版的Wi-Fi、蓝牙及板载音频驱动。
- CPU名称修正参数存在，但在该快照发布时尚待重启验证。
