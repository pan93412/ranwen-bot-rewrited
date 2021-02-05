import logging
from ranwen_bot import Bot
import os

bot = Bot(os.environ["TOKEN"])
bot.set_logging(logging.INFO)
bot.register_help_message()
bot.start_polling()