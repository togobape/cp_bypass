import time, sys
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# For Webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('bin/4.16.1_0.crx')
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 20)
time.sleep(10)


extension_url = "chrome-extension://dhdgffkkebhmkfjojejmpbldmpobfkfo/options.html#nav=dashboard"
browser.get(extension_url)

browser.switch_to.window(browser.window_handles[0])
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


print("==============================================================================")
print("=================                   adf.ly                   =================")
print("==============================================================================")

links = [{"short" : "http://veewhoje.com/2lTM", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "http://lyksoomu.com/tlx", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@id='skip_bu2tton']//img[@alt='Skip Ad']")))
        
        skip_button = browser.find_element_by_xpath("//a[@id='skip_bu2tton']//img[@alt='Skip Ad']")
        
        time.sleep(10)
        
        print("Button found.!")
        
        while browser.current_url != link["end_url"] :
            # ActionChains(browser).move_to_element(skip_button).click().perform()
            skip_button.click()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(2)
        
        print(browser.current_url)
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
        
    

# Problematic Have to check
print("==============================================================================")
print("=================                   al.ly                    =================")
print("==============================================================================")

links = [{"short" : "https://dausel.co/0G55Dt", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://dausel.co/9WCUnt", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(15)
        
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='btn skip-btn redirect']//strong[contains(text(), 'Continue')]")))
        time.sleep(5)
        skip_button = browser.find_element_by_xpath("//a[@class='btn skip-btn redirect']")
        
        while browser.current_url == link["short"] :
            ActionChains(browser).move_to_element(skip_button).click().perform()
            print("Button Clicked..!")
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            print(browser.current_url)
            time.sleep(2)
        
        print(browser.current_url)
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    

print("==============================================================================")
print("=================                 shorte.st                  =================")
print("==============================================================================")

links = [{"short" : "http://destyy.com/edRMKl", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "festyy.com/edQHIp", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    
    try:
        browser.get(link["short"])
        time.sleep(1)
        parentGUID = browser.current_window_handle


        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='skip-btn show']")))
        time.sleep(3)
        skip_button = browser.find_element_by_xpath("//span[@class='skip-btn show']")
        # skip_button.click()
        while browser.current_url == link["short"]:
            ActionChains(browser).move_to_element(skip_button).click().perform()
            print("Button Clicked..!")
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(2)
            
        print(browser.current_url)
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)

    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")

    
'''
# Not working. Site get blocked.
print("==============================================================================")
print("=================                    bc.vc                   =================")
print("==============================================================================")

links = [{"short" : "http://bc.vc/VhT9DgL", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "http://bc.vc/uOddC5y", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    browser.get(link["short"])
    
    time.sleep(7)
    
    
    if browser.current_url == link["end_url"] :
        pass
    
    
'''
print("==============================================================================")
print("=================                   za.gl                    =================")
print("==============================================================================")

links = [{"short" : "https://za.uy/MDpsr1", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://za.gl/SJCeu", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        time.sleep(3)
        skip_button = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        for i in range(7):
            ActionChains(browser).move_to_element(skip_button).click().perform()
            print("Button Clicked..!")
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(2)
            
        print(browser.current_url)
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    

print("==============================================================================")
print("=================                droplink.co                 =================")
print("==============================================================================")

links = [{"short" : "https://droplink.co/ypru", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://droplink.co/link2", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        print("Waiting for skip button 1")
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Click here to continue']")))
        skip_button = browser.find_element_by_xpath("//input[@value='Click here to continue']")
        # EC.
        skip_button.click()
        
        print("Waiting for skip button 2")
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='yuidea-generate']//a[contains(text(), 'Continue')]")))
        skip_button_2 = browser.find_element_by_xpath("//div[@id='yuidea-generate']//a[contains(text(), 'Continue')]")
        ActionChains(browser).move_to_element(skip_button_2).click().perform()
        # skip_button_2.click()
        
        time.sleep(2)
        
        skip_button_3 = browser.find_element_by_xpath("//button[contains(text(), 'Get Link')]")
        skip_button_3.click()
        
        time.sleep(1)
        
        print("Waiting for skip button 4")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        skip_button_4 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        skip_button_4.click()
        
        time.sleep(1)
        
        if browser.current_url == link["end_url"] :
            print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
            
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    

print("==============================================================================")
print("=================                   ouo.io                   =================")
print("==============================================================================")

links = [{"short" : "https://ouo.io/oxqg4r", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://ouo.io/dkFmBw", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    browser.get(link["short"])
    
    time.sleep(3)
    
    try:
        # First One
        # time.sleep(10)
        # wait.until(EC.element_to_be_clickable((By.ID, "btn-main")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-main']")))
        time.sleep(3)
        body = browser.find_element_by_id('btn-main')
        ActionChains(browser).move_to_element(body).click().perform()
        print("First Button clicked")

        # Check for another window

        # allGUID = browser.window_handles;
        # print(allGUID)
        # browser.switch_to.window(parentGUID);

        # Second One
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-main']")))
        body = browser.find_element_by_id('btn-main')
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(body).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(2)
            
        # ActionChains(browser).move_to_element(body).click().perform()
        # print("Second Button clicked")

        # time.sleep(3)

        # browser.switch_to.window(parentGUID)

        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR1: {err}")
        pass
    
    
    

print("==============================================================================")
print("=================                 pingit.im                  =================")
print("==============================================================================")

links = [{"short" : "https://pingit.im/Ec1y", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://pingit.im/zyi1Io34", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'CLICK HERE TO CONTINUE')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        print("Waiting for captcha to get verified..")
        time.sleep(15)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CLICK HERE TO CONTINUE')]")))
        skip_button_c = browser.find_element_by_xpath("//button[contains(text(), 'CLICK HERE TO CONTINUE')]")
        ActionChains(browser).move_to_element(skip_button_c).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        time.sleep(6)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    

print("==============================================================================")
print("=================                 adbull.me                  =================")
print("==============================================================================")

links = [{"short" : "https://adbull.me/mD9kk1LS", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://adbull.me/4FUbD", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'CLICK HERE TO CONTINUE')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        print("Waiting for captcha to get verified..")
        time.sleep(15)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CLICK HERE TO CONTINUE')]")))
        skip_button_c = browser.find_element_by_xpath("//button[contains(text(), 'CLICK HERE TO CONTINUE')]")
        ActionChains(browser).move_to_element(skip_button_c).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        time.sleep(12)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
        
    

print("==============================================================================")
print("=================                 adshort.co                 =================")
print("==============================================================================")

links = [{"short" : "https://adshort.co/dJc89Ixh", "end_url" : "https://faucetpay.io/?r=4218525"}, {"short" : "https://adshort.co/hoz1zQ", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        print("Waiting for captcha to get verified..")
        time.sleep(15)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Click here to continue')]")))
        skip_button_c = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button_c).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button_c).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        time.sleep(17)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Obtener vínculo')]")))
        
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Obtener vínculo')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    

print("==============================================================================")
print("=================                   exe.io                   =================")
print("==============================================================================")

links = [{"short" : "https://exe.io/NL2M", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://exe.io/vltwXS9K", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        print("Waiting for captcha to get verified..")
        time.sleep(17)
        
        print("Waiting for time to over")
        time.sleep(12)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Get Link ')]")))
        
        time.sleep(2)
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link ')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    
'''
# Site cannot be reached
print("==============================================================================")
print("=================                   cuty.io                  =================")
print("==============================================================================")

links = [{"short" : "https://cuty.io/AEfp4CgjO", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://cuty.io/7CYnaLHhie7k", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    browser.get(link["short"])
    
    if browser.current_url == link["end_url"] :
        pass
    
    

'''
# Problem with IP request.
print("==============================================================================")
print("=================                urlshortx.com               =================")
print("==============================================================================")

links = [{"short" : "https://xpshort.com/FTGzmnkn", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://xpshort.com/9mObdTa", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    try:
        browser.get(link["short"])
        time.sleep(3)
        
        print("Waiting for Captcha to get Verified")
        time.sleep(15)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
        continue_button = browser.find_element_by_xpath("//a[contains(text(), 'Continue')]")
        
        # continue_button.click()
        ActionChains(browser).move_to_element(continue_button).click().perform()
        
        print("Waiting for time to Over")
        time.sleep(15)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
        continue_button_2 = browser.find_element_by_xpath("//button[contains(text(), 'Continue')]")
        ActionChains(browser).move_to_element(continue_button_2).click().perform()
        # continue_button_2.click()
        
        browser.switch_to.window(browser.window_handles[1])
        
        time.sleep(10)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        get_link_button = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        ActionChains(browser).move_to_element(get_link_button).click().perform()
        # get_link_button.click()
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(get_link_button).click().perform()
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[1])
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
    
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")
    
    


print("==============================================================================")
print("=================                shrinkme.io                 =================")
print("==============================================================================")

links = [{"short" : "https://shrinke.me/GUVuE8", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://shrinke.me/SsEVtW", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        print("Waiting for captcha to get verified..")
        time.sleep(17)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        time.sleep(2)
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        
        # ActionChains(browser).move_to_element(skip_button).click().perform()
        # time.sleep(2)
        # browser.switch_to.window(parentGUID)
        
        # print("Waiting for captcha to get verified..")
        # time.sleep(17)
        
        print("Waiting for time to over")
        time.sleep(15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        
        time.sleep(2)
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")    
    


print("==============================================================================")
print("=================                 shrink.pe                  =================")
print("==============================================================================")

links = [{"short" : "https://aii.sh/pU4Fg", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://aii.sh/WEDh", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(3)
        
        print("Waiting for captcha to get verified..")
        time.sleep(17)
        
        ad_frame = browser.find_elements_by_tag_name("iframe")[-1]
        browser.switch_to.frame(ad_frame)
        
        close_button = browser.find_element_by_xpath("//span[contains(text(), 'Close')]")
        ActionChains(browser).move_to_element(close_button).click().perform()
        
        browser.switch_to.window(parentGUID)
        
        time.sleep(2)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        
        print("Waiting for time to over")
        time.sleep(10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        
        time.sleep(2)
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")    
    
    

print("==============================================================================")
print("=================                    fc.lc                   =================")
print("==============================================================================")

links = [{"short" : "https://fc-lc.com/iBuHtTa", "end_url" : "https://www.freepik.com/collection/freepik-by-felipe-novoa/3513525"}, {"short" : "https://fc-lc.com/puZB3", "end_url" : "https://faucetpay.io/?r=4218525"}]

for link in links:
    try:
        browser.get(link["short"])
        
        time.sleep(5)
        
        print("Waiting for captcha to get verified..")
        time.sleep(17)
        
        ad_frame = browser.find_elements_by_tag_name("iframe")[-1]
        browser.switch_to.frame(ad_frame)
        
        close_button = browser.find_element_by_xpath("//span[contains(text(), 'Close')]")
        ActionChains(browser).move_to_element(close_button).click().perform()
        
        browser.switch_to.window(parentGUID)
        
        time.sleep(2)
        
        skip_button = browser.find_element_by_xpath("//button[contains(text(), 'Click here to continue')]")
        ActionChains(browser).move_to_element(skip_button).click().perform()
        time.sleep(2)
        browser.switch_to.window(parentGUID)
        
        print("Waiting for time to over")
        time.sleep(10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Get Link')]")))
        
        time.sleep(2)
        skip_button_2 = browser.find_element_by_xpath("//a[contains(text(), 'Get Link')]")
        
        while browser.current_url != link["end_url"] :
            ActionChains(browser).move_to_element(skip_button_2).click().perform()
            time.sleep(2)
            browser.switch_to.window(parentGUID)
            time.sleep(3)
            
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print(Fore.RED+Style.BRIGHT+" >> Failed"+Style.RESET_ALL)
        print(f"[+] ERROR: {err}")    
    


print("===================================================")
print("============ All Link Visit Finished ==============")
print("===================================================")



browser.quit()

