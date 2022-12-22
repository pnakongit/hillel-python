class Notification:
    def __init__(self, name):
        self.name = name
        self._format = 'Dear \033[95m {}\033[0m inform you about \033[94m{}\033[0m'

    def print_notification(self, message: str):
        print(self._format.format(self.name, message))


class StudentNotification(Notification):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self._format = 'Dear \033[92m {}\033[0m inform you about \033[93m{}\033[0m'


class TeacherNotification(Notification):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self._format = 'Dear \033[91m {}\033[0m inform you about \033[94m{}\033[0m'


class GroupNotification(Notification):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self._format = 'Dear \033[96m {}\033[0m inform you about \033[92m{}\033[0m'


# test
student = StudentNotification('Test_student')
teacher = TeacherNotification('Test_teacher')
group = GroupNotification('Test_group')


student.print_notification('test_message for student')
teacher.print_notification('test_message for teacher')
group.print_notification('test_message for group')
