from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈𝘼𝙪𝙙𝙞𝙤 𝙦𝙪𝙖𝙡𝙞𝙩𝙮", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 𝘼𝙪𝙙𝙞𝙤 𝙑𝙤𝙡𝙪𝙢𝙚", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 𝘼𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙐𝙨𝙚𝙧𝙨", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 𝘿𝙖𝙨𝙝𝙗𝙤𝙖𝙧𝙙", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ 𝘾𝙡𝙤𝙨𝙚", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝙃𝙚𝙡𝙥𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙈𝙚𝙣𝙪",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 𝘼𝙪𝙙𝙞𝙤 𝙌𝙪𝙖𝙡𝙞𝙩𝙮", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 𝘼𝙪𝙙𝙞𝙤 𝙑𝙤𝙡𝙪𝙢𝙚", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 𝘼𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙐𝙨𝙚𝙧𝙨", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 𝘿𝙖𝙨𝙝𝙗𝙤𝙖𝙧𝙙", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
            InlineKeyboardButton(text="🔙 Go Back", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 𝙍𝙚𝙨𝙚𝙩 𝘼𝙪𝙙𝙞𝙤 𝙑𝙤𝙡𝙪𝙢𝙚 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 𝙇𝙤𝙬 𝙑𝙤𝙡", callback_data="LV"),
            InlineKeyboardButton(text="🔉 𝙈𝙚𝙙𝙞𝙪𝙢 𝙑𝙤𝙡", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 𝙃𝙞𝙜𝙝 𝙑𝙤𝙡", callback_data="HV"),
            InlineKeyboardButton(text="🔈 𝘼𝙢𝙥𝙡𝙞𝙛𝙞𝙚𝙙 𝙑𝙤𝙡", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 𝘾𝙪𝙨𝙩𝙤𝙢 𝙑𝙤𝙡𝙪𝙢𝙚 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 𝙂𝙤 𝙗𝙖𝙘𝙠", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 𝘾𝙪𝙨𝙩𝙤𝙢 𝙑𝙤𝙡𝙪𝙢𝙚 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME}  𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 𝙀𝙫𝙚𝙧𝙮𝙤𝙣𝙚", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 𝘼𝙙𝙢𝙞𝙣𝙨", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 𝘼𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝙐𝙨𝙚𝙧𝙨 𝙇𝙞𝙨𝙩𝙨", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 𝙂𝙤 𝙗𝙖𝙘𝙠", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ 𝙐𝙥𝙩𝙞𝙢𝙚", callback_data="UPT"),
            InlineKeyboardButton(text="💾 𝙍𝙖𝙢", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 𝘾𝙥𝙪", callback_data="CPT"),
            InlineKeyboardButton(text="💽 𝘿𝙞𝙨𝙠", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 𝙂𝙤 𝙗𝙖𝙘𝙠", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨**", buttons
