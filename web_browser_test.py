from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

browser.get('https://aetna-uat.assurecare.com/MC/login?returnUrl=%2Fhome')

try:
    #Send Username
    username = browser.find_element_by_name("username")  # Find the input field
    username.click()
    username.send_keys("default")

    #Send password
    password = browser.find_element_by_name('password') # Find the password input field
    password.click()
    password.send_keys("P@ssw0rd")

    loginButton = browser.find_element_by_css_selector(".mat-raised-button.mat-accent")
    loginButton.click()
    try:
        for handle in browser.window_handles:
            print(handle)
            browser.switch_to_window(handle)

        # WebDriverWait(browser,3).until(
        # EC.presence_of_element_located((By.CLASS_NAME,".mat-raised-button.mat-accent")).click()
        # )

    except:
        # browser.close()
        pass
    # role = browser.find_element_by_css_selector(".mat-raised-button.mat-accent")
    # role.click()
except:
    pass
