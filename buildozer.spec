[app]

title = Universal Units
package.name = universalunits
package.domain = com.kundan.universalunits

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.4

requirements = python3,kivy,kivymd==1.1.1,pillow

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.presplash_color = #027783
android.permissions = INTERNET

# ✅ Play Store required
android.api = 35
android.minapi = 21

# ✅ IMPORTANT: Fix 16KB issue
android.ndk = 25b
p4a.branch = develop

# CPU architectures
android.archs = arm64-v8a, armeabi-v7a

# ✅ Version must increase
android.numeric_version = 1021103

android.allow_backup = True
android.accept_sdk_license = True
android.copy_libs = 1

android.release_artifact = aab
android.debug_artifact = apk

# -------- SIGNING --------
android.release_keystore = upload-key.keystore
android.release_keyalias = upload
android.release_keystore_password = Krishna7546@#
android.release_keyalias_password = Krishna7546@#


[buildozer]

log_level = 2
warn_on_root = 1
