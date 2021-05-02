from typing import Any, Dict, Optional
import requests
import pytz
import os
from datetime import date,datetime
from deta import App #comment this when you're developing locally

app = App() #comment this when you're developing locally

token:str = os.getenv('TOKEN')
chat_id:str = os.getenv('CHAT_ID')

def sendTGMessage(message:str)->None:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    msg_data = {'chat_id':chat_id,'text':message,"parse_mode":"Markdown"}
    resp = requests.post(url, msg_data).json()
    print("Message Not Send" if resp['ok'] is False else "👉    Message Sent")

@app.lib.cron() #comment this when you're developing locally
def getCowinData(event:Optional[str]=None)->None:
    tz = pytz.timezone("Asia/Calcutta")
    time= datetime.now(tz).strftime('%H:%M:%S')
    tdate = date.today().strftime("%d-%m-%Y")
    data = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=304&date={tdate}").json()
    nos_centers = len(data['centers'])
    print(nos_centers)
    message = f"No Vaccination Centers Available in Kottayam \n\nat {time} on {tdate}" if nos_centers<=0 else f"{nos_centers} Available in Kottayam on {tdate} at {time}"
    sendTGMessage(message)    

if __name__ == "__main__":
    """ Uncomment these lines when deploying
    """
    getCowinData()
