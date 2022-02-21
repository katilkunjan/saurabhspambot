from saurabhspambot import saurabh, saurabh2, saurabh3, saurabh4, saurabh5, saurabh6, saurabh7, saurabh8, saurabh9, saurabh10, saurabh11, saurabh12, saurabh13, saurabh14, saurabh15, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from saurabhspambot import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"

saurabh_Help = "__Click On Below Buttons for help__"


@saurabh.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh11.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh12.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh13.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh14.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@saurabh15.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=saurabh_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/heartbrokenperson1")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmechk <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @tera_baap_katil**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @tera_baap_katil**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @tera_baap_katil**
"""                     
           
           
@saurabh.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh2.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh3.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh4.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh5.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh6.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh7.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh8.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh9.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh10.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh11.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh12.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh13.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh14.on(events.CallbackQuery(pattern=r"help_back"))
@saurabh15.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Riz_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/heartbrokenperson1")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own saurabh X Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@saurabh.on(events.CallbackQuery(pattern=r"spam"))
@saurabh2.on(events.CallbackQuery(pattern=r"spam"))
@saurabh3.on(events.CallbackQuery(pattern=r"spam"))
@saurabh4.on(events.CallbackQuery(pattern=r"spam"))
@saurabh5.on(events.CallbackQuery(pattern=r"spam"))
@saurabh6.on(events.CallbackQuery(pattern=r"spam"))
@saurabh7.on(events.CallbackQuery(pattern=r"spam"))
@saurabh8.on(events.CallbackQuery(pattern=r"spam"))
@saurabh9.on(events.CallbackQuery(pattern=r"spam"))
@saurabh10.on(events.CallbackQuery(pattern=r"spam"))
@saurabh11.on(events.CallbackQuery(pattern=r"spam"))
@saurabh12.on(events.CallbackQuery(pattern=r"spam"))
@saurabh13.on(events.CallbackQuery(pattern=r"spam"))
@saurabh14.on(events.CallbackQuery(pattern=r"spam"))
@saurabh15.on(events.CallbackQuery(pattern=r"spam"))

async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own saurabh X Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@saurabh.on(events.CallbackQuery(pattern=r"raid"))
@saurabh2.on(events.CallbackQuery(pattern=r"raid"))
@saurabh3.on(events.CallbackQuery(pattern=r"raid"))
@saurabh4.on(events.CallbackQuery(pattern=r"raid"))
@saurabh5.on(events.CallbackQuery(pattern=r"raid"))
@saurabh6.on(events.CallbackQuery(pattern=r"raid"))
@saurabh7.on(events.CallbackQuery(pattern=r"raid"))
@saurabh8.on(events.CallbackQuery(pattern=r"raid"))
@saurabh9.on(events.CallbackQuery(pattern=r"raid"))
@saurabh10.on(events.CallbackQuery(pattern=r"raid"))
@saurabh11.on(events.CallbackQuery(pattern=r"raid"))
@saurabh12.on(events.CallbackQuery(pattern=r"raid"))
@saurabh13.on(events.CallbackQuery(pattern=r"raid"))
@saurabh14.on(events.CallbackQuery(pattern=r"raid"))
@saurabh15.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own saurabh X Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@saurabh.on(events.CallbackQuery(pattern=r"extra"))
@saurabh2.on(events.CallbackQuery(pattern=r"extra"))
@saurabh3.on(events.CallbackQuery(pattern=r"extra"))
@saurabh4.on(events.CallbackQuery(pattern=r"extra"))
@saurabh5.on(events.CallbackQuery(pattern=r"extra"))
@saurabh6.on(events.CallbackQuery(pattern=r"extra"))
@saurabh7.on(events.CallbackQuery(pattern=r"extra"))
@saurabh8.on(events.CallbackQuery(pattern=r"extra"))
@saurabh9.on(events.CallbackQuery(pattern=r"extra"))
@saurabh10.on(events.CallbackQuery(pattern=r"extra"))
@saurabh11.on(events.CallbackQuery(pattern=r"extra"))
@saurabh12.on(events.CallbackQuery(pattern=r"extra"))
@saurabh13.on(events.CallbackQuery(pattern=r"extra"))
@saurabh14.on(events.CallbackQuery(pattern=r"extra"))
@saurabh15.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own saurabh X Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
