import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time
from urllib.parse import quote
import openpyxl
import pandas as pd
import atexit

#PATH_TO_BRAVE_BROWSER = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
class WhatsAppBot:
    def __init__(self):
        # constants
        self.DEFAULT_EXT="91"
        self.SCREENSHOT_FOLDER = "screenshots"
        
        options = webdriver.ChromeOptions()
        #options.binary_location = PATH_TO_BRAVE_BROWSER
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # fluent wait
        self.wait = WebDriverWait(self.driver, timeout=30, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        # closing
        atexit.register(self.__close)
        
    # function to correctly format the number
    # default is indian
    def format_number(self, phone_number):
        phone_number = phone_number.replace(" ", "").replace("+", "").strip()
        if len(phone_number) == 10:
            phone_number = "{}{}".format(self.DEFAULT_EXT, phone_number)
        return phone_number
        
    # send message to number
    def sendMessage(self, number : str, message : str, delayAfterMessage : int = 3):
        message = quote(message)
        number = self.format_number(number)
        url = "https://web.whatsapp.com/send?phone=" + number + "&text=" + message
        self.driver.get(url)
        try:
            messageBox = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@title="Type a message"]')))
            messageBox.send_keys(Keys.RETURN)
            sleep(delayAfterMessage)
        except TimeoutException:
            t = str(time())
            error_string = "Error in sendin message to {}".format(number)
            print(error_string)
            
            with open("error.log", "a") as f:
                f.write("\n{} : {}".format(t, error_string))
                f.close()
            
            if (not os.path.exists(self.SCREENSHOT_FOLDER)):
                os.makedirs(self.SCREENSHOT_FOLDER)
            self.driver.save_screenshot(os.path.join(self.SCREENSHOT_FOLDER, "{}.png".format(t)))
            
    def sendBulkMessage(self, df : pd.DataFrame, message : str = "Hello from WhatsApp Bot!", column = 1, delayAfterMessage : int = 4):
        numbers = df.iloc[:, column].tolist()
        
        for i in range(len(numbers)):
            self.sendMessage(numbers[i], message, delayAfterMessage)
    
    # change default phone extention
    def changeDefaultExt(self, newExt : str):
        newExt = newExt.replace(" ", "").replace("+", "").strip()
        self.DEFAULT_EXT = newExt
    
    # change default screenshot folder
    def changeDefaultScreenshotLocation(self, newLocation : str):
        self.DEFAULT_EXT = newLocation
    
    def __close(self):
        self.driver.quit()
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to Excel file containing numbers to send message to")
    parser.add_argument("-c", "--column", help="Column name or number where numbers are located", default=1)
    parser.add_argument("message", nargs='?', help="Text file containing message to send", default="Hello from WhatsApp Bot!")
    parser.add_argument("-d", "--delay", help="Time (in seconds) to wait after sending the message. Default = 4", default=4, type=int)
    parser.add_argument("-s", "--string", help="Treat message as string input", action='store_true')
    parser.add_argument("-e", "--extension", help="Change default phone extention. Default is Indian: 91")
    parser.add_argument("--screenshot", help="Defines error screenshot folder")
    args = parser.parse_args()
    
    bot = WhatsAppBot()
    
    if (args.string):
        message = args.message
    else:
        with open(args.message) as f:
            message = f.read()
            f.close()
    
    if (args.extension is not None):
        bot.changeDefaultExt(args.extension)
        
    if (args.screenshot is not None):
        bot.changeDefaultScreenshotLocation(args.screenshot)
    
    try:
        df = pd.read_excel(args.file, dtype=str)
    except FileNotFoundError:
        print("File not found:", args.file)
        exit()
        
    bot.sendBulkMessage(df=df, message=message, column=args.column, delayAfterMessage=args.delay)
