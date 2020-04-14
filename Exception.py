# a = int(input("Enter the Number:"))
# result = a/2
# print(result)

# text = "sakib"
# print(text[3])
# print("Done")

try:
    list = [20,10,15]
    reslut = list[1] / list [0]
    print("Done")
except ZeroDivisionError:
    print("Not Found")