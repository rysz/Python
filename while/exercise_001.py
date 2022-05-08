#while loop
import random 

roll = 0
count = 0

while roll != 5:
  count = count + 1
  roll = random.randint(1, 5)
  print(roll)

print(f'It took {count} rolls to roll a 5!')
print()

#While loop with break() and else()
#Allow the player to exit the game prematurely by typing the letter q instead of a name.
#We use an if statement to check the value the user typed in. If they entered q, we call the break statement.
#The break statement instructs the Python interpreter to exit the loop and continue running the code after the while statement's code block.
#In this case, the else statement is skipped--there's no winner.
import random 

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  
  name = input('Enter a name, or \'q\' to quit:  ' )
  
  #strip() - strip out the empty spaces by using the string helper method
  #if the player entered nothing... continue
  if name.strip() == '':
      continue
  
  if name.strip() == 'q':
    break
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')

