from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

class TelegramBotView:
    @staticmethod
    def show_start(bot, message):
        answer = 'Вітаю вас у Resbot! Що здаємо сьогодні?'
        bot.send_message(message.chat.id, answer)

    @staticmethod
    def show_tests(bot, message, test_names):
        keyboard = InlineKeyboardMarkup()

        for name in test_names:
            button = InlineKeyboardButton(name, callback_data=('test_' + name))
            keyboard.add(button)

        answer = 'Вам доступні наступні тести, оберіть потрібний'

        bot.send_message(message.chat.id, answer, reply_markup=keyboard)

    @staticmethod
    def show_question(bot, message, question_title, options):
        keyboard = InlineKeyboardMarkup()
        
        for option in options:
            button = InlineKeyboardButton(option.text, callback_data=('option_' + option.text))
            keyboard.add(button)

        answer = question_title

        bot.send_message(message.chat.id, answer, reply_markup=keyboard)
        
    @staticmethod
    def show_test_ending(bot, message):
        answer = 'Дякуємо за проходження тесту! Дізнатися результат - /results'
        bot.send_message(message.chat.id, answer)

    @staticmethod
    def show_results(bot, message, results):
        answer = ''

        if results:
            answer = '**Ваші результати:** \n\n'
            for result in results:
                answer += f'{result["test_name"]} - {result["points"]}/{result["max_points"]}\n'
        else:
            answer = 'Жодного тесту ще не пройдено'

        bot.send_message(message.chat.id, answer)
