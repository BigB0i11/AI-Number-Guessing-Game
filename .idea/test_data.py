import json
import random
from AI_NumberGame import BinarySearchAi, AI_Logic

all_prev_guesses = []

# Simulate 100 games
for i in range(100):
    target = random.randint(0, 20)
    COM = BinarySearchAi(0, 20)
    attempts = 0
    prev_guess = []

    while True:
        guess = COM.guess(attempts, prev_guess)
        if guess < target:
            feedback = 'higher'
        elif guess > target:
            feedback = 'lower'
        else:
            feedback = 'correct'
            prev_guess.append(guess)
            break

        COM.update_range(feedback, guess)
        attempts += 1
        prev_guess.append(guess)

    all_prev_guesses.extend(prev_guess)  # Add all guesses from this run

# Save all simulated guesses
with open('prev guess', 'w') as f:
    json.dump(all_prev_guesses, f)

# Optional: update frequency analysis
AI_Logic()

print("Simulation Done, Last Run Attempts:", attempts)
