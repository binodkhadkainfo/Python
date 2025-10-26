#Let's Practice
"""
# Write a  Program to ask the user to enter names of their 
# 3 favorite movies & store them in a list

movies = []  
movies.append(input("Enter the first movie: "))  
movies.append(input("Enter a second movie: "))  
movies.append(input("Enter a third movie: "))  
print(movies)  

#Output:
# Enter the first movie: KGF
# Enter a second movie: PUSPA
# Enter a third movie: LOVE YOU
# ['KGF', 'PUSPA', 'LOVE YOU']

#___________________________________________________________________
# Program to check if a list contains a palindrome sequence

list1 = ["r", "a", "c", "e", "c", "a", "r"]  
copy_list1 = list1.copy()  
copy_list1.reverse()  

if (copy_list1 == list1):  
    print("Palindrome")  
else:  
    print("NOT Palindrome")  


#  Output: Palindrome

# A Palindrome is a word,phrase,number,or sequence that reads the same forward and backward
#______________________________________________________________________________

# WAP to count the number of students with the “A” grade in the following tuple.

#        ["C" , "D" , "A" , "A” , "B" , "B" , "A"]
grade = ("C","D","A","A","B","B","A")
print (grade.count("A"))

#Output :-  3
#_______________________________________________________________________________
#Store the above values in a list & sort them from “A” to “D”.

#        ["C" , "D" , "A" , "A” , "B" , "B" , "A"]

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)

# Output:- ['A', 'A', 'A', 'B', 'B', 'C', 'D']

"""