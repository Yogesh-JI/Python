salary=int(input('enter your current salary :'))
service=int(input('enter the year of service:'))
if service > 10:
    print('your net bonus will be:',((salary*0.1)+salary))
elif service>6 and service<10:
    print('your net bonus will be:',(salary*0.08+salary))
elif service<6:
         print('your net bonus will be:',(salary*0.05+salary))
