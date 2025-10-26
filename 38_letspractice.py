"""
#====================================================================================================
1) Create a class "Programmer" for storing information of a few programmers working at Microsoft.

class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
m = programmer("binod", 2000000, 999999)
print (m.name, m.salary, m.pin)
b = programmer("manita",2000000, 999999)
print( b.name, b.salary, b.pin)
#====================================================================================================
2) Write a class "Calculator" capable of finding the square, cube, and square root of a number.

class calculator:
    def __init__(self, n):
            self.n = n

    def square(self):
            print(f"The Square is {self.n*self.n}")

    def cube(self):
            print(f"The cube is {self.n*self.n*self.n}")


    def squareroot(self):
            print(f"The Squareroot is {self.n**1/2}")

a = calculator(4)            
a.square()
a.cube()
a.squareroot()

#====================================================================================================
3) Create a class with a class attribute a; Create an object from it and set 'a' directly using 
                                        the object a=o. Does this change the class attribute?

                                        
class Demo:
    a =4

o = Demo()
print(o.a)  #prints the class attribute because instance attribute is not present

o.a = 0     #Instance attribute is set
print(o.a)          #prints the instance attribute because instance attribute is present

print(Demo.a)       #Prints the class attribute

#====================================================================================================
4) Add a static method in problem 2, to greet the user with "Hello".


class calculator:
    def __init__(self, n):
            self.n = n

    def square(self):
            print(f"The Square is {self.n*self.n}")

    def cube(self):
            print(f"The cube is {self.n*self.n*self.n}")


    def squareroot(self):
            print(f"The Squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("hello boss")
     



a = calculator(4)            
a.hello()
a.square()
a.cube()
a.squareroot()

#====================================================================================================
5) Create a class Train which has methods to book a ticket, get status (number of seats), and get 
                                    fare information of a train running under Indian Railways.

from random import randint

class Train:
    def __init__(self, train_no):
        self.train_no = train_no
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.train_no} from {fro} to {to}")
    
    def getStatus(self):
        pass  # You can define this later

    def getFare(self, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {fare}")


t = Train(98)
t.book("Okhaldhunga", "Lalbandi")
t.getFare("Okhaldhunga", "Lalbandi")


#====================================================================================================
"""
#====================================================================================================








































