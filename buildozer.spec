[app]
# ─────────────────────── Application ───────────────────────
title             = FaceRecognitionApp
package.name      = facerecognition
package.domain    = org.example
version           = 1.0
orientation       = portrait
fullscreen        = 1
icon.filename     = tick.png                  # adjust if you have a real icon
source.dir        = .
source.include_exts = py,png,mp3,xlsx

# Entry point
# (Buildozer infers main.py automatically, but keep the line explicit)
main.py           = main.py

# ─────────────────────── Requirements ──────────────────────
#
#  ❗ IMPORTANT:
#  • Use **opencv** *only* if you replace your current OpenCV calls
#    with the p4a-compatible subset in the recipe.
#  • If you simply delete all `cv2` imports, remove “opencv” below.
#
requirements       = python3,kivy,opencv,numpy,openpyxl,plyer
android.need_dpi   = False                    # faster build if unneeded

# ────────────────── Android SDK / NDK / API ─────────────────
android.api        = 33                       # Target API level
android.minapi     = 21                       # Lowest supported Android
android.ndk        = 23b                      # Stable NDK
android.ndk_path   =                          # leave blank ⇒ fetched by CI

# ───────────────────── Permissions ──────────────────────────
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# ───────────────────── Architectures ────────────────────────
android.archs      = arm64-v8a,armeabi-v7a

# ───────────── Additional Gradle / Java Memory ─────────────
#  Avoid “DexArchiveMerger” OOM:
android.gradle_dependencies = com.android.tools.build:gradle:8.4.0
android.gradle_options = -Dorg.gradle.jvmargs="-Xmx4600m"

# ───────────────────── Customisations ───────────────────────
# Uncomment if you keep assets in these folders
# presplash.filename = presplash.png
# android.entrypoint = org.kivy.android.PythonActivity
