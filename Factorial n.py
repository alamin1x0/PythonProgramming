n= int(input("Give the value of n:"))
fact=1
if n<0:
    print("Negative number is not Allow")
elif(n==0 or n==1):
    print("Value of factorial 0 or 1 is", fact)
else:
    for i in range(2,(n+1)):
        fact=fact*i
        print("factorial value of n is", fact)
