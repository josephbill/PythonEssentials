# iterator : any object that contains a countable number of values
# iterator : any object that can be traversed / looped/
# any object that implements the iterator protocol , _iter_() and _next_()

# iterator vs Iterable  : iterables (lists,strings,tuples,sets,dictionaries) all have the method _iter_() / iter()
# iter() method enables objects to be traversed/ looping
mytuple = ("1","2",3)
myIterable = iter(mytuple)
# access to the next()
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
x = "joseph"
myIterable = iter(x)
print(next(myIterable))
# just loop over iterables using a for loop

# create an iterator that returns numbers , stating with 1 , and each sequence will increase by 1 -> 1,2,3,4,5
# classes and objects
class MyNumbers:
    # making the class mynumbers an iterable using the iter method
    def __iter__(self):
        self.a = 1
        return self
    # next method to provide trasversal ability for my class
    def __next__(self):
        x = self.a
        self.a += 1
        return x
# object
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))












