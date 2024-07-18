from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from tgbot.bot import bot
from tgbot.handlers.common import register_handlers_common
from tgbot.handlers.notes import register_handlers_notes


dp = Dispatcher(bot, storage=MemoryStorage())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await set_commands(bot)
    register_handlers_common(dp)
    register_handlers_notes(dp)
    await dp.skip_updates()
    await dp.start_polling()
