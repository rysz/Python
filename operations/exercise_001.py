print(type('7'))
print(type(7))
print(type(7.1))
print()

#The isinstance() function tells you whether the value is what you expected. It returns the value True if your expectation is correct and False if it's incorrect.
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))
print()

x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False 
print(type(x))
print()