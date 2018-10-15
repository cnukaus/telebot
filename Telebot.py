#https://stackoverflow.com/questions/45903197/how-to-get-channels-members-count-with-telegram-api

# list: https://lonamiwebs.github.io/Telethon/methods/channels/index.html
from telethon import TelegramClient, sync
from telethon.tl.functions import channels
#from telethon.tl.functions.channels import GetFullChannelRequest
import configparser
import os
import sys

def read_config(fname):
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(sys.path[0],fname))
        return config['gram']['api_id'],config['gram']['hash']
    except e as exception:
    	print(exception)



(api_id,api_hash) = read_config("password.ini")
print (api_id)


client = TelegramClient('session_name', api_id, api_hash)
client.start()
if (client.is_user_authorized() == False):
    phone_number = 'PHONE NUMBER'
    client.send_code_request(phone_number)
    myself = client.sign_in(phone_number, input('Enter code: '))
dialog_count = 10
print(client.get_dialogs(dialog_count))
dialogs, entities = client.get_dialogs(dialog_count)
for i, entity in enumerate(entities):
                    i += 1  # 1-based index
                    print('{}. {}. id: {}'.format(i, get_display_name(entity), entity.id))

#links = channels.get_channels()
channel = client.get_entity(entity.id)

#ch_full = client(GetFullChannelRequest(channel=ch))

members = client.get_participants(channel)
print(len(members))