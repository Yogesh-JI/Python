import functools as fn

l=[654654,4984,948,984654,48,894,55,5,4,8,6548,]
f=list(filter(lambda i:i>15,l))
print(f)
o=list(filter(lambda i:i%2==0,l))
print(o)
h=list(map(lambda toor:toor**2,l))
print(h)
r=str(fn.reduce(lambda x,y:x+y,l))
print(r)


