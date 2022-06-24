from re import T
from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#PATH_TO_BRAVE_BROWSER = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
class WhatsAppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.binary_location = PATH_TO_BRAVE_BROWSER
        #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
        #options.add_argument("--profile-directory=Default")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    
        
    # send message to number
    def sendMessage(self, number : str, message : str, delay : int = 15):
        url = "https://web.whatsapp.com/send?phone=" + number + "&text=" + message
        self.driver.get(url)
        sleep(delay)
        messageBox = self.driver.find_element(By.XPATH, '//div[@title="Type a message"]')
        messageBox.send_keys(Keys.RETURN)
        sleep(1)
        
    def close(self):
        self.driver.quit()
        
    
bot = WhatsAppBot()
bot.sendMessage("+919104684900", "Test 2", 30)
bot.close()
