import telebot

token = '5686453165:AAGlca6xNrTg9BhOX6miug3475Y-o1LPq-Q'

bot  =  telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m):
	bot.send_message(m.chat.id, 'hello welcome to test bot!')

@bot.message_handler(commands=['help'])
def help(m):
	bot.send_message(m.chat.id, 'try again later')

@bot.message_handler(content_types=['start'])
def echo(m):
	bot.send_message(m.chat.id, m.text)

@bot.message_handler(content_types=['photo'])
def photo(m):
	bot.send_message(m.chat.id, 'nice photo')

bot.polling()
