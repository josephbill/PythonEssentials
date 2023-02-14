# Set allow us to store multiple items in a single variables
# sets are unordered , unchangeable , unindexed
# to define a set use curly braces
# sets do not have duplicated
# True and 1 are also considered the same
# sets will allow different data types
shoppingSet = {"Bread","Sugar","Salt"}
print(shoppingSet)
# getting length of set
# len()
print(len(shoppingSet))
# setting items in a set : same data types or mixed data types
# shoppingSet = {"Bread","Sugar","Salt"} same
# shoppingSet = {"Bread","Sugar","Salt",True,200} mixed data types


# Access Items
# to access items in a set we use the concept loop
# Loop : repetitive task
# for in  :
for x in shoppingSet:
    print(x)
# to check if item exist in a set
check = "Bread"
print(check in shoppingSet)

# updating a set add , removing
# add
# in a set u cannot change the items , but you can add new items  , add()
shoppingSet.add("Flour") # adds value to start of the set
print(shoppingSet)
# adding items from another set to the current set
juiceFlavours = {"Mango","Passion","Apple"}
shoppingSet.update(juiceFlavours) # adds the values to the end of the set
print(shoppingSet)
# adding other iterable ( collections of data , lists , tuples ,dictionaries ) / join tuples
simpleList = ["Oranges","Soap","spoons"]
simpleTuple = ("Forks","Spades")
set2 = {"item2","item3"}
shoppingSet.update(simpleList)
shoppingSet.update(simpleTuple)
shoppingSet.update(set2)
print(shoppingSet)
# removing
# to remove an item in a set
# shoppingSet.remove("Spades") # use remove when you know the items to remove
# shoppingSet.discard("Forks")
# print(shoppingSet)
# x = shoppingSet.pop() # the pop method removes a random element from set
# print(x)
# shoppingSet.clear() # empties the set
# print(shoppingSet)
# del shoppingSet #deletes the set completely
# print(shoppingSet)

# https://www.w3schools.com/python/python_sets_methods.asp : sets methods

# Joining tuples , update , union
set3 = {"item5",5}
set4 = shoppingSet.union(set3)  # union creates a new set .
print(set4)
# intersection_update  : join sets but will only keep the items that are present in both sets
x = {"apple","banana"}
y = {"microsoft","apple"}
x.intersection_update(y)
print(x)
# intersection  # returns a new set
x = {"apple","banana"}
y = {"microsoft","apple"}
z = x.intersection(y)
print(z)
# symmetric_difference_update  : keeps elements not present in both
x = {"apple","banana"}
y = {"microsoft","apple"}
x.symmetric_difference_update(y)
print(x)
# symmetric_difference  : new set
x = {"apple","banana"}
y = {"microsoft","apple"}
z = x.symmetric_difference(y)
print(z)
# True and 1 are always same , False and 0 Are always the same.
x = {"apple", "banana", "cherry", True, False}
y = {"google", 1, "apple", 2, 0}
z = x.symmetric_difference(y)
print(z)












