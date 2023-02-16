# try,except,else,finally
# the try block : lets you test a block of code for errors
# except block : handling of the error
# else : when no error execute this code
# finally: runs regardless of any error

# Exception Handling :
x = -1
try:
    print(x)
except:
    print("An error occured , check if email is defined")
else:
    print(str(x) + " from else") # try not to do the same thing as in try
finally:
    print("Finally block")  # try not to do the same thing as in try

# raise keyword : works with a condition if condition is met , raise an error message/exception/typeerror
if x < 0:
  raise Exception("sorry x shouldn't be less than zero")
