"""Let's Practice
====================
# using for & range()
------------------------------------------------------------------------------------
#Print numbers from 1 to 100.


for va in range(1,101):
    print(va)

------------------------------------------------------------------------------------

Print numbers from 100 to 1.

for car in range(100,0,-1):
    print (car)

------------------------------------------------------------------------------------

Print the multiplication table of a number n.

num =int(input("enter a number"))

for i in range(1,11):
    print(num*i)

_______________________________________________________________________________________
=======================================================================================
---------------------------------------------------------------------------------------
"""
#Write a program to find the sum of first n numbers. (using for loop)
"""
n = int(input("Enter a number: "))

sum = 0
for i in range(1, n + 1):
    sum += i                    # Add each number from 1 to n to the sum

print("Total sum is:", sum)
#__________________________________________________________________________
"""
#Write a program to find the factorial of first n numbers. (using for)
"""
num = int(input("enter a number"))
fact =1
for i in range(1,num+1):
    fact *=num
    print("factorial is:",fact)
"""
#__________________________________________________________________________
#Write a program to find the sum of first n numbers. (using for while)
"""
num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum += i  # Add i to sum
    i += 1    # Increment i for the next iteration

print(sum)
"""
#___________________________________________________________________________
#Write a program to find the factorial of first n numbers. (using while loop)
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1

print("factorial =",fact)
