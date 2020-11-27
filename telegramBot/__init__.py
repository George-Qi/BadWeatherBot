from telegram.ext import Updater, CommandHandler
from telegramBot.cmdHandler import start, newNotify, myNotify, delNotify, setTimezone, help
# from ..loadConfig import tg_bot_token

tg_bot_updater = Updater('1428782186:AAHCEdp6nz1NvUOTiK9oj5WhhoxLUMF2Qmg')
tg_bot_dispatcher = tg_bot_updater.dispatcher


tg_bot_dispatcher.add_handler(CommandHandler('start', start))
tg_bot_dispatcher.add_handler(CommandHandler('newNotify', newNotify))
tg_bot_dispatcher.add_handler(CommandHandler('myNotify', myNotify))
tg_bot_dispatcher.add_handler(CommandHandler('delNotify', delNotify))
tg_bot_dispatcher.add_handler(CommandHandler('setTimezone', setTimezone))
tg_bot_dispatcher.add_handler(CommandHandler('help', help))


