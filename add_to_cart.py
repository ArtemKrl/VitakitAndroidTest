from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
driver.find_element_by_id('com.vitacore.vitakit:id/add_to_basket').click()


try:
    driver.find_element_by_id('com.vitacore.vitakit:id/plus')
except NoSuchElementException:
    driver.find_element_by_id('com.vitacore.vitakit:id/plus')

