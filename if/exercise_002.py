print(type('Hello world'))
print(type(7))
print(type(True))
print(type(False))
print(type('True'))
print(type('False'))
print()

#The bool() function converted the strings 'True' and 'False' to the Boolean value True.
# When the function is supplied with an empty string, it returns False, while any other non-empty string returns True.
print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('Hello world!'))
print()

#The bool() function converts any non-zero value to True, but it converts the value 0 to False.
print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))
print()

#operators
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print()

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')