import random

low = 1
high = 100
guesses = 0
max_guesses = 5
number = random.randint(low, high)

while guesses < 5:
    guess = int(input(f"\nPick a # from {low} - {high}: "))

    if guess < low or guess > high:
        print(f"{guess} is out of bounds.")
    elif guess == number:
        print(f"Well done! {number} was the right answer.")
        break
    elif guess > number:
        print(f"Pick a smaller # than: {guess}")
    elif guess < number:
        print(f"Pick bigger # than: {guess}")
    
    guesses += 1

if guesses == 5:
    print(f"\nGame Over! The answer was {number}")