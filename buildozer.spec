[app]
# ─────────────────────────────────────────────────────────────
# 1.  Application Metadata
# ─────────────────────────────────────────────────────────────
title = Face Attendance
package.name = faceattendance
package.domain = com.digitalapurv
version = 1.0.0

# ─────────────────────────────────────────────────────────────
# 2.  Source Files & Assets
# ─────────────────────────────────────────────────────────────
source.dir = .
entrypoint = main.py
source.include_exts = py,kv,png,jpg,jpeg,atlas,xlsx,mp3,wav,ttf,txt

# ─────────────────────────────────────────────────────────────
# 3.  Python / Native Dependencies (p4a recipe names)
# ─────────────────────────────────────────────────────────────
requirements = python3,kivy,opencv,numpy,pillow,openpyxl,pyglet

# ─────────────────────────────────────────────────────────────
# 4.  Build Bootstrap & Android Toolchain
# ─────────────────────────────────────────────────────────────
bootstrap = sdl2
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a
android.enable_androidx = True
android.copy_libs = True

# ─────────────────────────────────────────────────────────────
# 5.  Runtime Behaviour
# ─────────────────────────────────────────────────────────────
orientation = portrait
fullscreen = False
android.keep_screen_on = True

# ─────────────────────────────────────────────────────────────
# 6.  Permissions
# ─────────────────────────────────────────────────────────────
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,VIBRATE

# ─────────────────────────────────────────────────────────────
# 7.  Optional Icons / Splash (uncomment & supply files)
# ─────────────────────────────────────────────────────────────
# icon.filename = %(source.dir)s/data/icon.png
# android.presplash_color = #FFFFFF

# ─────────────────────────────────────────────────────────────
# 8.  Host‑side System Packages (fixes most compile errors)
# ─────────────────────────────────────────────────────────────
apt_packages = build-essential,autoconf,automake,libtool,libtool-bin,make,gcc,g++,pkg-config,libjpeg-dev,zlib1g-dev,libfreetype6-dev,libpng-dev,libblas-dev,liblapack-dev,ffmpeg

# ─────────────────────────────────────────────────────────────
# 9.  Advanced p4a / Gradle Tweaks (optional)
# ─────────────────────────────────────────────────────────────
# p4a.branch = master
# android.gradle_dependencies = androidx.multidex:multidex:2.0.1
# android.add_javac_opts = -Xmx4096M

# ─────────────────────────────────────────────────────────────
# 10. Buildozer Behaviour
# ─────────────────────────────────────────────────────────────
[buildozer]
log_level = 2
warn_on_root = 1
# clean_build = 1
