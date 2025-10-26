"""                                              
       Lists in Python
    ________________________

A built-in data type that stores set of values

It can store elements of different types (integer, float, string, etc.)
----------------------------------------------------------------
marks = [   87    ,    64     ,    33    ,    95   ,   76   ]
#        marks[0] , marks[1]  ,  marks[1] ,marks[1], marks[1]
----------------------------------------------------------------------------------------------
student = ["bin”, 20, "kathmandu”] # we can store multiple types of data in a single list
-----------------------------------------------------------------------------------------------
student[0] = “binod” #allowed in python

len(student)  #returns length 

#_________________________________________________________________________

marks=[94.4,55.9,77.9,77.8,48.3]
print (type(marks))

# Output : <class 'list'>
#-------------------------------------
marks=[94.4,55.9,77.9,77.8,48.3]
print (marks[0])
print (marks[1])

# Output : 94.4
#          55.9
--------------------------------------
"""
"""
                                                 ____________________
                                                 |Strings  |immutable|
                                                 |-------------------
                                                 |List     |mutable  |
                                                 |___________________|
                            
#String is immutable: A string is immutable, meaning its value cannot be changed after creation.

            str ="hello"
            print(str[0])
            str[0]="i"

            Output:- TypeError: 'str' object does not support item assignment
                            
#----------------------------------------------------------------------------------------
#List is mutable:- meaning its elements can be changed, added, or removed after creation.


student = ["dragup", 99.99, "kathmandu", "nepal"]
print(student[0])
student[0] = "bin"
print(student)

#Output:-  dragup
#          ['bin', 99.99, 'kathmandu', 'nepal']

"""
#____________________________________________________________________________
"""
# List Slicing
    Similar to string slicing
#----------------------------------------------------------------------
 #   list_name[starting_idx : ending_idx ] #ending idx is not included
#-----------------------------------------------------------------------
#        0 , 1 , 2 , 3 , 4
marks = [87, 64, 33, 95, 76]
print(marks[1:4])

# Output :- [64,33,95]
#-------------------------------
#        0 , 1 , 2 , 3 , 4
marks = [87, 64, 33, 95, 76]
print(marks[ :4])

# Output :- [87,64,33,95]
#[ :4] -- automatically starting index count 0
#-------------------------------

#        0 , 1 , 2 , 3 , 4
marks = [87, 64, 33, 95, 76]
print(marks[1: ])

# Output :- [64,33,95,76]
#[1: ] -- automatically ending index count last

#-------------------------------

#        -5, -4 , -3 , -2 , -1
marks = [87,  64,  33,  95, 76]
print(marks[-3:-1])


# Output :- [33,95]

#__________________________________________________________________

#List Methods
----------------

list = [2, 1, 3]
-------------------
#list.append(4) #adds one element at the end [2, 1, 3, 4] 

list = [2,1,3]
list.append(4)
print(list)

#OutPut :-  [2,1,3,4]

-------------------------------------------------------------
list.sort() #sorts in ascending order  [1, 2, 3] 
            #sorts in descending order [3, 2, 1]

list = [2,1,3]
list.sort()
print(list)

#Output:- [1,2,3]
----------------------------------------------------------------

#list.sort(reverse=True) #sorts in descending order [3, 2, 1]

list =[2,1,3]
print(list.sort(reverse=True))
print(list)

#Output:- None
#         [3,2,1]
-----------------------------
list =[2,1,3]
list.sort(reverse=True)
print(list)

#Output:- [3,2,1]
-------------------------------
list = ["banana","litchi","apple"]
list.sort(reverse=True)
print(list)

#Output:- ['litchi','banana','apple']
----------------------------------------------------------------

#list.reverse() #reverses list [3, 1, 2]

list= ['a','d','e','f','c','b']
list.reverse()
print(list)

#Output:-  ['b', 'c', 'f', 'e', 'd', 'a']
---------------------------------------------------------

list.insert( idx, el) #insert element at index
#       0,1,2
list = [2,1,3]
list.insert(1,5)
print(list)

#Output:- [2,5,1,3]
-----------------------------------------------------------
#list.remove (0) # removes first occurrence of element
------------------

list = [2,1,3,1]
list.remove(3)
print(list)

# Output:- [2,1,1]
-------------------------------------------------------

#list.pop(idx)#removes element at index

#         0   1   2   3   4   5
list = [  2,  1,  3,  1,  4,  1]
list.pop(2)
print(list)

#Output:- [2,1,1,4,1]

    """