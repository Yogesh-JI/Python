i=9
while i>8:
    x=int(input('enter total class:'))
    y=int(input('enter the number of class you attend:'))
    percentage=(y/x)*100
    if percentage >= 75:
        print('you are eligible to write the exam')
    else:

        print("sorry you cant sit in exam")    
    