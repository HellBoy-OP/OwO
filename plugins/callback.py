from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from utils import mp
from config import Config
playlist=Config.playlist

HELP = """

<b>✓ Add bot and helper account in your Group with admin rights.

✓ Start a VoiceChat.</b>

**📍 Common Commands :**

• `/play` - __Reply to an audio file or YouTube link to play it or use /play <song name>.__
• `/dplay` - __Play music from Deezer, Use /dplay <song name>__
• `/player` - __Show current playing song.__
• `/help` - __Show help for commands__
• `/playlist` - __Shows the playlist.__

**📍 Admin Commands :**
• `/skip` - __Skip current or n where n >= 2__
• `/join` - __Join voice chat.__
• `/leave` - __Leave current voice chat.__
• `/vc` - __Check which VC is joined.__
• `/stop` - __Stop playing.__
• `/radio` - __Start Radio.__
• `/stopradio` - __Stops Radio Stream.__
• `/replay` - __Play from the beginning.__
• `/clean` - __Remove unused RAW PCM files.__
• `/pause` - __Pause playing.__
• `/resume` - __Resume playing.__
• `/volume` - __Change volume(0-200).__
• `/mute` - __Mute in VC.__
• `/unmute` - __Unmute in VC.__
• `/restart` - __Update restarts the Bot.__
"""



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    admins = await mp.get_admins(Config.CHAT)
    if query.from_user.id not in admins and query.data != "help":
        await query.answer(
            "😒",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "replay":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} Empty Playlist"
        else:
            pl = f"{emoji.PLAY_BUTTON} **Playlist :**\n" + "\n".join([
                f"**{i}**. **🎸 {x[1]}**\n   👤 **Requested by :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "pause":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"{emoji.PLAY_BUTTON} **Playlist :**\n" + "\n".join([
                f"**{i}**. **🎸 {x[1]}**\n   👤 **Requested by :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="resume"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    
    elif query.data == "resume":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"{emoji.PLAY_BUTTON} **Playlist :**\n" + "\n".join([
                f"**{i}**. **🎸 {x[1]}**\n   👤 **Requested by :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data=="skip":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"{emoji.PLAY_BUTTON} **Playlist :**\n" + "\n".join([
                f"**{i}**. **🎸 {x[1]}**\n   👤 **Requested by :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏯", callback_data="pause"),
                        InlineKeyboardButton("⏩", callback_data="skip")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
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
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )

