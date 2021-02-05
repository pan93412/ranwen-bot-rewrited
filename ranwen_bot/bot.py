from ranwen_bot.bot_base import BotBase
from ranwen_bot.messages import help_message as i18n_help_message
from aiogram import types
import logging

class Bot(BotBase):
    def register_help_message(self) -> None:
        async def _help_message(message: types.Message):
            logging.debug(f"{message.from_user.id}'s language_code is: {message.from_user.language_code}")
            await message.reply(i18n_help_message(message.from_user.language_code))  # type: ignore
        logging.debug("Registered help_message handler.")
        self.dispatcher.register_message_handler(_help_message, commands=['start', 'help'])  # type: ignore
