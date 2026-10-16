[app]
title = Brand New AI
package.name = brandnewai
package.domain = org.brandnew
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy,gtts,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WAKE_LOCK,FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.cmake = 3.22.1

[buildozer]
log_level = 2
warn_on_root = 1
