#Generate a random number between 1 and 10 and allow the user to guess.

#Display the current guess number.
#If the guess is too low, tell the user "Your guess is too low, try again!"
#If the guess is too high, tell the user "Your guess is too high, try again!"
#If the user enters a nonnumeric value, tell the user "Numbers only, please!"

import random

value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')