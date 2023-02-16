# a variable is only available inside the region it has been created. Idea of a scope
# local scope / Global scope
# global scope : variables created outside functions
x = 200 # this is accessible to all files
# the global keyword : the global keyword makes variables global
# local scope : variables created inside functions have a local scope
# in the example below x,y are local thus not available outside the function
def sampleMethod():
    global y  # makes the local scope variable , global
    x = 100
    y = 200
    return x + y

print(sampleMethod())

# # what of scope when a function is inside a function
def samplefunction():

    def innerFunction():
        print(y) # inner function ends here  # return , print
    return innerFunction()

samplefunction()



