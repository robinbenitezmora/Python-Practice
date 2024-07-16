import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# Your telegram API credentials
api_id = 'API_ID'
api_hash = 'API_HASH'
token = 'BOT_TOKEN'
message = 'Working ....'

# Create a bot object
phone = 'YOUR_PHONE_NUMBER_WITH_COUNTRY_CODE'
client = TelegramClient('anon', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

    try:
        receiver = InputPeerUser('USER_ID', 'USER_HASH')
        client.send_message(receiver, message, parse_mode='html')
    except Exception as e:
        print(e)
    client.disconnect()
else:
    print('Already authorized')
    receiver = InputPeerUser('USER_ID, 'USER_HASH')
    client.send_message(receiver, message, parse_mode='html')
    client.disconnect()

                             