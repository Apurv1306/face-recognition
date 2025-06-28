[app]
# Title and package metadata
title           = FaceAttendanceApp
package.name    = faceattendance
package.domain  = org.yourorg

# Source files
source.dir      = .
source.include_exts = py,mp3,png,jpg,kv,txt

# App version
version         = 0.1

# Python requirements
# — must include everything main.py imports:
requirements    = python3,kivy,opencv-python,numpy,playsound,openpyxl

# Orientation
orientation      = portrait

# Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE

# (Optional) If you need to access the file system at runtime:
#android.request_camerapermission = True

[buildozer]
# Target API and architectures
android.api     = 31
android.ndk     = 23b
android.archs   = armeabi-v7a,arm64-v8a

# (Optional) Increase log verbosity
log_level       = 2
