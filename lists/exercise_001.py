#create a list of values
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))
print()

#any type of value can be added to the list
sundry = ['John', 3.14, 7, False]

print(sundry)
print(type(sundry))
print()

#create and empty list
my_list = []

#Use an index to access individual elements
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')
print()

#A slice defines a range of elements by using a special syntax.
#At first glance, it looks similar to the syntax that uses an index to access a single element of the list.
#But the slice syntax uses a colon (:). The colon separates the beginning of the slice, on the left, and the end of the slice, on the right.
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print('\nPrint a slice, starting at index 2 to index 5 (index 5 excluded):')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3 (index 3 excluded):')
print(colors[:3])

print('\nPrint a slice, starting at index 4 to the end of the list (last item included):')
print(colors[4:])

print('\nPrint a slice, starting at the 4th from the end to the 2nd from the end (last item excluded):')
print(colors[-4:-1])

#reverse and sort the list
colors.reverse()
print(colors)

colors.sort()
print(colors)
print()

#treat the list like a queue
#A queue is a special term in programming that refers to a list that stores items in the order in which they were added.
#Queues are useful when you need to do some calculation logic on many items in a specific order. After you add items to the list, you remove them for processing one by one.
#A pop operation removes an item from the queue for processing. You can remove an item from the beginning of the list ("first in, first out", or FIFO).
#Or you can remove an item from the end of the list ("last in, first out", or LIFO).
#The pop() helper function allows you to select an item from the list by using its index. The first item is 0, and the last item is -1.

#The pop() helper function takes the item at the index that you pass in as an argument. 
#It removes the item from the list and assigns it to a variable for processing. In this case, we don't do any real processing on the item.
print(colors)

color = colors.pop(0)
print('popped', color)

print(colors)
print()

#add and remove elements
print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)
print()

#combine lists
print(colors)

new_colors = ['lime', 'gray']
colors.extend(new_colors)

print(colors)
print()

#clear the list
print(colors)

colors.clear()

print(colors)
print()