list1=["India","USA","Australia","UK"]
list2=["Pune","New York","Sydney","London","Melbourne"]

total_cost=[45,67,65,87]
sale_price=[55,77,89,76]
s=zip(list1, list2)
print(list(s))

for x,y in zip(list1, list2):
    print(x,y)

for x,y in zip(total_cost,sale_price):
    print(y-x)

for x,y in zip(list1,list2):
    print(y,x)