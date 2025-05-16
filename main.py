from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from flask import Flask
import threading
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8000)

@dp.message(command=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот знакомств.")

async def start_bot():
    await dp.start_polling(bot)

if name == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(start_bot())
