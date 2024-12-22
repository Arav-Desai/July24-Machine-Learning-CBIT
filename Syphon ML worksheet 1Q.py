ask = int(input("Enter the number:"))
num = 1
for i in range(1, ask + 1):
    # num=num*i
    if ask < 1559:
        num = num * i
    else:
        print("result exceeds the storage capacity")
        break
if ask < 1559:
    print(f"The factorial of {ask} is {num}.")