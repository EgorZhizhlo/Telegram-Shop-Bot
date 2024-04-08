from aiogram import Bot, Dispatcher, types
from LavaBusiness import AioLava

market1_TOKEN = ""
market_TOKEN = ""

SECRET_KEY = ""
PROJECT_ID = ""
lava = AioLava(SECRET_KEY, PROJECT_ID)

market_bot = Bot(token=market_TOKEN, parse_mode=types.ParseMode.HTML)
market_dp = Dispatcher(market_bot)
