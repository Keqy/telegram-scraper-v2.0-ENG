from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sync import TelegramClient
import os
import time

def inviting(client, channel, users):
    client(InviteToChannelRequest(
        channel=channel,
        users=[users]
    ))


def parsing(client, index: int, id: bool, name: bool):
    all_participants = []
    all_participants = client.get_participants(index)
    if name:
        with open('usernames.txt', 'r+') as f:
            usernames = f.readlines()
            for user in all_participants:
                if user.username:
                    if ('Bot' not in user.username) and ('bot' not in user.username):
                        if (('@' + user.username + '\n') not in usernames):
                            f.write('@' + user.username + '\n')
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
    if id:
        with open('userids.txt', 'r+') as f:
            userids = f.readlines()
            for user in all_participants:
                if (str(user.id) + '\n') not in userids:
                    f.write(str(user.id) + '\n')


def config():
    while True:
        os.system('cls||clear')

        with open('options.txt', 'r+') as f:
            if not f.readlines():
                f.write("NONEID\n"
                        "NONEHASH\n"
                        "True\n"
                        "True\n")
                continue
                
        options = getoptions()
        sessions = []
        for file in os.listdir('.'):
            if file.endswith('.session'):
                sessions.append(file)

        key = str(input((f"1 - Update API_ID [{options[0].replace('\n', '')}]\n"
                         f"2 - Update API_HASH [{options[1].replace('\n', '')}]\n"
                         f"3 - Scrape user-id [{options[2].replace('\n', '')}]\n"
                         f"4 - Scrape user-name [{options[3].replace('\n', '')}]\n"
                         f"5 - Add user-bot account [{len(sessions)}]\n"
                          "6 - Reset options\n"
                          "e - Escape\n"
                          "Enter: ")
                    ))

        if key == '1':
            os.system('cls||clear')
            options[0] = str(input("Enter your API_ID ")) + "\n"

        elif key == '2':
            os.system('cls||clear')
            options[1] = str(input("Enter your API_HASH: ")) + "\n"

        elif key == '3':
            if options[2] == 'True\n':
                options[2] = 'False\n'
            else:
                options[2] = 'True\n'

        elif key == '4':
            if options[3] == 'True\n':
                options[3] = 'False\n'
            else:
                options[3] = 'True\n'
        
        elif key == '5':
            os.system('cls||clear')
            if options[0] == "NONEID\n" or options[1] == "NONEHASH":
                print("Check API_ID and API_HASH")
                time.sleep(2)
                continue

            print("User-bots:\n")
            for i in sessions:
                print(i)

            phone = str(input("Enter account phone number: "))
            client = TelegramClient(phone, int(options[0].replace('\n', '')), 
                                    options[1].replace('\n', '')).start(phone)
            
        elif key == '6':
            os.system('cls||clear')
            answer = input("Are you sure?\nAPI_ID and API_HASH will be deleted\n"
                           "1 - Reset options\n2 - Escape\n"
                           "Enter: ")
            if answer == '1':    
                options.clear()
                print("Options have been reset")
                time.sleep(2)
            else:
                continue

        elif key == 'e':
            os.system('cls||clear')
            break

        with open('options.txt', 'w') as f:
            f.writelines(options)


def getoptions():
    with open('options.txt', 'r') as f:
        options = f.readlines()
    return options
