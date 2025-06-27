name: Build APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y libffi-dev libssl-dev \
          libsqlite3-dev libjpeg-dev zlib1g-dev \
          libncurses5 libncurses5-dev libncursesw5-dev \
          libtinfo5 libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
          libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev \
          libavcodec-dev libfreetype6-dev libglib2.0-dev libmtdev-dev \
          build-essential git-core python3-pip python3-setuptools \
          zip unzip openjdk-17-jdk curl wget

    - name: Install Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer cython

    - name: Initialize Buildozer (if needed)
      run: |
        cd ${{ github.workspace }}
        buildozer init || true

    - name: Build APK
      run: |
        cd ${{ github.workspace }}
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: FaceRecognitionApp
        path: bin/*.apk
"""
