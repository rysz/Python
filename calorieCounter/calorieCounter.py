print("Today's date?")
date = input()

print("Breakfast calories?")
breakfast = int(input())

print("Lunch calories?")
lunch = int(input())

print("Dinner calories?")
dinner = int(input())

print("Snack calories?")
snack = int(input())
total = breakfast + lunch + dinner + snack
print("Calorie content for " + date + ": " + str(total))