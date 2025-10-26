"""
Loops in Python
Loops are used to repeat instruction.
=============================================
while Loops
=========================
    while condition:
        #some work 
"""
#___________________________________________________________________________________
"""
#print numbers from 1 to  5
count = 1

while count<=5:
    print("hello",count)

    count +=1

    #OutPut:-  hello1
               hello2
               hello3
               hello4
               hello5
"""
#____________________________________________________________________________________________
"""
#print numbers from 1 to 9
count = 1
while count<=9:
    print("hi",count)

    count = count+1

    #OutPut:-  hi1
               hi2
               hi3
               hi4
               hi5
               hi6
               hi7
               hi8
               hi9
    """
#___________________________________________________________________________________________
"""
# print numbers from 1 to 8
count = 1

while count<=8:
    print(count)

    count = count+1
    
    #OutPut:-  1
               2
               3
               4
               5
               6
               7
               8
               9
"""
#________________________________________________________________________________________
"""
#print numbers from 5 to 1
count = 5

while count >= 1:
    print ("count down number :",count)
    count = count-1

    #OutPut: 5
             4
             3
             2
             1
    
    """
#___________________________________________________________________________________________
"""
#using while loop and multiplied by 2

n = int(input("enter a number:"))
i = 1

while i<=10:
    print(n*i)

    i = i+1

"""
#___________________________________________________________________________________________
"""
 Break & Continue
#======================

Break : used to terminate the loop when encountered.
---------------------------------------------------------

i = 1

while i<=9:
    if (i==3):
        break
    print (i)

    i += 1

    #OutPut:- 1
              2
-------------------------------------------------------------
Search for a number x in this tuple using loop and break:
[1,4, 9, 16, 25, 36, 49, 64, 81,100]


nums = (1,4, 9, 16, 25, 36, 49, 64, 81,100)

x=int(input("enter a number"))
i = 0
while i< len(nums):
    if (nums[i]==x):
        print ("Found at Idx:",i)
        break

    else:
        print ("finding..")


    i +=1

#      OutPut:- enter a number4

#               finding..
#               Found at Idx: 1
#____________________________________________________________________________________________

Continue : terminates execution in the current iteration & continues execution of the loop
with the next iteration.

i = 1

while i<=5:
    if(i==3):
        i +=1
        continue #skip
    
    print(i)
    i +=1
---------------------------------------------------------------------------

# print Odd numbers
i = 1

while i<=5:
    if(i%2==0):
        i +=1
        continue #skip
    
    print(i)
    i +=1

#   OutPut:- 1
#            3
#            5
    
#-------------------------------------------------------------

# print Even numbers
i = 1

while i<=8:
    if(i%2 !=0):
        i +=1
        continue #skip
    
    print(i)
    i +=1

#   OutPut:- 2
#            4
#            6
#            8

#____________________________________________________________________________________________
"""
