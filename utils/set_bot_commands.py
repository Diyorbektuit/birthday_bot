from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("group", "Guruh yaratish"),
            types.BotCommand("position", "Guruhlarda lavozim yaratish"),
            types.BotCommand("add_user", "Guruhga odam qo'shish"),
            types.BotCommand("birthday", "Guruhdagilarni tug'ulgan kuniga qancha vaqt qolganini ko'rish")
        ]
    )
