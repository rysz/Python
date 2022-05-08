#set
#created with curly brackets
my_set = {"Micheal Jackson", "Thriller", "Thriller", 1982}
#set can be created from a list
my_list = ["Micheal Jackson", "Thriller", "Thriller", 1982]
my_set_list = set(my_list)

#set only contain unique elements
print("#set only contain unique elements (Thriller is now only displayed once): ", my_set)
print("#set can be created from a list: ", my_set_list)

#set can be amended (mutable)
my_set.add("Added Item")
print("#set can be amended (mutable): ", my_set)



#intersecting
my_set_1 = {"Thriller", "Back in Black", "AC/DC"}
my_set_2 = {"Back in Black", "AC/DC", "The Dark Side of the moon"}

#venn diagram intersect (inner join) - return data from both sets where it's the same 
my_set_intersected = my_set_1 & my_set_2
print("my_set_intersected = my_set_1 & my_set_2: ", my_set_intersected)

#venn diagram intersect (inner join) - return data from both sets where it's the same
#alternative syntax... why TBC
print("my_set_1.intersection(my_set_2): ", my_set_1.intersection(my_set_2))
print("my_set_2.intersection(my_set_1): ", my_set_1.intersection(my_set_2))

#venn diagram - find the difference in my_set_1 but not my_set_2 (right or left join depending on how being called)
print("my_set_1.difference(my_set_2): ", my_set_1.difference(my_set_2))
print("my_set_2.difference(my_set_1): ", my_set_2.difference(my_set_1))

#venn diagram - union the two sets
print("my_set_1.union(my_set_2)", my_set_1.union(my_set_2))

