Okay so, this is a telegram bot which sends you a message every 6 hours about vaccine availability in your district.

## How to use it?
Edit the source file `main.py` with some stuff
- Telegram Bot Token, get it talking to Botfather bot. Line 9
> Check this [one](https://blog.athulcyriac.xyz/telegram-bot-gh-actions) for more explanations
- Telegram chat id, line 10
- District code for Cowin API, line 22 check table below for district code

| Code | District           |
| :---: | :--: |
| 301  | Alappuzha          |
| 307  | Ernakulam          |
| 306  | Idukki             |
| 297  | Kannur             |
| 295  | Kasaragod          |
| 298  | Kollam             |
| 304  | Kottayam           |
| 305  | Kozhikode          |
| 302  | Malappuram         |
| 308  | Palakkad           |
| 300  | Pathanamthitta     |
| 296  | Thiruvananthapuram |
| 303  | Thrissur           |
| 299  | Wayanad            |

## Running this
You can use https://deta.sh 's Micros to run this script. You might wanna make an account there and install it's CLI. Then run

- `deta login`
- `deta new`
- `deta cron set "6 hours"`

Mostly that's all