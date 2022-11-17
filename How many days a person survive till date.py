class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

monthDays = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

def countLeapYears(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
    return (n2 - n1)

a=int(input("Enter valid Date of Birth:"))
b=int(input("Enter valid Month of Birth:"))
c=int(input("Enter valid Year of Birth:"))
d=int(input("Enter current Date:"))
e=int(input("Enter current Month:"))
f=int(input("Enter current Year:"))
dt1 = Date(a, b,c)
dt2 = Date(d,e,f)

print(getDifference(dt1, dt2), "days")
			
    

			
