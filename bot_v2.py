import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.handler import SkipHandler
from pars_film import film_rait, film_name
from all_film import all_film

# Создание бота и вызов
bot = Bot(token="1626448931:AAE5qbxP9aJ3w6SXfINj2Rn8NC1AaVYSaVM")
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['help'])
async def cmd_help(message):
    await message.answer(
        text='''
    Мои команды:
    /help - увидеть это сообщение со списком команд
    /start - приветствие
    filmadmin - выведет случайный фильм из личного топа создателя бота
    /filmdb - выведет случайный фильм из топ 250 рейтинга IMDb
    /alo - alo
        '''
    )


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer(f"Привет {message.chat.first_name}, а ты раскабанел")
    await cmd_help(message)


@dp.message_handler(commands=['filmdb'])
async def film_imdb(message):
    x = random.randint(0, 249)
    if x < 10:
        await message.answer(text=f"{film_name[x][2:]} {film_rait[x]} IMDb")
    elif x > 10 and x < 100:
        await message.answer(text=f"{film_name[x][3:]} {film_rait[x]} IMDb")
    else:
        await message.answer(text=f"{film_name[x][4:]} {film_rait[x]} IMDb")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def send_text(message):
    text = message.text
    if message.text.lower() == 'привет':
        await message.answer(text='Привет, создатель')
    elif message.text.lower() == 'пока':
        await message.answer(text='Прощай, создатель')
    elif message.text.lower() == 'filmadmin':
        await message.answer(random.choice(all_film))


@dp.message_handler(commands=['filmadmin'])
async def film_admin(message: types.Message):
    await bot.send_message(random.choice(all_film))

@dp.message_handler(commands=['alo'])
async def alo(message: types.Message):
    await bot.send_message(message.from_user.id, text='alo')

    #async def echo_message(msg: types.Message):
    #await bot.send_message(msg.from_user.id, msg.text)

'''
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
    
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
'''

'''
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")

'''

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
