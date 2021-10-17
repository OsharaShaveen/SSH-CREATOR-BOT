import telethon

import requests

import json

 from telethon.sync import TelegramClient

api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
bot_token = '12345:0123456789abcdef0123456789abcdef'


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


servers=json.loads(requests.get('https://single-developers.herokuapp.com/servers').content)

for server in servers:

    id=str(server)

    ip=servers[str(server)]['ip']

    location=servers[str(server)]['location']

    emoji=servers[str(server)]['emoji']

    print(

f"""◇ Server ID : {id}

◇ Server Host : {ip}

◇ Server Location : {emoji} {location} {emoji}

""")

serverid=input('Server ID : ')

 

server=json.loads(requests.get(f'https://single-developers.herokuapp.com/servers?id={serverid}').content)

status=requests.get(f'https://single-developers.herokuapp.com/servers?status={serverid}').content

ip=server['ip']

location=server['location']

emoji=server['emoji']

print(

f"""

◇ Server ID : {serverid}

◇ Server Host : {ip}

◇ Server Location : {emoji} {location} {emoji}

 

◇ Server Status : {str(status)}"""

)

 

username=input('User Name : ')

password=input('Password : ')

 

ssh=serverid+'$'+username+'$'+password

ssh_result=requests.get(f'https://single-developers.herokuapp.com/create?ssh={str(ssh)}').content

try:

    json_ssh=json.loads(ssh_result)

    user_name=json_ssh['username']

    passwd=json_ssh['password']

    port=json_ssh['port']

    ex_date=json_ssh['ex_date']

    login=json_ssh['login']

    print(

f"""

◇ Server Location : {emoji} {location} {emoji}

 

◇ Server Host : {ip}

◇ SSL Port : {port}

◇ User Name : {username}

◇ Password : {passwd}

◇ Expire Date : {ex_date}

◇ Login : {login}

 

<  https://t.me/SingleDevelopers  />"""

)

except:

    print(ssh_result)

 

 

Api by 
