from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def yes_no_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="\U00002705 ДА",
        callback_data="yes")
    )
    kb.add(InlineKeyboardButton(
        text="\U0000274C НЕТ",
        callback_data="no")
    )
    return kb.as_markup(resize_keyboard=True)


def kit_ord_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="\U0001F3E1 Заказать кухню",
        callback_data="kitchen")
    )
    kb.add(InlineKeyboardButton(
        text="\U0001F4DD Вопрос по заказу",
        callback_data="order")
    )
    return kb.as_markup()

