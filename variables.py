# Variables and Data Types
# to create variables in python simply state the name of the variable followed by a assignment symbol =
# variables are given the data types by their values
greeting = "Hello World"  # greeting is a string variable.
print(greeting)
miles = 1000.0 # float variable.

# casting : simply changing/specifying the data type of variable
x = str(3)  # string '3'
y = int(3) # always be interpreted as an integer
z = float(3) # 3.0 : float
print(int(miles))

# Get the data type of an existing variable
xy = '5'
a = '5'
c = int(xy) + int(a)

d = 5
f = 5
s_um = d + f
d_iff = d - f
d_ivision = d / f
m_ultiplication = d * f
print(s_um, d_iff, d_ivision, m_ultiplication)
# type () : returns the data type of a varibale
print(c)
print(type(xy))
# variables in python are Case sensitive
name1 = "Joseph"
name1 = "Whitney"
Name1 = "Mary"  #Name1 will not overwrite name1
name1 = Name1
print(name1)

# Assigning multiple values to variables
# can allow you to assign values to multiple variables in one line

# 1. Many values to multiple variables
fruit1, fruit2, fruit3 = 'orange', 'Banana', 'Cherry'
print(fruit1)
print(fruit2)
print(fruit3)
# 2. One value , to multiple variables
fruit4 = fruit5 = fruit6 = 'Apple'
print(fruit4)
print(fruit5)
print(fruit6)
# 3. Unpack a collection
fruits = ["apple", "cherry", "banana"]  # array : single variable holds multiple values.
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)


























