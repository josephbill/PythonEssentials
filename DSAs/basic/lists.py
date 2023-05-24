# Lists : lists are used to store multiple items in a single variable.
# 4 ways to store multiple items / collections of data : lists, tuple,set,dictionaries (iterables)
shoppingBasket = ["Kales", "flour", "sugar", "Kales", "flour", "sugar"]
# lists() # converting tuples to lists.
# features on lists
# 1. List items are ordered , changeable and allow duplicate values
# 2. List items are indexed : start counting from 0
# 3. Lists items can be accessed , added , removed and changed.

# Accessing List Items
# list items are accessed by referring to their indexed numbers
print(shoppingBasket[0])
# negative indexing : this means start from the end
print(shoppingBasket[-1])
# range of indexes : ranges are specified by adding a start and end position  start:end
print(shoppingBasket[2:5])  # ranges use the position flow , only removing the elements in the start position
print(shoppingBasket[:4]) # if i give end position , it returns the first n elements : where n points to the integer given
print(shoppingBasket[2:]) # if i give start position , it removes the first n elements
print(shoppingBasket[-4:-2])  # specify negative indexes if you want to start the access from the end of the list.

# checking if items exist in a list
# we use the keyword in
x = input("check basket for this item ")
if x in shoppingBasket:
    print("yes " + x + " in basket")
else:
    print("no " + x + " in basket")

# change lists items
# to change the value of a specific item , refer to the index and replace the value by assigning a new one
shoppingBasket[3] = "Soap"
shoppingBasket[4] = "Bread"
shoppingBasket[5] = "Cooking Oil"

print(shoppingBasket)

# to change a range of item values
# to change the values in a specific range , definae a list with the new values and refer to the index numnbers where we want to insert
# the index values
shoppingBasket[1:4] = ['apples', 'oranges', 'Juice']
print(shoppingBasket)
# how to add / Insert
# to insert a new item to my shopping basket , use insert() method
# reference the index and the new value for the insert process
shoppingBasket.insert(0, "Spinach")
print(shoppingBasket)
# append (adds item to end of list)
shoppingBasket.append("Cereals")
print(shoppingBasket)
# to extend is also to add
# extending in python is joining two lists together
toolShopping = ['hammers', 'screws', 'screw drivers']
shoppingBasket.extend(toolShopping)
print(shoppingBasket)
# you can also add other iterables (lists,sets,tuples and dictionaries)
# example of a tuple
tupleExample = ('kiwi', 'gel')
shoppingBasket.extend(tupleExample)
print(shoppingBasket)

# Remove items in lists
# 1. We can use the remove method to remove a known item
shoppingBasket.remove("Bread")
print(shoppingBasket)
# 2. We can use the pop method together with an index position
shoppingBasket.pop(1)
# if index is not specified in pop , it simply removes the last item
shoppingBasket.pop()
print(shoppingBasket)
# 3. Using the del keyword
del shoppingBasket[2]
print(shoppingBasket)
# 4. To empty or remove everything
shoppingBasket.clear()
print(shoppingBasket)




# https://www.w3schools.com/python/python_lists_sort.asp : Sorting a list
# https://www.w3schools.com/python/python_lists_copy.asp  : copying a list
# https://www.w3schools.com/python/python_lists_join.asp  : joining a list
# https://www.w3schools.com/python/python_lists_methods.asp : glossary of list methods















