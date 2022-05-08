#Generate a random number between 1 and 5 and allow the user to guess.
#Keep prompting the user for their guess until they guess correctly. Then, display the number of guesses.

import random

value = random.randint(1, 5)
count = 0
guess = 0
while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} tries!')