numbers=[1,4,45,564,656,54,48,498,]
print(len(numbers))
print(max(numbers))         #only work when data types are same
numbers.sort()       #arrange list elements in increasing order
print(numbers)
numbers.pop()        #to remove last elements from list
print(numbers)
numbers.reverse()    #to print list in decreasing order
print(numbers)
numbers.append(69)   #to simply insert a value in the last
print(numbers)
numbers.insert(1,45) #first for index second for value
print(numbers)
print(numbers[::2])    #start from zero index and print every second index value(basically the value given in the last)
