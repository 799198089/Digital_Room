# 这个文件用于简要说明如何在Ubuntu电脑上运行 在Windows系统下分发的Unity的程序

## 基本信息
* 图形API: 一般情况下，Windows使用Direct X, Linux使用OpenGL图形APIs
* Unity 3DGS插件在Linux系统下仅支持Vulkan APIs

## Windows下的Unity设置
* 在Unity Hub中为对应Unity版本添加Linux Build Support
* 为方便调试，在Unity Project Settings/Player/Graphics APIs中，将两种系统的图形API统一设定为Vulkan  
* 在Project Settings/Quality中disable Anti Aliasing，否则会导致画面发白

## Ubuntu设置
* apt安装Vulkan
* 对build得到的.x86_64文件设置权限(chmod 777)
* 使用./xxx.x86_64命令来启动Unity分发程序
