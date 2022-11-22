n=int(input('enter the range:'))
s=''
for i in range(2,n+1):
    for j in range(i-1):
        s+=str(j+2)+' '
    print(s)
    s=''    