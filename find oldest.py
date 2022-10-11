print ('enter 0 for oldest and  1 for youngest')
t=str(input('enter your choice:'))
goodu=int(input('enter your age:'))
lazy=int(input('enter your age:'))
murga=int(input('enter your age:'))
if t==Y:
    
    if goodu>lazy and goodu> murga:
        print(' goodu is oldest')
    elif lazy> goodu and lazy>murga:
        print('lazy is oldest')    
    elif murga>goodu and murga>goodu:
        print('murga is oldest')


else:

    if lazy< goodu and lazy<murga:  

       print(' lazy is youngest')  
    elif goodu<lazy and goodu< murga: 
       print(' goodu is youngest') 
    elif murga<goodu and murga<goodu:
       print(' murga is youngest')  
      