first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
#%: Modulus operator, which gives you the remainder (if any) after you divide one value into another. It's useful to know whether one value is evenly divisible by the other.
modulus = first_value % second_value
#**: Exponent operator. For example, "5 to the fourth power" is expressed as 5 * 5 * 5 * 5.
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))
print()

#Round
pi = 3.14
print(type(pi))
print(int(pi))
print(round(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
print(round(uptime))
print()

#Round to specifc decimal place
first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)
print()
