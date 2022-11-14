n=int(input())
i=1
h=0
b=n
while n>0:
    if i%2==0:
        h+=i
        n-=1
    i+=1
a=h/b      
print('{:.2f}'.format(a))    