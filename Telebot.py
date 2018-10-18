#https://stackoverflow.com/questions/45903197/how-to-get-channels-members-count-with-telegram-api
#https://github.com/LonamiWebs/Telethon/blob/master/telethon_examples/interactive_telegram_client.py
#https://telethon.readthedocs.io/en/latest/extra/examples/chats-and-channels.html?highlight=participant%20count#retrieving-all-chat-members-channels-too
# list: https://lonamiwebs.github.io/Telethon/methods/channels/index.html
#https://lonamiwebs.github.io/Telethon/constructors/messages/dialogs.html
#https://lonamiwebs.github.io/Telethon/
#Retrieving all chat members:Use the telethon.telegram_client.TelegramClient.iter_participants friendly 
from telethon import TelegramClient, sync
from telethon.tl.functions import channels
from telethon import utils
#from telethon.tl.functions.channels import GetFullChannelRequest
import configparser
import os
import sys
import re

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
#client = InteractiveTelegramClient('session_id', 'phone', api_id, api_hash)
dialog_count = 3
dialogs=client.get_dialogs(dialog_count)
#print('total:', dialogs.total, '; have:', len(dialogs))
for dia in dialogs:
	print(utils.get_display_name(dia))
	#print(client.get_participants(dia))
matchedchatids = re.findall("(?<=PeerChannel\\(channel_id\\=).*?(?=\\))",str(client.get_dialogs(dialog_count)))  #"(?<=entity=Channel\\(id\\=).*?(?=,)" "(?<=title\\=').*?(?=')"   
for item in matchedchatids:
    print (item)
    print(client.get_entity(item))
    #print(len(client.get_participants(item)))
dialogs, entities = client.get_dialogs(dialog_count)
for i, entity in enumerate(entities):
                    i += 1  # 1-based index
                    print('{}. {}. id: {}'.format(i, get_display_name(entity), entity.id))

#links = channels.get_channels()
channel = client.get_entity(entity.id)

#ch_full = client(GetFullChannelRequest(channel=ch))

members = client.get_participants(channel)
print(len(members))