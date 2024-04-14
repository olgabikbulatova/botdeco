from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.for_start import kit_ord_kb, yes_no_kb


router = Router()  # [1]


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    kb = kit_ord_kb()
    await message.answer(
        "Привет, это бот фабрики мебели Деко."
        "Я помогу Вам сделать заказ или отвечу на вопросы о Вашем текущем заказе."
        "Что Вас интересует:",
        reply_markup=kb
    )


@router.callback_query(F.data == "kitchen")
async def kitchen(callback: CallbackQuery):
    await callback.message.answer(
        "У вас уже есть готовый проект кухни?",
        reply_markup=yes_no_kb()
    )


@router.callback_query(F.data == "order")
async def order(callback: CallbackQuery):
    await callback.message.answer("Введите номер Вашего договора")
