import json
import  telegramSender
import requests

# Your JSON data
json_data = '''[
    {"meterCount":179,"consDate":"2024-09-01T00:00:00","cons":60.29999999999973,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-02T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-03T00:00:00","cons":63.80000000000018,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-04T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-05T00:00:00","cons":64.90000000000009,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-06T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-07T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-08T00:00:00","cons":56.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-09T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-10T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-11T00:00:00","cons":0.09999999999990905,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-12T00:00:00","cons":56.69999999999982,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-13T00:00:00","cons":56.70000000000027,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-14T00:00:00","cons":0.0,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"},
    {"meterCount":179,"consDate":"2024-09-15T00:00:00","cons":8.299999999999727,"estimationType":0,"commonCons":null,"meterStatusDesc":"-"}
]'''

# Parse the JSON data
data = json.loads(json_data)
message =''

# Get the "cons" values for the last three dates (13th, 14th, and 15th)
for record in data[-3:]:  # Get last three records
    cons_date = record['consDate'][:10]  # Extract date part
    cons_value = record['cons']
    message += (f"תאריך: {cons_date}, קוב: {cons_value:.2f}\n")

# print(f"Date: {cons_date}, Cons: {cons_value}")
print(message)

chat_id = '5628449279'  # Replace with your chat ID (or user ID)
bot_token = '7287725167:AAEzQwEBC5_jmiXcOx21R25HuxsuapeXqJU'  # Replace with the bot token from BotFather
# message = 'Hello, this is a test message from Python!'

telegramSender.send_telegram_message(chat_id, message, bot_token)