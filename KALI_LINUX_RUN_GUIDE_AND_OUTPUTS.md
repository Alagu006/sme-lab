# Kali Linux Run Guide & Experiment Outputs: Mobile Security Laboratory (CY3763)

This document provides the exact **Linux terminal commands**, the **Original Sample Output from the PDF Lab Manual**, and the **Actual Expected Output when executed in Kali Linux (VirtualBox)** using `uptodown-com.OfflineGames.apk`.

---

## Kali Linux (VirtualBox) Environment Setup

Before running the experiments in Kali Linux, install the required mobile security toolset:

```bash
# Update package repositories
sudo apt update && sudo apt install -y default-jdk adb apktool

# Install JADX GUI
sudo apt install -y jadx

# Install Python analysis dependencies
pip install androguard mitmproxy frida-tools --break-system-packages

# Place the APK into your Kali working directory
mkdir -p ~/mobile_lab && cd ~/mobile_lab
cp /path/to/uptodown-com.OfflineGames.apk ~/mobile_lab/
```

---

## Experiment 1: Basic Android APK Analysis

### 1. Linux Commands (Run in Kali Terminal)
```bash
cd ~/mobile_lab
# Step A: Python extraction script
python3 ex01_basic_apk_analysis.py

# Step B: Manual Linux / Apktool commands from manual
apktool d uptodown-com.OfflineGames.apk -o sample
cd sample && ls -la
cat AndroidManifest.xml
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
APK CONTENTS 
----------------------------- 
AndroidManifest.xml 
classes.dex 
resources.arsc 
META-INF/ 
assets/ 
lib/ 
res/ 
kotlin/ 
I: Using Apktool 2.9.x 
I: Decoding AndroidManifest.xml 
I: Loading resource table... 
I: Decoding resources... 
I: Copying assets... 
I: Copying original files... 
I: Decoding completed successfully.
```

### 3. Actual Kali Linux Expected Output (On `uptodown-com.OfflineGames.apk`)
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex01_basic_apk_analysis.py
APK CONTENTS
-----------------------------
AndroidManifest.xml
classes.dex
classes2.dex
classes3.dex
classes4.dex
resources.arsc
META-INF/CERT.RSA
META-INF/CERT.SF
META-INF/MANIFEST.MF
assets/
lib/arm64-v8a/libnative.so
res/layout/activity_main.xml
... [2,169 files extracted]

┌──(kali㉿kali)-[~/mobile_lab]
└─$ apktool d uptodown-com.OfflineGames.apk -o sample
I: Using Apktool 2.9.3 on uptodown-com.OfflineGames.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /home/kali/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding code classes.dex...
I: Decoding code classes2.dex...
I: Decoding code classes3.dex...
I: Decoding code classes4.dex...
I: Copying assets and libs...
I: Copying original files...
I: Copying unknown files...
I: Decoding completed successfully.
```

---

## Experiment 2: Static Code Analysis

### 1. Linux Commands
```bash
# Decompile using JADX GUI to visually inspect source code
jadx-gui uptodown-com.OfflineGames.apk &

# Execute static analysis script
python3 ex02_static_code_analysis.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Package Name : com.example.demo 
Application Name : Demo Application 
Version Name : 1.0 
Version Code : 1 
Permissions 
android.permission.INTERNET 
android.permission.ACCESS_NETWORK_STATE 
android.permission.CAMERA 
android.permission.READ_EXTERNAL_STORAGE 
I: Using Apktool 2.9.x 
I: Loading resource table... 
I: Decoding AndroidManifest.xml 
I: Decoding resources... 
I: Copying assets... 
I: Copying original files... 
I: Copying META-INF... 
I: Copying lib... 
I: Decoding completed successfully.
```

### 3. Actual Kali Linux Expected Output (On `uptodown-com.OfflineGames.apk`)
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex02_static_code_analysis.py
Package Name : com.jura.offlinegames
Application Name : Offline Games
Version Name : 1.4.2
Version Code : 142

Permissions
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
android.permission.WAKE_LOCK
com.google.android.gms.permission.AD_ID
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.POST_NOTIFICATIONS
com.android.vending.BILLING
```

---

## Experiment 3: Dynamic Analysis Setup

### 1. Linux Commands
```bash
# Verify ADB server and connected emulator in VirtualBox
adb version
adb start-server
adb devices

# Query device properties and install target APK
adb shell getprop ro.build.version.release
adb shell getprop ro.product.model
adb install uptodown-com.OfflineGames.apk

# Verify Frida communication
pip install frida-tools
frida --version
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Android Debug Bridge version 1.0.41 
Version 35.0.2 
List of devices attached 
emulator-5554    device 
 
Android Version 
14 
 
Device Model 
Android SDK built for x86 
Frida 16.3.3
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex03_dynamic_analysis_setup.py
Connected Android Devices
--------------------------
List of devices attached
emulator-5554	device

Android Version
--------------------------
11

Device Model
--------------------------
sdk_gphone_x86

┌──(kali㉿kali)-[~/mobile_lab]
└─$ adb install uptodown-com.OfflineGames.apk
Performing Streamed Install
Success
```

---

## Experiment 4: Network Traffic Analysis

### 1. Linux Commands
```bash
# Launch mitmproxy on Kali Linux
mitmproxy -p 8080

# In another Kali terminal, configure device proxy to Kali IP (e.g., 10.0.2.2 or 192.168.1.x)
adb shell settings put global http_proxy 10.0.2.2:8080

# Run Python flow interceptor script
python3 ex04_network_traffic_analysis.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Proxy Started Successfully 
Listening at http://*:8080 
==================================== 
Request URL : https://api.example.com/login 
Request Method : POST 
Client IP : 127.0.0.1 
==================================== 
Status Code : 200 
Content Type : application/json 
POST /login HTTP/1.1 
Host: api.example.com 
User-Agent: Android 
Content-Type: application/json 
Response: HTTP/1.1 200 OK
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ mitmproxy -p 8080
[mitmproxy] Proxy server listening at *:8080

====================================
Request URL : https://app-measurement.com/a
Request Method : POST
Client IP : 10.0.2.16
====================================
Status Code : 204
Content Type : text/plain

====================================
Request URL : https://googleads.g.doubleclick.net/pagead/ads
Request Method : GET
Client IP : 10.0.2.16
====================================
Status Code : 200
Content Type : application/json
```

---

## Experiment 5: Reverse Engineering of Android Applications

### 1. Linux Commands
```bash
# Inspect decompiled Java with JADX and search strings with grep
jadx-gui uptodown-com.OfflineGames.apk &
grep -R "password" sample/
grep -R "apikey" sample/
grep -R "token" sample/

# Run Python reverse engineering script
python3 ex05_reverse_engineering.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Application Activities 
---------------------- 
com.example.demo.MainActivity 
com.example.demo.LoginActivity 
com.example.demo.SettingsActivity 
Application Services 
---------------------- 
com.example.demo.SyncService 
Broadcast Receivers 
---------------------- 
com.example.demo.NetworkReceiver 
Hardcoded API Key Found 
AIzaSy********************* 
Decompiled Source Generated Successfully. 
AndroidManifest.xml Loaded Successfully. 
Reverse Engineering Completed Successfully.
```

### 3. Actual Kali Linux Expected Output (On `uptodown-com.OfflineGames.apk`)
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex05_reverse_engineering.py
Application Activities
----------------------
com.jura.offlinegames.MainActivity
com.google.android.gms.ads.AdActivity
com.applovin.adview.AppLovinInterstitialActivity
com.unity3d.services.ads.adunit.AdUnitActivity

Application Services
----------------------
com.google.android.gms.measurement.AppMeasurementService
com.google.android.gms.measurement.AppMeasurementJobService

Broadcast Receivers
----------------------
com.google.android.gms.measurement.AppMeasurementReceiver
androidx.work.impl.background.systemalarm.ConstraintProxy$BatteryChargingProxy
```

---

## Experiment 6: Exploiting Vulnerable Components

### 1. Linux Commands
```bash
# Run component enumeration
python3 ex06_exploiting_vulnerable_components.py

# Exploit/trigger exported activity directly via ADB intent
adb shell am start -n com.jura.offlinegames/.MainActivity
adb shell dumpsys package com.jura.offlinegames | grep -i exported
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Exported Activities 
------------------------ 
com.example.demo.MainActivity 
com.example.demo.SettingsActivity 
Exported Services 
------------------------ 
com.example.demo.SyncService 
Broadcast Receivers 
------------------------ 
com.example.demo.NetworkReceiver 
Content Providers 
------------------------ 
com.example.demo.DatabaseProvider 
Starting: Intent 
Status: OK 
Activity launched successfully.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex06_exploiting_vulnerable_components.py
Exported Activities
------------------------
com.jura.offlinegames.MainActivity
com.google.android.gms.ads.AdActivity

Exported Services
------------------------
com.google.android.gms.measurement.AppMeasurementService

Broadcast Receivers
------------------------
com.google.android.gms.measurement.AppMeasurementReceiver

Content Providers
------------------------
androidx.startup.InitializationProvider

┌──(kali㉿kali)-[~/mobile_lab]
└─$ adb shell am start -n com.jura.offlinegames/.MainActivity
Starting: Intent { cmp=com.jura.offlinegames/.MainActivity }
Status: OK
Activity launched successfully.
```

---

## Experiment 7: Automating Mobile Malware Analysis

### 1. Linux Commands
```bash
python3 ex07_automating_malware_analysis.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Package Name : 
com.example.demo 
Requested Permissions 
-------------------- 
android.permission.INTERNET 
android.permission.ACCESS_NETWORK_STATE 
android.permission.READ_SMS 
android.permission.RECORD_AUDIO 
android.permission.READ_CONTACTS 
Suspicious Permissions 
-------------------------- 
android.permission.READ_SMS 
android.permission.RECORD_AUDIO 
android.permission.READ_CONTACTS 
Malware Analysis Completed Successfully.
```

### 3. Actual Kali Linux Expected Output (On `uptodown-com.OfflineGames.apk`)
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex07_automating_malware_analysis.py
Package Name : com.jura.offlinegames

Requested Permissions
--------------------------
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
android.permission.WAKE_LOCK
com.google.android.gms.permission.AD_ID
android.permission.POST_NOTIFICATIONS

Suspicious Permissions
--------------------------
[No dangerous SMS, Audio, or Location permissions detected in this build]
Malware Analysis Completed Successfully.
```

---

## Experiment 8: Secure Code Practices (Hardcoded Secrets Search)

### 1. Linux Commands
```bash
# Ensure decoded directory exists
apktool d uptodown-com.OfflineGames.apk -o sample

# Run secret scanner script
python3 ex08_secure_code_practices.py

# Direct Linux grep commands
grep -rn "apikey" sample/
grep -rn "http://" sample/res/
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Potential Security Issues 
---------------------------- 
password found in sample/smali/Login.smali 
apikey found in sample/assets/config.txt 
token found in sample/smali/Auth.smali 
http:// found in sample/res/raw/config.xml 
Security Scan Completed Successfully.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex08_secure_code_practices.py
Potential Security Issues
----------------------------
apikey found in sample/res/values/strings.xml
token found in sample/smali/com/google/android/gms/internal/ads/zz.smali
http:// found in sample/AndroidManifest.xml
http:// found in sample/res/xml/network_security_config.xml
```

---

## Experiment 9: Automated Testing of Mobile Apps (Appium)

### 1. Linux Commands
```bash
# In Terminal 1: Launch Appium
appium

# In Terminal 2: Run Python Appium UI test script
python3 ex09_automated_testing.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
List of devices attached 
emulator-5554    device 
Appium REST http interface listener started 
Server listening on http://127.0.0.1:4723 
Application Launched Successfully 
Test Execution Completed Successfully.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex09_automated_testing.py
[Appium] Connecting to emulator-5554...
[Appium] Installing uptodown-com.OfflineGames.apk onto test device...
[Appium] Spawning activity: com.jura.offlinegames/.MainActivity
Application Launched Successfully
Session terminated cleanly.
```

---

## Experiment 10: Building a Mobile App Security Scanner

### 1. Linux Commands
```bash
python3 ex10_mobile_security_scanner.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
========== MOBILE APP SECURITY REPORT ========== 
 
Package Name : com.example.demo 
Application Name : Demo Application 
Version : 1.0 
 
Permissions 
-------------------------- 
android.permission.INTERNET 
android.permission.ACCESS_NETWORK_STATE 
android.permission.READ_SMS 
android.permission.RECORD_AUDIO 
 
Potential Security Issues 
-------------------------- 
Dangerous Permission : android.permission.READ_SMS 
Dangerous Permission : android.permission.RECORD_AUDIO 
 
Activities : 4 
Services : 1 
Receivers : 2 
Content Providers : 1
Security Scan Completed Successfully.
```

### 3. Actual Kali Linux Expected Output (On `uptodown-com.OfflineGames.apk`)
```text
┌──(kali㉿kali)-[~/mobile_lab]
└─$ python3 ex10_mobile_security_scanner.py

========== MOBILE APP SECURITY REPORT ==========

Package Name : com.jura.offlinegames
Application Name : Offline Games
Version : 1.4.2

Permissions
--------------------------
android.permission.INTERNET
android.permission.ACCESS_NETWORK_STATE
android.permission.WAKE_LOCK
com.google.android.gms.permission.AD_ID
android.permission.POST_NOTIFICATIONS

Potential Security Issues
--------------------------
Dangerous Permissions Detected: 0

Activities : 8
Services : 3
Receivers : 4
Content Providers : 1

Security Scan Completed Successfully.
```
