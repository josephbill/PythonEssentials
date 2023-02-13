# program should take two input values
def compare_numbers(a,b):
    if type(a) == int and type(b) == int:
        if a == b:
            return "a and b are equal"
        elif a > b:
            return "a is greater than b"
        else:
            return "b is greater than a"
    else:
        return "invalid input"

a = int(input(" Enter number a : "))
b = int(input(" Enter number b : "))
print(compare_numbers(a,b))


#  2
def calculator(c,d):
    if type(c) == int and type(d) == int:
      sum = c + d
      difference = c - d
      product = c * d
      # division
      if d == 0:
          return "division by zero not allowed"
      else:
          division = c / d
          if c == d:
              return "a and b are equal\nsum: {}\ndifference: {}\nproduct: {}\ndivision: {}".format(sum, difference, product, division)
          else:
              return "sum: {}\ndifference: {}\nproduct: {}\ndivision: {}".format(sum, difference, product, division)

    else:
        return "invalid input"


c = int(input(" Enter number c : "))
d = int(input(" Enter number d : "))
print(calculator(c,d))
