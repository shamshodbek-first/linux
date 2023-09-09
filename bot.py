import logging
from aiogram import *
from aiogram.types import *

API_TOKEN = '6518533177:AAEo7mWZmm3aH7l8rPZ7plQr4ZKjvFuhH7g'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button3 = KeyboardButton("📞 Telfon raqamimni ulashmoq",request_contact=True)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True ).add(button3)
button1 = KeyboardButton('✅ Ovoz bermoq')
button2 = KeyboardButton("💳 Hisobim")
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True ).add(button1).add(button2)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Open budget botimizga Xush kelibsiz. Bu bot open budjet sayti uchun maxsus!  😳 Har bitta ovozga 5000 so`m 😳  Admin: Shamshodbek Hamdamqulov! Ovoz berish uchun ,avval Telfon raqamizni qoldirib, Shuni Bosing➡️💵/info💵⬅️",reply_markup=keyboard1)

@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await message.reply("Tanlang",reply_markup=keyboard2)
    @dp.message_handler()



    @dp.message_handler()
    async def kb_answer (message: types.Message):

        if message.text == '✅ Ovoz bermoq':
            await message.answer("https://openbudget.uz/boards/initiatives/initiative/31/35b8ddf5-8e49-4042-ade7-adc853ebe087, 🙋‍Shu saytga kirib Ovoz bering! Ovoz bergandan so'ng berganligingizni tasdiqlash uchun screenshot oling va  adminga tashlang, admin tekshirib ko`radi va sizning hisobingizga 5000 so'm otkazadi!  ")
        elif message.text == "💳 Hisobim":
            await message.answer("Sizning hisobingizdagi mablag` 0 so'm ")
        else:
            await message.answer("🤔 Siz to'g'ridan to'g'ri savol yubordiz! Bolimni Tanlang!/info ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
