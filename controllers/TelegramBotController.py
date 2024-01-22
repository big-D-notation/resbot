import telebot

from controllers.TestController     import TestController
from controllers.QuestionController import QuestionController
from controllers.OptionController   import OptionController
from controllers.ResultController   import ResultController

from views.TelegramBotView import TelegramBotView

from resources.config import bot_token

bot = telebot.TeleBot(bot_token);

testResult = {}


class TelegramBotController:
    @staticmethod
    def get_bot():
        return bot

    @staticmethod
    @bot.message_handler(func=lambda message: message.text == '/start')
    def handle_start(message):
        TelegramBotView.show_start(bot, message)

    @staticmethod
    @bot.message_handler(func=lambda message: message.text == '/tests')
    def handle_tests(message):
        tests = TestController.get_all_tests()
        test_names = []

        for test in tests:
            test_names.append(
                test.title
            )

        TelegramBotView.show_tests(bot, message, test_names)

    @staticmethod
    @bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
    def test_button_click(call):
        global testResult

        test = TestController.get_test_by_test_title(call.data[5:])
        testResult['current_test'] = test.title
        
        testResult['answers'] = []

        testResult['questions'] = QuestionController.get_questions_by_test_id(test.id)

        question = testResult['questions'][0]

        options = OptionController.get_options_by_question_id(question.id)
        TelegramBotView.show_question(bot, call.message, question.title, options)


    @staticmethod
    @bot.callback_query_handler(func=lambda call: call.data.startswith('option_'))
    def option_button_click(call):
        global testResult

        test = TestController.get_test_by_test_title(testResult['current_test'])
        testResult['answers'].append(call.data[7:])

        if len(testResult['answers']) == len(testResult['questions']):
            points = TelegramBotController.find_result_points()            
            ResultController.add_result(
                stud_tg=call.from_user.username,
                test_id=test.id,
                points=points
            )  

            testResult = {}
            TelegramBotView.show_test_ending(bot, call.message)
            return

        currentQuestionIndex = len(testResult['answers'])

        question = testResult['questions'][currentQuestionIndex]

        options = OptionController.get_options_by_question_id(question.id)
        TelegramBotView.show_question(bot, call.message, question.title, options)


    @staticmethod
    def find_result_points():
        global testResult

        test = TestController.get_test_by_test_title(testResult['current_test'])
        right_answers_amount = 0

        questions = QuestionController.get_questions_by_test_id(test.id)

        for i in range(len(questions)):
            option = OptionController.get_right_option_by_question_id(questions[i].id)
            if option and option.text == testResult['answers'][i]:
                right_answers_amount += 1


        final_mark = (test.max_points / len(questions)) * right_answers_amount
        
        return final_mark
    
    @bot.message_handler(func=lambda message: message.text == '/results')
    def handle_results(message):
        results = ResultController.get_all_results_by_stud_tg(message.from_user.username)
        resultsToRender = []

        for result in results:
            resultToRender = {}
            test = TestController.get_test_by_test_id(result.test_id)

            resultToRender['test_name'] = test.title
            resultToRender['points'] = result.points
            resultToRender['max_points'] = test.max_points

            resultsToRender.append(resultToRender)
    
        TelegramBotView.show_results(bot, message, resultsToRender)
