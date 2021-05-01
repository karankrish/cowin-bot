import requests
import pytz
from datetime import date,datetime
from deta import App

app = App()

def sendTGMessage(message:str)->None:
    url = f'https://api.telegram.org/bot1287952207:AAG3BjXt1XTBorfvRPwE-zFFd-XBCtIwXdY/sendMessage'
    msg_data = {'chat_id':"523986211",'text':message,"parse_mode":"Markdown"}
    resp = requests.post(url, msg_data).json()
    print("Message Not Send" if resp['ok'] is False else "👉    Message Sent")

@app.lib.cron()
def getCowinData(event):
    tz = pytz.timezone("Asia/Calcutta")
    time= datetime.now(tz).strftime('%H:%M:%S')
    date = date.today().strftime("%d-%m-%Y")
    data = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=304&date={date}").json()
    nos_centers = len(data['centers'])
    print(nos_centers)
    message = f"No Vaccination Centers Available in Kottayam \n\nat {time} on {date}" if nos_centers<=0 else f"{nos_centers} Available in Kottayam on {date} at {time}"
    sendTGMessage(message)