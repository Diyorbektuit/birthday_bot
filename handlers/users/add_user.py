import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from api.position_api import group_position, take_position_id
from api.group_api import take_group_id, user_groups
from api.user_api import take_admin_id, add_group_user
from states.AddUserState import AddUserState
from loader import dp, bot


@dp.message_handler(commands=['add_user'], state=None)
async def add_user1(message: types.Message):
    user_id = take_admin_id(message.from_user.id)
    groups = user_groups(user_id)
    await message.reply(f"Qaysi guruhga qo'shmoqchisiz?\n"
                        f"Sizda ushbu guruhlar mavjud:{groups}")
    await AddUserState.body.set()


@dp.message_handler(state=AddUserState.body)
async def add_user2(message: types.Message, state: FSMContext):
    admin_id = take_admin_id(message.from_user.id)
    group_id = take_group_id(message.text)
    await state.update_data(
        {"admin_id": admin_id, "group_id": group_id}
    )
    positions = group_position(group_id)
    await message.answer(f"Qaysi lavozimga qo'shmoqchisiz?\n"
                         f"Bu guruhda ushbu lavozimlar bor:{positions}")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.position_id)
async def add_user3(message: types.Message, state: FSMContext):
    position_id = take_position_id(message.text)
    await state.update_data(
        {"position_id": position_id}
    )
    await message.answer("Qo'shmoqchi bo'lgan odamizni telegram idsini yuboring")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.tg_id)
async def add_user4(message: types.Message, state: FSMContext):
    tg_id = message.text
    try:
        user = await bot.get_chat(tg_id)
    except aiogram.utils.exceptions.ChatNotFound:
        await message.answer("Bu idli user topilmadi iltimos idisini bosqattan tekshirib yuboring")
        return

    first_name = user.first_name or 'None'
    last_name = user.last_name or 'None'
    username = user.username or 'None'

    await state.update_data(
        {"tg_id": tg_id, "first_name": first_name, "last_name": last_name, "username": username}
    )

    await message.answer("Tug'ulgan kununi yuboring yil-oy-kun (e.g., 1999-09-09):")
    await AddUserState.next()



@dp.message_handler(state=AddUserState.birthday)
async def add_user5(message: types.Message, state: FSMContext):
    birthday = message.text
    data = await state.get_data()
    admin_id = data.get("admin_id")
    group_id = data.get("group_id")
    position_id = data.get("position_id")
    tg_id = data.get("tg_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    username = data.get("username")
    await message.reply(add_group_user(admin_id, group_id, position_id, tg_id, first_name, last_name, username, birthday))
    await state.finish()
