n=int(input())
s=0
for i in range(n):
    for j in range(n,0,-1):
        if i*j==n:
            s+=i
if s==n:
    print('Perfect')
else:
    print('Not Perfect')    