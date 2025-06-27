[app]
title = FaceRecognitionApp
package.name = facerecognition
package.domain = org.example
source.dir = .
source.include_exts = py,png,mp3,xlsx
version = 1.0
requirements = python3,kivy==2.0.0,numpy,playsound,openpyxl,pillow
orientation = portrait
fullscreen = 1

# Entry point
main.py = main.py

# Presplash and Icon (optional if tick.png is just used in code)
icon.filename = tick.png

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# Android-specific requirements
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# Audio and camera support
android.enable_camera = 1
android.entrypoint = org.kivy.android.PythonActivity

# Uncomment to package assets if needed
# android.source.include_exts = mp3,png,xlsx

# (Optional) Presplash image
# presplash.filename = presplash.png

# Application storage
android.private_storage = True
