[app]
title = FaceRecognitionApp
package.name = facerecognition
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 1.0
orientation = portrait
fullscreen = 1
icon.filename = tick.png
presplash.filename = tick.png
requirements = python3,kivy,numpy,opencv,openpyxl,plyer
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = armeabi-v7a, arm64-v8a
android.gradle_dependencies = com.android.tools.build:gradle:8.4.0
android.gradle_options = -Dorg.gradle.jvmargs="-Xmx4600m"
