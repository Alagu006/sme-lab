# Ex. No. : 8 - SECURE CODE PRACTICES
# AIM: To identify insecure coding practices such as hardcoded credentials in decoded application files.

import os

keywords = [
    "password",
    "apikey",
    "token",
    "secret",
    "http://"
]

directory = "sample"

print("Potential Security Issues")
print("----------------------------")
for root, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(root, file)
        try:
            with open(path, "r", errors="ignore") as f:
                data = f.read().lower()
                for keyword in keywords:
                    if keyword in data:
                        print(keyword, "found in", path)
        except:
            pass
