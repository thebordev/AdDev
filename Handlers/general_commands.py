from aiogram import types
from aiogram.dispatcher.filters import Text

from misc import dp
from db import Users
import keyboard

@dp.message_handler(commands=['start', 'help'])
async def register(message: types.Message):
    Users().register_user(message.from_user.id,
                          message.from_user.username,
                          message.from_user.first_name,
                          message.from_user.last_name)
    text = "Привет, " + message.from_user.first_name + "! Меня разработал @thebordevs, видеоролик по созданию этого бота ты сможешь найти на его YouTube\nКод проекта на GitHub"
    await message.answer(text, reply_markup=keyboard.start())
    await message.answer("<b>Что я умею?</b>"
                         "\n\n<i>Я могу вести статистику твоего Телеграм канала, вести переговоры с рекламодателями, "
                         "зарабатывая тем самым тебе копеечку. Добавь бота в администраторы своего сообщества, предоставь доступ к"
                         "сообщениям и все! Предложения по рекламным контрактом буду присылать тебе лично, но такжже ты и сам можешь найти его себе на нашей "
                         "бирже! Все очень просто!</i>", parse_mode="HTML", reply_markup=keyboard.main())
