from datetime import date
a=(input("Enter DOB: "))
y=int(a[4:])
m=int(a[2:4])
d=int(a[:2])
DOB=date(y,m,d)
todaydate=input("Enter today's date: ")
yy=int(todaydate[4:])
mm=int(todaydate[2:4])
dd=int(todaydate[:2])
Today=date(yy,mm,dd)
l=Today-DOB
print(l.days)
