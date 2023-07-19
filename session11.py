numbers = list(range (10, 101, 10))
print(numbers)
print (type(numbers))

numbers.append(30)
numbers.append(77)
numbers.append(95)
print(numbers)

print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(list(reversed(numbers)))
print("index of 50:-", numbers.index(50))
print("repetition of 30:-", numbers.count(30))
data = [70,30,50,90,20]
print("data is:- ", data)
data.sort()
print("data in sorted arrangement:- ", data)

names = ["john", "anna", "sia", "kia", "angel"]
names.sort()
print("Sorted name:-", names)
print(min(names))
print(max(names))
names.remove("sia")
# del names[2]

data= [10,20,30,40,50]
"""
data.pop()
print(data)
data.pop(0) #remove using index number
print(data)
data.clear()
print(data)
"""

# data.insert(len(data), 99)
data.insert(-1, 99)
print(data)


#explore set

john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers)

numbers = list(range(10,101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("numbers now:- ", numbers)
print("numbers type:-", type(numbers))

numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(220)
print("numbers after add:- ", numbers)

numbers.pop()
numbers.pop()
print(numbers)

numbers.remove(50)
numbers.discard(30)
numbers.discard(90)

john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"fionna", "sia", "jack"}
fionna_followers = {"sia","joe"}

followers = john_followers.intersection(jake_followers).intersection(fionna_followers)
print(followers)

print(fionna_followers.issubset(john_followers))
print(john_followers.issuperset(fionna_followers))

A = {1,2,3,4,5}
B = {4,5,6,7,8}

C = A - B
D = A & B
E = A ^ B
F = A | B
G = A.symmetric_difference(B)

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print("symmetric difference:- ", G)

#explore dictionary

my_tuple = ()
print(my_tuple, type(my_tuple))

my_list = []
print(my_list, type(my_list))

my_set = set() # can also be used for other data types list(), dict()
print(my_set, type(my_set))

my_dictionary = {}
print(my_dictionary, type(my_dictionary))