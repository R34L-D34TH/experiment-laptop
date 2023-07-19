# explore dictionary
my_data = {101:"john", 201:"fionna", 301:"george", 661: "harry"}
print(my_data)

print(min(my_data))
print(max(my_data))
print(sum(my_data))

print(my_data[201])
my_data.pop(201)
print(my_data)

#del my_data[201]
my_data[775]= "leo"
print(my_data)
my_data[775]= "kim"
print(my_data)
del my_data[775]
print(my_data)

columns = ['ldh', 'cdg', 'umb']
population = {}.fromkeys(columns, 1200)
print(population)

items = list (population.items())
print(items)
