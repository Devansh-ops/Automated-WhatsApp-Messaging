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

message = '''Greetings%20from%20Sigma%20Xi%2C%0A%0AThank%20you%20for%20signing%20up%20for%20the%20Sigma%20Xi%20VIT%27s%20Xientia.%20%0A%0AOur%20panel%20of%20speakers%20will%20lead%20you%20through%20all%20of%20the%20pollution%20control%20tactics%2C%20including%20attempting%20to%20manage%20a%20pollutant%20after%20it%20has%20been%20discharged%20in%20order%20to%20lessen%20its%20influence%20on%20the%20environment%2C%20as%20well%20as%20pollution%20management%20for%20a%20sustainable%20environment.%20We%20hope%20to%20see%20you%20at%20Xientia%21%0A%0AFor%20any%20queries%20contact%3A%0ASabrina%20Manickam%2C%207459818283%0ADevansh%20Sehgal%2C%2091046%2084900%0A%0AEvent%20Details%3A%0ADate%3A%2027th%20November%202021%0ATiming%3A%2012%20noon%20-2%20pm%0AMeeting%20Link%3A%20https%3A%2F%2Fbit.ly%2FXientia_SigmaXI%0A%0AFind%20us%20on%3A%0ALinkedIn%3A%0Awww.linkedin.com%2Fcompany%2Fsigma-xi-vit%2Fmycompany%2F%0A%0AInstagram%3A%0Awww.instagram.com%2Fsigmaxi.vit%2F%0A%0AFacebook%3A%0Awww.facebook.com%2FSigmaXiVIT%2F%0A%0ARegards%0ATeam%20Sigma%20Xi%20VIT'''
 
workbook = pd.read_excel('Xientia.xlsx')
 
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