# Grade Sheet

marks = int(input("Enter Your Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif (marks >= 90 and marks <= 100):
    print("A+")
elif (marks >= 80 and marks < 90):
    print("A")
elif (marks >= 70 and marks < 80):
    print("B+")
elif (marks >= 60 and marks < 70):
    print("B")
elif (marks >= 50 and marks < 60):
    print("C+")
elif (marks >= 40 and marks < 50):
    print("C")
else:
    print("D+")
