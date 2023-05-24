# Defination of what a dictionary is
# iterable used to store items in key and value pairs
# Features : ordered -> python 3.7 , in 3.6 and below , dictionaries were unordered
# changeable but do not allow duplicates.
# dictionary values can be of different data types
# syntax of a simple dictionary
# shoppingDictionary = {
#     key:value
# }
# shoppingDictionary = {
#     "item1": 5,
#     "item2": "Milk",
#     "item3": True,
# }
shoppingDictionary = {
    "item1": "Bread",
    "item2": "Milk",
    "item3": "Flour",
}
# to get length of a dictionary (len())
print(len(shoppingDictionary))


# Accessing Items Values in Dictionaries
# access is done by referencing the key name inside square brackets
# for example to access milk
print(shoppingDictionary["item2"])
# we can also use an inbuilt method get()
x = shoppingDictionary.get("item3")
print(x)
# to get the keys in a dictionary we use the keys() method
x = shoppingDictionary.keys()
print(x)
# if you want all values  we use the values() method
print(shoppingDictionary.values())
# We also have an items() method : returns each in item in a dictionary , as tuples in a list
print(shoppingDictionary.items())
# check if keys exists in a specific dictionary
check = "item7"
if check in shoppingDictionary:
    print("Yes, the item is there")
else:
    print("No, item not found")


# Modifications/Updates , changing values, adding values , removing values
# change the value of a specific item
# to change reference the key and assign new value
shoppingDictionary["item3"] = "salt"
print(shoppingDictionary["item3"])
# we can achieve above by also using the update() method
shoppingDictionary.update({"item2":"FLour"})
print(shoppingDictionary["item2"])

# add
# to add, reference the key and assign new value
shoppingDictionary["item4"] = "Sugar"
# update can also be used to add
shoppingDictionary.update({"item5": "Eggs"})
print(shoppingDictionary.values())

# removing
# remove using the pop()method which requires a key in the dictionary as info/arguments
shoppingDictionary.pop("item5")
print(shoppingDictionary.values())
# popitem() in 3.6. and below , will remove the last inserted item
# popitem() in 3.7 , this removes a ran
# # the del keyword remove the item with the specified name
# del shoppingDictionary["item1"]
# print(shoppingDictionary.values())dom item
# shoppingDictionary.popitem()
# print(shoppingDictionary.values())
# finally we have clear to empty the dictionary
# shoppingDictionary.clear()
# print(shoppingDictionary.values())

# copy a dictionary
# simply use the copy inbuilt method
copyDictionary = shoppingDictionary.copy()
# dict() will also allow you to do the same
dictDictionary = dict(shoppingDictionary)
print(copyDictionary)
print(dictDictionary)
# NESTED DICTIONARIES
myFamily = {
    "child1": {
            "name": "Joseph",
            "age" : "26"
    },
    "child2": {
        "name": "Mary",
        "age": "26"
    },
    "child3": {
        "name": {
            "firstname": "Joseph",
            "lastname": "Mbugua"
        },
        "age": "26"
    },
}
# access to nested dictionaries
# say we wanted name info on child two
# reference child 2 using the key and then get the details you want using the key
print(myFamily["child2"]["name"])
print(myFamily["child3"]["name"]["firstname"])

# excercise
car = {
    "brand":"ford",
    "model": "mustang",
}
# to get the print of the car model
print(car["model"])
# change the value of the model , to be a  tuscan
car.update({"model": "tuscan"}) #{} curly braces [] square brackets () round brackets / parentheses
car["model"] = "tuscan"
# add a key and value pair : year : 1964
car["year"] = "1964"
car.update({"year": "1964"})
#  remove a random key item in the dictionary
car.popitem()
# remove the year
car.pop("year")
# how can i empty the dictionary
car.clear()
















