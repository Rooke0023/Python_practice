#CS50 practice 
#Time Stamp 3:44:00

"""The variable below is a list of dictionaries containing key/value pairs. Imagine the whole thing as a table where the rows are regarded as lists and the column names are the key name of the dictionaries. To simplify, the list is helping us visualize the whole thing as a table."""
students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for student in students:        #iterates over every single item in the "students" variable
    print(student["name"], student["house"], student["patronus"], sep=", ")

