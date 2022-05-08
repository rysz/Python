#tuples
#create tuple with round brackets
my_tuple = (1, 2, 3)
print(my_tuple)

#tuples cannot be amended (imutable)
my_tuple_amended = my_tuple + (4, 5, 6)
print(my_tuple_amended)

#tuples can contain tuples 
my_tuple_nested = (1, 2, ("rock", "pop"), (3,4), ("disco", 5, 6), ("funk", (7, 8, 9)))

print(my_tuple_nested[0])
print(my_tuple_nested[1])
print(my_tuple_nested[2])
print(my_tuple_nested[2][0])
print(my_tuple_nested[2][1])
print(my_tuple_nested[3])
print(my_tuple_nested[3][0])
print(my_tuple_nested[3][1])
print(my_tuple_nested[4])
print(my_tuple_nested[4][0])
print(my_tuple_nested[4][1])
print(my_tuple_nested[4][2])
print(my_tuple_nested[5])
print(my_tuple_nested[5][0])
print(my_tuple_nested[5][1][0])
print(my_tuple_nested[5][1][1])
print(my_tuple_nested[5][1][2])




