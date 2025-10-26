"""  Types of Operators
_________________________

An operator is a symbol that performs a certain operation between operands.


Arithmetic Operators (+, -, *, /, %, **)
Relational/Comparison Operators (==, !=, >, <, >=, <=)
Assignment Operators (=, +=, -=, *=, /=, %=, **=)
Logical Operators (not, and, or)
"""
#___________________________________________________________________________

#   Arithmetic Operators (+, -, *, /, %, **)
#  _____________________________________________
"""
a = 5
b = 2  
print(a + b)
print(a - b)  
print(a * b)
print(a / b)  
print(a % b)  # Modulo operator # remainder  
print(a ** b) # Power operator #a raised to the power of b = a^b

#____________________________________________________________________________
"""
#    Relational Operators  (==, !=, >, <, >=, <=)
#  ________________________________________________
"""                            ---------------------------
                            | math    | a = b  | a≠b  |
                            ---------------------------
                            | python  | = =    | !=   |       <-- not
                            ---------------------------

a = 50  
b = 20  
print(a == b)    # False  
print(a !- b)    # True  
print(a >= b)    # True  
print(a  > b)     # True  
print(a <= b)    # False  
print(a  < b)     # False  

#______________________________________________________________________________
"""
#Assignment Operators     (= , += , -= ,*= , /= , %= , **=)
"""#______________________
num = 10
num = num+10
print("num:", num)       #Output : 20
-----------------------------------------------
num = 10
num += 10
print("num:", num)  #Output : 20
-----------------------------------------------
num = 10
num -= 10
print("num:", num)  #Output : 0
-----------------------------------------------
num = 10
num *= 5
print("num:", num)  #Output : 50
-----------------------------------------------
num = 10
num /= 5
print("num:", num)  #Output : 2
-----------------------------------------------
num = 10
num %= 5  #using modulo
print("num:", num)  #Output : 0     #remander
-----------------------------------------------
num = 10
num **= 5
print("num:", num)  #Output : 1,00,000

"""

#___________________________________________________________________________

   #Logical Operators (not, and, or)
#______________________________________
""" 
                                            ___________________________
                                            | example :-              |
                                            |------------             |
                                            |print(not False)         |
                                            | Output :- True          |
                                            |__________________________
                                            |print (not True)         |
                                            |Output :- False          |
                                            |__________________________

a = 50
b = 30
print (not True)
print (not False)

Output:- False
         True
         
-----------------------

val1 = True
val2 = True 
print( "and Operator: ", val1 and val2)

Output :- and Operator:True
-----------------------------------------
val1 = True
val2 = False 
print( "and Operator: ", val1 and val2)

Output :- and Operator:False
------------------------------------------
val1 = True
val2 = False
print("OR Operator :",val1 and val2)

Output :- and Operator:True

"""
#___________________________________________________
#Type Casting
#-------------
"""
a = 1
b = "2"
c = int(b)
sum = a+b
print(sum)

Output :- 3
"""