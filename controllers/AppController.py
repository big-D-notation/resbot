import threading

from controllers.WebAdminController    import WebAdminController
from controllers.TelegramBotController import TelegramBotController

from models.option   import Option
from models.question import Question 
from models.result   import Result
from models.student  import Student
from models.test     import Test

from utils.database import Database


class AppController:
    def __init__(self):
        self.db = Database().get_connection()

    def run_app(self):
        try:
            self.db.create_tables(
                [Student, Test, Question, Option, Result]
            )

            web_controller = WebAdminController()

            app = web_controller.get_app()
            bot = TelegramBotController.get_bot()

            app.add_url_rule('/admin/add_test',    view_func=web_controller.add_test,    methods=['GET','POST'])
            app.add_url_rule('/admin/add_student', view_func=web_controller.add_student, methods=['GET','POST'])
            app.add_url_rule('/admin/tests',       view_func=web_controller.tests,       methods=['GET'])
            app.add_url_rule('/admin/students',    view_func=web_controller.students,    methods=['GET'])
            app.add_url_rule('/admin/results',     view_func=web_controller.results,     methods=['GET'])
            app.add_url_rule('/',                  view_func=web_controller.index,       methods=['GET'])

            
            bot_thread = threading.Thread(target=bot.polling)
            bot_thread.start()

            app.run(port=7000)
            
        finally:
            bot_thread.join()
        

        