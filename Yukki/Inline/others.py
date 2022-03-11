from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 𝙂𝙀𝙏 𝙇𝙔𝙍𝙄𝘾𝙎",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ 𝙔𝙊𝙐𝙍 𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ 𝙂𝙍𝙊𝙐𝙋 𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬇️ 𝙂𝙀𝙏 𝘼𝙐𝘿𝙄𝙊/𝙑𝙄𝘿𝙀𝙊",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝙂𝙊 𝘽𝘼𝘾𝙆",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 𝘾𝙇𝙊𝙎𝙀 𝙈𝙀𝙉𝙐",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ 𝙂𝙀𝙏 𝘼𝙐𝘿𝙄𝙊",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⬇️ 𝙂𝙀𝙏 𝙑𝙄𝘿𝙀𝙊",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ 𝙂𝙊 𝘽𝘼𝘾𝙆", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 𝘾𝙇𝙊𝙎𝙀 𝙈𝙀𝙉𝙐", callback_data=f"close"),
        ],
    ]
    return buttons
