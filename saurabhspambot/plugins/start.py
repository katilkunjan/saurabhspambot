import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import saurabh, saurabh2, saurabh3, saurabh4, saurabh5, saurabh6, saurabh7, saurabh8, saurabh9, saurabh10, saurabh11, saurabh12, saurabh13, saurabh14, saurabh15, ALIVE_PIC, OWNER_ID
from saurabhspambot.plugins.help import * 


SAURABH_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"

Saurabh_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/full_masti_clubs")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
SaurabhX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/heartbrokenperson1"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/full_masti_clubs")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/bhumiharsaurabh/saurabhspambot")
        ]
        ]
        
        
#USERS 


@saurabh.on(events.NewMessage(pattern="/start"))
@saurabh2.on(events.NewMessage(pattern="/start"))
@saurabh3.on(events.NewMessage(pattern="/start"))
@saurabh4.on(events.NewMessage(pattern="/start"))
@saurabh5.on(events.NewMessage(pattern="/start"))
@saurabh6.on(events.NewMessage(pattern="/start"))
@saurabh7.on(events.NewMessage(pattern="/start"))
@saurabh8.on(events.NewMessage(pattern="/start"))
@saurabh9.on(events.NewMessage(pattern="/start"))
@saurabh10.on(events.NewMessage(pattern="/start"))
@saurabh11.on(events.NewMessage(pattern="/start"))
@saurabh12.on(events.NewMessage(pattern="/start"))
@saurabh13.on(events.NewMessage(pattern="/start"))
@saurabh14.on(events.NewMessage(pattern="/start"))
@saurabh15.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       SaurabhBot = await event.client.get_me()
       bot_id = saurabhBot.first_name
       bot_username = SaurabhBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       Thesaurabh = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [katil](https://t.me/tera_baap_katil)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(Thesaurabh,
                  SAURABH_IMG,
                  caption=ownermsg, 
                  buttons=saurabh_Button)
       else:
            await event.client.send_file(Thesaurabh,
                  SAURABH_IMG,
                  caption=usermsg, 
                  buttons=SaurabhX_Button)
                
