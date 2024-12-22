sum=0
while True:
    num=int(input("Enter the number:"))
    sum+=num*num
    ask=input("Do you want to continue?")
    if ask !='n' and ask!='N' :
        continue
    else: break
print(f"The sum of all the squares entered by the user is {sum}")