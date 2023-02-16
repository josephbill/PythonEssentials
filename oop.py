# classes and objects
# OBJECT ORIENTED PROGRAMMING (OOP) # we should treat our programs /programming  with a level of abstraction , reusability
# class : blueprint for an object  / template for creating creating object
# we use class keyword
class TestClass:
    x = 10  #variables inside classes , are reffered to as property
    def powerMethod(self):
        y = pow(10,2)
        print(y)
# objects are creation of classes
# to create objects reference the class name as a function call
object1 = TestClass()
print(object1.x)
print(object1.powerMethod())
# in oop  , classes will define the property and methods that work on those properites
# vehicle -> 4 seaters -> seats 4, engine , speed limit , tyre type , color  # objects will be the different brands
# we have a function called the init() , initialization function , that defines info about an object created from a set blueprint
# self in classes points to the current object being created
class Student:
    def __init__(self,name,age,unit,doa):
        self.name = name
        self.age = age
        self.unit = unit
        self.doa = doa

    def greetstudent(self):
        other = "!"
        print("hello " + self.name + other)

# create the objects with iniatialized values
student1 = Student("Joseph","14","Form1","Thursday")
student2 = Student("Mary","14","Form1","Thursday")
print(student1.name)
student1.greetstudent()
student2.greetstudent()

