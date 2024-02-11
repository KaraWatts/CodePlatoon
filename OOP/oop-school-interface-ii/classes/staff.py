from .person import Person
import csv

"""
Staff class
    - name
    - age, int
    - role
    - employee_id, int
    - password
- Create staff from csv data
"""
class Staff(Person):
    all_staff_lst = []
    STAFF_ROLES = ['principal', 'janitor', 'teacher']

    @classmethod
    def is_valid_role(cls, role):
        if role.lower() in cls.STAFF_ROLES:
            return True
        return False

    @classmethod
    def all_staff(cls, path_to_file):
        with open(path_to_file, mode='r', newline='') as csvfile:
            # Turn each row of the csv file into a dictionary
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Destructure dictionary into vars we can pass as named arguments
                # to the Student class constructor
                a_staff = Staff(**row)
                cls.all_staff_lst.append(a_staff)

        return cls.all_staff_lst

    def __init__(self, name=None, age=None, role=None, employee_id=None, password=None):
        super().__init__(name, age, role)
        self.employee_id = int(employee_id)
        self.password = password

    def __repr__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role} | Employee ID: {self.employee_id} | Password: {self.password}"

        # Maybe too fancy, but this does work
        # return f"{super().__repr__()} | Schoold ID: {self.school_id} | Password: {self.password}"
