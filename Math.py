# a module is basically a file with methods that can be implemented in other class
# to include a module we use the import statement
import math
# built in math functions
# min & max : return the minimum value and max value respectively inside a collection
x = min(100,200,400)
y = max(100,200,400)
print(x)
print(y)
# abs : conversion to positive number
x  = abs(-1.25)
print(x)
# pow : returns the value of x to power of y pow(x,y)
x = pow(4,3)
print(x)

# Math module
# sqrt
x = math.sqrt(64)
print(x)
# rounding off , math.ceil : roundoff upwards to the nearest integer and then we have floor to round off downwards to the nearest integer
x = math.ceil(2.4)
y = math.floor(2.4)
print(x)
print(y)
# math.pi (return the value 3.14.......)

# https://www.w3schools.com/python/module_math.asp : more math methods