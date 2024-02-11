class Person:
    """
    Person class. Parent class for Students, Staff
        - name
        - age, int
        - role
    """
    def __init__(self, name, age, role):
        self._name = name.lower()
        self.age = int(age) #TODO: Handle casting error if age invalid
        self.role = role

    @property
    def name(self):
        return self._name.capitalize()
    

    def __repr__(self):
        return f"Name: {self.name} | Age: {self.age} | Role: {self.role}"

# Informal test
# alice = Person("Alice", "5", "student")
# bob = Person("Bob", 6, "student")

# print(alice)
# print(bob)
# print([alice, bob])