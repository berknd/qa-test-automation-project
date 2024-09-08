from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

url = "https://the-internet.herokuapp.com/broken_images"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

elementsDiv = driver.find_element("css selector", "#content .example")
imgElements = elementsDiv.find_elements("tag name", "img")

for img in imgElements:
    src = img.get_attribute('src')
    try:
        response = requests.head(src)
        if response.status_code == 200:
            print("PASS", url, src.split("/")[-1], "Image found.", response.status_code)
        else:
            print("FAIL", url, src.split("/")[-1], "Image not found.", response.status_code)
    except requests.RequestException as e:
        print("FAIL", url, f'Error checking image {src.split("/")[-1]}: {e}')