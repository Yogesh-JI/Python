import math
def add(num1,num2):
    return(num1+num2)
def substract(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)
def modulus(num1,num2):
    return(num1%num2)
def sqrt(num):
    return(math.sqrt(num))
def exponential(num):
    return(math.exp(num))
def sine(num1,num2):
    return(math.sin(math.radians(num1,num2)))
def cos(num1,num2):
    return(math.cos(math.radians(num1,num2)))
def tan(num1,num2):
    return(math.tan(math.radians(num1,num2)))
def degrees(num):
    return(math.radians(num))
def radians(num):
    return(math.degrees(num))




while True:
    next=str(input('wanna do calculation(y/n):'))
    if next=='y' or next =='yes':
        choice=input("enter your choice (1.sum/2.substraction/3.multiplication/4.divide/5.reminder/6.square root of a number/7.exponent of e/8.value of sin/9.value of cos/10.value of tan/11.radian value/12.degree value/:  ")
        print('for example if you to do addition enter 1')
        if choice in ('1','2','3','4','5','6','7','8','9','10','11','12'):
           if choice == '1':
            num1=float(input("enter first num:"))
            num2=float(input("enter second num:"))
            print(num1,"+",num2,"=",add(num1,num2))
           elif choice == '2':
            num1=float(input("enter first num:"))
            num2=float(input("enter second num:"))
            print(num1,'-',num2,'=',substract(num1,num2))
           elif choice == '3':
            num1=float(input("enter first num:"))
            num2=float(input("enter second num:"))
            print(num1,'*',num2,'=',multiply(num1,num2))
           elif choice =='4':
            num1=float(input("enter first num:"))
            num2=float(input("enter second num:"))
            print(num1,'/',num2,'=',divide(num1,num2))
           elif choice == '5':
            num1=float(input("enter first num:"))
            num2=float(input("enter second num:"))
            print(num1,'%',num2,'=',modulus (num1,num2))
           elif choice == '6':
            num1=float(input("enter the number which square root you want:"))
            print(math.sqrt(num1))
           elif choice == '7':
            num1=float(input("enter the power of e:"))
            print(math.exp(num1))
           elif choice == '8':
            num1=float(input("enter the angle of sin:"))
            print(math.sin(math.radians(num1)))
           elif choice == '9':
            num1=float(input("enter the angle of cos:"))
            print(math.cos(math.radians(num1)))
           elif choice == '10':
            num1=float(input("enter the angle of tan:"))
            print(math.tan(math.radians(num1)))
           elif choice == '11':
            num1=float(input("enter the number you want to convert into radians:"))
            print(math.radians(num1))
           elif choice == '12':
            num1=float(input("enter the radian you want to convert into degrees:"))
            print(math.degrees(num1))
        else:
           print("invalid input")
    else:
        break        