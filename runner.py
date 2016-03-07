__author__ = 'rizkivmaster'

import telepot
import time

import telegram_controller
bot = telepot.Bot('192652578:AAFe4CnDrrnAQ2JQ4MBeksASE9fKQGoaqCg')
telegram_controller.set_bot(bot)
bot.notifyOnMessage(telegram_controller.handle)
print 'Listening...'

while(True):
    time.sleep(2)