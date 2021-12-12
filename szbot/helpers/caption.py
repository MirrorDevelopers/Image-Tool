from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

imgcaption = """
☘️ **Random Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** :  [🎨 Imᥲgᥱ Tooᥣs Bot](https://t.me/logogenbot )
🌷 **Requestor** : {message.from_user.username}
⚡️ **Powered By **: `InfinityGO ´
◇───────────────◇
©2021 InfinityGO team  **All Right Reserved**⚠️️
"""
repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="➕Add me to your group ➕", url=f"http://t.me/LogoGenBot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="🗣️Join my updates", url=f"https://t.me/TeamInfinityGo") 
        ]
      ]      
    )
