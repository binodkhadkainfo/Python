#====================================================================================================
#1. Write a program using functions to find greatest of three numbers.
"""
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    
print(greatest(a,b,c))
"""

#====================================================================================================
#2. Write a python program using function to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
"""
# Formula is : fahrenheit = (celsius * 9/5) + 32
# Formula is : celsius = (fahrenheit - 32) * 5/9

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").strip().lower()

if choice == 'c':
    c = float(input("Enter temperature in Celsius: "))
    f = c_to_f(c)
    print(f"{round(f, 2)}°F")
elif choice == 'f':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = f_to_c(f)
    print(f"{round(c, 2)}°C")
else:
    print("Invalid choice! Enter 'C' or 'F'.")

"""
#====================================================================================================
#3. Howdoyou preventa python print() function to print a new line at the end.
"""
print("hi how are you")
print("what are you doing now")
print("i am good,", end=" ")
print("i am reading book", end="")
"""
#====================================================================================================
#4. Write a recursive function to calculate the sum of first n natural numbers.
"""
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(5)=1+2+3+4+5

sum(n) = 1+2+3+4.... n-1+n
sum(n)= sum(n-1)+n
"""
"""
def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

print(sum(4))
"""

#====================================================================================================
#5. Write a python function to print first n lines of the following pattern:
#        ***
#        **                      -for n=3
#        * 

"""
def pattern(n):
    if (n==0):
        return
    print ('*'*n)
    pattern(n-1)

pattern(3)

#OutPut: ***
#        **
#        *   
"""
#====================================================================================================
#6. Write a python function which converts inches to cms.
"""
def inch_to_cms(inch):
    return inch*2.54
n=int(input("Enter value in inches:"))
print (f"The corresponding value in cms is{inch_to_cms(n)}")
"""
#====================================================================================================
#7. Write a python function to remove a given word from a list ad strip it at the same time.

"""
def remove_word_and_strip(word_list, target_word):
    target_word = target_word.strip()
    cleaned_list = []

    for word in word_list:
        stripped_word = word.strip()
        if stripped_word != target_word:
            cleaned_list.append(stripped_word)

    return cleaned_list

    """

#====================================================================================================
#8. Write a python function to print multiplication table of a given number.

"""
def print_multiplication_table(number, up_to=10):
    print(f"\nMultiplication Table of {number}:\n")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

"""


#====================================================================================================
#====================================================================================================
#----------------------------------------------------------------------------------------------------
#====================================================================================================
#====================================================================================================




#Lets Practice
#====================================================================================================
#Write a functions to print the length of a list. (list is the parameter)
"""
ist =["kathmandu","sarlahi","lalbandi","okhadhunga","jymire"]
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(lst):  
    print(len(lst))

print_len(cities)
print_len(heroes)
print_len(ist)

#OutPut:     6
#            4
#            5
"""
#====================================================================================================

#Write a functions to print the elements of a list in a single line. (list is the parameter)
"""
ist =["kathmandu","sarlahi","lalbandi","okhadhunga","jymire"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_list(list):
    for item in list:
        print(item,end=" ")


print_list(ist)
print_list(heroes)
print()

#OutPut:- kathmandu sarlahi lalbandi okhadhunga jymire thor ironman captain america shaktiman 
"""
#====================================================================================================

# Write  a functions to find the factorial of n.(n is the parameter)
"""

def cal_fact (n):
    fact=1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(6)
"""
#====================================================================================================
#Write a functions to convert USD to NPR.
"""
def converter(usd_value):
    nrs_value = usd_value*136
    print(usd_value,"USD=",nrs_value,"NRS")

converter(1)

#OutPut:- 1 USD= 136 NRS
"""
#====================================================================================================