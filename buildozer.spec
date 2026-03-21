[app]

# (str) Title of your application
title = 注册码生成工具

# (str) Package name
package.name = licensegen

# (str) Package domain (needed for android/ios packaging)
package.domain = com.sxh

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license, images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
#version.regex = __version__ = ['"](.*)['"]
#version.filename = %(source.dir)s/main.py

# (list) Application requirements
# 如果你的代码还用到了其他库，比如 requests、openpyxl 等，请加在这里
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ./kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 25c

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage to True or False
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) Android addional directories to add to the java classpath
#android.add_src =

# (list) List of Java .jar files to add to the libs so that they can be included at packaging time.
#android.add_jars =

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src =

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_libraries =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = arm64-v8a

#
# iOS specific
#
ios.python_version = 3
# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# (bool) Enable debug on iOS
ios.debug = False
# (list) iOS frameworks to add
#ios.frameworks = libSDL2.dll

#
# Blackberry specific
#
# (bool) If True the package will be a blackberry native package instead of a bar file.
blackberry.native_package = False
# (list) Permissions
#blackberry.permissions = access_internet, play_audio, read_geolocation, record_audio, set_audio_volume, use_camera
# (list) BlackBerry signing keys
#blackberry.debug_token = debugtoken
# (str) BlackBerry NDK path
#blackberry.ndk_path = C:\bbndk\host_10_2_0_132\win32\x86\usr\bin
# (str) BlackBerry signing server signing key
#blackberry.signing_key = author.p12
# (str) BlackBerry signing server csj file
#blackberry.csj_file = author.csj
# (str) BlackBerry signing server password
#blackberry.password = password

# (str) Path to blackberry deploy tool
#blackberry.deploy_path = blackberry-deploy

# (list) BlackBerry signing server domains
#blackberry.domain = blackberry.com

# (list) Additional dependencies
#blackberry.dependencies =

# (list) Additional blackberry permissions
#blackberry.permissions =

# (bool) Make the application (and its python dependencies) as a single bar file
blackberry.bar = True