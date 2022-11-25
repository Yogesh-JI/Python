import random
print('WE ARE HERE TO PLAY A GAME.first computer is going to choose a number from 1 to 6 then you,if your '
'choosen number matches with the number choosen by computer you WIN otherwise you LOOSE.')

print('type Y if you wanna play further else press N')

us=0
pcs=0
pc=random.randint(1,6)
fn=int(input('enter a number: '))
if fn in range(1,7): 
    print('the number choosen by pc is:',pc)
    if fn==pc:
        print('congrants you win')
        us+=1
    else:
        print('you loose ')
        pcs+=1    
else:
    print('please enter a number between 1 to 6 ')

while True:
    q=input('wanna play one more time: ')
    if q=='y'or q=='Y'or q=='n' or q=='N':
        if q=='Y' or q=='y':
            u=int(input('input a number from 1 to 6:  '))
            if u in range(1,7):
                print('number choosen by pc: ',pc)
                if pc==u:
                   us+=1
                   print('congrants you win')
                else:
                   pcs+=1
                   print('you are loosing dear')
            else:
                print('please enter a number between 1 to 6 ')       
        elif q=='n' or q=='N':
           print('sad to see you go')
           break
    else:
        print('please respond according to instructions')    
        
if us>0 or pcs>0:
    print('your total score is:',us)   
    print('PC total score is:',pcs)     
else:
    print('You dont even played')     
            