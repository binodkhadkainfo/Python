
"""                      
                                        _______________________
                                        |String  | immutable  |
                                        |Lits    |   mutable  |
                                        |Tuples  | immutable  |
                                        -----------------------

Tuples in Python
-----------------

# A built - in data type that let's us create immutable sequences of values.

tup = (2,1,3,1)
print(type(tup))

# Output:-   <class 'tuple'>
____________________________________________________________________
       0   1   2   3
tup = (2  ,1  ,3  ,1)
print (tup[0])
print (tup[1])

#Output:- 2
#         1

_____________________________________________________________________

tup = (1)
print(tup)
print(type(tup))

# Output :- 1
#          <class 'int>
________________________________________________________________
tup = (1,)
print(tup)
print(type(tup))

# Output :- (1,)
#          <class 'tuple'>
________________________________________________________________
tup = (1.0)
print(tup)
print(type(tup))

# Output :- 1.0
#           <class'float'>
_______________________________________________________________
tup = ("hello")
print(tup)
print(type(tup))

# Output :- hello
#           <class'str'>
______________________________________________________________
tup = ("hello",)
print(tup)
print(type(tup))

# Output :- 'hello'
#           <class'tuple'>
______________________________________________________________
       0   1   2   3
tup = (1  ,2  ,3  ,4)
print(tup[1:3])

# Output:- (2,3)
_______________________________________________________________

# Tuple methods
       0  1  2  3
tup = (2, 1, 3, 1)  
tup.index(el)  # Returns index of first occurrence  
tup.count(el)  # Count & total occurrence  
________________________________________________________________
       0  1  2  3
tup = (1, 2, 3, 4)  
print(tup.index(2))

# Output = 1  
________________________________________________________________
# Using tup.count(element)  
tup = (1, 2, 3, 4, 5)  
print(tup.count(2))  

# Output: 1  
________________________________________________________________
tup = (1, 2, 3, 2, 4, 2, 2, 5, 2)  
print(tup.count(2))  

# Output: 5  
_________________________________________________________________

"""