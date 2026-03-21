[app]
title = 注册码生成工具
package.name = licensegen
package.domain = com.sxh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

# Android 配置（关键修改）
android.api = 30
android.minapi = 21
android.ndk = 25c
android.sdk = 30
android.accept_sdk_license = True
android.arch = arm64-v8a

# 明确指定 Build-Tools 版本
android.build_tools = 30.0.3
