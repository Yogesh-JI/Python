num=int(input('enter any number:'))
n,m=0,1
sum=0
for i in range(0,num):
    print(sum)
    sum=n+m
    n=m
    m=sum
    