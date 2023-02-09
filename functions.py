# Function is simply a block of organized and reusable code that is used to perform a single , related action.
# How to define a function in python
# 1. Are defined using the keyword def
# 2. Followed by a function name
# 3. Followed by a set of parentheses ():
# 4. def checkout() e.g
# 5. FUnction need to be called inorder for the code to be executed
# 6. to call a function we use the name of the function followed by a set of parentheses.
def greeting():
    # write the logic / block of code that the function should run
    # to end a function we use the RETURN keyword
    message = print("hello from greeting")  #block of code
    return message # final output of the function on call.

greeting() #call to a function


# 7. Functions in python can have what we call parameters , parameters are : information that a function needs in its code execution
# to define a function with parameters . Add the parameters in the parentheses as variables.
# in above example , if the greeting comes from my user then the defination will look like this

message = "hello from user"
def greeting_from_user(greet):  #here greet is referred to as a function parameter
    print(greet)
    return

greeting_from_user(message)   # message is referred to as a function arguement.
# multiple parameters
def simple_add(num1,num2):
    print(int(num1) + int(num2))
    return

simple_add(1,1)

# default arguements  : intialize parameters with a default value
def default_arguements(num1,num2 = 1):
    division = (int(num1) / int(num2))
    print(int(division))
    return


default_arguements(20,10)


# SCOPE OF VARIABLES IN A FUNCTION
# two basic scopes of variables in python : global scope(variables) / local scope(variables)
# global variables are defined outside functions and can be accessed by all functions within the file scope
# local variables are defined within functions and can only be accessed within the function that defines them.
# local variables can be made accessible to other function by passing them as arguments to the other functions

# the other functions should accepted parameters and the call to those functions should be made within the function which defined
# the local variables

result = 0  # here total is a global variable
# message_local = " The intial version "  # here total is a global variable
def sum(num1,num2):
    message_local = "the operation result is "  # message_local belongs to the sum method : thus a local scope
    result = num1 + num2 # result here is a localized
    print(message_local + str(result))
    return result

def division(num1,num2):
    result = num1 / num2 # result here is a localized
    print(str(result))
    return result

sum(10,10)
division(10,10)


# ANONYMOUS FUNCTIONS : they are not declared using the def keyword.
# they are created using the lambda keyword
# they can take a number of arguments but can only return one value in the form of an expression
# We cant use print methods directly when writing the lambda functions
# they can only access global variables and listed parameters

# lambda [arg,arg,arg] : expression  # simple syntax
# to work with them well , store the lambda function inside a variable

sum = lambda num1, num2: num1 + num2
print("value of", sum(10,10))



















