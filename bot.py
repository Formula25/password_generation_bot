import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import message_texts
import password
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from rich import print


#sqlite3.connect(

#Вывод сообщения о запуске сервера
print("[green]Сервер запущен![/green]")

# Подключение токена из виртуального окружения
#TOKEN = os.getenv("TOKEN")
#bot = Bot(token=TOKEN)
bot = Bot(token="5552245555:AAEfGwuZIfRmgTBujfeqsvBQkThGeB9BptM")
dp = Dispatcher(bot)


# Кнопки выбора сложности пароля
pass_btn = InlineKeyboardMarkup(row_width=1)
easy_pass_btn = InlineKeyboardButton(text='Легкий пароль', callback_data="easy")
medium_pass_btn = InlineKeyboardButton(text='Средний пароль', callback_data="medium")
hard_pass_btn = InlineKeyboardButton(text='Сложный пароль', callback_data="hard")
pass_btn.add(easy_pass_btn, medium_pass_btn, hard_pass_btn)

# Кнопка создания еще одного пароля


# Приветственное сообщение
@dp.message_handler(commands="start")
async def cmd_start(msg: types.Message):
    # Вывод картинки перед сообщением
    await bot.send_photo(
            msg.from_user.id,  
            types.InputFile("/Users/arseniitaturevich/code/password_gen_bot/img/9bf70e1154de93a5.png"))
    kb = [
        [
            types.KeyboardButton(text="Создать пароль 🎰"),
            types.KeyboardButton(text="Информация"),
            types.KeyboardButton(text="Советы по безопасности")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Что вы хотите сделать?"
    )
    # Отправка сообщения и вывод кнопок на клавиатуре
    await msg.answer(
            f"Приветик, {msg.from_user.first_name}!\n{message_texts.HELLO}",
            reply_markup=keyboard
            )


right_commands = ("Информация", "Создать пароль 🎰", "Советы по безопасности")


# действие при нажатии кнопки "Создать пароль"
@dp.message_handler(lambda message: message.text == 'Создать пароль 🎰')
async def url_command(message: types.Message):
   await message.answer('Выберите сложность пароля:', reply_markup=pass_btn)


# действие при нажатии кнопки "Информация"
@dp.message_handler(lambda message: message.text == "Информация")
async def information(message: types.Message):
    await message.answer(message_texts.INFO)


# действие при нажатии кнопки "Советы по безопасности"
@dp.message_handler(lambda message: message.text == "Советы по безопасности")
async def tips(message: types.Message):
    await message.answer(message_texts.TIPS)


# проверка того, какое сообщение отправляет пользователь в бота
@dp.message_handler(lambda message: message.text not in right_commands)
async def wrong_commands(message: types.Message):
    await bot.send_message(
            message.from_user.id,
            message_texts.WRONG_COMMAND, 
            reply_to_message_id=message.message_id
            )


# Вывод информации при команде /info
@dp.message_handler(commands="info")
async def info(msg: types.Message):
    await msg.answer(message_texts.INFO)


# Вывод паролей по уровню сложностей
@dp.callback_query_handler()
async def callback_password(callback_query: types.CallbackQuery):
    code = callback_query.data
    if code ==  "easy":
        get_password = password.easy_pass_gen()
        await bot.send_message(
                callback_query.from_user.id, 
                text=f'Ваш пароль: \n\n`{get_password}`',
                parse_mode="MARKDOWN"
                )
        print(f"Пароль: {get_password}\nСоздан пользователям: {callback_query.from_user.username}")
        print("-")
    elif code == "medium":
        get_password = password.medium_pass_gen()
        await bot.send_message(
                callback_query.from_user.id, 
                text=f'Ваш пароль: \n\n`{get_password}`',
                parse_mode="MARKDOWN"
                )
        print(f"Пароль: {get_password}\nСоздан пользователям: {callback_query.from_user.username}")
        print("-")
    elif code == "hard":
        get_password = password.hard_pass_gen()
        await bot.send_message(
                callback_query.from_user.id, 
                text=f'Ваш пароль: \n\n`{get_password}`',
                parse_mode="MARKDOWN"
                )
        print(f"Пароль: {get_password}\nСоздан пользователям: {callback_query.from_user.username}")
        print("-")


@dp.message_handler(commands="tips")
async def get_tips(msg: types.Message):
    await msg.answer(message_texts.TIPS)


if __name__ == '__main__':
    executor.start_polling(dp)

