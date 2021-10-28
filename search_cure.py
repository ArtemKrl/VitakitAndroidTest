
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

driver.find_element_by_id('com.vitacore.vitakit:id/search_text').click()
driver.find_element_by_id('com.vitacore.vitakit:id/search_text').send_keys('Азатиоприн')
driver.find_element_by_xpath("//android.widget.TextView[@text='Азатиоприн']").click()

check_name = driver.find_element_by_id('com.vitacore.vitakit:id/description').text
print(check_name)
true_name = "Азатиоприн 50 шт в уп. "

assert check_name == true_name
