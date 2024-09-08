from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random

url = "https://the-internet.herokuapp.com/checkboxes"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

checkboxesForm = driver.find_element("css selector", "#content .example #checkboxes")
checkboxInputs = checkboxesForm.find_elements("tag name", "input")

for _ in range(random.randint(1,5)):
    for index, checkbox in enumerate(checkboxInputs):
        firstStatus = checkbox.is_selected()
        checkbox.click()
        lastStatus = checkbox.is_selected()
        if firstStatus != lastStatus:
            if lastStatus: print("PASS", url, f"{index+1} Checkbox is checked.")
            else: print("PASS", url, f"{index+1} Checkbox is unchecked.")
        else:
            if firstStatus: print("FAIL", url, f"{index+1} Checkbox is not unchecked.")
            else: print("FAIL", url, f"{index+1} Checkbox is not checked.")
    