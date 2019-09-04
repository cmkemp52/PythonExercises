total = float(input('Total bill? '))
lvl = input("Level of service? ")
spl = float(input("Split how many ways? "))

if(lvl == "good"):
    print("Tip amount: $%.2f" %(total*0.2))
    tot = total*0.2+total
    print("Total amount: $%.2f" %tot)
    print("Amount per person: $%.2f" %(tot/spl))
elif(lvl == "fair"):
    print("Tip amount: $%.2f" %(total*0.15))
    tot = total*0.15+total
    print("Total amount: $%.2f" %tot)
    print("Amount per person: $%.2f" %(tot/spl))
elif(lvl == "bad"):
    print("Tip amount: $%.2f" %(total*0.1))
    tot = total*0.1+total
    print("Total amount: $%.2f" %tot)
    print("Amount per person: $%.2f" %(tot/spl))