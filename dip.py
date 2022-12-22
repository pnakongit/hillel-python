import json


class TXTWriter:
    def write(self, file_name: str, data: dict):
        with open(file_name + ".txt", 'w') as txt_file:
            txt_file.write(str(data))


class JSONWriter:
    def write(self, file_name, data):
        with open(file_name + ".json", "w") as json_file:
            json_file.write(json.dumps(data))


class Group:
    def __init__(self, name, students: list):
        self.name = name
        self.students = students
        self.profile = {}

    def save_profile(self, writer):
        writer().write(self.name, self.profile)

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')


class Student:
    def __init__(self, name):
        self.name = name
        self.profile = {}

    def save_profile(self, writer):
        writer().write(self.name, self.profile)

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')


class Teacher:
    def __init__(self, name):
        self.name = name
        self.profile = {}

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')

    def save_profile(self, writer):
        writer().write(self.name, self.profile)


# Test

test_student = Student('Jon')
test_student.add_profile(group='8b', faculty='Finance')

test_student.save_profile(TXTWriter)
test_student.save_profile(JSONWriter)

