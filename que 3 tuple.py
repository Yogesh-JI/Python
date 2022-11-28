x=int(input('how many input you wanna give:'))
c=[]
for i in range(x):
    name=str(input('enter the name:'))
    c.append(name)

print(tuple(c))   