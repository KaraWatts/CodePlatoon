class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = False

    def guess(self, user_guess):
        if user_guess > self.answer:
            return 'High'
        elif user_guess < self.answer:
            return 'Low'
        self.last_guess = True
        return 'Correct'
        
    def solved(self):
        return self.last_guess
        


game = GuessingGame(10)

print(game.solved())   # => False

print(game.guess(5))  # => 'low'
print(game.guess(20)) # => 'high'
print(game.solved())   # => False

print(game.guess(10)) # => 'correct'
print(game.solved())   # => True

