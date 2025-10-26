"""

File 110 in Python
Python can be used to perform operations on a file. (read & write data)
Types of all files

1. Text Files : .txt, .docx, .log etc.

2. Binary Files : . mp4, .mov, .png, .jpeg etc.
---------------------------------------------------------------------------------

Open, Read & Close File
-------------------------

We have to open a file before reading or writing.  

f = open("file_name",     "mode")
              ↓               ↓
          sample.txt      r : read mode  
          demo.docx       w : write mode  



data = f.read()  
f.close()
-------------------------------------------------------------------------------
===============================================================================
_______________________________________________________________________________
"""
"""
#----------------------------------------------------------------------------------------------
f= open("demo.txt","r")
data =f.read()
print(data)
print(type(data))
f.close()
#------------------------------------------------------------------------------------------------------------------

Character                                           Meaning

'r'                                          open for reading (default)

'w'                                          open for writing, truncating the file first

'x'                                          create a new file and open it for writing
 
'a'                                          open for writing, appending to the end of the file if it exists

'b'                                          binary mode

't'                                          text mode (default)

'+'                                          open a disk file for updating (reading and writing)
#------------------------------------------------------------------------------------------------------------------
Reading a file
----------------
data = f.read()                                 #reads entire file
data = f.readline()                             #reads one line at a time
#------------------------------------------------------------------------------------------------------------------
"""
"""
f = open("demo.txt","w")
f.write("i am a coder")
f.close()"""
#------------------------------------------------------------------------------------------------------------------
"""with Syntax
------------------
with open( “demo.txt”, “a") as f:
        data = f.read()
#------------------------------------------------------------------------------------------------------------------
  Deleting a File
----------------------

using the os module

Module (like a code library) is a file written by another programmer that generally has
a functions we can use.

    import os
    os.remove( filename )


"""