
def count(*ok):
    odd=0
    even=0
    for i in ok:
        if i%2==0:
            even+=1
            
        elif i%2==1:
            odd+=1  
    print(even) 
    print(odd)
count(32,21,64,100,13)        




