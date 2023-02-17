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
# self in classes points to the current object being createdy
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


# MAIN CONCEPTS IN OOP programming
# 1. Classes : see examples above
# 2. Objects : see example above
# 3. Encapsulation : describes an idea of wrapping data and methods that will work on the data within one unit
class Subject:
    def __init__(self,name,student):
        self.name = name
        self.student = student


    def addedSubject(self):
            print("The subject " + self.name + " has been added to " + self.student.name)

mathsubject = Subject("Math",student2)
mathsubject.addedSubject()



# 4. Inheritance :  capability of one class to derive and inherit properties(variables and methods working on those variables) from another class
# two levels of parties involved : parent -> child
# benefits  of inheritance
# 1. reusability
# 2. it represents real world relationship.
# 3. its transitive in nature ,  class a(parent) , class b(child) , class c(child of B) if b inherits from a , then all classes under b have access to
# all properties derived from class a

# in python we have 3 types of inheritance
# - single inheritance  : enables a derived class (child class) to inherit props from a single parent class
# - multilevel inheritance : enables a derived class to inherit props form an immediate parent class which in turn inherits props from another parent class
# - hierarchical inheritance : enables more than one derived class to inherit props from a parent class
# - multiple inheritance : enables one derived class to inherit props from more than one parent class
# person class : parent
# employee class : child

# base/parent class
class Person(object):
    def __init__(self,name,staffnumber):
        self.name = name
        self.staffnumber = staffnumber

    def display(self):
        print(self.name)
        print(self.staffnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My staff number is {}".format(self.staffnumber))

# to inherit from above base class use the parentheses (round brackets) to indicate the parent class
class Employee(Person):
    # name / staff will be derived from the parent class
    def __init__(self, name , staffnumber , salary, department):
         self.salary = salary
         self.department = department

    # invoke/call the init function in parent class
         Person.__init__(self,name,staffnumber)

    # 5. Polymorphism : simply means having many forms
    # we perform polymorphism by defining the same method but giving a different output in the derived classes.
    def details(self):
        print("My name is {}".format(self.name))
        print("My staff number is {}".format(self.staffnumber))
        print("My Salary is {}".format(self.salary))
        print("My department is {}".format(self.department))

#
a = Employee('Joseph',1234,100000,"software developer")
# call methods from the parent class
a.display()
a.details()

# 6. Data Abstraction































