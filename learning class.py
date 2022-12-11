class laptop:

    def __init__(self):
        self.name='asus'
        self.processor='19'

    def printop(self):
        print('my laptop is '+self.name,'and the processor is',self.processor)


    # def conf(self):
    #     print(14,45,56,'you')

r1=laptop()

# laptop.conf()
r1.printop()



class laptop:

    def __init__(self,name,processor):
        self.name=name
        self.processor=processor

    def printop(self):
        print('my laptop is '+self.name,'and the processor is',self.processor)

r=laptop('hp','i9')
r.printop()



class identity:

    def __init__(person,n,r):
        person.name=n
        person.number=r

    def printop(person):
        print('my name is ',person.name,'and the number is',person.number)

f=identity('yogesh',69)
f.printop()




class person:
    def __init__(self):
        self.name='shubham'
        self.age='18'
    def update(self,name):
        self.name=name
    def compare(self,other):
        if self.age==other:
            return True
        else:
            return False
person1=person()
person2=person()
person2.compare('18')
# print(person1.name)
# print(person2.name)
if person1.compare(person2):
    print('true')
else:
    print('False')





class car:
    def __init__(self,brand,mil):
        self.brand=brand
        self.mil=mil

car1=car('bmw',15)   
car2=car('tata',10)       

print(car1.brand)
print(car2.brand)





class student:
    def __init__(self,mk1,mk2,mk3):
        self.web=mk1
        self.python=mk2
        self.math=mk3
    def average(self):
        d=(self.web+self.python+self.math)/3
        print(d)

s1=student(5,4,3)
s2=student(7,8,9)
s3=student(1,6,9)

s1.average()
s2.average()
s3.average()



