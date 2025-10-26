# Recursion
"""---------------
Recursion is a function which calls itself.
tis used to directly use a mathematical formula as function.

Example:
factorial(n) = n x factorial (n-1)


This function can be defined as follows:

def factorial (n)
    if i == 0 or i==1: #base condition with doesn't call the function any further
    return 1
else :
    return n*factorial (n-1) # function calling itself

    """

"""
#recursive function
def show(n):
    if (n==0):
        return
    print (n)
    show(n-1) 

show(100)
"""
"""
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2*1
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1

#(The programmer needs to be extremely careful while working with recursion to ensure
thatthe function doesn't infinitely keep calling self. Recursion is sometimes the most
direct way to code on algorithm.)

factorial(n) = n*factorial(n-1)

factorial(n) = n*factorial(n-1)



def factorial(n):
    if (n==1 or n==0):
        return 1
    return n* factorial(n-1)

n = int(input("enter a number"))
print(f"The factorial of this number is:{factorial(n)}")
"""
#______________________________________________________________________________________________
#----------------------------------------------------------------------------------------------
#==============================================================================================
