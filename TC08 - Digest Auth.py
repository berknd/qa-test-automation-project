from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

username = "admin"
password = "admin"
link = "the-internet.herokuapp.com/digest_auth"

url = "https://{}:{}@{}".format(username, password, link)

service = Service(executable_path=r".\chromedriver-win64\chromedriver.exe")

chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)

try:
    pElement = driver.find_element("css selector", "#content .example p").text
    if "Congratulations" in pElement:
        print("PASS", "https://"+link, "Digest auth is successful.")
    else: 
        print("FAIL", "https://"+link, "Digest auth is unsuccessful.")
except:
    print("FAIL", "https://"+link, "Digest auth is unsuccessful.")

