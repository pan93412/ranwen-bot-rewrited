from __future__ import annotations
import logging
from aiogram import Bot, Dispatcher, executor

# todo: 更加抽象
class BotBase:
    bot: Bot
    dispatcher: Dispatcher

    def __init__(self, token: str):
        self.bot = Bot(token = token)
        self.dispatcher = Dispatcher(self.bot)

    def set_logging(self, level: int = logging.INFO) -> None:
        logging.basicConfig(level=level)

    def get_bot(self) -> Bot:
        return self.bot
    
    def get_dp(self) -> Dispatcher:
        return self.dispatcher
    
    def start_polling(self) -> None:
        '''
        Note: it is a blocking function and should be run the last.
        '''
        executor.start_polling(self.dispatcher, skip_updates=True)
