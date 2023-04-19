# testing sending message through the bot with hardcoded chatID

import requests
from decouple import config

bot_token = config('BOT_TOKEN')


def telegram_bot_getme_method(): # works
    # check the authentication token of the bot
    getme_method = 'https://api.telegram.org/bot' + bot_token + '/getMe'
    response = requests.get(getme_method)
    return response.json()

def telegram_bot_getChat_method():
    # check the authentication token of the bot
    chat_id = config('CHAT_ID_BIJOY')
    getme_method = 'https://api.telegram.org/bot' + bot_token + '/getChat?chat_id=' + chat_id
    response = requests.get(getme_method)
    return response.json()
    

# test = telegram_bot_getme_method()
test = telegram_bot_getChat_method()
print(test)