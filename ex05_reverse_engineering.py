# Ex. No. : 5 - REVERSE ENGINEERING OF ANDROID APPLICATIONS
# AIM: To perform reverse engineering on an Android application to understand its architecture.

from androguard.misc import AnalyzeAPK

apk, dex, analysis = AnalyzeAPK("uptodown-com.OfflineGames.apk")

print("Application Activities")
print("----------------------")
for activity in apk.get_activities():
    print(activity)

print("\nApplication Services")
print("----------------------")
for service in apk.get_services():
    print(service)

print("\nBroadcast Receivers")
print("----------------------")
for receiver in apk.get_receivers():
    print(receiver)
