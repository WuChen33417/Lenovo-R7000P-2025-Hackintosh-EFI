# EFI 组件清单

v2.0.0：从当前EFI读取。启用状态不代表全部功能长期验证通过。

| 状态 | BundlePath | 版本 |
|---|---|---|
| 启用 | `Lilu.kext` | 1.7.3 |
| 启用 | `ForgedInvariant.kext` | 1.5.0 |
| 启用 | `AMFIPass.kext` | 1.4.1 |
| 启用 | `AppleMCEReporterDisabler.kext` | 1.2 |
| 启用 | `BrightnessKeys.kext` | 1.0.4 |
| 启用 | `LegionITEKbdFix.kext` | 1.0.0 |
| 启用 | `NVMeFix.kext` | 1.1.4 |
| 启用 | `RealtekRTL8111.kext` | 2.4.2 |
| 启用 | `RestrictEvents.kext` | 1.1.7 |
| 启用 | `VirtualSMC.kext` | 1.3.9 |
| 启用 | `SMCBatteryManager.kext` | 1.3.9 |
| 启用 | `SMCLightSensor.kext` | 1.3.9 |
| 启用 | `USBToolBox.kext` | 1.2.0 |
| 启用 | `UTBMap.kext` | 1.1 |
| 启用 | `VoodooI2C.kext/Contents/PlugIns/VoodooI2CServices.kext` | 1 |
| 启用 | `VoodooI2C.kext/Contents/PlugIns/VoodooGPIO.kext` | 1.1 |
| 启用 | `VoodooI2C.kext` | 2.9.1 |
| 启用 | `VoodooI2C.kext/Contents/PlugIns/VoodooInput.kext` | 1.1.7 |
| 启用 | `VoodooI2CHID.kext` | 1 |
| 启用 | `VoodooPS2Controller.kext` | 2.3.8 |
| 停用 | `VoodooPS2Controller.kext/Contents/PlugIns/VoodooInput.kext` | 1.1.7 |
| 启用 | `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Keyboard.kext` | 2.3.8 |
| 停用 | `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Mouse.kext` | 2.3.8 |
| 停用 | `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Trackpad.kext` | 2.3.8 |
| 启用 | `WhateverGreen.kext` | 1.7.2 |
| 启用 | `YogaSMC.kext` | 1.5.3 |
| 启用 | `MtkWlan.kext` | 0.12.1 |
| 启用 | `MtkWlanNative.kext` | 0.4.15 |
| 启用 | `BlueToolFixup.kext` | 2.7.2 |
| 启用 | `MtkBt.kext` | 0.2.4 |
| 启用 | `LegionBtFix.kext` | 0.3.0 |
| 启用 | `AppleALC.kext` | 1.9.8 |
| 启用 | `SimpleHDA.kext` | 1.0.0 |

## ACPI

- `SSDT-EC.aml`：启用
- `SSDT-PLUG-ALT.aml`：启用
- `SSDT-USB-Reset.aml`：启用
- `SSDT-USBX.aml`：启用
- `SSDT-XOSI.aml`：启用

## UEFI驱动

- `apfs_aligned.efi`：启用
- `HfsPlus.efi`：启用
- `OpenRuntime.efi`：启用
- `ResetNvramEntry.efi`：启用
