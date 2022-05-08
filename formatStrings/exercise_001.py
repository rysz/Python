first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string)
print()

#In this case, third_string points to a literal string that embeds a double quote inside a string defined with single quotes.
#Conversely, fourth_string points to a literal string that embeds a single quote inside a string defined with double quotes.
third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)
print()

#But what if you need to embed a single quote in a literal string, and you want to define the string by using single quotes?
#Or, conversely, use a double quote inside a literal string defined with double quotes? In this case, you can use the \ character to create an escape sequence.
fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)
print()

#But what if you need to display the contents of an escape sequence without performing the escape sequence's command?
#In other words, what if you need to literally display the value \n?
#In that case, you prefix a literal string with the r character to produce a raw output, without any escaping.
#This is helpful if you need to ignore escape sequences, and display the entire string as it appears in code.
ninth_string = r"A literal string with a \n new line character printed raw"

print(ninth_string)
print()

#If you need to display a string across multiple lines, you can use the new line escape sequence we just learned about.
#Alternatively, you can create a multi-line string by defining the string with a set of three single quotes, or a set of three double quotes.
tenth_string = '''A literal string
on more than one line
sometimes known as a verbatim string'''

eleventh_string = """Another literal string
     on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)
print()

first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')