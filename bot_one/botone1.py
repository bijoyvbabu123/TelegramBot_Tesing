import telegram
import asyncio
from decouple import config


async def send_message() : 

    # Replace YOUR_BOT_TOKEN with your actual bot token
    bot = telegram.Bot(token=config('BOT_TOKEN'))

    # Replace RECIPIENT_MOBILE_NUMBER with the recipient's actual mobile number
    recipient_mobile_number = config('MOBILE_ROSH')

    # Get the recipient's Telegram user ID
    try:
        recipient = await bot.get_chat(recipient_mobile_number)
        print("*******************", recipient)
    except telegram.TelegramError as e:
        print(f"Error getting recipient: {e}")
        exit()

    # Send the hello message to the recipient
    try:
        await bot.send_message(chat_id=recipient.chat_id, text='Hello, recipient!')
    except telegram.TelegramError as e:
        print(f"Error sending message: {e}")
        exit()

    print('Message sent successfully!')


if __name__ == '__main__':
    asyncio.run( send_message() )




import asyncio
import aiogram

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = aiogram.Bot(token='6097692400:AAFg5jaORo64SuYqkXi3KePUBZNgcy_NtAA')

async def get_user_chat_id(mobile_number):
    try:
        chat = await bot.get_chat(mobile_number)
    except aiogram.BotError as e:
        print(f"Error getting chat information: {e}")
        return None
    return chat.id

recipient_mobile_number = '+918891701113'
print("********************", "this is the number")
chat_id = asyncio.run(get_user_chat_id(recipient_mobile_number))
print("********************", chat_id)
if chat_id is not None:
    print(f"The chat ID for {recipient_mobile_number} is {chat_id}.")
else:
    print(f"Failed to get chat ID for {recipient_mobile_number}.")
