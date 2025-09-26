amount= float(input("ener the actual amount"))
resale_amount= float(input("ener the resail amount"))

if (resale_amount > amount):
    cost = resale_amount-amount
    print("total Profit ={0}",format(amount))
else:
    print("No Profit!!!")