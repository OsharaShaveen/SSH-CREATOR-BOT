from telethon import TelegramClient, events
import json
import requests


api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
bot_token = '12345:0123456789abcdef0123456789abcdef'


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)




def stat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "Your Banner Image Link",
    "caption": "Hello ! \n I'm Doenets.lk Bot \n\n What does I Know \n\n • G.C.E. (A/L) EXAMINATION - 2020 \n • G.C.E. (O/L) EXAMINATION (After Rescrutiny) - 2019 \n • GRADE 5 SCHOLARSHIP EXAMINATION (AFTER APPES) - 2020 \n\n ~ @Uvindu_Bro 🇱🇰 ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "➕ Add me to your Group",
                    "url": "https://t.me/DonentsLKBot?startgroup=new"
                }, 
                {
                    "text": "🔊 Channel",
                    "url": "https://t.me/UvinduBro"
                }
            ]
        ]
    }
}


  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

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






# Start Command

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    stat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


# AL result Command

@bot.on(events.NewMessage(pattern='/al'))
async def ALresult(event):
    indexx=str(event.raw_text).split(' ')
    print(indexx)
    await event.respond(Al(indexx[1]),parse_mode='html')
    raise events.StopPropagation


#Ol Result Command

@bot.on(events.NewMessage(pattern='/ol'))
async def OLresult(event):
    olindexx=str(event.raw_text).split(' ')
    print(olindexx)
    await event.respond(Ol(olindexx[1]),parse_mode='html')
    raise events.StopPropagation


#Grade 5 Scholarship Command

@bot.on(events.NewMessage(pattern='/g5'))
async def G5result(event):
    g5indexx=str(event.raw_text).split(' ')
    print(g5indexx)
    await event.respond(G5(g5indexx[1]),parse_mode='html')
    raise events.StopPropagation


    


def main():
    """Start the bot. \n \n ~ @UvinduBro"""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
