e=int(input("number of element you wanna enter:"))
k=[]
for i in range(e):
    k.append(int(input("enter the element:")))
print(k)

for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i]>k[j]:
            k[i],k[j]=k[j],k[i]
print(k)

# The code uses a nested for loop to compare each element with the others and swap them if necessary. The outer loop iterates over the list, while the inner loop compares each element with the others starting from the next index. If the element at index j is smaller than the element at index i, they are swapped. This process continues until the list is completely sorted in ascending order