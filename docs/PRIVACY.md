# 公开副本的隐私处理

仅在上传副本进行处理，未更改正在使用的启动U盘：

- 清空 `PlatformInfo.Generic.SystemSerialNumber` 和 `MLB`。
- 将 `SystemUUID` 置为全零UUID，将6字节 `ROM` 置零。
- 清空OpenCore `Misc.Security.PasswordHash`、`PasswordSalt`。
- 排除历史 `config-before*.plist`、Finder元数据、日志；不上传原始备份、系统信息报告、屏幕录制、显示器原始EDID或NVIDIA安装日志。
- 对上传树全部文件搜索原始SMBIOS序列号、MLB、UUID和ROM的文本/二进制表示，未发现残留。

公开副本不是可直接替换使用的私人备份。使用前填写独立生成的机器身份信息，填写后的配置应保存在仓库外。不要将真实序列号、MAC地址、账户凭据或系统诊断日志直接提交到公开Issue。
