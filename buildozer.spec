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
android.permissions = INTERNET,CAMERA
debug = True
android.target_sdk_version = 34
android.min_sdk_version = 24
android.ndk = 26b
android.sdk_path = /usr/local/lib/android/sdk
android.ant_path = /usr/bin/ant
