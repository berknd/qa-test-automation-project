from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random

url = "https://the-internet.herokuapp.com/add_remove_elements/"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

elementsDiv = driver.find_element("css selector", "#content .example #elements")
lenButtonsStart = len(elementsDiv.find_elements("tag name", "button"))

addRemoveButton = driver.find_element("css selector", "#content .example button")

numberOfButtons = random.randint(1,9)

for i in range(numberOfButtons):
    addRemoveButton.click()

elementsDiv = driver.find_element("css selector", "#content .example #elements")
lenButtonsBefore = len(elementsDiv.find_elements("tag name", "button"))

addedButtons = elementsDiv.find_elements("tag name", "button")

for button in addedButtons:
    button.click()

elementsDiv = driver.find_element("css selector", "#content .example #elements")
lenButtonsAfter = len(elementsDiv.find_elements("tag name", "button"))

if lenButtonsStart != 0:
    print("FAIL", url, "There are buttons down before clicking 'Add Element' button.")

if lenButtonsBefore == numberOfButtons:
    print("PASS", url, f"{numberOfButtons} Buttons are added.")
elif lenButtonsBefore == lenButtonsStart:
    print("FAIL", url, f"{numberOfButtons} Buttons are not added.")
else:
    print("FAIL", url, f"{lenButtonsBefore-lenButtonsStart} Buttons are partially added.")

if lenButtonsAfter == 0:
    print("PASS", url, f"{len(addedButtons)} Buttons are deleted.")
elif lenButtonsAfter == lenButtonsBefore:
    print("FAIL", url, f"{len(addedButtons)} Buttons are not deleted.")
else:
    print("FAIL", url, f"{lenButtonsBefore-lenButtonsAfter} Buttons are partially deleted.")