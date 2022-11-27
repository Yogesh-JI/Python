# ()
# ordered
# immutable
# duplication of elements allowed
# non homogenes


m=(1,2,3,4,5)
print(len(m))

tup=('tuple',)     #for single value tuple adding comma is mandatory


duke=('gosh',23,10.23,'bone')
print(duke[3])


print(type(duke))      # to know about collection/data type
like=list(duke) 
like.insert(3,'push')    
duke=tuple(like)   
print(duke)
  
tp=(10,20,30,40,50)  # converting tuple into  list so we can make change in it
pt=list(tp)
pt.reverse()
print(tuple(pt))

name='yogesh'
t=[]
for i in name:
    t.append(i)
g=tuple(t)    
print(g)


n=('yogesh',)
print(n)

del (tup)       #deleting a tuple
print(tup)

tuple1=('ergeg',6554654,'wefrgwefg',4564.023)
rep=('gg','gwegwee',6546,5665,)    
gf=tuple1+rep                                    #adding/concatination of two tuple
print(gf)