n=input("Enter the int number:")
if n.isdigit():
    n=int(n)
    num=0
    count=0
    con=True
    while con:
        n=n/10
        n=int(n)
        count+=1
        if n<1:
            print(f"Total No. of digits of the given number is {count}")
            con=False
else:
    print("The entered value is not a number.")