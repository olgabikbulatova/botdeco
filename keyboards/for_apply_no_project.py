from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kit_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="\U00002705 Прямая", callback_data="kit_straight"),
            InlineKeyboardButton(text="\U00002705 Угловая", callback_data="kit_corner")
        ],
        [
            InlineKeyboardButton(text="\U00002705 П-образная", callback_data="kit_ptype"),
            InlineKeyboardButton(text="\U00002705 С островом", callback_data="kit_isl")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def material_kb() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="\U0000267B Пластик", callback_data="plastic"),
            InlineKeyboardButton(text="\U0001F530 МДФ", callback_data="mdf")
        ],
        [
            InlineKeyboardButton(text="\U0001F3A8 Эмаль", callback_data="painted"),
            InlineKeyboardButton(text="\U00002754 Не знаю", callback_data="dont_know")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def order_date_kb() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="в этом месяце", callback_data="this_month"),
            InlineKeyboardButton(text="в следующем месяце", callback_data="next_month")
        ],
        [
            InlineKeyboardButton(text="в ближайшие полгода", callback_data="in_6m"),
            InlineKeyboardButton(text="через год", callback_data="in_year")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

