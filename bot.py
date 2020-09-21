import telebot
import time
import nasScrape

with open('config.txt') as f:
    bot_token = f.readline()
    groupId = f.readline()

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'To use, include a $ in front of the ticker name')

@bot.message_handler(func=lambda msg: msg.text is not None and '$' in msg.text)
def findStock(message):
    texts = message.text.split()
    tickerList = nasScrape.findTicker(texts)
    for i in tickerList:
        try:
            stockInfo = nasScrape.findPrice(i)
            bot.send_message(groupId,stockInfo)
        except:
            pass
bot.polling()

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)