class University:
    def __init__(self, name: str = None):
        self.name = name
        self.profile = {}

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')


class Group(University):
    def __init__(self, students: list, name: str = None):
        super().__init__(name=name)
        self.students = students

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')


class Student(University):
    def __init__(self, name: str = None):
        super().__init__(name=name)

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')


class Teacher(University):
    def __init__(self, name: str = None):
        super().__init__(name=name)

    def add_profile(self, **kwargs):
        self.profile = {}
        for elem in kwargs:
            if elem not in self.profile:
                self.profile[elem] = kwargs[elem]
            else:
                print(f'key {elem} is already in the profile')
