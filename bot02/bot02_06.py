import requests

from decouple import config


token = config('BOT_TOKEN')


url = config('DOMAIN_URL')

payload = {
    'url': url
}

url = f'https://api.telegram.org/bot{token}/setWebhook'
response = requests.post(url, data=payload)

# Check the response status code
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print(f'Something went wrong: {response.status_code}')
