#
message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())
print()

#
message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())
print()

#
location = 'Mississippi'
print(location.count('s'))
print()

#
print(len('how many characters in this string?'))
print()

#Call the startswith() and endswith() functions to inspect the contents of a string to find out if it matches what you expected it to start with or end with, respectively.
message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))
print()

#The find() method locates the zero-based position of one string inside another string.
#In other words, starting with the number 0, the method tells you where the search string is located.
#If it can't find the string, it returns -1.
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))
print()

#Python provides the lstrip() to remove empty space characters from the left side of a string, and the rstrip() function
#to remove them from the right side of a string. Or, you can use the strip() function to remove both.
message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')
print()

#The replace() function swaps every instance of a string with a different string.
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
print()

#The rjust() and ljust() methods add empty space characters to a string to provide justification to the right or left, respectively.
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))
