import csv


class Student:
    students = []

    def __init__(self, id, first_name, last_name, age, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id} | FN: {self.first_name} | LN: {self.last_name} | AGE: {self.age} | {self.grade}"

    @classmethod
    def read_student_csv(cls):
        with open("./data.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls.students.append(cls(**row))
        return cls.students

    @classmethod
    def create_a_student(cls):
        first_name = input("What is your first name:\n")
        last_name = input("What is your last name:\n")
        age = input("What is your age? \n")
        grade = input("What is your grade?\n")
        student_dict = {
            "id": str(len(cls.students) + 1),
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "grade": grade,
        }
        cls.students.append(cls(**student_dict))

    @classmethod
    def delete_a_student(cls):
        stud_id = input("What is the student id you are looking for?\n")
        for stud in cls.students:
            if stud.id == stud_id:
                cls.students.remove(stud)
                print("Student DELETED")
                return None
        print("Student was not found")

    @classmethod
    def save_data(cls):
        with open("./data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "first_name", "last_name", "age", "grade"])
            for stud in cls.students:
                writer.writerow(
                    [stud.id, stud.first_name, stud.last_name, stud.age, stud.grade]
                )


Student.read_student_csv()
while True:
    choice = input(
        """
1. View all Students
2. Add a student
3. Delete a student
4. exit
"""
    )
    if choice == "1":
        for student in Student.students:
            print(student)
    elif choice == "2":
        Student.create_a_student()
    elif choice == "3":
        Student.delete_a_student()
    else:
        Student.save_data()
        break
