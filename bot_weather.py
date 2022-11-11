from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from config import tele_api_token
from wether_api import query_weather


# initializing bot and dispatcher
bot = Bot(token=tele_api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    usernames = message.from_user.full_name
    await message.answer(f"Hi {usernames} !\n\nWelcome to LeeReub\U0001F916, a Weather Bot Made by @Sc_ul\n\n"
                         f"<b>What This Bot Can Do?</b>\n\n"
                         f"This Bot gives you the weather details from any city you have requested at a time. "
                         f"It doesn't matter where ever your are and the the city you are requesting details from, "
                         f"it includes at least    vital detail.\n\n"
                         f"<b>How To Use This Bot?</b>\n\n "
                         f"Type in a  <b>\"weather\"</b>  command and a valid city name eg"
                         f" <b>\"/weather Zomba\", \"/weather Southampton\"</b>. ", parse_mode="HTML")


@dp.message_handler(commands=['weather'])
async def the_message(message: types.Message, command: Command.CommandObj):
    if command.args:
        await message.answer(query_weather(command.args), parse_mode='HTML')
    else:
        await message.reply('\U00002139 <b>Please include city name in your command</b>', parse_mode='HTML')


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f'Include command  <b>" /weather {message.html_text} "</b>  to request weather details!. '
                         f'Not just only <b>"{message.html_text}"</b>',
                         parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp)
