from models.result import Result

class ResultController:
    @staticmethod
    def add_result(stud_tg, test_id, points):
        return Result.create(stud_tg=stud_tg, test_id=test_id, points=float(points))
    
    def get_all_results_by_stud_tg(stud_tg):
        return list(Result.select().where(Result.stud_tg==stud_tg).execute())
    