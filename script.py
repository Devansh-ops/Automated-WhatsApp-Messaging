'''
import subprocess
import sys
 
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
 
install("pyautogui")
install("pandas")
install("openpyxl")
'''
 
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
import math

message = '''Greetings%20from%20Sigma%20Xi%2C%0A%0AThank%20you%20for%20registering%20for%20Sigma%20Xi%E2%80%99s%20%3Chover.js%3E.%20We%20are%20delighted%20to%20have%20you%20attend%20our%20event.%0A%0AOur%20speaker%2C%20Madabhushi%20Priya%20Saaketh%20will%20guide%20you%20through%20the%20basics%20of%20Frontend%20Web%20development%2C%20covering%20the%20major%20scripting%20languages%20such%20as%20HTML%2C%20CSS%2C%20Javascript%2C%20jQuery%20and%20AJAX%2C%20that%20power%20the%20internet%20wave.%20%0AHe%20will%20guide%20you%20through%20the%20process%20of%20styling%20web%20apps%2C%20explain%20how%20to%20work%20on%20open-source%20projects%20and%20follow%20modern%20frontend%20practices.%0A%0AEvent%20details%3A%20%0A%0ADate%3A%2019th%20November%202021%20%0ATime%3A%206%3A00%20pm%20to%207%3A30%20pm%20%0APlatform%3A%20Microsoft%20Teams%20%0AMeeting%20Link%3A%20https%3A%2F%2Fbit.ly%2FHover_js%0A%0AFor%20any%20queries%20contact%3A%0A%0AMaster%20Muskan%0A%2B91%2073780%2099975%0AKinit%20Sai%20%0A%2B91%2095909%2011533%0A%0AFind%20us%20on%3A%20%0A%0ALinkedIn%3A%20%0Alinkedin.com%2Fcompany%2Fsigma-xi-vit%2Fmycompany%2F%20%0A%0AInstagram%3A%20%0Ainstagram.com%2Fsigmaxi.vit%2F%20%0A%0AFacebook%3A%20%0Afacebook.com%2FSigmaXiVIT%2F%20%0A%0ARegards%20%0ATeam%20Sigma%20Xi%20VIT'''
 
workbook = pd.read_excel('hover.xlsx')
 
data_dict = workbook.to_dict('list')
numbers = data_dict['Number']
first = True
for num in numbers:
    if (math.isnan(num)):
        continue
    print("Sending message to", int(num))
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+f"91{int(num)}+"+"&text="+message)
    if first:
        time.sleep(12)
        first=False
    width,height = pg.size()
    time.sleep(8)
    pg.click(width/2,height/2)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')