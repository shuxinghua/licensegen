[app]

title = 注册码生成工具
package.name = licensegen
package.domain = com.sxh
source.dir = .
source.include_exts = py,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 25c
android.ndk_api = 21
android.accept_sdk_license = True
android.arch = arm64-v8a

# 关键优化：跳过所有非必要的依赖下载
android.reduce_sdl2_image_deps = 1
android.sdl2_image_deps = 0
p4a.ignore_git = 1

[buildozer]
log_level = 2
