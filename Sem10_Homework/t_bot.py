import telebot as tb
import calculator

bot_token = ""

def run_bot():
    bot = tb.TeleBot(bot_token, parse_mode=None)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Введите выражение для вычисления")

    @bot.message_handler(func=lambda m: True)
    def get_expr(message):
        expr = message.text
        if calculator.is_valid(expr):
            result = calculator.run_calc(expr)
            bot.reply_to(message, f'Результат = {result}')
        else:
            bot.reply_to(message, "Неверное выражение")
        bot.reply_to(message, "Введите выражение для вычисления")

    bot.polling()
