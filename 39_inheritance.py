"""
  Inheritance & more on OOPS
------------------------------
Inheritance is a way of creating a new class from an existing class.
----------------------------------------------------------------------
#  Syntax

class Employee: #Base Class
    #Code

class Programmer(Employee):  #Derived or child class
    #Code
_________________________________________________________________________________
*We can use the method and attributes of 'Employee' in 'Programmer' object.

*Also, we can overwrite or add new attributes and methods in 'Programmer' class.
---------------------------------------------------------------------------------
TYPES OF INHERITANCE
----------------------
* Single inheritance
* Multiple neritance
* Multilevel inheritance
============================================================================================
-----------------------------------------------------------------------------------------"""

"""
# _________________________ #
# |  SINGLE INHERITANGE   | #
# ------------------------- #
Single inheritance occurs when child class inherits only a single parent class.


           ____________________
           |      Base        |
           ---------↓----------
           ____________________
           |     Derived      |
           --------------------

---------------------------------

class Employee:
    company ="DragUp"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary} ")

class programmer(Employee):
    company = "DragUpTech"
    def show(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee
b = programmer

print(a.company, b.company)

#OutPut:-   DragUp DragUpTech

#================================================================================================================"""
"""
#-----------------------------#
#  | Multiple Inheritance  |  #
#-----------------------------#


 ______________            ___________________
 |  Parent 1  |            |    Parent 2     |
 --------------            -------------------
        |                          |
        |                          |
        _____________________________
                    |
                    |
           ____________________
           |      Child       |
           --------------------




class Employee:
    company = "DragUp"
    name = "helloup"

    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"

    def PrintLanguages(self):
        print(f"Out of all languages, here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "DragUpTech"

    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


# Create instances
a = Employee()
b = Programmer()

# Call methods
b.show()             # Inherited from Employee
b.PrintLanguages()   # Inherited from Coder
b.showLanguage()     # Defined in Programmer
#============================================================================================================================"""
"""
#-----------------------------#
#  | Multi Level Inheritance  |  #
#-----------------------------#



           ____________________
           |      Parent      |
           ---------↓----------
           ____________________
           |     Child 1      |
           ---------↓----------
           ____________________
           |     Child 2      |
           --------------------

           
#  Syntax

class Employee: 
    a=1

class Programmer:
    b=2

class Manager:
    c=3

o = Employee()
print(o.a)   #Prints the a attribute 
#print(o.b) #Shows an error as there is no b attribute in Employee class

o = Programmer:
print(o.a, o.b)

o = Manager:
print(o.a, o.b, o.c)
#====================================================================================================================
#====================================================================================================================
#================================================================================================================="""
"""

#-----------------------------#
#      | SUPER()METHOD |      #
#-----------------------------#
# super() method is used to access the methods of a super class in the derived class.
super.()__init__()
# __init__()       Calls constructor of the base class
#-------------------------------------------------------------------------------------

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of Manager")
    c = 3

#o = Employee()
#print(o.a) #Prints the a attribute

#o = Programmer()
#print(o.b)

o = Manager()
print (o.a, o.b, o.c)


# OutPut:-  constructor of Programmer
#           constructor of Manager
#           1 2 3

"""

#====================================================================================================================
#====================================================================================================================
"""
#-----------------------------#
#      | CLASS  METHOD |      #
#-----------------------------#

#A class method is a method which is bound to the class and not the object of the class.

# @classmethod decorators used to creats a class method.


#      Syntax:

#    @classmethod
#        def(cls,p1,p2):
#--------------------------------------------------------------

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

#OutPut:- The class attribute of a is 1

"""
#====================================================================================================================
#====================================================================================================================


#-----------------------------#
#  | @PROPERTY  DECORATORS |  #
#-----------------------------#

# Consider the following class:
"""
Syntax:

class Employee:
    @property
    def name(self):
        return self.ename

If e = Employee() is an object of class employee, we can print (e.name) to print the
ename by internally calling name() function.

#----------------------------------------------------------------------------------------
#-----------------------------#
#  | @PROPERTY  DECORATORS |  #
#-----------------------------#

class Employee:
    a = 1  # Class attribute

    # Class method to show class-level attribute
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    # Getter for 'name'
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # Setter for 'name'
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

#-----------------------------#
#         | USAGE |           #
#-----------------------------#

e = Employee()

# This creates an instance variable 'a' that shadows the class variable
e.a = 45

# Using the setter method via @property to assign full name
e.name = "Binod Khadka"  # Splits and sets fname and lname

# Accessing the split values directly
print(e.fname, e.lname)  # Output: Binod Khadka

# Accessing full name using the getter
print(e.name)  # Output: Binod Khadka

# Calling class method to show class-level 'a'
e.show()  # Output: The class attribute of a is 1


"""
#====================================================================================================================
#====================================================================================================================
"""
#-----------------------------#
# | @.GETTERS AND @.SETTERS | #
#-----------------------------#



The method name with '@property' decorator is called getter method.
We can define a function + @ name.setter decorator like below:


Syntax:
@name. setter n
def name (self,value):
self.ename = value

#------------------------------------------------------------------------
#-----------------------------#
# | @GETTERS AND @SETTERS |  #
#-----------------------------#

class Employee:
    def __init__(self):
        self._name = ""

    # Getter method
    @property
    def name(self):
        return self._name

    # Setter method
    @name.setter
    def name(self, value):
        self._name = value

#-----------------------------#
#         | USAGE |           #
#-----------------------------#

e = Employee()

# Using the setter
e.name = "Binod Khadka"

# Using the getter
print(e.name)  # Output: Binod Khadka


"""
#====================================================================================================================
#====================================================================================================================
"""
#------------------------------------#
# | OPERATOR OVERLOADING IN PYTHON | #
#------------------------------------#

Operators in Python can be overloaded using dunder methods.

These methods are called when a given operator is used on the objects.

Operators in Python can be overloaded using the following methods:

pl+p2  # pl.__add__ (p2)
p1-p2  # pl.__sub__(p2)
p1*p2  # pl.__mul__(p2)
p1/p2  # pl.__truediv__(p2)
p1//p2 # pl.__floordiv__ (p2)

Other dunder/magic methods in python:

str__() # used to set what gets displayed upon calling str(obj)

#==================================================================================================================
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = Number (1)
m = Number (2)

print(m + n) 

#Output:- 3
"""

#==================================================================================================================
#==================================================================================================================
