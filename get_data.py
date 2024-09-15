import requests
import time
import json
from datetime import datetime, timedelta
import  telegramSender


# Get current date
current_date = datetime.now()
three_days_ago = current_date - timedelta(days=3)

# Format both dates as YYYY-MM-DD
current_date_str = current_date.strftime("%Y-%m-%d")
three_days_ago_str = three_days_ago.strftime("%Y-%m-%d")

token = requests.post(
    url="https://eu-customerportal-api.harmonyencoremdm.com/consumer/login",
    json= {"email":"nadavgil18@gmail.com","pw":"AAAaaa111","deviceId":"270566787934916747718271777073275455358"},
    verify=True,

    headers={"Content-Type":"application/json", "path":"/consumer/login"}
    )

# token = token.json()["token"]
print(token.json()["token"])
time.sleep(5)
data = requests.get(
    url = f"https://eu-customerportal-api.harmonyencoremdm.com/consumption/daily/179/{three_days_ago_str}/{current_date_str}",
    verify=True,
    headers={"X-Access-Token": token.json()["token"]}

)

data = json.loads(data.content)
message = ''
# Get the "cons" values for the last three dates (13th, 14th, and 15th)
for record in data[-3:]:  # Get last three records
    cons_date = record['consDate'][:10]  # Extract date part
    cons_value = record['cons']
    message += (f"תאריך: {cons_date}, קוב: {cons_value:.2f}\n")

chat_id = '5628449279'  # Replace with your chat ID (or user ID)
bot_token = '7287725167:AAEzQwEBC5_jmiXcOx21R25HuxsuapeXqJU'  # Replace with the bot token from BotFather

telegramSender.send_telegram_message(chat_id, message, bot_token)
