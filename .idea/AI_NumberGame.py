import random
import json
from random import randrange
DEBUG_MODE = False
def AI_Logic():
    raw = dict()
    for number in prev_guess:
        raw[number] = raw.get((number), 0) + 1
    logic = list()
    for key, val in list(raw.items()):
        logic.append((key, val))
    logic.sort()
    AI_Count = max(logic, key=lambda x: x[1]) if logic else None
    if AI_Count is None:
        return None
    AI_guess = AI_Count[0]
    return AI_guess

class BinarySearchAi:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def guess(self, attempts, prev_guess):
        if attempts == 0:
            if prev_guess:
                AI_ans = AI_Logic()

            else:
                AI_ans = randrange(self.low, self.high)
        else:
            AI_ans = (self.low + self.high) // 2
        return AI_ans

    def update_range(self, feedback, guess):
        if feedback == 'higher':
            self.low = guess + 1
        elif feedback == 'lower':
            self.high = guess - 1


COM = BinarySearchAi(0, 20)
attempts = 0
prev_guess = list()
valid_answers = ['higher', 'lower', 'correct']
while True:
    guess = COM.guess(attempts, prev_guess)
    if DEBUG_MODE == True:
        target = random.randint(0, 20)
        if guess < target:
            feedback = 'higher'
        elif guess > target:
            feedback = 'lower'
        else:
            feedback = 'correct'
            break
    else: #checking to see something
        print(guess)
        feedback = input("Is the number higher, lower or correct:").strip().lower()
        if feedback not in valid_answers:
            print("Invalid Answer")
            continue
        COM.update_range(feedback, guess)
        attempts += 1
        if feedback == 'correct':
            print("Number of Guesses needed:", attempts)
            prev_guess.append(guess)
            break



