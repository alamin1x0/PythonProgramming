import math
a =int(input("Give the value of a:"))
b =int(input("Give the value of b:"))
c =int(input("Give the value of c:"))
d=(b*b)-(4*a*c)
if d==0:
    x=-b/(2*a)
    print("Roots is equal=",x)
elif d>0:
    x1=-b+math.sqrt(d)/(2*a)
    x2=-b-math.sqrt(d)/(2*a)
    print("Roots are:", x1,x2)
else:
    print("Roots are Imaginary")
    
    

      
