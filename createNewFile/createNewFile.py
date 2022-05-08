#Lists
#create list with square brackets
my_list = [1, 2, 3]
print(my_list)

#lists can be amended - change a value
my_list[0] = "chicken"
print(my_list)

#lists can be amended - add a new value at the end
my_list.append('another chicken')
#lists can be amended - add multiple values
my_list.extend(['yet another chicken', 5, 8])
print(my_list)

#tuples
#create tuple with round brackets
my_tuple = (1, 2, 3)
print(my_tuple)

#tuples cannot be amended 
my_tuple_amended = my_tuple + (4, 5, 6)
print(my_tuple_amended)

#tuples can contain tuples 
my_tuple_nested = (1, 2, ("rock", "pop"), (3,4), ("disco", 5, 6), ("funk", (7, 8, 9)))

print(my_tuple_nested[0])


