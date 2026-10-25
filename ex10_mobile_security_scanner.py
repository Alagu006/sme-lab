# Ex. No. : 10 - BUILDING A MOBILE APP SECURITY SCANNER
# AIM: To develop a Python-based Mobile App Security Scanner that automatically analyzes an Android APK file.

from androguard.misc import AnalyzeAPK

dangerous_permissions = [
    "android.permission.READ_SMS",
    "android.permission.SEND_SMS",
    "android.permission.READ_CONTACTS",
    "android.permission.RECORD_AUDIO",
    "android.permission.ACCESS_FINE_LOCATION"
]

apk, dex, analysis = AnalyzeAPK("uptodown-com.OfflineGames.apk")

print("\n========== MOBILE APP SECURITY REPORT ==========\n")
print("Package Name :", apk.get_package())
print("Application Name :", apk.get_app_name())
print("Version :", apk.get_androidversion_name())

print("\nPermissions")
print("--------------------------")
permissions = apk.get_permissions()
for permission in permissions:
    print(permission)

print("\nPotential Security Issues")
print("--------------------------")
for permission in permissions:
    if permission in dangerous_permissions:
        print("Dangerous Permission :", permission)

print("\nActivities :", len(apk.get_activities()))
print("Services :", len(apk.get_services()))
print("Receivers :", len(apk.get_receivers()))
print("Content Providers :", len(apk.get_providers()))

print("\nSecurity Scan Completed Successfully.")
