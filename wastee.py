a=input()
f=a.split()
an=[int(x) for x in f]
an.sort()
print(an[0],max(an))