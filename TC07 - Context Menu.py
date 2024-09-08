from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

url = "https://the-internet.herokuapp.com/context_menu"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

driver.get(url)

theBox = driver.find_element("css selector", "#content .example #hot-spot")

actions = ActionChains(driver)
actions.context_click(theBox).perform()

try:
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print("PASS", url, f"'{alert_text}' Alert is activated after right clicking in the box.")
except NoAlertPresentException:
    print("FAIL", url, "Alert is not activated and right button is not clicked in the box.")
finally:
    driver.quit()