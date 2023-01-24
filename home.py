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

try:
    # Leng 4_1
    # steep 1
    driver.get("https://practice.automationtesting.in/")
    # steep 2
    driver.execute_script('window.scrollBy(0, 600);')
    # steep 3
    driver.find_element_by_css_selector('[data-product_id="160"]').click()
    # steep 4
    driver.find_element_by_class_name('reviews_tab').click()
    # steep 5
    driver.find_element_by_class_name('star-5').click()
    # steep 6
    driver.find_element_by_id('comment').send_keys('Nice book!')
    # steep 7
    driver.find_element_by_id('author').send_keys('Tester_Maks')
    # steep 8
    driver.find_element_by_id('email').send_keys('testingmaks1@gmail.com')
    # steep 9
    driver.find_element_by_id('submit').click()

finally:
    time.sleep(7)
    driver.close()