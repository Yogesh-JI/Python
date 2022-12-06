# unordered
# immutable(some Exception)
# duplication is not allowed



mset={'car','boat','pool',1,2}
for i in mset:
    if i=='boat':
        print(i)
        break

m2={'sdfgs','sdasf','sfgasd',1,2}
# tople1=('H','E','L','L','O')
# s=''
# for i in tople1:
#     s+=i
# print(s)    

mset.add('hathi')
print(mset)
mset.update(m2)
print(mset)
#mset.pop()
mset.union(m2)
print(mset)
u=mset.intersection(m2)
v=mset.symmetric_difference(m2)
print(u)
print(v)