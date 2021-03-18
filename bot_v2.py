import logging
import asyncio
import random
from aiogram import Bot, Dispatcher, executor, types
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
    /film - выведет случайный фильм и его рейтинг
        '''
    )


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer(f"Здарова {message.chat.first_name}, копать ты раскабанел")
    await cmd_help(message)


@dp.message_handler(commands=['film'])
async def cmd_all_film(message):
    await message.answer(random.choice(all_film))


@dp.message_handler(content_types=types.ContentType.TEXT)
async def send_text(message):
    text = message.text
    if message.text.lower() == 'привет':
        await message.answer(text='Привет, создатель')
    elif message.text.lower() == 'пока':
        await message.answer(text='Прощай, создатель')


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
