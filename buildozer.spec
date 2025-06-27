[app]

# (str) Title of your application
title = FaceApp Attendance

# (str) Package name (MUST BE UNIQUE, e.g., com.yourname.yourapp)
# IMPORTANT: Change 'yourcompany' and 'faceapp' to something unique to you.
package.name = com.yourcompany.faceapp

# (str) Package domain (needed for android/ios packaging)
# IMPORTANT: Change 'yourcompany.com' to your own domain or a unique placeholder.
package.domain = yourcompany.com

# (str) Application versioning (method 1)
version = 0.1

# (str) Kivy application main file
# IMPORTANT: This must match the exact filename of your main Python app.
# Based on your provided code, it is 'face_recognition.py'.
main.py = main.py

# (str) The directory where your source code is located
# '.' means the current directory (the root of your project)
source.dir = .

# (list) Source files to include (let empty to include all the files
# in the current directory)
# Ensure all your Python files, images, and audio files are included.
source.include_exts = py,png,jpg,mp3,wav,kv,xml,json

# (list) Application requirements
# These packages will be installed by pip in the Android environment.
# 'cython' is crucial for Kivy and many Python extensions to compile for Android.
requirements = python3,kivy,opencv,numpy,requests,setuptools,pyjnius,android,certifi,cython

# (str) Kivy version to use
kivy.version = 2.3.0

# (str) Android API level to use (targetSdkVersion)
# Using a recent stable API level for better compatibility and security.
android.api = 33

# (str) Minimum Android API level required (minSdkVersion)
android.minapi = 21

# (str) Android target SDK version (same as android.api for consistency)
android.targetsdk = 33

# (list) Android architecture to build for
# Building for both common ARM architectures for broader device compatibility.
android.archs = arm64-v8a, armeabi-v7a

# (str) Specify the NDK version to use. This can help with build stability.
# NDK r25b (version 25.2.8704281) is often a stable choice for Kivy/OpenCV.
android.ndk = 25b

# (bool) Enable multidex for apps with a large number of methods.
# This helps prevent "Too many methods" errors during compilation.
android.enable_multidex = 1

# (list) Android permissions
# INTERNET for Google Forms/email, CAMERA for webcam,
# READ/WRITE_EXTERNAL_STORAGE for broader compatibility (though user_data_dir is internal).
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Icon file to use. This should be a .png file in your project root.
# Uncomment and specify if you have a custom icon (e.g., 'icon.png').
# icon.filename = %(source.dir)s/icon.png

# (str) A string that specifies the orientation of the screen.
orientation = portrait

# (int) The version number of your application.
# This is an integer value that is incremented with each release.
android.version_code = 1
