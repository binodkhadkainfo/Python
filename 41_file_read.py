# Open the file named "file.txt"
f = open("file.txt", "r") # "r" means read mode (this is the default mode in Python)
data = f.read()
print(data)
f.close()
