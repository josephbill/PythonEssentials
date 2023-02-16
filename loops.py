# define : a technique in python programming that will allow us to repeat tasks based off a condition.
# We have two primitive loops 1. while Loop 2. for loops

# WHILE LOOP
# the loop allows us to execute a set of statements/logic as a long as a condition is true.
# to print 1 to 6 using a while loop.
# the loop needs a condition : written in code using operators
# < 7 : condition , starting point -> intialization counter -> mostly used in the condition formulation
# incrementors : increases the initial value and decrementors :  decrement the initial value
# stop the loop when the condition is met , decrementor will create infinite loop (which may crush the program) : NB.. depends on the condition
start = 1
# while condition:
#     # logic
# +=
# while start < 7:
#     print(start)
#     start += 1

# to stop a loop make the condition false.

# SPECIAL STATEMENTS IN WHILE LOOP
# BREAK : allows us to stop the loop even when the condition is true
# maybe in above loop , we need to stop the loop when start = 3

while start < 7:
    print(start)
    # here we can place the break after the logic runs
    if start == 3:
        break
    start += 1

# CONTINUE : skips the current loop and continue with the next
# to exclude 3 from the loop print out
start = 0
while start < 6:
    start += 1
    # here we can place the break after the logic runs
    if start == 3:
        continue
    print(start)

# ELSE statement : we can run a block of code once when the condition is no longer true
start = 1
while start < 7:
    print(start)
    start += 1
else:
    print("start is no longer less than 6")

# FOR LOOP
# Popular for iterating/looping over sequences/collections (lists, tuples , dictionaries , sets and strings)
# allows execution of a set of statements on each item in the collection or sequence
# lists
fruits = ["apple","banana","cherry"]
tupleFruit = ("apple","banana","cherry")
for x in fruits:
    if x == "apple":
        print("i have reached apple")
    else:
        print(x)

for x in tupleFruit:
    print(x)

# loop a string
for x in "joseph":
    print(x)

# the range function : species number of times to loop through a set of code
for x in range(6):
    print(x)
for x in range(2,6):
    print(x)

# range with increment value
for x in range(2,10,3):
    print("Last loop " + str(x))


# ELSE IN in for loop : specifies a block of code to execute when the loop is done

for x in range(5):
    print(x)
    # break
else:
    print("Loop has finished")


# NESTED LOOPS
# a loop inside a loop
loopone = ["red","mango","joseph"]
looptwo = ["a","b","c"]

for x in loopone:  # in nested loop , the outer loop has to complete , inorder to move to the second item in the inner loop
  for y in looptwo:
      print(x,y)

# PASS STATEMENT : helps us to avoid errors when the loop body is empty
emptyvariable = ''
for x in [1,2,3]:
 pass


# Look at the following links for looping examples on more collections
# https: // www.w3schools.com / python / python_dictionaries_loop.asp
# https: // www.w3schools.com / python / python_sets_loop.asp
# https: // www.w3schools.com / python / python_tuples_loop.asp
# https: // www.w3schools.com / python / python_lists_loop.asp





































