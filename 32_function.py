#  Functions & Recursions
#=====================================================================================
"""
A function is a group of statements performing a specific task.
----------------------------------------------------------------
def func_name( param1, param2..) :
   #some work
return val
func_name( arg1, arg2 ..) #function call
-----------------------------------------------------------------


When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of times.
#=====================================================================================
#Example of syntax of a function
#---------------------------------
The syntax of function look a follows:

def fun1():
    print("hello")

    The function can be called any numbers of time, anywhere in the program
#=====================================================================================
# Function call
-----------------
Whenever we want to call a function, we put the name of the function followed by
parentheses as follows:

fun1()            #This is called function call.
#=====================================================================================
# Function Defination
------------------------
The part containing the exact set of instruction which are executed durig the function
sell.

Quick Quiz: Write a program to greet a user with “Good day” using functions.
#=====================================================================================
#Types of Function in python
-------------------------------
There are two types of functions in python:

* Builtin functions (Already present in python)
* User defined functions (Defined by the user)

Examples of but in functions includes len), print(), range() etc.
The func1( function we defined is an example of user defined function.
#=====================================================================================
# Functions with Arguments
-------------------------------
A function can accept some value it can work with. We can put these values in the
parentheses.

Afunction can also return value as shown below:
def greet(name):
    gr ="hello"+ name
    return gr

a =greet("binod")

#=====================================================================================
#  Default paremeter value
#-------------------------------
We can have a value as default agdefault argument in a function.

Ifwe specify name = “stranger” in the line contaiping def, this value is used when no
argument is passed.

Example:

    def greet(name = "stranger"):
        #function body
    greet()    #name will be "stranger" in function body (default)
    greet("harry")#    name will be "harry" in function body (passed)

#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------
#=====================================================================================
"""
"""
#Write a program to input from 3 different user for finding average value
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

average =(a+b+c)/3
print(average)

a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

average =(a+b+c)/3
print(average)

a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

average =(a+b+c)/3
print(average)
"""
#------------------------------------------------------------------------------------
#Write a program to input from 5 different user for finding average value

# Function Defination
"""
def man():
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    c = int(input("enter a number:"))

    average =(a+b+c)/3
    print(average)

man()       #Function Call
man()
man()
man()
man()
"""
#==================================================================================
"""
def greet(name):
    gr = "hello " + name  # Added a space after "hello"
    return gr

a = greet("binod")
print(a)  # Output: hello binod
"""
#=====================================================================================
#=====================================================================================
#-------------------------------------------------------------------------------------
#=====================================================================================
#=====================================================================================

"""
def sum(a,b):
   sum = a+b
   print(sum)
   return sum

sum(2,3)

sum(9,5)
"""

#=============================================================================
"""
def triy():
   print("hi")

triy()
triy()

# OutPut:-  hi
#           hi
"""
#=============================================================================
"""
def val():
    print("hello")

new = val()   #Output : hellp
print(new)    #Output : None"""
#=============================================================================
#average of 3 numbers
"""
def average(a,b,c):
    sum = a+b+c
    avg =sum/3
    print(avg)
    return avg

average(3,4,5)
"""
#===========================================================================
#---------------------------------------------------------------------------
"""
Built in Functions                               User defined Functions

print()
len()
type()
range()


"""