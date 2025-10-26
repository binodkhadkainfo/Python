"""Loops in Python 
===================
while Loops
=========================="""
"""nums = [1,2,3,4,5,6]

for va in nums:
    print (va)

#     Output :-  1
#                2
#                3
#                4
#                5
#                6          """
#_________________________________________________________________________________
"""
st = "binod"

for ca in st:
    print(ca)
"""
#OutPut:-   b
#           i
#           n
#           o
#           d
#__________________________________________________________________________________

# Let's practice
#Print the elements of the following list using a loop:
#[1,4, 9, 16, 25, 36, 49, 64, 81,100]
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter a number:"))

idx =0
for val in nums:
    if val==x:
        print ("Number of Idx is :",idx)
        break

    idx += 1
    
    """
#____________________________________________________________________________________
"""
Range()
============

Range functions returns a sequence of numbers, starting from 0 by default, and increments by
1 (by default), and stops before a specified number.
=============================================================================================

# range(5)    => 0,1,2,3,4 

------------------------------------------------------------------------------------------------


sto = range(5)

for va in sto:
    print(va)

    # OutPut: 0
    #         1
    #         2
    #         3
    #         4 

_________________________________________________________________________________________________   

for va in range(9):                    #range(stop)
    print (va)

for var in range(2,9):                 #range(start,  stop)
    print(var)    

for ca in range(2,20,2):               #range(start,    stop ,    step)
    print(ca)

------------------------------------------------------------------------------------------------

print even numbers 

for ev in range(2,100,2):
    print (ev)
-------------------------------------------------------------------------------------------------

print odd numbers

for od in range(1,100,2):
    print(od)

"""
#===============================================================================================
#_______________________________________________________________________________________________

#Pass Statement
#==================
#pass is a null statement that does nothing. It is used as a placeholder for future code.
"""
for el in range(10):
    #empty             # if you use 'pass' then code will execute
print("hi") 

#OutPut: IndentationError: expected an indented block
# we can use pass 

for el in range(10):
    pass
print("hey")


"""