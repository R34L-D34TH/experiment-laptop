cafe_name = 'John\'s Cafe'
print (cafe_name)

print(len(cafe_name))
print(min(cafe_name))
print(max(cafe_name))


cafe = """John's cafe delight
- Authentic Italian Restraunt"""

print(cafe)

quote =  "Be \nExceptional"
quote1 =  r"Be \nExceptional" #will not read escape character

print(quote)
print(quote1)

names = "john, jim, Jennie, jack, Joe"
print(names)
print(names[1]) # indexing
print(names[-1])
print(names[1:5]) #slicing

new_names = names * 2
print(new_names)
print(names + new_names)
names += ", kia"
print("kia" in names)
print("kia" not in names)

#Strings are immutable

print(names)
names.upper()
print("now:-", names)

upper_case = names.upper()
lower_case = names.lower()

print("Names upper:- ", upper_case)
print("Names lower:- ", lower_case)


s1 = names.capitalize()
s2 = names.title()
s3 = names.swapcase()
s4 = names.replace("j", 'KO')

print(s1)
print(s2)
print(s3)
print(s4)

password = input("Enter your password")

#rstrip(), lstrip()
print("Password:- ", password.strip())

data = "00000000000003020600"
print("data:- ", data.strip('0'))

number = 3.5600000
number = float(str(number).strip('0'))
print(number, type(number))

message = "Vaibhav Bhardwaj"
print(message)
print(message.center(40))
print(message.ljust(50))
print(message.rjust(50))

data = "50"
print(data.zfill(50))

msg = "lift me a little bit"
print(msg.find('tt'))

quote = "search the candle rather than cursing the darkness"

idx1 = quote.find('candle')
idx2 = idx1 + len("candle")
print(quote[idx1 : idx2])

names = "john, jim, Jennie, jack, Joe"

split_names = names.split(", ")
print(split_names)