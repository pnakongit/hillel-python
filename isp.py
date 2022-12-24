class Salary:
    def get_salary(self):
        print('I  get Salary')


class Lectures:
    def listen_lectures(self):
        print('I listen to lectures')


class Study:
    def studying(self):
        print('I am studying')


class Teach:
    def teach_students(self):
        print('I teach students')


class Group(Lectures, Study):
    def __init__(self, students: list, name: str = None):
        self.name = name
        self.students = students


class Student(Lectures, Study):
    def __init__(self, name: str = None):
        self.name = name


class Teacher(Salary, Teach):
    def __init__(self, name: str = None):
        self.name = name
