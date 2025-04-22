'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from defunc import *
import time
import random
import os

if __name__ == "__main__":
    while True:
        options = getoptions()
        if not options or options[0] == "NONEID\n" or options[1] == "NONEHASH\n":
            print("Add API_ID and API_HASH")
            time.sleep(2)
            config()
            continue
        
        api_id = int(options[0].replace('\n', ''))
        api_hash = str(options[1].replace('\n', ''))
        if options[2] == 'True\n':
            user_id = True
        else:
            user_id = False
        if options[3] == 'True\n':
            user_name = True
        else:
            user_name = False

        os.system('cls||clear')
        selection = str(input("1 - Options\n"
                              "2 - Scraping\n"
                              "3 - Inviting\n"
                              "e - Exit\n"
                              "Enter: "))
        

        if selection == '1':
            config()


        elif selection == '2':
            chats = []
            last_date = None    
            size_chats = 200
            groups = []         

            print("Select an account for scraping\n"
                "(The account must be in a group for scraping)\n")

            sessions = []
            for file in os.listdir('.'):
                if file.endswith('.session'):
                    sessions.append(file)


            for i in range(len(sessions)):
                print(f"[{i}] -", sessions[i], '\n')
            i = int(input("Enter: "))
            
            client = TelegramClient(sessions[i].replace('\n', ''), api_id, api_hash).start(sessions[i].replace('\n', ''))

            result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=size_chats,
                hash=0
            ))
            chats.extend(result.chats)

            for chat in chats:
                try:
                    if chat.megagroup is True:
                        groups.append(chat)         
                except:
                    continue

            i = 0
            print('Clear usernames and userids database: clear') 
            print('-----------------------------')
            for g in groups:
                print(str(i) + ' - ' + g.title)
                i+=1
            print(str(i + 1) + ' - ' + 'Scrape everything')
            g_index = str(input())

            if g_index == 'clear':
                f = open('usernames.txt', 'w')
                f.close()
                f = open('userids.txt', 'w')
                f.close

            elif int(g_index) < i + 1:
                target_group = groups[int(g_index)]
                parsing(client, target_group, user_id, user_name)
                print('Scraped.')
                input('press "Enter"')

            elif int(g_index) == i + 1:
                for g_index in groups:
                    parsing(client, g_index, user_id, user_name)
                print('Scraped.')
                input('press "Enter"')
            

        elif selection == '3':
            with open('usernames.txt', 'r') as f:
                users = list(f)

            print("Select an account for inviting\n"
                  "(The account must be in a group for inviting)")
            
            sessions = []
            for file in os.listdir('.'):
                if file.endswith('.session'):
                    sessions.append(file)

            for i in range(len(sessions)):
                print(f"{i} -", sessions[i])
            i = int(input("Ввод: "))
            
            client = TelegramClient(sessions[i].replace('\n', ''), api_id, api_hash)

            channelname = input('Enter the group name for inviting (without "@")\nEnter: ')

            for limit in range(20):
                try:
                    inviting(client, channelname, users[limit].replace('\n', ''))
                    print(users[limit].replace('\n', ''))
                    time.sleep(random.randrange(15, 40))

                except UserPrivacyRestrictedError:
                    print(f'User {users[limit].replace('\n', '')} forbade to invite him. Skip :(')

                except PeerFloodError:
                    print('Telegram is spammed. Closing the inviter.')
                    input('press "Enter"')
                    break

                except Exception as error:
                    print(error)
                    break

        elif selection == 'e':
            break
