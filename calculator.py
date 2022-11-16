d=str(input('what you want to perform:'))
a=int(input('input a number:'))
b=int(input('input a number:'))
def add(a,b):
    print('the result:',a+b)
def sub(a,b):
    print('the result:',a-b)
def multi(a,b):
    print('the result:',a*b)
def div(a,b):
     print('the result:',a/b)   

    
if d=='add'or d=='+':
    add(a,b)
elif d=='sub'or d=='-':
    sub(a,b)  
elif d=='multi' or d=='*':
    multi(a,b) 
elif d=='div'or d=='/':
    div(a,b)         