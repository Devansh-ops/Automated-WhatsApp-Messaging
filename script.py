from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import openpyxl
import pandas as pd
import atexit

#PATH_TO_BRAVE_BROWSER = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
class WhatsAppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.binary_location = PATH_TO_BRAVE_BROWSER
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # fluent wait
        self.wait = WebDriverWait(self.driver, timeout=60, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        # closing
        atexit.register(self.__close)
        
    # function to correctly format the number
    # default is indian
    def format_number(self, phone_number):
        phone_number = phone_number.replace(" ", "").replace("+", "").strip()
        if len(phone_number) == 10:
            phone_number = "91{}".format(phone_number)
        return phone_number
        
    # send message to number
    def sendMessage(self, number : str, message : str, delayAfterMessage : int = 3):
        message = quote(message)
        number = self.format_number(number)
        url = "https://web.whatsapp.com/send?phone=" + number + "&text=" + message
        self.driver.get(url)
        messageBox = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]')))
        messageBox.send_keys(Keys.RETURN)
        sleep(delayAfterMessage)
    
    def sendBulkMessage(self, df : pd.DataFrame, message : str = "Hello from WhatsApp Bot!", column = 1, delayAfterMessage : int = 1):
        numbers = df.iloc[:, column].tolist()
        
        for i in range(len(numbers)):
            self.sendMessage(numbers[i], message, delayAfterMessage)
        
        
        
    def __close(self):
        self.driver.quit()
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to Excel file containing numbers to send message to")
    parser.add_argument("-c", "--column", help="Column name or number where numbers are located", default=1)
    parser.add_argument("message", nargs='?', help="String or Text file containing message to send", default="Hello from WhatsApp Bot!")
    parser.add_argument("-d", "--delay", help="Time (in seconds) to wait after sending the message. Default = 3", default=3)
    args = parser.parse_args()
    
    bot = WhatsAppBot()
    
    df = pd.read_excel(args.file, dtype=str)
    
    bot.sendBulkMessage(df, args.message, args.column, args.delay)
