year= int(input("Give the value of year:"))
if((year%4==0 and year%100==0) or (Year%400==0)):
    print("This is a leap year")
else:
    print("This is not leap year")
