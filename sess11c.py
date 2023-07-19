#for each loop

data = list(range(10, 101, 10))

for idx in range (len(data)):
    print (data[idx])

for element in data:
    print(element)

student = {
    "rollno" : 101,
    "name" : "fionna",
    "age" : 21
}

print ("dictionary data")

items =  student.items()

for item in items:
    print(item[0], item[1])

print("dictionary keys only")
keys = student.keys()
for key in keys:
    print("only keys",key)

for key in student:
    print("keys and values:- ", key, student[key])