# Mobile Security Laboratory: Experiment Guide & Troubleshooting Manual

This guide details what to observe, potential errors, and step-by-step rectifications for all 10 experiments in the **CY3763 – Security in Mobile Exploitation Laboratory** using `uptodown-com.OfflineGames.apk`.

---

## Quick Reference Table

| Ex. No. | Experiment Title | Primary Tool / Library | Key Focus Area | Common Gotcha |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Basic Android APK Analysis | Python `zipfile` | Archive structure & assets | Console flooded by 2,000+ files |
| **02** | Static Code Analysis | Androguard (`AnalyzeAPK`) | Package, Version, Permissions | Freezing/Debug log spam during DEX parse |
| **03** | Dynamic Analysis Setup | ADB, Frida | Emulator connection, properties | ADB server offline / Device unauthorized |
| **04** | Network Traffic Analysis | mitmproxy | HTTP/HTTPS requests & headers | SSL Handshake failure / Cert Pinning |
| **05** | Reverse Engineering | Androguard, APKTool, JADX | Decompiled classes, services | Multi-DEX analysis lag |
| **06** | Exploiting Vulnerable Components | Androguard | Exported activities & receivers | Protected vs. Unprotected components |
| **07** | Automating Malware Analysis | Androguard | Dangerous permission mapping | False positives on legitimate apps |
| **08** | Secure Code Practices | Python file scanner | Hardcoded keys, tokens, `http://` | `FileNotFoundError` if `sample/` missing |
| **09** | Automated Testing | Appium, Selenium | Automated UI launch & session | Port 4723 connection refused |
| **10** | Mobile Security Scanner | Androguard scanner | Comprehensive security report | Memory overhead on production APKs |

---

## Detailed Experiment Guides

### Experiment 1: Basic Android APK Analysis
- **What to Look Out For:**
  - Verify that the target file is a valid PKZip archive containing the core Android files:
    - `AndroidManifest.xml` (binary configuration)
    - `classes.dex`, `classes2.dex` (Dalvik executable bytecode)
    - `resources.arsc` (compiled resources table)
    - `META-INF/` (cryptographic signatures: `CERT.RSA`, `CERT.SF`, `MANIFEST.MF`)
    - `lib/` (native shared object libraries: `.so` files for `arm64-v8a`, `armeabi-v7a`, `x86`)
- **Possible Errors:**
  1. `FileNotFoundError: [Errno 2] No such file or directory`: Script cannot locate `uptodown-com.OfflineGames.apk`.
  2. `zipfile.BadZipFile: File is not a zip file`: APK download was corrupted or incomplete.
  3. **Console Flooding:** In real-world apps like `uptodown-com.OfflineGames.apk`, iterating all names prints 2,169 lines instantly.
- **How to Rectify:**
  - Place `uptodown-com.OfflineGames.apk` in the same directory as the script or specify the full path.
  - Verify file integrity: ensure file size is approximately 14.8 MB.
  - For clean presentation in viva or papers, print counts of file categories rather than the full raw list.

---

### Experiment 2: Static Code Analysis
- **What to Look Out For:**
  - Application package identifier (e.g. `com.jura.offlinegames`).
  - Target/Min SDK versions and version code.
  - Declared permissions (e.g., `android.permission.INTERNET`, `ACCESS_NETWORK_STATE`).
- **Possible Errors:**
  1. **Terminal Flooded with Thousands of DEBUG Messages (`_create_basic_block`) / Long Delay:**
     - *Cause:* `AnalyzeAPK()` from `androguard.misc` automatically performs full control-flow graph (CFG) analysis across all 4 `.dex` files. In large production apps (with AndroidX and Jetpack Compose), this analyzes tens of thousands of methods and prints debug logs.
  2. `ModuleNotFoundError: No module named 'androguard'`.
- **How to Rectify:**
  - **Quick Fix (Disable Logging):** Before calling `AnalyzeAPK`, suppress Androguard's logger:
    ```python
    from loguru import logger
    logger.remove()  # disables debug log spam
    ```
  - **Optimal Fix (Fast Manifest Extraction):** If you only need manifest metadata (package, version, permissions), use Androguard's lightweight `APK` parser which runs in under 0.5 seconds:
    ```python
    from androguard.core.bytecodes.apk import APK
    apk = APK("uptodown-com.OfflineGames.apk")
    print("Package:", apk.get_package())
    ```
  - If module is missing: `pip install androguard`.

---

### Experiment 3: Dynamic Analysis Setup (ADB & Frida)
- **What to Look Out For:**
  - `adb devices` returns an attached emulator (e.g., `emulator-5554    device`).
  - System property queries return valid Android release version (`getprop ro.build.version.release` $\rightarrow$ `11`, `12`, `13`, or `14`).
- **Possible Errors:**
  1. `'adb' is not recognized as an internal or external command`: ADB is not added to the system `PATH`.
  2. `List of devices attached` is empty: Emulator is not running or USB debugging is disabled.
  3. Device listed as `unauthorized` or `offline`.
- **How to Rectify:**
  - Add Android SDK platform-tools (`C:\Users\<user>\AppData\Local\Android\Sdk\platform-tools`) to system environment variables.
  - Launch Android Studio AVD (Android Virtual Device) before running the script.
  - Restart the ADB daemon:
    ```bash
    adb kill-server
    adb start-server
    adb devices
    ```
  - Unlock the emulator screen and accept the **"Allow USB Debugging"** RSA fingerprint prompt.

---

### Experiment 4: Network Traffic Analysis (mitmproxy)
- **What to Look Out For:**
  - Captured HTTP/HTTPS request URLs, request methods (`GET`, `POST`), and client IP addresses.
  - Server response codes (e.g., `200 OK`, `302 Found`, `403 Forbidden`).
- **Possible Errors:**
  1. `Address already in use`: Another service is using port 8080.
  2. `SSL: CERTIFICATE_VERIFY_FAILED`: Target app fails HTTPS handshakes due to Android Network Security Configuration or Certificate Pinning.
- **How to Rectify:**
  - Launch mitmproxy on a custom port: `mitmproxy -p 8888`.
  - On the Android device/emulator, navigate to `http://mitm.it` in the browser, download the certificate, and install it under **Settings $\rightarrow$ Security $\rightarrow$ Install from Storage**.
  - For apps using certificate pinning, use a Frida script to bypass trust-manager checks.

---

### Experiment 5: Reverse Engineering of Android Applications
- **What to Look Out For:**
  - Lists of Activities (UI screens), Services (background tasks), and Broadcast Receivers (system event listeners).
- **Possible Errors:**
  1. Long processing time when decompiling multi-DEX APKs.
  2. `AttributeError` when accessing components if the manifest is obfuscated.
- **How to Rectify:**
  - Disable loguru debug output as shown in Experiment 2.
  - Use APKTool on Kali/Command prompt: `apktool d uptodown-com.OfflineGames.apk -o decoded_app` to inspect readable Smali code.

---

### Experiment 6: Exploiting Vulnerable Components
- **What to Look Out For:**
  - Exported components (`android:exported="true"`) that do not enforce permission protection (`android:permission`).
  - Exported Content Providers that could allow unauthorized SQL querying or data leakage.
- **Possible Errors:**
  1. Assuming all exported activities are vulnerable: Many activities (like the main launch activity) must be exported by design.
  2. Crash if APK does not declare any Content Providers (returns empty list).
- **How to Rectify:**
  - Check whether the exported activity contains sensitive intent-filters or parameter extras.
  - Verify if an activity can be triggered via ADB:
    ```bash
    adb shell am start -n com.jura.offlinegames/.MainActivity
    ```

---

### Experiment 7: Automating Mobile Malware Analysis
- **What to Look Out For:**
  - Identification of high-privilege Android permissions that malware typically abuses:
    - `READ_SMS`, `SEND_SMS` (toll fraud, OTP interception)
    - `READ_CONTACTS`, `READ_CALL_LOG` (information theft)
    - `RECORD_AUDIO`, `CAMERA` (spyware capabilities)
    - `ACCESS_FINE_LOCATION` (tracking)
- **Possible Errors:**
  1. False alarms: Gaming apps frequently request network permissions for ads or storage for caching without being malware.
- **How to Rectify:**
  - Correlate requested permissions with app functionality. A calculator app requesting `SEND_SMS` is malicious; a navigation app requesting `ACCESS_FINE_LOCATION` is benign.

---

### Experiment 8: Secure Code Practices (Hardcoded Secrets)
- **What to Look Out For:**
  - Strings matching `password`, `apikey`, `token`, `secret`, or insecure plain-text HTTP URLs (`http://`).
- **Possible Errors:**
  1. `FileNotFoundError`: The target directory `"sample"` does not exist.
  2. Script hanging on massive non-text files or crashing with `UnicodeDecodeError`.
- **How to Rectify:**
  - Decode the APK first before running the search:
    ```bash
    apktool d uptodown-com.OfflineGames.apk -o sample
    ```
  - Always open files with `errors="ignore"` (as implemented in the script) to skip binary assets safely.

---

### Experiment 9: Automated Testing of Mobile Apps (Appium)
- **What to Look Out For:**
  - Appium establishing a session with the Android UiAutomator2 server on the emulator.
  - Target application launching automatically and terminating cleanly.
- **Possible Errors:**
  1. `urllib3.exceptions.MaxRetryError` / `ConnectionRefusedError`: Appium server is not running on `http://127.0.0.1:4723`.
  2. `UnknownError: Neither ANDROID_HOME nor ANDROID_SDK_ROOT is set`.
- **How to Rectify:**
  - Install and launch the Appium server in a separate terminal:
    ```bash
    npm install -g appium
    appium driver install uiautomator2
    appium
    ```
  - Set `ANDROID_HOME` in your environment variables.

---

### Experiment 10: Building a Mobile App Security Scanner
- **What to Look Out For:**
  - Single aggregated security report summarizing:
    - Application metadata (Package, Name, Version)
    - Dangerous permissions summary
    - Component inventory (Activities count, Services count, Receivers count, Providers count)
- **Possible Errors:**
  1. Redundant log output or memory spike on multi-gigabyte APKs.
- **How to Rectify:**
  - Run the scanner on a dedicated thread or pass `AnalyzeAPK` with minimal decompilation settings.
  - Redirect output to a report file: `python ex10_mobile_security_scanner.py > security_report.txt`.
