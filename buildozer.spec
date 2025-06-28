[app]
# App metadata
title           = FaceAttendanceApp
package.name    = faceattendance
package.domain  = org.yourorg
version         = 0.1

# Source files to include
source.dir      = .
source.include_exts = py,mp3,png,jpg,xlsx,kv

# Python modules your main.py imports
requirements    = python3,kivy,opencv,numpy,openpyxl,playsound

# (Optional) If you use any Kivy .kv files, list them here:
# kv_files       = yourlayout.kv

# Portrait only (camera preview)
orientation      = portrait

# Permissions your app needs
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE

# Let the user request the camera at runtime
android.request_camerapermission = True

[buildozer]
# Android SDK/NDK versions
android.api     = 31
android.ndk     = 23b
android.archs   = armeabi-v7a,arm64-v8a

# Enable verbose logs (optional)
log_level       = 2

# (Optional) If you need to bundle extra Java libs or specify Gradle deps:
# android.gradle_dependencies = 'com.github.bumptech.glide:glide:4.9.0'
