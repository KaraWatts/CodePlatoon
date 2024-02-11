class Person:

    def __init__(self, name, age, role):
        self.name = name
        self.age = int(age)
        self.role = role

        def __repr__(self):
            return


alice = Person('Alice', '5', 'student')
bob = Person("Bob", 6, 'student')