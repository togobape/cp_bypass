import time, sys, os
from colorama import Fore, Style
from selenium import webdriver
# For Firefox
from selenium.webdriver.firefox.options import Options
# Essential Modules
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# For Webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome(options=chrome_options)
# # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# wait = WebDriverWait(browser, 20)
# time.sleep(15)

# Firefox Version
# https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
# https://addons.mozilla.org/firefox/downloads/file/3947043/tampermonkey-4.17.6161.xpi
# moz-extension://f08359e3-dfda-4443-b263-81377d1ea4a3/

# Prepare for execution
current_dir = os.getcwd()
os.mkdir("bin")
os.system("cd bin/ && wget https://addons.mozilla.org/firefox/downloads/file/3947043/tampermonkey-4.17.6161.xpi")
print("Plugin Downloaded")
os.system("cd bin/ && wget https://raw.githubusercontent.com/togobape/cp_bypass/main/tempermonkey.js")
print("Bypasser Downloaded")
os.system("cd bin/ && wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz")
print("Gecko Driver Downloaded")
os.system("cd bin/ && tar -xvzf geckodriver-v0.31.0-linux64.tar.gz")
print("Gecko Extracted")
os.system("chmod +x bin/geckodriver")
print("CHMOD of gecko changed")

# Browser Loading Section
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path=r'bin/geckodriver')
browser.install_addon(f'{current_dir}/bin/tampermonkey-4.17.6161.xpi', temporary=True)
wait = WebDriverWait(browser, 20)
time.sleep(15)

print("Browser Loaded")

# For Firefox
browser.switch_to.window(browser.window_handles[0])

extension_url = "moz-extension://f08359e3-dfda-4443-b263-81377d1ea4a3/options.html#nav=dashboard"

# browser.get(extension_url)
browser.get("about:addons")

time.sleep(5)

print("Extension Loaded")

extension_button = browser.find_element_by_xpath("//button[@name='extension']")
extension_button.click()

more_option_button = browser.find_element_by_xpath("//button[@action='more-options']")
more_option_button.click()

time.sleep(1)

preferance_button = browser.find_element_by_xpath("//panel-item[@action='preferences']")
preferance_button.click()

time.sleep(1)

browser.switch_to.window(browser.window_handles[1])
time.sleep(2)

dashboard_button = browser.find_element_by_xpath("//div[contains(text(), 'Installed Userscripts')]")
dashboard_button.click()

with open("bin/tempermonkey.js", "r") as recaptcha_file:
	recaptcha_script = recaptcha_file.read()

add_button = browser.find_element_by_xpath("//div[@tvid='utils']")
add_button.click()

time.sleep(2)

upload_button = browser.find_element_by_xpath("//input[@type='file']")
upload_button.send_keys(f"{current_dir}/bin/tempermonkey.js")

time.sleep(2)

# print(browser.window_handles)
browser.switch_to.window(browser.window_handles[0])
browser.close()
time.sleep(2)

browser.switch_to.window(browser.window_handles[2])
browser.close()
time.sleep(2)

browser.switch_to.window(browser.window_handles[1])
install_button = browser.find_element_by_xpath("//input[@class='button install']")
install_button.click()

browser.switch_to.window(browser.window_handles[0])
add_button = browser.find_element_by_xpath("//div[@tvid='dashboard']")
add_button.click()

time.sleep(5)

print("Captcha Bypassser Installed")

browser.get("http://stackoverflow.com")
time.sleep(1)
parentGUID = browser.current_window_handle


time.sleep(10)


browser.quit()
