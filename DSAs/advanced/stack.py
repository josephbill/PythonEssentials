# a stack is a linear data structure that allows access of items using a Last in First Out Principle.
# its implementation will vary to when needed
# look at this methods : push : add elements to stack , pop : remove element from stack , peek : see what a stack has.
# empty/full : returns true if stack is empty or full .
# search(target) : returns the distance between the top of the stack and the taget index.
# size : returns number of items in the stack

# example using a stack to reverse a string
def reverse_string(string):
    stack = []
    # loop the string to append each character to the stack
    for char in string:
        stack.append(char)
    # empty variable to represent the reversed string
    reversed = ""

    # loop the stack removing the last element added and adding it to the empty variable string
    while stack:
        reversed += stack.pop()

    return reversed

print(reverse_string("Joseph"))

# evaluating key strokes

# Given a string which may include this symbol representing a backspace < , return the interpreted version of the string
# which erases characters next to the < symbol respective to the symbols occurances  i.e.

# evaluate_keystrokes('abcde<fg<h')
# # => 'abcdfh'
#
# evaluate_keystrokes('abcd<<<fg<h')
# # => 'afh'

def evaluate_keystrokes(string):
    stack = []
    # loop the string checking for the < symbol if it present pop it off
    for char in string:
        if char == "<":
            stack.pop()
        else:
            stack.append(char)

    # loop the stack to get the new string
    newstring = ""
    while stack:
        newstring = stack.pop() + newstring

    return newstring

print(evaluate_keystrokes("abcd<<<fg<h"))

