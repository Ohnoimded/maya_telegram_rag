import telebot
from components.configs import Config
from components.llms import Brain


API_TOKEN = Config.TELEGRAM_API_TOKEN
bot = telebot.TeleBot(API_TOKEN)
brain =Brain()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am Maya! Type /help for commands.")


@bot.message_handler(commands=['clear'])
def history_clear(message):
    bot.reply_to(message, "Cleared history")
    raise NotImplemented


@bot.message_handler(commands=['suggest'])
def suggest(message):
    response = brain.process_query('Give me a property with Parking, 2 BHK 1200 sqft')

    if response:
        chatbot_response = response
        bot.reply_to(message, chatbot_response)
    else:
        bot.reply_to(message, "Failed to process the response from the LLM.")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "List of available commands:\n" \
                "/start - Start the bot\n" \
                "/help - Show this help message\n\n" \
                "Just send a message to have a conversation."
    bot.reply_to(message, help_text)


@bot.message_handler()
def process_message(message):
    user_input = message.text
    response = brain.process_query(query=user_input)

    if response:
        chatbot_response = response
        bot.reply_to(message, chatbot_response)
    else:
        bot.reply_to(message, "Failed to process the response from the LLM.")

def main():
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

if __name__ == "__main__":
    main()