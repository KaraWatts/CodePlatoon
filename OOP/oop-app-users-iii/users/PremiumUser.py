# Your PremiumUser class goes here
from users.User import User
class PremiumUser(User):

    def __init__(self, name, email, first_language):
        super().__init__(name, email, first_language)
        