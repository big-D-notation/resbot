from models.option import Option

class OptionController:
    @staticmethod
    def add_option(question_id, text, is_right):
        option = Option.create(
            question_id=question_id, 
            text=text, 
            is_right=is_right
        )
        return option

    @staticmethod
    def get_right_option_by_question_id(question_id):
        return list(Option.select().where(Option.question_id == question_id & Option.is_right).execute())[0]

    @staticmethod
    def get_options_by_question_id(question_id):
        options = list(
            Option.select()
                .where(Option.question_id == question_id)
                .execute()
        )
        return options
