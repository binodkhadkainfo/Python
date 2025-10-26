"""Conditional Statement

if - elif - else (SYNTAX)


if (condition):
                 Statement 1
                 
                 
elif(condition):
                Statement 2
                
else:
                StatementN
                """
#_________________________________________________________________________

#Traffic Light Code
"""
light=input("Light Colour:")

if(light=="red"):
    print ("STOP")

elif (light=="yellow"):
    print ("LOOK")

elif (light == "green"):
    print ("GO")
else:
    print ("light is damage")

"""
#Nesting
"""
age = int(input("enter your age:"))
if (age>=18):
    if (age>= 40):
        print("you can drive")
    else:
        print("you cannot drive")
else :
    print("youiiii")      

"""