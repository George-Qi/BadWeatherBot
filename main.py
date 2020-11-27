from telegramBot import tg_bot_updater, tg_bot_dispatcher

tg_bot_updater.start_polling()
print("Telegram Bot Started ... ")
tg_bot_updater.idle()
