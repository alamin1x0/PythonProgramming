digit=int(input("enter an integer number: "))
temp=digit
sum=0
while(temp!=0):
    r=temp%10
    sum=sum*10+r
    temp=temp/10
if(digit==sum):
    print("true")
else:
    print("false")
