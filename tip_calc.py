total = float(input('Total bill? '))
lvl = input("Level of service? ")

if(lvl == "good"):
    print("Tip amount: $%.2f" %(total*0.2))
elif(lvl == "fair"):
    print("Tip amount: $%.2f" %(total*0.15))
elif(lvl == "bad"):
    print("Tip amount: $%.2f" %(total*0.1))