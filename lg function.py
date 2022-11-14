def siya(a,b):  #here a nad b are PARAMETERS
    print(a-b)
siya(56,67)    #we pass ARGUMENTS in PARAMETERS


def multi(a,b):
    d=a*b
    return d
c=multi(56,2)   
print(c) 


def name(fn,*ls):
    print('my name:',fn)
    print(fn)
    print(ls)
name('shubham','chaubey','yo')    



def ram(*siya):
    print(siya[0])
ram('ghar','lol',9,0.5,3+5j)    



