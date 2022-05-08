#Write a program to convert temperatures from Fahrenheit to Celsius
#The mathematical formula for converting a temperature measured in Fahrenheit to a
#temperature measured in Celsius is shown in the following code:

#celsius = (fahrenheit - 32) * 5/9

#Solution
fahrenheit = input('What is the temperature in Fahrenheit?  ')

if fahrenheit.isnumeric() == False:
    print('Input is not a number.')
    exit()

fahrenheit = int(fahrenheit)

celsius = int((fahrenheit - 32) * 5/9)
print('Temperature in celsius is ' + str(celsius))