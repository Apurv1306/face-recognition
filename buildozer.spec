[app]

# (str) Title of your application
title = FaceApp Attendance

# (str) Package name
package.name = faceappattendance

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.2.1,opencv-python,numpy,requests

# (str) The category of the application
# semi-colon separated e.g. categories = entertainment;
categories = business

# (list) List of service to declare
# services = NAME:ENTRYPOINT_FILE.py

# (str) Kivy version to use
kivy.version = 2.2.1

# (str) Source code where the main.py lives
source.dir = .

# (list) List of inclusions for the APK (relative to the source.dir)
source.include_exts = py,png,mp3,kv,json

# (list) List of exclusions for the APK (relative to the source.dir)
# source.exclude_dirs = tests, bin

# (str) The entry point of your application
main.py = main.py

# (bool) If your application uses Cython for speedup (default is False)
# cython = False

# (list) Android permissions
# android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.permissions = INTERNET,CAMERA

# (bool) Enable or disable the debug mode
debug = True

# (list) Android target SDK version
# android.target_sdk_version = 33

# (list) Android minimum SDK version
# android.min_sdk_version = 21

# (str) Android NDK version
# android.ndk = 25b

# (str) Android SDK version
# android.sdk = 33

# (str) Android API level to use
# android.api = 21

# (str) Android NDK path (if not set, Buildozer will download it)
# android.ndk_path = /opt/android-ndk

# (str) Android SDK path (if not set, Buildozer will download it)
# android.sdk_path = /opt/android-sdk

# (str) Java Development Kit path (if not set, Buildozer will download it)
# android.jdk_path = /opt/jdk

# (str) The default orientation of the application (portrait or landscape)
# android.orientation = portrait

# (bool) If you want to use the Android support library (default is False)
# android.enable_multidex = False

# (bool) If you want to enable the Android debug bridge (adb)
# android.enable_adb = False

# (bool) If you want to enable the Android Logcat
# android.enable_logcat = False

# (bool) If you want to enable the Android profiling
# android.enable_profiling = False

# (bool) If you want to enable the Android build with Gradle
# android.enable_gradle = False

# (str) The name of the keystore file to sign the APK
# android.release_keystore = my-release-key.keystore

# (str) The alias of the key in the keystore
# android.release_keyalias = my-key-alias

# (str) The password of the keystore
# android.release_storepass = password

# (str) The password of the key
# android.release_keypass = password

# (bool) If you want to sign the APK (default is False)
# android.signed_apk = False

# (bool) If you want to zipalign the APK (default is False)
# android.zipalign = False

# (bool) If you want to clean the build directory before building
# android.force_build = False

# (bool) If you want to install the APK on the device after building
# android.install_on_device = False

# (bool) If you want to run the application on the device after installing
# android.run_on_device = False

# (bool) If you want to deploy the application on the device after building
# android.deploy_on_device = False

# (bool) If you want to enable the Android P4A (Python for Android)
# android.enable_p4a = False

# (str) The name of the P4A distribution
# android.p4a_dist_name = my_p4a_dist

# (list) The list of P4A recipes to include
# android.p4a_recipes = hostpython3,kivy,openssl,requests,sqlite3

# (str) The URL to the P4A repository
# android.p4a_url = https://github.com/kivy/python-for-android.git

# (str) The branch of the P4A repository
# android.p4a_branch = master

# (str) The commit hash of the P4A repository
# android.p4a_commit =

# (bool) If you want to use the P4A local build
# android.p4a_local_build = False

# (str) The path to the P4A local build directory
# android.p4a_local_build_dir = /tmp/p4a_build

# (list) The list of P4A command line arguments
# android.p4a_args =

# (bool) If you want to use the P4A debug mode
# android.p4a_debug = False

# (bool) If you want to use the P4A verbose mode
# android.p4a_verbose = False

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4a custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_ndk = False

# (str) The path to the P4A custom NDK
# android.p4a_custom_ndk_path =

# (bool) If you want to use the P4A with a custom JDK
# android.p4a_use_custom_jdk = False

# (str) The path to the P4A custom JDK
# android.p4a_custom_jdk_path =

# (bool) If you want to use the P4A with a custom Gradle
# android.p4a_use_custom_gradle = False

# (str) The path to the P4A custom Gradle
# android.p4a_custom_gradle_path =

# (bool) If you want to use the P4A with a custom Ant
# android.p4a_use_custom_ant = False

# (str) The path to the P4A custom Ant
# android.p4a_custom_ant_path =

# (bool) If you want to use the P4A with a custom Maven
# android.p4a_use_custom_maven = False

# (str) The path to the P4A custom Maven
# android.p4a_custom_maven_path =

# (bool) If you want to use the P4A with a custom pip
# android.p4a_use_custom_pip = False

# (str) The path to the P4A custom pip
# android.p4a_custom_pip_path =

# (bool) If you want to use the P4A with a custom virtualenv
# android.p4a_use_custom_virtualenv = False

# (str) The path to the P4A custom virtualenv
# android.p4a_custom_virtualenv_path =

# (bool) If you want to use the P4A with a custom wheel
# android.p4a_use_custom_wheel = False

# (str) The path to the P4A custom wheel
# android.p4a_custom_wheel_path =

# (bool) If you want to use the P4A with a custom buildozer
# android.p4a_use_custom_buildozer = False

# (str) The path to the P4A custom buildozer
# android.p4a_custom_buildozer_path =

# (bool) If you want to use the P4A with a custom toolchain
# android.p4a_use_custom_toolchain = False

# (str) The path to the P4A custom toolchain
# android.p4a_custom_toolchain_path =

# (bool) If you want to use the P4A with a custom SDK
# android.p4a_use_custom_sdk = False

# (str) The path to the P4A custom SDK
# android.p4a_custom_sdk_path =

# (bool) If you want to use the P4A with a custom NDK
# android.p4a_use_custom_
