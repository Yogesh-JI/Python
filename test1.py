s=str(input())
r=s[::-1]
b=r[0:2]
print(s[0:2]==r[0:2] or s[0:2]==b[::-1])