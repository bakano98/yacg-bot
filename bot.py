import os
import telebot
from API_TOKEN import TOKEN
from telegram import ParseMode
from spreadsheet import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["greet"])
def greet(msg):
    bot.send_message(msg.chat.id, "hello back to u")


@bot.message_handler(commands=["listRemaining"])
def listRemaining(msg):
    bot.send_message(msg.chat.id, getThisMonthItemsFormatted(),
                     parse_mode=ParseMode.HTML)


@bot.message_handler(commands=["list"])
def list(msg):
    toSend = "Events for this week:\n" + getThisWeekItemsFormatted()
    bot.send_message(msg.chat.id, toSend, parse_mode=ParseMode.HTML)


@bot.message_handler(commands=["upcoming"])
def upcoming(msg):
    bot.send_message(msg.chat.id, getUpcoming(), parse_mode=ParseMode.HTML)

bot.polling()
