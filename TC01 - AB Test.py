from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://the-internet.herokuapp.com/abtest"

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options1 = Options()
chrome_options1.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver1 = webdriver.Chrome(service=service, options=chrome_options1)
driver1.maximize_window()
driver1.get(url)
driver1_h3 = driver1.find_element("css selector", "#content .example h3").text

chrome_options2 = Options()
chrome_options2.add_argument("--incognito")
chrome_options2.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver2 = webdriver.Chrome(service=service, options=chrome_options2)
driver2.maximize_window()
driver2.get(url)
driver2_h3 = driver2.find_element("css selector", "#content .example h3").text

if driver1_h3 != driver2_h3:
    print("PASS", url, "h3 elements are different.")
else:
    print("FAIL", url, "h3 elements are not different.")