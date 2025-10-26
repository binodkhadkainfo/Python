#Dictionaries in Python 
"""#----------------------
#Dictionaries are used to store data values in key:value pairs 
#They are unordered, mutable(changeable) & don’t allow duplicate keys

dict = {
"name" : "binod", 
"cgpa" : 9.6,
"marks" : [98, 97, 95], 

}
print(dict)
#dict["name”], dict["cgpa”], dict["marks”]
#dict["key”] = “value” #to assign or add new """
#___________________________________________________________________________
"""
info = {
    "key" : "value",
    "subject":["machine learning","AI","Data science"],
    "topic": ("machine","data","files"),
    "name" : "binod",
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    "topics" :("hi","hello")
}    
print(info)

# Output:- {'key': 'value', 'subject': ['machine learning', 'AI', 'Data science'],
#  'topic': ('machine', 'data', 'files'), 'name': 'binod', 'learning': 'coding',
#  'age': 20, 'is_adult': True, 'topics': ('hi', 'hello')}
#____________________________________________________________________________


info = {
    "key" : "value",
    "subject":["machine learning","AI","Data science"],
    "topic": ("machine","data","files"),
    "name" : "binod",
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    "topics" :("hi","hello")
}

info["key"] = "assign"
info["height"] = 5.9
print(info)

# Output:-{'key': 'assign', 'subject': ['machine learning', 'AI', 'Data science'],
#  'topic': ('machine', 'data', 'files'), 'name': 'binod',
#  'learning': 'coding', 'age': 20,
#  'is_adult': True, 'topics': ('hi', 'hello'), 'height': 5.9}

#_______________________________________________________________________________

null_dict = {}     #empty dictnary
null_dict["name"] = "binod"
print (null_dict)

#Output:- {'name': 'binod'}
"""
#_______________________________________________________________________________
"""
#   Nested Dictionaries

#A nested dictionary = is a dictionary inside another dictionary.

student = {
    "name" : "binod",
    "subjects" : {
        "maths" : 98,
        "science" : 100,
        "AI" : 100,
    }
}
print(student)

# OutPut:- {'name': 'binod', 'subjects': {'maths': 98, 'science': 100, 'AI': 100}}
"""
#______________________________________________________________________________

#Dictionary Methods
#----------------------
# myDict.keys() #returns all keys
# myDict.values() #returns all values  
# myDict.items() #returns all (key, val) pairs as tuples
# myDict.get( "key") #returns the key according to value
#myDict.update( newDict) #inserts the specified items to the dictionary
#-------------------------------------------------------------------------
# Dict.keys()
"""
info = {
    "key" : "value",
    "learning" : "coding",
    "age" : 20,
    }

print (info.keys())
"""
# Output:- dict_keys(['key', 'learning', 'age'])
#_____________________________________________________________________

# dict.values()
"""
info = {
    "key" : "value",
    "learning" : "coding",
    "age" : 20,
    }
print(info.values())
"""
# Output:- dict_values(['value', 'coding', 20])
#______________________________________________________________________________

#dict.items()
"""
info = {
    "key" : "value",
    "learning" : "coding",
    "age" : 20,
    }
print(info.items())
"""
# OutPut:- dict_items([('key', 'value'), ('learning', 'coding'), ('age', 20)])
#_______________________________________________________________________________ 
#dict.get ()
"""
info = {
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    }
print(info.get("age"))
print(info.get(""))     #None
"""
# Output:- 20
#          None

#_______________________________________________________________________________ 
#dict.update()

info = {
    "learning" : "coding",
    "age" : 20,
    "is_adult" : True,
    }
info.update ({"city":"kathmandu"})
print(info)

#Output:{'learning': 'coding', 'age': 20, 'is_adult': True, 'city': 'kathmandu'}
#______________________________________________________________________________