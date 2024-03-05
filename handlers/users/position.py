from aiogram import types
from aiogram.dispatcher import FSMContext
from api.position_api import create_position
from api.group_api import take_group_id, user_groups
from api.user_api import take_admin_id
from states.CreatePositionState import CreatePositionState
from loader import dp


@dp.message_handler(commands=['position'], state=None)
async def create_position1(message: types.Message):
    await message.reply('Lavozim nomini yuboring:')
    await CreatePositionState.body.set()


@dp.message_handler(state=CreatePositionState.body)
async def create_position_2(message: types.Message, state: FSMContext):
    admin_id = take_admin_id(message.from_user.id)
    position = str(message.text)
    groups = user_groups(admin_id)
    await state.update_data(
        {"admin_id": admin_id, "position": position}
    )
    await message.answer(f"Qaysi guruhda lavozim yaratmoqchisiz?\n"
                         f"Sizda ushbu guruhlar mavjud:{groups}")
    await CreatePositionState.next()


@dp.message_handler(state=CreatePositionState.group)
async def create_position_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    admin_id = data.get("admin_id")
    position = data.get("position")
    group_id = take_group_id(message.text)
    await message.reply(create_position(admin_id, group_id, position))
    await state.finish()