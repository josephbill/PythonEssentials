# We use operators to manipulate the value of operands (Values/Variables)
# Types of operators
# 1. Arithmetic operators (+,-,/,*,%,**,//)
# 2. Comparison operators (>,<,<=,>=,!=,==)
# 3. Assignment Operators (=,+=,-=,*=,%=,**=,//=)
# 4. Logical Operators (and,or,not)
# # week 2
# others , membership operators / bitwise / identity operators

# COMPARISON OPERATORS
# ==	Equal	4 == 5 false. 4 == 4 true  a == b
# !=	Not Equal	4 != 5 is true.
# > 	Greater Than	4 > 5 false. 5 > 4 true   a > b  , b > a
# <	    Less Than	4 < 5 is true. 5 < 4 false
# >=	Greater than or Equal to	4 >= 5 false. 4 <= 5  true
# <=	Less than or Equal to	4 <= 5 is true. 4 <= 4 true

a = 4
b = 5

# Equal
print("a == b : ", a == b)

# Not Equal
print("a != b : ", a != b)

# Greater Than
print("a > b : ", a > b)

# Less Than
print("a < b : ", a < b)

# Greater Than or Equal to
print("a >= b : ", a >= b)

# Less Than or Equal to
print("a <= b : ", a <= b)

# d = 7
# e = 6
# # %
# modulus = d % e
# print(modulus)
#
# f = 13
# g = 6
# floorDivision = f // g
# print(floorDivision)


# ASSIGNMENT OPERATORS
# =	    Assignment Operator 	 a = 10
# +=	Addition Assignment	a += 5 (Same as a = a + 5)
# -=	Subtraction Assignment	a -= 5 (Same as a = a - 5)
# *=	Multiplication Assignment	a *= 5 (Same as a = a * 5)
# /=	Division Assignment	a /= 5 (Same as a = a / 5)
# %=	Modolus/Remainder Assignment	a %= 5 (Same as a = a % 5)
# **=	Exponent Assignment	a **= 2 (Same as a = a ** 2)
# //=	Floor Division Assignment	a //= 3 (Same as a = a // 3)


# Assignment Operator
a = 10

# Addition Assignment
a += 5
print("a += 5 : ", a)
# Subtraction Assignment
a -= 5
print("a -= 5 : ", a)
# Multiplication Assignment
a *= 5
print("a *= 5 : ", a)
# Division Assignment
a /= 5
print("a /= 5 : ", a)
# Remainder Assignment
a %= 3
print("a %= 3 : ", a)
# Exponent Assignment
a **= 2
print("a **= 2 : ", a)
# Floor Division Assignment
a //= 3
print("a //= 3 : ", a)

# LOGICAL OPERATORS
# and Logical AND	If both the operands are true then condition becomes true.	(a and b) is true. AND &&
# or Logical OR	    If any of the two operands are non-zero then condition becomes true.	(a or b) is true. OR ||
# not Logical NOT	Used to reverse the logical state of its operand. !

# Conditionals or Control flow statements are used together with logical operators. (DECISION MAKING PROCESS)

# In the decision making process in python we use an if else statement
# if condition:
#     # code to execute if the condition is True
# else:
#     # code to execute if the condition is False

variableCompare = 5
secondVariable = 10
# e.g. my python program should print out hey there if the value of variableCompare is 7
# simple if
if variableCompare == 10:
    print("simple if")
else:
    print("condition not met")

# multi conditional
if variableCompare == 10:
    print("from multi conditional")
elif variableCompare == 7:
    print("form the multi conditional")
elif variableCompare == 6:
    print("form the multi conditional")
else:
    print("none meet condition")

# we can cojoin the conditional with logical operators
# or
if variableCompare == 10 or secondVariable == 6:
    print("from or")
elif variableCompare == 5 and secondVariable == 10:
    print("from and")
else:
    print("No condition met.")
