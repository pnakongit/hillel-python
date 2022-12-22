students_evaluations_data = {'Ivan Mazepa': [90, 95, 93, 98, 100, 86, 97],
                             'Pavlo Nakon': [92, 93, 95, 100, 100, 99, 97],
                             'Petro Kovalenko': [91, 100, 95, 100, 100, 99, 97]}


# before srp
class RankCalculator:
    def __init__(self):
        self.students_rank = {}

    def calculate_rank(self, students_evaluations):
        for elem in students_evaluations:
            self.students_rank[elem] = int(sum(students_evaluations[elem]) / len(students_evaluations[elem]))

    def get_top_student(self):
        return max(self.students_rank)


# after srp
class RankCalculator:
    def __init__(self):
        self.students_rank = {}

    def calculate_rank(self, students_evaluations):
        for elem in students_evaluations:
            self.students_rank[elem] = int(sum(students_evaluations[elem]) / len(students_evaluations[elem]))


class TopStudent:
    def get_top_student(self, rank_data: RankCalculator):
        return max(rank_data.students_rank)


# Test
rank_date = RankCalculator()
rank_date.calculate_rank(students_evaluations_data)
print(TopStudent().get_top_student(rank_date))


class Group:
    def __init__(self, name, students: list):
        self.name = name
        self.students = students


class Student:
    def __init__(self, name, ):
        self.name = name


class Teacher:
    def __init__(self, name, ):
        self.name = name
