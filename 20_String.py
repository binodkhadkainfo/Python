"""      Strings
      ------------- 
 string is data type that stores a sequences of  characters.

"""
#str1 = "this is string"
#str2 = """this is string"""
#str3 = 'this is \n sting'

#\n for new line and \t for print tab


#Basic Operation
"""
* Concatenation
    "hello"   + "world"     --->  "hello world"  
 ------------------------------------------------------
     str1 = "hello"
     str2 = "boss"
     print (str1+str2) 
       
 ------------------------------------------------------       
* length of str

    len(str)
 ---------------------------------
   first = "binod"
   print(len(first))
"""
#---------------------------------------
# Indexing
"""

b   i    n   o   d
0   1    2   3   4


str = "binod"
print(str[2])

"""
#______________________________________________________________
# Slicing 
"""
Accessing part of a string
---------------------------

str[starting_idx : ending_idx] # ending idx is not included 

str = "ApnaCollege" 
str[1:4] is "pna" 
str[ :4] is same as str[0:4]
str[1: ] is same as str[1:len(str)] 
----------------------------------------
money = "dollars"
print(money[1:4])

# OutPut:- oll
"""
#--------------------------------------
#Slicing
#--------
#Negative Index
#----------------
"""
 A  p  p  l  e
-5 -4 -3 -2 -1 

str = "Apple" 
str[-3:-1] is "pl" 
-----------------------------------
money = "dollars"
print (money[-4:-1])

# OutPut:- lar
"""
#___________________________________________________________________

#String Functions 
#--------------------
"""
str = "I am a coder."
-------------------------
str.endswith("er.") # returns true if string ends with substr 
str.capitalize() # capitalizes 1st char 
str.replace(old, new) # replaces all occurrences of old with new 
str.find(word) # returns 1st index of 1st occurrence 
str.count("am") # counts the occurrence of substr in string 

------------------______________________________-------------

str.endswith("er.") # returns true if string ends with substr 

str = "I am studying python from Youtube"
print(str.endswith("ube"))
 

Output : True

str = "I am studying python from Youtube”
print(str.endswith("app")) 

Output : False

----------------------____________________----------------------

str.capitalize() # capitalizes 1st char 

str = "i am studying python from Youtube"
print(str.capitalize())
print(str)

Output : I am studying python from Youtube
         i am studying python from Youtube

# str.capitalize() returns a new string with the first 
         character capitalized — it doesn’t modify the original string

                 
str = "i am studying python from Youtube"
str = str.capitalize()
print(str)

Output : I am studying python from Youtube

#If you want to keep the change, you’d need to reassign it.
-------------------_____________________---------------------

str.replace(old, new) # replaces all occurrences of old with new
-------------------------

str = "i am studying python from Youtube"
print(str.replace("o", "a"))

Output:-  i am studying pythan fram Yautube
----------
str = "i am studying python from Youtube"
print(str.replace("python", "java"))

Output:-  i am studying java fram Yautube

--------------___________________________---------------------
str.find(word) # returns 1st index of 1st occurrence

str = "i am from studying python from Youtube"
print(str.find ("o"))

Output :- 7
--------------
str = "i am from studying python from Youtube"
print(str.find ("z"))

Output :-   -1 # -1 is an unvalid index

-----------------___________________________------------------

str.count("am") # counts the occurrence of substr in string 
------------------

str = "i am from studying python from Youtube"
print(str.count ("o"))

Output:- 4 
_____________________________________________________________
"""