import re
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pytesseract as tess
from PIL import Image
import re

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
driver.find_element_by_id('com.vitacore.vitakit:id/login_edit_text').send_keys('+79083474315')

driver.find_element_by_id('com.vitacore.vitakit:id/password_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/login_button').click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Обратная связь']").click()

driver.find_element_by_id('com.vitacore.vitakit:id/user_name_edit_text').send_keys('Test')
driver.find_element_by_id('com.vitacore.vitakit:id/user_email_edit_text').send_keys('test@testmail.com')
driver.find_element_by_id('com.vitacore.vitakit:id/user_phone_edit_text').send_keys('+79083474315')
driver.find_element_by_id('com.vitacore.vitakit:id/user_message_edit_text').send_keys('TEST TEST TEST')

driver.find_element_by_id('com.vitacore.vitakit:id/send_button').click()
driver.save_screenshot("/Users/Artem.Korol/Downloads/VITAKIT_APP/screenshots/"+"feedback"+".png")
tess.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
img = Image.open("/Users/Artem.Korol/Downloads/VITAKIT_APP/screenshots/"+"feedback"+".png")
text = tess.image_to_string(img, lang="rus")

searching = re.search(r'Ваш отзыв отправлен', text)
check_name = searching.group(0)
true_name = "Ваш отзыв отправлен"

assert check_name == true_name




# TouchAction(driver).tap(None, 532, 533, 2).perform()
# TouchAction(driver).write("111")
