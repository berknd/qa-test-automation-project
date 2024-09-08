from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

url = "https://the-internet.herokuapp.com/drag_and_drop"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

driver.get(url)

elementsDiv = driver.find_elements("css selector", "#content #columns div header")
firstPlacement = [x.text for x in elementsDiv]

sourceElement = driver.find_element("css selector", "#content #columns #column-a")
targetElement = driver.find_element("css selector", "#content #columns #column-b")

actions = ActionChains(driver)
actions.drag_and_drop(sourceElement, targetElement).perform()

elementsDiv = driver.find_elements("css selector", "#content #columns div header")
lastPlacement = [x.text for x in elementsDiv]

if firstPlacement != lastPlacement:
    print("PASS", url, f"Drag and drop is successful from {firstPlacement} to {lastPlacement}")
else:
    print("FAIL", url, f"Drag and drop is unsuccessful from {firstPlacement} to {lastPlacement}")