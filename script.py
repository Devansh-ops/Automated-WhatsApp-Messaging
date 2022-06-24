from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

PATH_TO_BRAVE_BROWSER = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
class WhatsAppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = PATH_TO_BRAVE_BROWSER
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://google.com")
        self.driver.maximize_window()
        print(self.driver.title)
        sleep(1)
        
WhatsAppBot()