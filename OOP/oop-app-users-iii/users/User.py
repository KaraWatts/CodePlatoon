# Your User class goes hereclass 

class User:
    def __init__(self, name, email, first_language):
        self.name = name
        self.email = email
        self.first_language = first_language
       

    def __str__(self) -> str:
        return f'My name is {self.name}, I speak {self.first_language}, you can reach me at {self.email}.'
    
    def add_post(self, text):
        print(f"{text}")
        


    
