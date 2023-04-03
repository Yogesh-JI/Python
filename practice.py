# def gcd(n,m):
#     if m==0:
#         return n
#     else:
#         return gcd(m,n%m)

# n=int (input("enter 1:"))
# m=int (input("enter 2:"))
# print("the result is ",gcd(n,m))

# class nam:
#     def setname(self,name):
#         self.name=name
#     def getname(self):
#         return self.name

# p1=nam()
# p2=nam()

# n=str(input("enter the first name:"))
# p1.setname(n)

# m=str(input("enter the second name:"))
# p2.setname(m)

# print(p1.getname())

# print(p2.getname())


# matrix=[]
# for i in range(3):
#     row=[]
#     for j in range(3):
#         el=int(input(f"enter the elements[{i+1}{j+1}]:"))
#         row.append(el)
#     matrix.append(row)

# p=[print(i) for i in matrix ]

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# num=int(input("enter the number:"))
# print(fact(num))


# def fibonacci(n):
#     # Initialize the first two Fibonacci numbers
#     fib = [0, 1]
    
#     # Calculate the remaining Fibonacci numbers
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib

# print(fibonacci(5))