#This takes a user inputted number and makes a multiplication table based off of it

num = int(input("Please give a number for multiplication tables: "))

i = 1
x = 1

while(i < num+1):
    while(x < num+1):
        print(f"{i} x {x} = {i*x}")
        x+=1
    x=1
    i+=1

