n=int(input("Give the value of n:"))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is not prime")
            break
        else:
            print(n,"is a prime number")
                  
      
