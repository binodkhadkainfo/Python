"""
OOP in Python
===============
To map with real world scenarios, we started using objects in code.
This is called object oriented programming.
=======================================================================================================

class Employee:
    language = "py"               #This is a class attribute
    salary = 200000000

binod = Employee()
binod.name ="bino"                #This is an instance attribute
print(binod.name, binod.language, binod.salary)

#       OutPut:- bino py 20000000
#--------------------------------------------------------------------------
#   Instance Attribute  |
#------------------------

class Employee:
    name ="binod"
    language = "py"               #This is a class attribute
    salary = 200000000

binod = Employee()
binod.name ="manita"                #This is an instance attribute
print(binod.name, binod.language, binod.salary)

#OutPut:- manita py 200000000
#-------------------------------------------------------------------------------------

class Employee:
    language ="python" #This is a class attribute
    salary = 2000000000

    def getinfo(self):
        print(f"This language is {self.language}.The salary is {self.salary}")

binod = Employee()
binod.getinfo()     #Employee.getinfo(binod)

#OutPut:- This language is python.The salary is 2000000000

#-------------------------------------------------------------------------------
#  Static Method  |
#------------------

class Employee:
    language ="python" #This is a class attribute
    salary = 2000000000


    def getinfo(self):
        print(f"This language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def using():
        print("hello i am using differnt methon")

binod = Employee()
binod.getinfo()
binod.using()

#OutPut:- This language is python.The salary is 2000000000
#         hello i am using differnt methon

=======================================================================================================
#   init Function  |
#-------------------
class CEO:
    language ="python"          #This is calss attribute
    salary = 1000000

    def __init__(self):  #dunder (double underscore) method which is automatically called
        print("I am creating an object")

binod = CEO()

# OutPut:- I am creating an object


------------------------------------------------------------------------------------------------
================================================================================================
Class & Object in Python
--------------------------

Class is a blueprint for creating objects.

#creating class

class Student:
    name = "binod khadka”

    
#creating object (instance)

s1 = Student()
print( s1.name)
=======================================================================================================

class Student:
    name = "binod"

s1 =Student()
print(s1.name)

s2 = Student()
print(s2.name)

#OutPut:- binod
#         binod
=======================================================================================================

class Car:
    colour = "blue"
    brand = "mercedes"

Car1 = Car()
print(Car1.colour)
print(Car1.brand)

#OutPut:- blue
#         mercedes
=======================================================================================================
   init Function
#-------------------
Constructor

All classes have a function called _init_(), which is always executed when the class is being initiated.

#creating class:                            #creating object:

class Student:                                s1 = Student( “karan” )
def _ _init_ _( self, fullname ):             print( s1.name)
self.name = fullname



*The self parameter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class.
----------------------------------------------------------------

class student:
    
    #default constructors
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
    
s1 = student("bin",98)
print (s1.name, s1.marks)

    
s2 = student("bino",99)
print (s2.name, s2.marks)

#  OutPut:- adding new student in Database..
#           bin 98
#           adding new student in Database..
#           bino 99

class Employee:
    language = "py"     #This is a class attribute
    salary = 200000000

binod = Employee()
binod.name ="bino"      #This is a class attribute
print(binod.name, binod.language, binod.salary)




========================================================================================================
"""
#    Class & Instance Attributes
# ---------------------------------

#  class.attr
#  obj.attr

#========================================================================================================
