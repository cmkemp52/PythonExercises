#Gives user a coin if they want one

coins = 0
print(f"You have {coins} coins")
response = input("Would you like a coin?")

while(response == "yes"):
    coins+=1
    print(f"You have {coins} coins")
    response = input("Would you like another?")

print("bye")
    