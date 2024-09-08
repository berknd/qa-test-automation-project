from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://the-internet.herokuapp.com/disappearing_elements"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

elementsDiv = driver.find_element("css selector", "#content .example ul")
liElements = elementsDiv.find_elements("tag name", "li")

for index, li in enumerate(liElements):
    aElement = li.find_element("tag name", "a")
    aElement.click()
    if driver.current_url != url:
        print("PASS", url, f"{index+1} Element is disappeared.")
        driver.back()
    else:
        print("FAIL", url, f"{index+1} Element is not disappeared.")