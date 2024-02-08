from users.PremiumUser import PremiumUser
from users.FreeUser import FreeUser
# Import and create your users here

mr_crabs = PremiumUser('Mr. Crabs', 'mr_crabs@bikinibottom.com', '$money$')
print(mr_crabs)
patrick = FreeUser('Patrick Star', 'email@email.com', 'Bubbles')
print(patrick)

mr_crabs.add_post('MR SQUIDWARD!!!')

patrick.add_post("ummmmmmmmm internet")
patrick.add_post("bubbles")
patrick.add_post("is this thing on?")
