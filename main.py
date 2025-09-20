import telebot
import random

bot = telebot.TeleBot(secret)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("heh", "Пишет слово he указанное количество раз"),
        telebot.types.BotCommand("flip", "Подбрасывает монетку"),
        telebot.types.BotCommand("start", "Приветствие"),
        telebot.types.BotCommand("hello", "Приветствие"),
    ],
)

cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])
    

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['flip'])
def flip(message):
    a = random.randint(0, 1)
    if a == 0:
        bot.reply_to(message, "Выпала решка")
    else:
        bot.reply_to(message, "Выпал орел")
    

bot.polling()
