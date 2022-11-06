p=str(input())

def nam (p):
    if len(p)%2==0:
        s=int(len(p)//2)
        print(p[s:])
    else:
        u=int(len(p)//2)
        r=u+1
        print(p[r-1:])    
nam(p)        
    