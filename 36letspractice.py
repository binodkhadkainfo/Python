#    Let's Practice
# --------------------

#===========================================================================================
#Create a new file “practice.txt” using python. Add the following data in it:
"""
Hi everyone
we are learning File 1/0
using Java.
like programming in Java.
#----------------------------------------
with open("practice.txt","w")
    f.write("hi everyone\nwe are learning file I/O\n")
    f.write("usigjava\n i like jave programming")

#========================================================================================"""
#===========================================================================================
#WAF that replace all occurrences of “java” with “python” in above file.
#---------------------------------------------------------------------------
"""
def check_for_word():

    with open("practice.txt","r") as f:
        data=f.read()
    new_data = data.replace("java","python")
    print(new_data)

    with open ("practice.txt","r") as f:
        f.write(new_data)

check_for_word()


        """
#===========================================================================================
#Search if the word “learning” exists in the file or not.
"""word = "learning"
with open("practice.txt","r") as f:
    data =f.read()
    if(data.find(word) !=-1):
        print("Found")
    else:
        print("not Found")"""

#===========================================================================================
#WAF to find in which line of the file does the word “learning”occur first.
#       Print -1 if word not found.

"""
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:  # Use standard quotes here
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()  # Corrected function call
"""


#===========================================================================================

#From a file containing numbers separated by comma, print the count of even numbers.
"""
count = 0  # Start count at 0, since we're counting even numbers
with open("practice.txt", "r") as f:
    data = f.read()
    nums = data.split(",")  # Split the data into a list of numbers as strings
    for val in nums:
        if int(val) % 2 == 0:  # Check if the number is even
            count += 1  # Increment the count for even numbers
    print(count)  # Print the total count of even numbers

"""