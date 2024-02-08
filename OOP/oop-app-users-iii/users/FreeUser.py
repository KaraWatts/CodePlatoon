from users.User import User
class FreeUser(User):
    

    def __init__(self, name, email, first_language):
        super().__init__(name, email, first_language)
        self.number_of_posts = 0

    

    def add_post(self, text):
        if self.number_of_posts < 2:
            print(f"{text}")
            self.number_of_posts += 1
        else:
            print(f"{self.name} upgrade your account for more posts")