# Ex. No. : 3 - DYNAMIC ANALYSIS SETUP
# AIM: To set up a dynamic analysis environment for Android applications using ADB and Frida.

import subprocess

print("Connected Android Devices")
print("--------------------------")
subprocess.run(["adb", "devices"])

print("\nAndroid Version")
print("--------------------------")
subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"])

print("\nDevice Model")
print("--------------------------")
subprocess.run(["adb", "shell", "getprop", "ro.product.model"])
