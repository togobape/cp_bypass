import time, sys
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

# Chrome Version
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_extension('bin/4.16.1_0.crx')
# chrome_options.add_argument("--start-maximized")
# chrome_options.headless=True

# browser = webdriver.Chrome(options=chrome_options)
# # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# wait = WebDriverWait(browser, 20)
# time.sleep(15)

# Firefox Version
# https://addons.mozilla.org/firefox/downloads/file/3947043/tampermonkey-4.17.6161.xpi
# moz-extension://f08359e3-dfda-4443-b263-81377d1ea4a3/
options = Options()
# options.headless = True
browser = webdriver.Firefox(options=options, executable_path=r'bin/geckodriver')
browser.install_addon('/root/Desktop/bot/AD_view/captcha_bypasser/bin/tampermonkey-4.17.6161.xpi', temporary=True)
wait = WebDriverWait(browser, 20)
time.sleep(15)

print("Browser Loaded")

# For Chrome
# extension_url = "chrome-extension://dhdgffkkebhmkfjojejmpbldmpobfkfo/options.html#nav=dashboard"

# For Firefox
browser.switch_to.window(browser.window_handles[0])

extension_url = "moz-extension://f08359e3-dfda-4443-b263-81377d1ea4a3/options.html#nav=dashboard"

# browser.get(extension_url)
browser.get("about:addons")

time.sleep(5)

with open("bin/tempermonkey.js", "r") as recaptcha_file:
	recaptcha_script = recaptcha_file.read()

add_button = browser.find_element_by_xpath("//div[@tvid='utils']")
add_button.click()

time.sleep(2)

upload_button = browser.find_element_by_xpath("//input[@type='file']")
upload_button.send_keys("/home/alibaba/bin/tempermonkey.js")

time.sleep(2)

# print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.close()
time.sleep(2)

browser.switch_to.window(browser.window_handles[1])
install_button = browser.find_element_by_xpath("//input[@class='button install']")
install_button.click()

browser.switch_to.window(browser.window_handles[0])
add_button = browser.find_element_by_xpath("//div[@tvid='dashboard']")
add_button.click()

time.sleep(5)

# browser.find_element_by_class_name('CodeMirror-scroll').send_keys(Keys.CONTROL + 'a') 
# browser.find_element_by_class_name('CodeMirror-scrol').send_keys(Keys.BACKSPACE) 
# browser.find_element_by_class_name('CodeMirror-scrol').send_keys(recaptcha_script) 
# browser.send_keys(recaptcha_script)

print("Captcha Bypassser Installed")

browser.get("http://stackoverflow.com")
time.sleep(1)
parentGUID = browser.current_window_handle


time.sleep(10)


browser.quit()

