# Ex. No. : 2 - STATIC CODE ANALYSIS
# AIM: To perform static code analysis on an Android application.

try:
    from loguru import logger
    logger.remove()
    from androguard.core.apk import APK
    apk = APK("uptodown-com.OfflineGames.apk")
except Exception:
    from androguard.misc import AnalyzeAPK
    apk, dex, analysis = AnalyzeAPK("uptodown-com.OfflineGames.apk")

print("Package Name :", apk.get_package())
print("Application Name :", apk.get_app_name())
print("Version Name :", apk.get_androidversion_name())
print("Version Code :", apk.get_androidversion_code())

print("\nPermissions")
for permission in apk.get_permissions():
    print(permission)
