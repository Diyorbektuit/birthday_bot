from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from api.user_api import create_admin
from loader import dp
@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(create_admin(message.from_user.first_name, message.from_user.username, str(message.from_user.id)))
    await message.reply("Salom bizning botimizga xush kelibsiz\n"
                        "/group guruh yaratish uchun\n"
                        "/position guruhga lavozim qo'shish uchun\n"
                        "/add_user guruhingizga odam qo'shish uchun")



