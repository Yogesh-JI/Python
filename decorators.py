

def div(a,b):
    print(a/b)


def newdiv(func):
    def innerfun(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfun
div=newdiv(div)  
div(2,4)             