#Set in Python
#----------------

#set is mutable but its element is immutable

"""
Set is the collection of the unordered items.
Each element in the set must be unique & immutable.

nums ={1,2,3,4}
set2 ={1,2,2,2}

repeated elements stored only once, so it resolved to {1, 2}
null_set = set() #empty set syntax 
"""
#_____________________________________________________________________________________
"""
collection = {1,2,3,4}
print(collection)
print(type(collection))
"""
#Output:- {1, 2, 3, 4}
#         <class 'set'>
#____________________________________________________________________________________
"""
collection = {1,1,1,2,2,3,4,5,"hello","hello","world"}
print(collection)
print(type(collection))
"""
# OutPut:- {1, 2, 3, 4, 5, 'hello', 'world'}
#          <class 'set'>

#___________________________________________________________________________________
"""collection = set()# the syntax of empty set
print(type(collection))
"""
#Output:- <class 'set'>
#__________________________________________________________________________________
#SET METHODS
#____________
"""{('float', 9.0), ('int', 9)}
set.add( el) #adds an element
set.remove( el) #removes the elem an
set.clear() #empties the set
set.pop() #removes a random value 
set.union( set2 ) #combines both set values & returns new
set.intersection( set2 ) #combines common values & returns new
"""
#___________________________________________________________________________________
""" Using set.add method 

collection = set()
collection.add(1)
collection.add("hi")
collection.add(2)
collection.add(1)
 
print(collection)
"""
#Output:- {1, 2, 'hi'}
#________________________________________________________________________________________

#using set.remove method
#-------------------------
"""
collection = set()
collection.add(1)
collection.add("hi")
collection.add(2)
collection.add(1)
collection.add(5)

print(collection)
 
collection.remove(5)
print(collection)
"""
#Output:- {1, 2, 5, 'hi'}
#         {1, 2, 'hi'}
#_________________________________________________________________________________________
#using set.clear method
"""
collection = set()
cllection.add(1)
collection.add("hi")
collection.add(2)
collection.add(1)
collection.add(5)

print(collection)

collection.clear()
print(collection)
"""
#Output:-  {1, 2, 5, 'hi'}
#          set()

#__________________________________________________________________________________________________________
#using set.pop method which can remove random values
"""
collection = {"hello","hi","who","i","am"}
print(collection)
collection.pop()
print(collection)
"""
#__________________________________________________________________________________________________________

#using set.union( set2 ) #combines both set values & returns new
"""
set1 ={1,2,3}
set2 ={2,3,4}

print (set1.union(set2))
"""
#Output:- {1, 2, 3, 4}
#__________________________________________________________________________________________________________

#using set.intersection( set2 ) #combines common values & returns new\
"""
set1={1,2,3}
set2={2,3,4}

print(set1.intersection(set2))
"""
#Output:- {2, 3}

#__________________________________________________________________________________________________________