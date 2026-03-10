"""
# File opening modes in Python

r  - open the file for reading (default mode)

w  - open the file for writing
     (creates a new file or overwrites existing content)

a  - open the file for appending
     (adds new content at the end of the file)

+  - open the file for updating
     (allows both reading and writing)

rb - open the file for reading in binary mode
     (used for images, videos, etc.)

rt - open the file for reading in text mode
     (this is the default text mode)

f = open("file.txt", "r")   # read text
f = open("file.txt", "w")   # write text
f = open("file.txt", "a")   # append text
f = open("image.jpg", "rb") # read binary file
"""
#===========================================================================================
# Open the file named "file.txt"
f = open("41_myfile.txt", "r") # "r" means read mode (this is the default mode in Python)
data = f.read()
print(data)
f.close()


