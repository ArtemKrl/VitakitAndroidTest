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

driver.find_element_by_id('com.vitacore.vitakit:id/recipe_number').click()


driver.find_element_by_id('com.vitacore.vitakit:id/qr_code').click()

elem_qr = driver.find_element_by_id('com.vitacore.vitakit:id/barcode')
assert elem_qr
