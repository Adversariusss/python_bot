import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from pars_film import film_rait, film_name
from admin_film import all_film
from aiogram.dispatcher.filters import Text

# Создание бота и вызов
bot = Bot(token="1626448931:AAE5qbxP9aJ3w6SXfINj2Rn8NC1AaVYSaVM")
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Создание команды /help
@dp.message_handler(commands=['help'])
async def cmd_help(message):
    await message.answer(
        text='''
    Мои команды:
    /help - увидеть это сообщение со списком команд
    /start - приветствие
    /filmdb - выведет случайный фильм из топ 250 рейтинга IMDb
    /filmadmin - выведет случайный фильм из личного топа создателя бота
        '''
    )


# Создание команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer(f"Привет {message.chat.first_name}")
    await cmd_help(message)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # buttons = ["Фильм из топ 250 рейтинга IMDb", "Фильм из личного топа владельца", "Пока не нужно советовать фйильм"]
    buttons = ["Фильм из личного топа владельца"]
    keyboard.add(*buttons)
    await message.answer("Я могу посоветовать тебе фильм.", reply_markup=keyboard)


"""
@dp.message_handler(Text(equals="Фильм топ 250 рейтинга IMDb"))
async def with_film(message: types.Message):
    z = str(film_imdb('/filmdb'))
    await message.answer(text=z) #film_imdb(message)
"""


# Создание ответа на кнопку "Фильм из личного топа владельца"
@dp.message_handler(Text(equals="Фильм из личного топа владельца"))
async def with_admin(message: types.Message):
    await message.answer(random.choice(all_film))


"""
@dp.message_handler(Text(equals="Пока не нужно советовать фильм"))
async def not_film(message: types.Message):
    if message.text == 'Пока не нужно советовать фильм':
        await cmd_help(message)
"""


# Создание команды /filmdb
@dp.message_handler(commands=['filmdb'])
async def film_imdb(message):
    x = random.randint(0, 249)
    if x < 10:
        await message.answer(text=f"{film_name[x][2:]} {film_rait[x]} IMDb")
    elif 10 < x < 100:
        await message.answer(text=f"{film_name[x][3:]} {film_rait[x]} IMDb")
    else:
        await message.answer(text=f"{film_name[x][4:]} {film_rait[x]} IMDb")


"""
@dp.message_handler(content_types=types.ContentType.TEXT)
async def send_text(message):
    text = message.text
    if message.text.lower() == 'filmadmin' or message.text.lower() == '/filmadmin':
        await message.answer(random.choice(all_film))
    else:
        pass
        # await cmd_help(message)
        # await message.reply(text=text)
"""


# Создание команды /filmadmin
@dp.message_handler(commands=['filmadmin'])
async def film_admin(message: types.Message):
    await message.answer(text=random.choice(all_film))


# Создание команды /alo - ответ: "alo"
@dp.message_handler(commands=['alo'])
async def alo(message: types.Message):
    await bot.send_message(message.chat.id, text='alo')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
