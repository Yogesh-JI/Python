j=int(input('enter the range:'))
def loop(n):
    s=''
    for i in range(2,n+1):
       for j in range(i-1):
        s+=str(j+2)+' '
       print(s)
       s=''    
loop(j)