from models.student import Student

class StudentController:
    @staticmethod
    def create_student(name, group, tg_nick):
        student = Student.create(
            name=name,
            group=group,
            tg_nick=tg_nick
        )
        return student
    
    @staticmethod
    def get_all_students():
        return list(Student.select().execute())
    