import re
import time
from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Pixel 4",
    "app": "C:\\Users\\Artem.Korol\\Downloads\\VITAKIT_APP\\App_bin\\VITAKIT.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)
driver.find_element_by_id('com.vitacore.vitakit:id/skip_view').click()

driver.find_element_by_id('com.vitacore.vitakit:id/button_access_allow').click()

driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Татарстан']").click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Казань']").click()
driver.find_element_by_id('com.vitacore.vitakit:id/tab_profile').click()
driver.find_element_by_id('com.vitacore.vitakit:id/login_edit_text').send_keys('+79201247901')

driver.find_element_by_id('com.vitacore.vitakit:id/password_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/login_button').click()
driver.find_element_by_id('com.vitacore.vitakit:id/tab_medicaments').click()
driver.find_element_by_id('com.vitacore.vitakit:id/search_text').click()
driver.find_element_by_id('com.vitacore.vitakit:id/search_text').send_keys('Азатиоприн')
driver.find_element_by_xpath("//android.widget.TextView[@text='Азатиоприн']").click()
time.sleep(1)

driver.find_element_by_id('com.vitacore.vitakit:id/add_to_basket').click()
time.sleep(1)


driver.find_element_by_id('com.vitacore.vitakit:id/tab_cart').click()

driver.find_element_by_id('com.vitacore.vitakit:id/button_choose_pharmacy').click()
driver.find_element_by_id('com.vitacore.vitakit:id/make_order').click()
driver.find_element_by_id('com.vitacore.vitakit:id/button_confirm').click()
create_deal = driver.find_element_by_id('com.vitacore.vitakit:id/title').text
num_deal = re.search(r'№\d*', create_deal)

number = num_deal.group(0)
check_name = driver.find_element_by_id('com.vitacore.vitakit:id/description').text
true_name = "Ваш заказ был сформирован и сейчас находится в обработке"

driver.find_element_by_id('com.vitacore.vitakit:id/tab_profile').click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Мои заказы']").click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Заказ {num}']".format(num=number)).click()

driver.find_element_by_id('com.vitacore.vitakit:id/order_cancel').click()

driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id('com.vitacore.vitakit:id/reason_edit_text').send_keys('Test')
driver.find_element_by_id('com.vitacore.vitakit:id/button_cancel').click()
time.sleep(1)

driver.swipe(470, 1460, 470, 800, 300)



# driver.find_element_by_xpath("//android.widget.TextView[@text='Заказ {num}']".format(num=number)).click()
check_name_2 = driver.find_element_by_id('com.vitacore.vitakit:id/order_view').text
true_name_2 = "Посмотреть"
assert check_name == true_name, check_name_2 == true_name_2
