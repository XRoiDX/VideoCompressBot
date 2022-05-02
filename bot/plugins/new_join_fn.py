#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005


from bot.database import Database
from bot.localisation import Localisation
from bot import (
    UPDATES_CHANNEL,
    DATABASE_URL,
    SESSION_NAME
)
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

db = Database(DATABASE_URL, SESSION_NAME)
CURRENT_PROCESSES = {}
CHAT_FLOOD = {}
broadcast_ids = {}

async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    if not await db.is_user_exist(message.chat.id):
        await db.add_user(message.chat.id)
    ## Force Sub ##
    if UPDATES_CHANNEL is not None:
        try:
            user = await client.get_chat_member(UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
               await message.reply_text(
                   text="ꜱᴏʀʀy ꜱɪʀ, ᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴄᴏɴᴀᴛᴄᴛ ᴍy [ᴏᴡɴᴇʀ](https://t.me/Space4AFML).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await message.reply_text(
                text="**🔶 PLEASE JOIN MY UPDATES CHANNEL 🔶!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ Uᴩᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ 🌸", url=f"https://t.me/{UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await message.reply_text(
                text="ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍy  [ᴏᴡɴᴇʀ](https://t.me/Space4AFML).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    ## Force Sub ##
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ Cʜᴀɴɴᴇʟ 🌸', url='https://t.me/XRoid_BotZ')
                ],
                [
                    InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ 🌸', url='https://t.me/XRoid_Support')
                ],
                [
                    InlineKeyboardButton('Dᴇᴠʟᴏᴩᴇʀ 🌸', url='https://github.com/XRoiDX'), # Bloody Thief, Don't Become a Developer by Stealing other's Codes & Hard Works!
                    InlineKeyboardButton('Oᴛʜᴇʀ Bᴏᴛꜱ 🌸', url='https://t.me/XRoid_BotZ/5') # Must Give us Credits!
                ]
            ]
        ),
        quote=True
    )
