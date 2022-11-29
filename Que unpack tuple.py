tuple1=(10,20,30,40,50)
(g,*i,j)=tuple1
# print(g)
# print(h)
# print(i)
# print(j)
i=0
while i in range(len(tuple1)):
    print(tuple1[i])
    i+=1

c=tuple(i)
print(c)

