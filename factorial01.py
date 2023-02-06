# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)    
# num=fact(8)   
# print(num) 
import math as m
s=int(input())
r=[]
for i in range(s+1):
    c=0
    for j in str(i):
        c+=m.factorial(int(j))
    if c==i:
        r.append(i)
print(r)