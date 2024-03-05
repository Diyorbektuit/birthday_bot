from aiogram import types
from aiogram.dispatcher import FSMContext
from api.api_birtday import birthday
from api.user_api import take_admin_id
from api.group_api import user_groups, take_group_id
from states.BirthdayState import BirthdayState
from loader import dp


@dp.message_handler(commands=['birthday'])
async def get_birthday(message: types.Message):
    admin_id = take_admin_id(message.from_user.id)
    groups = user_groups(admin_id)
    await message.reply(f"Qaysi guruhga qo'shmoqchisiz?\n"
                        f"Sizda ushbu guruhlar mavjud:{groups}")
    await message.reply("Qaysi guruh odamlarini tug'ulgan kunlariga qancha qolganini bilmoqchisiz?")
    await BirthdayState.body.set()


@dp.message_handler(state=BirthdayState.body)
async def get_birthday(message: types.Message, state: FSMContext):
    admin_id = take_admin_id(message.from_user.id)
    group_id = take_group_id(message.text)
    print(group_id)
    await message.reply(birthday(admin_id, group_id))
    await state.finish()