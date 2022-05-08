#loop for values in list
#create the list
dates = [1980, 1981, 1982]

#get the number of list items
n = len(dates)

print("print(dates[i])")
for i in range(n):
    print(dates[i])


#loop for a specifed range
print()
print("for i in range(-5, 6):")
for i in range(-5, 6):

    print(i)

#loop based on direct access 
print()
print("for date in dates:")
for date in dates:
    print(date)

#loop based on enumerate
print()
print("for i, date in enumerate(dates):")
for i, date in enumerate(dates):
  print(i, date)