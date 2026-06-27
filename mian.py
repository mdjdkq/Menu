[app]
title = FPS Helper
package.name = fpsapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,numpy

orientation = landscape
osx.kivy_version = 2.1.0
fullscreen = 1

android.permissions = INTERNET, SYSTEM_ALERT_WINDOW
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

