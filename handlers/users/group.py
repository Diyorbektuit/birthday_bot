from aiogram import types
from aiogram.dispatcher import FSMContext
from api.group_api import create_group
from api.user_api import take_admin_id
from states.CreateGroupState import CreateGroupState
from loader import dp


@dp.message_handler(commands=['group'])
async def send_group1(message: types.Message):
    await message.reply("Guruh nomini yuboring?")
    await CreateGroupState.body.set()


@dp.message_handler(state=CreateGroupState.body)
async def create_group2(message: types.Message, state: FSMContext):
    admin_id = take_admin_id(message.from_user.id)
    group_name = str(message.text)
    await message.reply(create_group(admin_id, group_name))
    await state.finish()