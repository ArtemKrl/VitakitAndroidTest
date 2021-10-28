
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
driver.find_element_by_id('com.vitacore.vitakit:id/login_edit_text').send_keys('+79083474315')

driver.find_element_by_id('com.vitacore.vitakit:id/password_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/login_button').click()

driver.find_element_by_id('com.vitacore.vitakit:id/tab_recipes').click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Рецепт 39']").click()

check_name = driver.find_element_by_id('com.vitacore.vitakit:id/medicament_name_title').text

driver.find_element_by_id('com.vitacore.vitakit:id/add_to_take').click()

driver.find_element_by_id('com.vitacore.vitakit:id/duration_edit_text').click()

driver.find_element_by_id('com.vitacore.vitakit:id/rb_n_day').click()

count = driver.find_element_by_id('com.vitacore.vitakit:id/count_days_edit_text')
count.clear()
count.send_keys(30)

TouchAction(driver).tap(None, 530, 354, 1).perform()

driver.find_element_by_id('com.vitacore.vitakit:id/frequency_edit_text').click()

time.sleep(1)

TouchAction(driver).tap(None, 530, 354, 1).perform()

driver.find_element_by_id('com.vitacore.vitakit:id/save_button').click()
driver.find_element_by_id('com.vitacore.vitakit:id/tab_taking_medication').click()


true_name = driver.find_element_by_id('com.vitacore.vitakit:id/title').text

assert check_name == true_name


