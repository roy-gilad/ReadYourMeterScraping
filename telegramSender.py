import requests


def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


# Usage
if __name__ == "__main__":
    chat_id = '5628449279'  # Replace with your chat ID (or user ID)
    bot_token = '7287725167:AAEzQwEBC5_jmiXcOx21R25HuxsuapeXqJU'  # Replace with the bot token from BotFather
    message = 'Hello, this is a test message from Python!'

    send_telegram_message(chat_id, message, bot_token)
