import random

easy_words = ["apple", "tiger", "race"]
medium_words = ["python", "password", "useful"]
hard_words = ["rascal", "honour", "guessit"]

print("**** Password Guessing Game **** ")
print("Choose a difficulty level:")
print("Easy | Medium | Hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to Easy level.")
    secret = random.choice(easy_words)

attempts = 0

print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"\n Congratulations! You guessed the password in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)

print("Game Over!")