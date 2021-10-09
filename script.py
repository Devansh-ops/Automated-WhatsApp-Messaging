import subprocess
import sys
 
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
 
install("pyautogui")
install("pandas")
 
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
 
message = '''Greetings from Sigma Xi,%0a
%0a
Thank you for registering for Sigma Xi’s Git Commit Merge. We are delighted to have you.%0a
%0a
Our speaker, Devansh Sehgal will guide you through the basics of GitHub which is a web-based version-control and collaboration platform for software developers. He will walk you through the A - Z of GitHub and also show how to host static websites through GitHub pages. %0a
%0a
Devansh will also guide you through open source contribution for the HacktoberFest.%0a
%0a
We look forward to your participation in the event. Please find the event details below:%0a
%0a
Date: 10th October 2021%0a
Timing: 3:00 PM to 5:00 PM%0a
Platform: MS Teams%0a
Meeting Link: https://bit.ly/SigmaGitCommitMerge%0a
%0a
You can join the event through the given link. %0a
%0a
You can also join the discord server for any doubts :  https://discord.gg/DkcSP5xH %0a
%0a
For any queries, contact:%0a
%0a
Amit Priyadarshi%0a
%2B91 77356 29090%0a
%0a
Krish Jain%0a
%2B91 9962153121%0a
%0a
Find us on:%0a
%0a
LinkedIn: %0a
www.linkedin.com/company/sigma-xi-vit/mycompany/%0a
%0a
Instagram: %0a
www.instagram.com/sigmaxi.vit/%0a
%0a
Facebook: %0a
www.facebook.com/SigmaXiVIT/%0a
%0a
Regards %0a
Team Sigma Xi VIT
'''
 
workbook = pd.read_excel('test.xlsx')
 
data_dict = workbook.to_dict('list')
numbers = data_dict['Number']
first = True
for num in numbers:
    print("Sending message to", int(num))
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+f"91{int(num)}+"+"&text="+message)
    if first:
        time.sleep(12)
        first=False
    width,height = pg.size()
    time.sleep(10)
    pg.click(width/2,height/2)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')