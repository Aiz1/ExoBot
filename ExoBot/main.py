import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types.message import Message
from myway import bot_token
loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)
if __name__ == '__main__':
    from fail import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
@dp.message_handler()
async def povtoryalka(message: Message):
    text = message.text
    await message.answer(text=text)