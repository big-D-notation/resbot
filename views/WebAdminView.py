from flask import redirect, render_template, url_for

class WebAdminView:
    @staticmethod
    def show_students(students):
        return render_template('students.jinja', students=students)

    @staticmethod
    def show_tests(tests):
        return render_template('tests.jinja', tests=tests)

    @staticmethod
    def show_add_test():
        return render_template('add_test.jinja')

    @staticmethod
    def show_add_student():
        return render_template('add_student.jinja')
    
    @staticmethod
    def show_results(students, results):
        return render_template('results.jinja', students=students, results=results)

    @staticmethod
    def redirect_to_students():
        return redirect(url_for('students'))

    @staticmethod
    def redirect_to_tests():
        return redirect(url_for('tests'))

    @staticmethod
    def redirect_to_add_student():
        return redirect(url_for('add_student'))

    @staticmethod
    def redirect_to_add_test():
        return redirect(url_for('add_test'))
