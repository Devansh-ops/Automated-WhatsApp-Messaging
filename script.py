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

message = '''Greetings%20from%20Sigma%20Xi%2C%0A%0AThank%20you%20for%20registering%20for%20Sigma%20Xi%E2%80%99s%20AI%20Conclave%2021.%20We%20are%20delighted%20to%20have%20you%20attend%20our%20event.%0AOur%20panel%20of%20speakers%20will%20walk%20you%20through%20all%20of%20the%20work%2C%20techniques%2C%20jargon%2C%20and%20tooling%20associated%20with%20Artificial%20Intelligence%20and%20Machine%20Learning.%20The%20event%20will%20cover%20everything%20you%20need%20to%20know%20about%20getting%20started%20with%20research%20in%20the%20field%20of%20AI%20and%20ML.%0A%0AEvent%20Details%3A%0ADate%3A%2013th%20November%202021%0ATime%3A%204%20p.m.%20-%206%20p.m.%0AMeeting%20Link%3A%20https%3A%2F%2Fbit.ly%2FSigmaAIConclave21%0A%0AFor%20any%20queries%20contact%3A%0AAnanya%20Pantvaidya%20%209967032670%0AShreyas%20Singh%20%209918644494%0A%0AFind%20us%20on%3A%0A%0ALinkedIn%3A%0Awww.linkedin.com%2Fcompany%2Fsigma-xi-vit%2Fmycompany%2F%0AInstagram%3A%0Awww.instagram.com%2Fsigmaxi.vit%2F%0AFacebook%3A%0Awww.facebook.com%2FSigmaXiVIT%2F%0A%0ARegards%0ATeam%20Sigma%20Xi%20VIT
'''
 
workbook = pd.read_excel('Test_2.xlsx')
 
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