from .staff import Staff
from .student import Student


class School:
    """
    - name
    - staff[]
    - students[]
    """
    def __init__(self, name, students_file_path=None, staff_file_path=None):
        self.name = name
        self.students = Student.all_students(students_file_path)
        self.staff = Staff.all_staff(staff_file_path)