# Ex. No. : 1 - BASIC ANDROID APK ANALYSIS
# AIM: To analyze the structure and contents of an Android Application Package (APK) file.

import zipfile

apk_file = "uptodown-com.OfflineGames.apk"

try:
    with zipfile.ZipFile(apk_file, "r") as apk:
        print("APK CONTENTS")
        print("-----------------------------")
        for file in apk.namelist():
            print(file)
except FileNotFoundError:
    print("APK file not found.")
