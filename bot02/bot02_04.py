import requests
import json

from decouple import config

# Set up the API request parameters
token = config('BOT_TOKEN')
chat_id = config('CHAT_ID_BIJOY')
message = 'Hello! Please choose an option:'
button1 = {'text': 'Button 1', 'callback_data': 'button1_bijoy'}
button2 = {'text': 'Button 2', 'callback_data': 'button2_bijoy'}
buttons = [[button1, button2]]
reply_markup = {'inline_keyboard': buttons}

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
