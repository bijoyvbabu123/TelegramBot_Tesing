# fixed keyboard response
import requests
import json
from decouple import config

# Set up the API request parameters
token = config('BOT_TOKEN')
chat_id = config('CHAT_ID_SREEJITH')
message = 'Blood needed. Are  you willing to donate'
button1 = {'text': 'Yes I am willing to donate'}
button2 = {'text': 'No I am not available'}
buttons = [[button1, button2]]
reply_markup = {'keyboard': buttons, 'one_time_keyboard': True, 'is_persistent': True, 'remove_keyboard': True}

# Construct the request payload
payload = {'chat_id': chat_id, 'text': message, 'reply_markup': json.dumps(reply_markup)}

# Send the request
url = f'https://api.telegram.org/bot{token}/sendMessage'
response = requests.post(url, data=payload)

# Check the response status code
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print(f'Something went wrong: {response.status_code}')
