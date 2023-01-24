from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
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
    # Отображение страницы товара
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click() # click button 'Login"
    #
    # driver.find_element_by_id('menu-item-40').click() # нажимаем вкладку 'Shop'
    # driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]').click() # открываем книгу
    # # Тест на название заголовка
    # name_book = driver.find_element_by_css_selector('.summary.entry-summary h1')
    # name_book_text = name_book.text
    # print('True' if name_book_text == 'HTML5 Forms' else 'False')
    #
    # # Количество товаров в категории
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click() # click button 'Login"
    # time.sleep(7)
    #
    # driver.find_element_by_id('menu-item-40').click() # нажимаем вкладку 'Shop'
    # driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product-category/html/"]').click() # Определяем количество книг в категории
    # books = driver.find_elements_by_css_selector('.products.masonry-done li')
    # number_book = len(books)
    # print('True' if number_book == 3 else 'False')

    # # Сортировка товаров
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click()  # click button 'Login"
    #
    # driver.find_element_by_id('menu-item-40').click() # нажимаем вкладку 'Shop'
    # sel = driver.find_element_by_class_name('orderby').get_attribute('value')
    # print('True' if sel == 'menu_order' else 'False')
    # sort_books = driver.find_element_by_class_name('orderby')
    # select = Select(sort_books)
    # select.select_by_value('price-desc')
    #
    # sort_books = driver.find_element_by_class_name('orderby').get_attribute('value')
    # print('True' if sel == 'menu_order' else 'False')

    # # Отображение, скидка товара
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click()  # click button 'Login"
    #
    # driver.find_element_by_id('menu-item-40').click() # нажимаем вкладку 'Shop'
    # driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/android-quick-start-guide/"]').click()
    # price_up = driver.find_element_by_css_selector('del .woocommerce-Price-amount.amount').text
    # assert price_up == '₹600.00'
    # price_after = driver.find_element_by_css_selector('ins .woocommerce-Price-amount.amount').text
    # assert price_after == '₹450.00'
    # android_click = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[itemprop="image"]')))
    # android_click.click()
    # android_close = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
    # android_close.click()

    # Проверка цены в корзине
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click()  # click button 'Login"
    #
    # driver.find_element_by_id('menu-item-40').click()  # нажимаем вкладку 'Shop'
    # driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
    # time.sleep(2)
    # items = driver.find_element_by_css_selector('.cartcontents').text
    # assert items == '1 Item'
    # price = driver.find_element_by_css_selector('.wpmenucart-contents .amount').text
    # assert price == '₹180.00'
    # driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()
    #
    # subtotal = WebDriverWait(driver, 10).until(
    #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .amount'), price))
    #
    # subtotal_txt = driver.find_element_by_css_selector('.cart-subtotal .amount').text
    # tax = driver.find_element_by_css_selector('[data-title="Tax"] .woocommerce-Price-amount').text
    # tax_subtotal = str(float(tax[1:]) + float(subtotal_txt[1:]))
    # total = WebDriverWait(driver, 10).until(
    #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .amount'), tax_subtotal))

    # # Работа в корзине
    # driver.get("https://practice.automationtesting.in/")
    # driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # # login
    # driver.find_element_by_id('username').send_keys(email)  # input email
    # driver.find_element_by_id('password').send_keys(password)  # input password
    # driver.find_element_by_css_selector('[name="login"]').click()  # click button 'Login"
    #
    # driver.find_element_by_id('menu-item-40').click()  # нажимаем вкладку 'Shop'
    # time.sleep(5)
    # driver.execute_script('window.scrollBy(0, 300);')
    # driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
    # time.sleep(7)
    # driver.find_element_by_css_selector('[href="/shop/?add-to-cart=165"]').click()
    # driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()
    # time.sleep(5)
    # driver.find_element_by_css_selector('[data-product_id="182"]').click()
    # driver.find_element_by_css_selector('.woocommerce-message a').click()
    # numbers = driver.find_element_by_css_selector('[type="number"]')
    # numbers.clear()
    # numbers.send_keys('3')
    # save_changes_btn = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Update Basket"]')))
    # save_changes_btn.click()
    # numbers = driver.find_element_by_css_selector('[type="number"]')
    # assert numbers.get_attribute('value') == '3'
    # time.sleep(5)
    # driver.find_element_by_css_selector('[name="apply_coupon"]').click()
    # error = driver.find_element_by_css_selector('.woocommerce-error li')
    # assert error.text == 'Please enter a coupon code.'

    # Покупка товара
    driver.get("https://practice.automationtesting.in/")
    driver.find_element_by_id('menu-item-50').click()  # click "My Account"
    # login
    driver.find_element_by_id('username').send_keys(email)  # input email
    driver.find_element_by_id('password').send_keys(password)  # input password
    driver.find_element_by_css_selector('[name="login"]').click()  # click button 'Login"

    driver.find_element_by_id('menu-item-40').click()  # нажимаем вкладку 'Shop'
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, 300);')
    driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
    time.sleep(5)
    driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/basket/"]').click()
    driver.find_element_by_class_name('wc-forward').click()
    # 6 steep
    driver.find_element_by_id('billing_first_name').clear()
    driver.find_element_by_id('billing_first_name').send_keys('Maks')
    driver.find_element_by_id('billing_last_name').clear()
    driver.find_element_by_id('billing_last_name').send_keys('Tester')
    driver.find_element_by_id('billing_email').clear()
    driver.find_element_by_id('billing_email').send_keys('testingmaks1@gmail.com')
    driver.find_element_by_id('billing_phone').clear()
    driver.find_element_by_id('billing_phone').send_keys('1234567890')
    driver.find_element_by_id('select2-chosen-1').click()
    driver.find_element_by_id('s2id_autogen1_search').send_keys('Montenegro')
    driver.find_element_by_css_selector('.select2-result-label span').click()
    driver.find_element_by_id('billing_address_1').clear()
    driver.find_element_by_id('billing_address_1').send_keys('two street')
    driver.find_element_by_id('billing_city').clear()
    driver.find_element_by_id('billing_city').send_keys('Budva')
    driver.find_element_by_id('billing_state').clear()
    driver.find_element_by_id('billing_state').send_keys('Conty')
    driver.find_element_by_id('billing_postcode').clear()
    driver.find_element_by_id('billing_postcode').send_keys('123456')
    driver.execute_script('window.scrollBy(0, 600);')
    time.sleep(2)
    driver.find_element_by_id('payment_method_cheque').click()
    driver.find_element_by_id('place_order').click()
    some_element_1 = WebDriverWait(driver, 20).until(
         EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'),
                                          'Thank you. Your order has been received.'))
    some_element_2 = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr:nth-child(3) > td'),
                                         'Check Payments'))

finally:
    time.sleep(7)
    driver.quit()
