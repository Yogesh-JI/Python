def nam(*siya):
    co=0
    do=0
    for i in siya:
        if len(i)>5:
            print(i)
            co+=1
        else:
            do+=1
    print('items having length more than 5:',co)  
    print('items haing length less than or equal to five:',do)      
nam('atul','shubham','anurag','rahul','dev','roy')