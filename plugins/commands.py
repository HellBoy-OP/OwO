from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME as U, mp
from config import Config
from .callback import HELP as uwu

CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nUse /help to get all commands 😪.</b>"
HELP = uwu



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('Channel', url='https://t.me/its_hellbot'),
        InlineKeyboardButton('Github', url='https://github.com/The-HellBot'),
    ],
    [
        InlineKeyboardButton('Owner', url='https://t.me/ForGo10god'),
        InlineKeyboardButton('Source', url='https://t.me/its_hellbot'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('Channel', url='https://t.me/its_hellbot'),
            InlineKeyboardButton('Github', url='https://github.com/The-HellBot'),
        ],
        [
            InlineKeyboardButton('Owner', url='https://t.me/ForGo10God'),
            InlineKeyboardButton('Source', url='https://t.me/its_hellbot'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
