[app]
title = Face Attendance
package.name = faceattendance
package.domain = com.digitalapurv
version = 1.0.0

source.dir = .
entrypoint = main.py
source.include_exts = py,kv,png,jpg,jpeg,atlas,xlsx,mp3,wav,ttf,txt

requirements = python3,kivy,opencv,numpy,pillow,openpyxl,pyglet

bootstrap = sdl2
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.ndk = 25.1.8937393
android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a
android.enable_androidx = True
android.copy_libs = 1

orientation = portrait
fullscreen = 0
android.keep_screen_on = 1

android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE

# icon.filename = %(source.dir)s/data/icon.png
# android.presplash_color = #FFFFFF

apt_packages = build-essential,autoconf,automake,libtool,libtool-bin,make,gcc,g++,pkg-config,libjpeg-dev,zlib1g-dev,libfreetype6-dev,libpng-dev,libblas-dev,liblapack-dev,ffmpeg

[buildozer]
log_level = 2
warn_on_root = 1
