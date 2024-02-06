
class User:
    def __init__(self, name, email, first_language):
        self.name = name
        self.email = email
        self.first_language = first_language

    def __str__(self) -> str:
        return f'My name is {self.name}, I speak {self.first_language}, you can reach me at {self.email}.'


user1 = User('John', 'John123@email.com', 'Sarcasm')
user2 = User('Jaxson', 'JaxAttack@email.com', 'Caninian')


print(user1)
print(user2)