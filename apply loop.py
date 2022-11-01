from unittest import skip


num=[12,75,150,180,145]
for i in num:
    if i>150:
        skip
    elif i%5==0:
        print(i)
    elif i>500:
        break   

print(num(1,6,-1))


