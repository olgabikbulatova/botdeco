from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from database.db import insert_db
from keyboards.contacts import get_contact
from keyboards.for_apply_no_project import kit_keyboard, material_kb, order_date_kb
from settings.settings import bot, admin_id

router = Router()


class NewApplyNoProject(StatesGroup):
    kitchen_type = State()
    kitchen_material = State()
    order_date = State()
    contacts = State()


k_type = {"kit_straight", "kit_corner", "kit_ptype", "kit_isl"}
k_material = {"plastic", "mdf", "painted", "dont_know"}
k_date = {"this_month", "next_mont", "in_6m", "in_year"}


@router.callback_query(StateFilter(None), F.data == "no")
async def kit_type(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Какой тип кухни Вам нужен?",
        reply_markup=kit_keyboard()
    )
    await state.set_state(NewApplyNoProject.kitchen_type)


@router.callback_query(NewApplyNoProject.kitchen_type, F.data.in_(k_type))
async def kit_mat(callback: CallbackQuery, state: FSMContext):
    await state.update_data(kitchen_type=callback.data)
    await callback.message.answer(
        "Какие фасады будут у Вашей кухни?",
        reply_markup=material_kb()
    )
    await state.set_state(NewApplyNoProject.kitchen_material)


@router.message(NewApplyNoProject.kitchen_type)
async def no_answer(message: Message):
    await message.answer(
        "Пожалуйста, выберите один из преложенных вариантов\n\n",
        reply_markup=kit_keyboard()
    )


@router.callback_query(NewApplyNoProject.kitchen_material, F.data.in_(k_material))
async def kit_date(callback: CallbackQuery, state: FSMContext):
    await state.update_data(kitchen_mtl=callback.data)
    await callback.message.answer(
        "Когда Вы планируете заказать кухню?",
        reply_markup=order_date_kb()
    )
    await state.set_state(NewApplyNoProject.order_date)


@router.message(NewApplyNoProject.kitchen_material)
async def no_answer(message: Message):
    await message.answer(
        "Пожалуйста, выберите один из преложенных вариантов\n\n",
        reply_markup=material_kb()
    )


@router.callback_query(NewApplyNoProject.order_date, F.data.in_(k_date))
async def get_user(callback: CallbackQuery, state: FSMContext):
    await state.update_data(order_date=callback.data)
    await callback.message.answer(
        "\U0001F4F2 Отправьте нам свой контакт \U0001F4F2, нажмите кнопку внизу экрана",
        reply_markup=get_contact()
    )
    await state.set_state(NewApplyNoProject.contacts)


@router.message(NewApplyNoProject.order_date)
async def no_answer(message: Message):
    await message.answer(
        "Пожалуйста, выберите один из преложенных вариантов\n\n",
        reply_markup=order_date_kb()
    )


@router.message(NewApplyNoProject.contacts, F.contact)
async def get_order_data(message: Message, state: FSMContext):
    user_data = await state.get_data()
    text_2 = (f"пользователь {message.contact.first_name} номер телефона {message.contact.phone_number}"
            f" хочет записаться на замер.\n\n"
            f"Предварительные данные по заказу:\n\n "
            f"тип кухни: {user_data['kitchen_type']}\n\n"
            f"фасады: {user_data['kitchen_mtl']}\n\n"
            f"планируемая дата заказа: {user_data['order_date']}\n\n")
    # передаем данные по запросу админу
    await bot.send_message(admin_id, text_2)
    # передать данные в бд user_id, name, phone, kitchen_type, kitchen_material, order_date
    insert_db(
        message.contact.user_id,
        message.contact.first_name,
        message.contact.phone_number,
        user_data['kitchen_type'],
        user_data['kitchen_mtl'],
        user_data['order_date']
    )
    await message.answer(
        f"Благодарим за обращение к нашему боту"
        f"Вы можете узнать больше информации о нашей компании и ознакомиться "
        f"с примерами работ на нашем сайте www.fabrikamebelideco.ru",
        reply_markup=ReplyKeyboardRemove()
    )
    # Сброс состояния и сохранённых данных у пользователя
    await state.clear()


@router.message(NewApplyNoProject.contacts)
async def no_answer(message: Message):
    await message.answer(
        "\U00002B07 Для того чтобы направить контакт нажмите на кнопку внизу экрана \U00002B07 \n\n",
        reply_markup=get_contact()
    )

