import logging
import os
from Config import Messages as tr
from Config import Config as C
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = C.UPDATES_CHANNEL
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.incoming & filters.command(['start', 'start@FZForceSubscribeBot']))
def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry, You are Banned to use me. Contact my [Owner](https://t.me/FZConnectBot).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(message.chat.id,
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                           InlineKeyboardButton("Join Updates Channel", url="https://t.me/FZBOTS"),
                           InlineKeyboardButton("Support", url="https://t.me/FZConnectBot")
                      ],

                  ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Join Updates Channel", url="https://t.me/FZBOTS"),
                    InlineKeyboardButton("Support Group", url="https://t.me/FZConnectBot")
                ],
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.incoming & filters.command(['source_code']))
def _source_code(client, message):
    client.send_message(message.chat.id,
        text=tr.SC_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Creator", url="https://t.me/Monster_ZeroX")
                ],
                [
                    InlineKeyboardButton("Join Updates Channel", url="https://t.me/FZBOTS"),
                    InlineKeyboardButton("Support", url="https://t.me/FZConnectBot")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.incoming & filters.command(['help']))
def _help(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry, You are Banned to use me. Contact my [Owner](https://t.me/FZConnectBot).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(
                chat_id=message.chat.id,
                text="🔔 **FORCE SUBSCRIBE** [🔔](https://telegra.ph/file/39cc7b8206cedfd5d96c2.jpg)\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.\n\n**SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.\n\n**COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe\n",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '-->', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        button = [
            [InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '-->', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
