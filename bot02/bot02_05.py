import requests

from decouple import config

# Set up the API request parameters
token = config('BOT_TOKEN')
chat_id = config('CHAT_ID_BIJOY')
message = 'Please select a response:'

# Define the custom keyboard buttons
keyboard = [['Yes'], ['Maybe']]

# Construct the request payload
payload = {'chat_id': chat_id, 'text': message, 'reply_markup': {'keyboard': keyboard, 'resize_keyboard': True, 'one_time_keyboard': True}}

# Send the request
url = f'https://api.telegram.org/bot{token}/sendMessage'
response = requests.post(url, data=payload)

# Check the response status code
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print(f'Something went wrong: {response.status_code}')
    print(response.json())
