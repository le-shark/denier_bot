import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=100):
        method = "getUpdates"
        params = {"timeout": timeout, "offset": offset}
        response = requests.get(self.api_url + method, data=params)
        return response.json()["result"]

    def send_message(self, chat_id, text):
        params = {"chat_id": chat_id, "text": text}
        method = "sendMessage"
        response = requests.post(self.api_url + method, data=params)
        print("Sent a message.")

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update

greet_bot = BotHandler("568360161:AAESA4aHcpKcKwUil6mAB6i8WO3IYWE1KTY")
now = datetime.datetime.now()

def main():
    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()

        if last_update:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            greet_bot.send_message(last_chat_id, 'Вообще-то не {}.'.format(last_chat_text))

            new_offset = last_update_id + 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
