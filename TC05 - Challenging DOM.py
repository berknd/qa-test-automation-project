from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

url = "https://the-internet.herokuapp.com/challenging_dom"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

def answerNumber():
    scripts = driver.find_elements("tag name", 'script')
    for script in scripts:
        script_content = script.get_attribute('innerHTML')
        if "Answer" in script_content:
            try: return int(script_content.split("Answer: ")[1][:5])
            except: return int(script_content.split("Answer: ")[1][:4])
    print("FAIL", url, "Canvas answer number not found.")
    return None

elementsDiv = driver.find_element("css selector", "#content .example .row div.large-2.columns")
aButtons = elementsDiv.find_elements("tag name", "a")

answer = answerNumber()

for a in range(len(aButtons)):
    aButtons[a].click()
    newAnswer = answerNumber()
    if answer != newAnswer and newAnswer != None:
        print("PASS", url, f"Button {a} is clicked.")
    else:
        print("FAIL", url, f"Button {a} is not clicked.")
    answer = newAnswer
    elementsDiv = driver.find_element("css selector", "#content .example .row div.large-2.columns")
    aButtons = elementsDiv.find_elements("tag name", "a")

elementsTable = driver.find_element("css selector", "table tbody")
trItems = elementsTable.find_elements("tag name", "tr")

for index, tr in enumerate(trItems):
    try:
        editDeleteButtons = tr.find_elements("tag name", "a")
        for indx, a in enumerate(editDeleteButtons):
            a.click()
            print("PASS", url, f"Action Column {index+1} Row {indx+1} Cell a element is clicked.")
    except:
        print("FAIL", url, f"Action Column {index+1} Row a elements are not clicked.")