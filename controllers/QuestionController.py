from models.question import Question

class QuestionController:
    @staticmethod
    def add_question(title, test_id):
        question = Question.create(
            title=title, test_id=test_id
        )
        return question

    @staticmethod
    def get_questions_by_test_id(test_id):
        questions = list(
            Question.select()
                .where(Question.test_id == test_id)
                .execute()
        )
        return questions
