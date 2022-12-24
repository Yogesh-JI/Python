h={
    'name':'yogesh',
    'age':19,
    'percentage':89.9,
    'year':2022
}
print(h.keys())
print(h.items())
print(h.values())

h['age']=34
print(h['age'])

h.update({'age':45})
print(h)
#h.pop('age')
print(h) 


print(h.keys())
print(h.values())
k=h.values()

for i in k:
    print(i)
    print(type(i))