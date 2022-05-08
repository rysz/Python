medicine = 'Coughussin'
dosage = 5
duration = 4.5

#The replacement fields have no values inside them. By using the member access operator, we call the format() function.
#We pass in the values we want to substitute in each replacement field, in the order in which they appear.
instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

#We fill the replacement fields with a zero-based numeric value, which accesses the argument passed into the format() function.
#We intentionally mixed up the order to show that you can use the arguments in any position of your format string.
#You do this by changing the ordinal position in the replacement field.
instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

#We fill the replacement fields with variable names.
# Those same variable names are passed as named arguments into the format() function.
instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)
print()

#The format() function is powerful and flexible. You can do the same thing with less typing using formatted string literals, also known as f-strings.
name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10
value = 3.14

#The format string takes care of the data type conversion for us, so we don't need to call str() around those values.
message = f'Count to {count}.  Multiply by {value}.'
print(message)
print()

#You can perform just about any expression inside a replacement field.
width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')
print()

#Format specifier syntax
#A format specifier uses a colon symbol (:) after the variable name, to specify how that value should be formatted.
value = 'hi'


#We use the less-than symbol (<) to align the text to the left of a string that is 25 total characters wide.
#The string hi occupies two of the 25 total characters.
#We add period symbols (.) on the left and right of the replacement field, to help us see the total width of the string.
print(f'.{value:<25}.')

#We use the greater-than symbol (>) to align the text to the right of a string that is 25 total characters wide.
print(f'.{value:>25}.')

#We use the caret symbol (^) to center the text in the middle of a string that is 25 total characters wide.
print(f'.{value:^25}.')

#We use the caret symbol (^) again. But this time, we preface it with a single dash symbol (-) to use instead of an empty space to fill the remaining width of the string.
print(f'.{value:-^25}.')


