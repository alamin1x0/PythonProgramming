import math
a =int(input("Give the value of a:"))
b =int(input("Give the value of b:"))
c =int(input("Give the value of c:"))
if (a+b>c and b+c>a and c+a>b):
    s=a+b+c
    Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area is  triangle", Area)

      
