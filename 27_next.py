
"""  Let's Practice

________________________________________________________________________________________
Store following word meanings in a python dictionary :

table : “a piece of furniture”, "list of facts & figures”
cat : “a small animal”
"""
"""

dictionary ={
    "table":["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}
print(dictionary)
"""
#OutPut: {'table': ['a piece of furniture', 'list of facts & figures'], 
#                      'cat': 'a small animal'}


"""#_______________________________________________________________________________________
 You are given a list of subjects for students. Assume one classroom is required for 1 
   subject. How many classrooms are needed by all students.

“python”, “java”, "C++", “python”, “javascript”,
"java”, “python”, “ava”, "C++”, "C”
"""

subject = {
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
}

print(len(subject))

#Output:-    5
#________________________________________________________________________________________
"""WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one hy one. Use subject name as key & marks as value.
"""
"""
marks = {}
x = int(input("enter a phy number: "))
marks.update({"phy":x})

y =int(input ("enter a math number: "))
marks.update({"math":y})

z = int(input("enter a chem number: "))
marks.update({"chem":z})

print(marks)
"""
#__________________________________________________________________________________________
"""
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)"""
"""
values ={
    ("float",9.0),
    ("int",9),
}

print(values)
"""
#Output:- {('float', 9.0), ('int', 9)}
#__________________________________________________________________________________________







