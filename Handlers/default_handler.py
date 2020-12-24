from aiogram import types

from misc import dp, bot
from settings import BOT_ID
from db import Channels, Users
import keyboard


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    if message.text == "Добавить канал ➕":
        await message.answer("<b>Как добавить свой канал в нашу базу?</b>\n\n"
                             "Чтобы добавить канал в нашу базу, добавьте в свое сообщества нашего бота @addev_bot, "
                             "потом перешлите любой пост из канала сюда.", parse_mode="HTML")

    if message['forward_from_chat']:
        if await bot.get_chat_member(message['forward_from_chat']['id'], BOT_ID):
            subs = await bot.get_chat_members_count(message['forward_from_chat']['id'])
            Channels().register_channel(message['forward_from_chat']['id'],
                                        message['forward_from_chat']['username'],
                                        message['forward_from_chat']['title'],
                                        message.from_user.id,
                                        message.from_user.username,
                                        subs)

            Users().add_channel_user(message.from_user.id, message['forward_from_chat']['username'])
            await message.answer(
                "Заявка на добавление в базу принята, ответ может занять некоторое время, просим прощения😔\n\n"
                "Как только ваш канал проверят, Вам придет сообщение 'Биржа открыта!', "
                "тогда вы сможете получать и выполнять заказы по рекламе. Спасибо, " + message.from_user.first_name + "!")
            await message.answer("Канал успешно добавлен в базу!", reply_markup=keyboard.main())
        else:
            await message.answer("Дайте права администратора боту, заново отпрвьте мне пост")