# Ex. No. : 9 - AUTOMATED TESTING OF MOBILE APPS
# AIM: To automate functional testing of an Android application using Appium.

from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.automation_name = "UiAutomator2"
options.app = "uptodown-com.OfflineGames.apk"

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

time.sleep(5)
print("Application Launched Successfully")
driver.quit()
