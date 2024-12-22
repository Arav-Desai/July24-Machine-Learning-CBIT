ask = int(input("Enter the number:"))
num = 1
for i in range(1, ask + 1):
    for j in range(1,i):
        if i < 1559:
            i=i*j
    num = num * i
if i < 1559:
    print(f"The factorial of {ask} is {num}.")