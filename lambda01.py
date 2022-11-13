def square(n):
    n**=2
    print(n)
square(9)    




x=lambda b,n,m:(b+n)*m
num=x(1,5,8)
print(num)
     


def name(x) :
    return lambda a: (a+x )+5 
num=name(10)   
print(num(5))