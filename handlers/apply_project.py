from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.contacts import get_contact
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from settings.settings import bot, admin_id

router = Router()  # [1]


class NewApplyWithProject(StatesGroup):
    choosing_project = State()
    getting_contact = State()


@router.callback_query(StateFilter(None), F.data == "yes")  # [2]
async def get_project(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Отправьте нам свой проект  в формате jpg или jpeg")
    # Устанавливаем пользователю состояние "выбирает проект"
    await state.set_state(NewApplyWithProject.choosing_project)


@router.message(NewApplyWithProject.choosing_project, F.photo)
async def get_user(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer(
        "\U0001F4F2 Отправьте нам свой контакт \U0001F4F2, нажмите кнопку внизу экрана",
        reply_markup=get_contact()
    )
    await state.set_state(NewApplyWithProject.getting_contact)


@router.message(NewApplyWithProject.choosing_project)
async def not_photo(message: Message):
    await message.answer(
        text="Пожалуйста отправьте ваш проект в формате jpg/jpeg\n\n",
    )


@router.message(NewApplyWithProject.getting_contact, F.contact)
async def send_contacts(message: Message, state: FSMContext):
    user_data = await state.get_data()
    text = f"пользователь {message.contact.first_name} номер телефона {message.contact.phone_number} отправил вам на просчет свой проект"
    # передаем данные по запросу админу
    await bot.send_photo(admin_id, user_data['photo'],caption=text)
    # передать данные в бд

    await message.answer(
        f"Благодарим за обращение к нашему боту"
        f"Вы можете узнать больше информации о нашей компании и ознакомиться "
        f"с примерами работ на нашем сайте www.fabrikamebelideco.ru",
        reply_markup=ReplyKeyboardRemove()
    )
    # Сброс состояния и сохранённых данных у пользователя
    await state.clear()

