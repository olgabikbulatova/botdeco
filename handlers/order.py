from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from database.db import find_order
from keyboards.contacts import get_contact
from settings.settings import bot, admin_id

router = Router()


@router.message(F.text)  # [2]
async def order_num(message: Message):
    try:
        order_id = int(message.text)
        if find_order(order_id):
            text = f'{message.from_user.full_name},  хочет задать вопрос по договору {find_order(order_id)}'
            await bot.send_message(admin_id, text)
            await message.answer(
                "Благодарим за обращение к нашему боту. Менеджер свяжется с Вами и ответит на Ваши вопросы",
                # reply_markup=get_keyboard()
            )
        else:
            await message.answer(
                f"Договор с таким номером не найден, оставьте свой номер телефона и мы свяжемся с Вами для решения вопроса",
                reply_markup=get_contact()
            )
    except (TypeError, ValueError) as e:
        await message.answer(
            "Договор с таким номером не найден, оставьте свой номер телефона и мы свяжемся с Вами для решения вопроса",
            reply_markup=get_contact()
        )


@router.message(F.contact)
async def send_contacts(message: Message):
    text1 = (f"клиент {message.contact.first_name} {message.contact.last_name} тел.{message.contact.phone_number} "
             f"хочет задать вопрос по заказу. номер договора клиент не помнит")
    await bot.send_message(admin_id, text1)
    await message.answer(
        "Благодарим за обращение к нашему боту",
        reply_markup=ReplyKeyboardRemove()
    )
