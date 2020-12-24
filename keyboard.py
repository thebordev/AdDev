from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

def start():
    keyboard = types.InlineKeyboardMarkup()
    yt = types.InlineKeyboardButton(text="YouTube",
                                    url="https://www.youtube.com/channel/UC1X3VwGvWQvWFkeZKAps86A?view_as=subscriber")
    gh = types.InlineKeyboardButton(text="GitHub", url="https://github.com/thebordev")
    tg = types.InlineKeyboardButton(text="Мой телеграм канал", url="https://t.me/thebordevs")
    keyboard.add(yt, gh, tg)
    return keyboard

def main():
    keyboard = types.ReplyKeyboardMarkup()
    menu_1 = KeyboardButton(text="Биржа рекламы 📊")
    menu_2 = KeyboardButton(text="Предложения 📝")
    menu_3 = KeyboardButton(text="Мои каналы 📚")
    menu_4 = KeyboardButton(text="Добавить канал ➕")
    keyboard.add(menu_1, menu_2, menu_3, menu_4)
    return keyboard
