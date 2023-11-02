from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/english_hindi_friends_chatting"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/Devil_ki_masoomiyat"),
            InlineKeyboardButton(text=_["S_B_7"], url=f"https://te.legra.ph/file/e8c8767cf21eeb7001d45.mp4"),
        ],
    ]

    return buttons
