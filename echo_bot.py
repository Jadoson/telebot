import telebot

BOT_TOKEN=""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.reply_to(message, "Test")
	
bot.infinity_polling()