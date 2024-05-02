# Empty dictionary
students = {}

# Dictionary with key-value pairs
students = {"Ali":25, "Ram":27, "Aima":8}
print(students)

age = students["Ram"]
print(age)

# Key along with its associated value is deleted
del students["Aima"]

print(students)

print(students.items())
print(students.keys())
print(students.values())


# Empty dictionary
stud = {}

# A dict can store multiple values in a list form
studs = {
     "Ali":["ID001",26,"A"],
     "Ram":["ID002",30,"B"],
     "Aima":["ID003",29,"C"]
     }

print(studs["Ram"])

print(studs["Ram"][0])
print(studs["Aima"][1:3])


# A dict can store multiple values in a dict form
# so u don't have to remember order can access
# via keys itself

studs1 = {
     "Ali":{"id1" : "ID001", "age" : 26, "grade" : "A"},
     "Ram":{"id1" : "ID002", "age" : 30, "grade" : "B"},
     "Aima":{"id1" : "ID003", "age" : 29, "grade" : "C"}
     }

print(studs1)

print(studs1["Ali"]["age"])

print(studs1["Aima"]["id1"], studs1["Aima"]["grade"])




    
     
