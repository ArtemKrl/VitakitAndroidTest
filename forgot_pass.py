import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import re
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pytesseract as tess
from PIL import Image
import re
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

driver.find_element_by_id('com.vitacore.vitakit:id/lost_password').click()

driver.find_element_by_id('com.vitacore.vitakit:id/login_edit_text').send_keys("+79201247901")
driver.find_element_by_id('com.vitacore.vitakit:id/next_button').click()

TouchAction(driver).tap(None, 136, 1665, 5).perform()

driver.find_element_by_id('com.vitacore.vitakit:id/password_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/password_repeat_edit_text').send_keys('qweqweqwe')

driver.find_element_by_id('com.vitacore.vitakit:id/save_button').click()
time.sleep(1)
driver.save_screenshot("/Users/Artem.Korol/Downloads/VITAKIT_APP/screenshots/"+"changepass"+".png")
tess.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
img = Image.open("/Users/Artem.Korol/Downloads/VITAKIT_APP/screenshots/"+"changepass"+".png")
text = tess.image_to_string(img, lang="rus")

searching = re.search(r'Пароль успешно изменен', text)
check_name = searching.group(0)
true_name = "Пароль успешно изменен"
assert check_name == true_name
