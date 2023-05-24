# tuples allow us to store multiple items in a single variables
# tuples are ordered but unchangeable.
# to define  a tuple  : defined with round brackets
shoppingTuple = ("Bread","Sugar","Salt","Bread","Sugar")
print(shoppingTuple)
# tuple are indexed : start is at 0
# tuples also allow duplicates
# to get the length of a tuple len()
print(len(shoppingTuple))
# tuple with one item : define by placing a comma.
tupleOne = ("Bread",)
# tuples can have items of the same data type or different data types
tuple1 = (1,5,6,7)
tuple2 = ("string",1,True,False,"another string")
type(tuple1)

# Accessing a Tuple
# access is done by reference to the index number
print(shoppingTuple[0])
print(shoppingTuple[-1]) # negative indexing #start from end
print(shoppingTuple[2:5]) # range
print(shoppingTuple[2:]) # to search out the first index in range.
print(shoppingTuple[:3]) # to search out the last index in range.
print(shoppingTuple[-4:-1]) # this will search from end of the tuple

# checking if item exists in a tuple
search = "Milk"
if search in shoppingTuple:
    print("Yes " + search + " is in tuple")
else:
    print("No " + search + " in tuple")

# Updating a tuple.
# if you want to add , remove or change items in a tuple then use this hack around
# covert the tuple to a list , then use the list methods to modify the items ,  convert the list back to a tuple
tempList = list(shoppingTuple) # conversion is via the list()
tempList[0] = "Milk"
#covert the above list back to a tuple
shoppingTuple = tuple(tempList)
print(shoppingTuple)

# add items
# add new items
tempList.append("Flour")
shoppingTuple = tuple(tempList)
print(shoppingTuple)
# add a tuple to am tuple
tuple3 = ("Oranges",)
shoppingTuple += tuple3  # joining a tuple tuple3 + shoppingTuple
print(shoppingTuple)
tempList = list(shoppingTuple) # conversion is via the list()

#remove items
# convert tuple to a list and then use the remove , pop ,
tempList.remove("Oranges")
del tempList[0]
shoppingTuple = tuple(tempList)
print(shoppingTuple)

# delete a tuple completely
# del shoppingTuple


# UnPacking a tuple : making an item in the tuple act as an independent value
(sugar, salt, bread, sugar, flour) = shoppingTuple
print(sugar)
print(salt)
print(bread)
print(sugar)
print(flour)
(sugar, salt, *bread) = shoppingTuple # if variables are less than number of items in tuple use an * to package remaining values as a list.
print(bread)
(*sugar, salt, bread) = shoppingTuple
print(sugar)

# replicate values in a tuple
duplicateTuple = shoppingTuple * 2 # joining a tuple tuple3 + shoppingTuple
print(duplicateTuple)

# exercises
# 1. Print the first item in the fruits tuple
fruits = ("apple","banana","oranges")
print(fruits[0])
# 2. Print number of items in the fruits tuple
print(len(fruits))
# 3. I want to access oranges without referencing its index position as 2.
print(fruits[-1])
# 4. I want the range of indexes that will output the third , fourth and fifth items
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
# tuple methods
x = fruits.count("apple") # shows number of times a value appears in a tuple
y = fruits.index("cherry") #searches for the first occurance in a tuple value
print(x)
print(y)












































