[app]
title = FaceApp Attendance
package.name = faceappattendance
package.domain = org.test
version = 0.1
requirements = python3,kivy==2.2.1,opencv-python,numpy,requests
categories = business
source.dir = .
source.include_exts = py,png,mp3,kv,json
main.py = main.py
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
debug = True
android.target_sdk_version = 34
# android.min_sdk_version = 34  # Removed this line to avoid conflict
android.ndk = 25b
android.sdk_path = /usr/local/lib/android/sdk
android.ant_path = /usr/bin/ant
android.api = 34
android.ndk_api = 34
