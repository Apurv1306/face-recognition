[app]
# ─────────────────────────────────────────────
# 1.  Application Metadata
# ─────────────────────────────────────────────
title = Face Attendance
package.name = faceattendance
package.domain = com.digitalapurv
version = 1.0.0

# ─────────────────────────────────────────────
# 2.  Source Files & Assets
# ─────────────────────────────────────────────
source.dir = .
entrypoint = main.py
source.include_exts = py,kv,png,jpg,jpeg,atlas,xlsx,mp3,wav,ttf,txt

# ─────────────────────────────────────────────
# 3.  Python / Native Dependencies (p4a recipes)
# ─────────────────────────────────────────────
requirements = python3,kivy,opencv,numpy,pillow,openpyxl,pyglet

# ─────────────────────────────────────────────
# 4.  Android Toolchain
# ─────────────────────────────────────────────
bootstrap          = sdl2
android.api        = 31
android.minapi     = 21
android.ndk_api    = 21
android.ndk        = 23b            # maps to 23.1.7779620
android.accept_sdk_license = 1
android.archs      = arm64-v8a,armeabi-v7a
android.enable_androidx = 1
android.copy_libs  = 1              # bundle stray .so files

# ─────────────────────────────────────────────
# 5.  Runtime Behaviour
# ─────────────────────────────────────────────
orientation             = portrait
fullscreen              = 0         # 0 = normal, 1 = immersive
android.keep_screen_on  = 1

# ─────────────────────────────────────────────
# 6.  Permissions
# ─────────────────────────────────────────────
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE

# ─────────────────────────────────────────────
# 7.  Optional Icons / Splash
# ─────────────────────────────────────────────
# icon.filename       = %(source.dir)s/data/icon.png
# android.presplash_color = #FFFFFF

# ─────────────────────────────────────────────
# 8.  Host-side APT Packages
# ─────────────────────────────────────────────
apt_packages = build-essential,autoconf,automake,libtool,libtool-bin,make,gcc,g++,pkg-config,libjpeg-dev,zlib1g-dev,libfreetype6-dev,libpng-dev,libblas-dev,liblapack-dev,ffmpeg

# ─────────────────────────────────────────────
# 9.  Buildozer Behaviour
# ─────────────────────────────────────────────
[buildozer]
log_level   = 2
warn_on_root = 1
# clean_build = 1
