# Security in Mobile Exploitation Laboratory (CY3763)

This repository contains the laboratory experiments and analysis scripts for **CY3763 – Security in Mobile Exploitation Laboratory**, executed against the target application [`uptodown-com.OfflineGames.apk`](uptodown-com.OfflineGames.apk) (15.56 MB).

---

## Repository Contents

| Ex. No. | File | Title | Primary Tool / Library |
| :---: | :--- | :--- | :--- |
| **01** | [`ex01_basic_apk_analysis.py`](ex01_basic_apk_analysis.py) | Basic Android APK Analysis | Python `zipfile` |
| **02** | [`ex02_static_code_analysis.py`](ex02_static_code_analysis.py) | Static Code Analysis | Androguard |
| **03** | [`ex03_dynamic_analysis_setup.py`](ex03_dynamic_analysis_setup.py) | Dynamic Analysis Setup | ADB, Frida |
| **04** | [`ex04_network_traffic_analysis.py`](ex04_network_traffic_analysis.py) | Network Traffic Analysis | mitmproxy |
| **05** | [`ex05_reverse_engineering.py`](ex05_reverse_engineering.py) | Reverse Engineering of Android Apps | Androguard, APKTool |
| **06** | [`ex06_exploiting_vulnerable_components.py`](ex06_exploiting_vulnerable_components.py) | Exploiting Vulnerable Components | Androguard |
| **07** | [`ex07_automating_malware_analysis.py`](ex07_automating_malware_analysis.py) | Automating Mobile Malware Analysis | Androguard |
| **08** | [`ex08_secure_code_practices.py`](ex08_secure_code_practices.py) | Secure Code Practices (Credential Scanner) | Python standard library |
| **09** | [`ex09_automated_testing.py`](ex09_automated_testing.py) | Automated Testing of Mobile Apps | Appium, UiAutomator2 |
| **10** | [`ex10_mobile_security_scanner.py`](ex10_mobile_security_scanner.py) | Building a Mobile App Security Scanner | Androguard |

---

## Target Application

- **File:** `uptodown-com.OfflineGames.apk`
- **File Size:** ~14.84 MB (15,560,578 bytes)
- **Architecture:** Multi-DEX (`classes.dex` through `classes4.dex`), Native C++ shared libraries in `lib/`

---

## Lab Documentation & Troubleshooting

For a detailed walkthrough of each experiment, key security observations, common runtime errors, and step-by-step rectifications, refer to:
- [**`EXPERIMENT_GUIDE_AND_TROUBLESHOOTING.md`**](EXPERIMENT_GUIDE_AND_TROUBLESHOOTING.md)

---

## Quick Setup & Execution

```bash
# 1. Install Dependencies
pip install androguard

# 2. Run Experiments
python ex01_basic_apk_analysis.py
python ex02_static_code_analysis.py
python ex10_mobile_security_scanner.py
```
