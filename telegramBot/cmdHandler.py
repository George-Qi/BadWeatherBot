def start(bot, update):
    """ Echo Start Message. """
    bot.message.reply_text('Hello tg Bot.')

def newNotify(bot, update):
    """ Create New Bad Weather Notify. """
    bot.message.reply_text('New Notify Established.')

def myNotify(bot, update):
    """ Show my Notify. """
    bot.message.reply_text('This is your Notify List.')

def delNotify(bot, update):
    """ del a Notify """
    bot.message.reply_text('Your Notify Deleted.')

def setTimezone(bot, update):
    """ Set User's timezone. """
    bot.message.reply_text('Your timezone Changed.')

def help(bot, update):
    """ show help """
    bot.message.reply_text('This is some help.')