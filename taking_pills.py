
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
driver.find_element_by_id('com.vitacore.vitakit:id/login_edit_text').send_keys('+79201247901')

driver.find_element_by_id('com.vitacore.vitakit:id/password_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/login_button').click()
driver.find_element_by_id('com.vitacore.vitakit:id/tab_taking_medication').click()

driver.find_element_by_id('com.vitacore.vitakit:id/add_button').click()

driver.find_element_by_id('com.vitacore.vitakit:id/medication_name_edit_text').send_keys('Азатиоприн')

driver.find_element_by_id('com.vitacore.vitakit:id/type_taking_text_view').click()
time.sleep(1)
TouchAction(driver).tap(None, 463, 841, 1).perform()

driver.find_element_by_id('com.vitacore.vitakit:id/date_taking_edit_text').click()
time.sleep(1)
driver.find_element_by_id('android:id/date_picker_header_year').click()
driver.find_element_by_xpath("//android.widget.TextView[@text=\"2022\"]").click()
driver.find_element_by_xpath("//android.view.View[@content-desc=\"28 октября 2022\"]").click()
driver.find_element_by_id('android:id/button1').click()
driver.find_element_by_id('com.vitacore.vitakit:id/time').click()
driver.find_element_by_xpath("//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc=\"15\"]").click()
driver.find_element_by_xpath("//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc=\"20\"]").click()


driver.find_element_by_id('android:id/button1').click()
driver.find_element_by_id('com.vitacore.vitakit:id/meal').click()
time.sleep(1)
TouchAction(driver).tap(None, 576, 1469, 1).perform()
driver.find_element_by_id('com.vitacore.vitakit:id/serving_size_plus').click()
driver.find_element_by_id('com.vitacore.vitakit:id/save_button').click()
driver.find_element_by_id('com.vitacore.vitakit:id/pills').click()
driver.find_element_by_id('com.vitacore.vitakit:id/date_to').text

check_name = driver.find_element_by_id('com.vitacore.vitakit:id/description').text
true_name = "Разовый прием, 15:20"
assert check_name == true_name






