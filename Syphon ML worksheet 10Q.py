def pro():
    cost=int(input("Enter the cost price:"))
    sell=int(input("Enter the selling price:"))
    inv=sell-cost
    profit={"cost_price":cost,"sell_price":sell,"inventory":inv}
    val=profit.get("inventory")
    print(f"dict:-{profit}")
    if val>0:
        print(f"Total profit:${val}")
    else:
        print(f"Total loss:${val}")

pro()