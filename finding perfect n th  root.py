import math as m
a=int(input())
b=int(input())
def fourth(a,b):
    for i in range(a,b):
        y=(m.sqrt(i))**0.5
        if int(y+0.5)**4==i:
            print(i)
            break
fourth(a,b)        




a=int(input())
b=int(input())
def fourth(a,b):
    for i in range(a,b):
        y=(i)**(1/3)
        if int(y+0.5)**3==i:
            print(i)
            break
fourth(a,b)     


s=str(input())
