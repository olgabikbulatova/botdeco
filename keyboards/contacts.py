from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_contact() -> ReplyKeyboardMarkup:
    gc = ReplyKeyboardBuilder()
    gc.button(text="Отправить контакт", request_contact=True)
    return gc.as_markup(resize_keyboard=True)

