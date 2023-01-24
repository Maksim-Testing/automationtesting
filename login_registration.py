from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Подключение Adblock
path_to_extension =\
    r'C:\Users\User\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.2_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
driver.implicitly_wait(7)
driver.maximize_window()
time.sleep(1)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.close()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
email = 'testingmaks1@gmail.com'
password = 'TesterM@ks2023'
try:
    # Leng 4_2
    driver.get("https://practice.automationtesting.in/")
    driver.find_element_by_id('menu-item-50').click() # click "My Account"
    # Registration
    driver.find_element_by_id('reg_email').send_keys(email) # input email
    time.sleep(3)
    driver.find_element_by_id('reg_password').send_keys(password) # input password
    time.sleep(3)
    driver.find_element_by_css_selector('[value="Register"]').click() # click button "Register"
    print('Test 1 = OK')

    # leng 4_3
    driver.get("https://practice.automationtesting.in/")
    driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # login
    driver.find_element_by_id('username').send_keys(email)  # input email
    driver.find_element_by_id('password').send_keys(password)  # input password
    driver.find_element_by_css_selector('[name="login"]').click() # click button 'Login"
    # проверка элемента 'Logout'
    logout = driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/my-account/customer-logout/"]')
    logout_get_text = logout.text
    assert logout_get_text == 'Logout'


finally:
    time.sleep(15)
    driver.close()