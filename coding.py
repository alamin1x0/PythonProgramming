check = str(input("Please input any word:"))
mid = len(check)//2
print(len(check))

dis = True
res = -1
for i in range(mid):
    res =res-i
    if check[i] == check[res]:
        continue
    else:
        dis = False
        break

if(dis):
    print("True")
else:
    print("False")