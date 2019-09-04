#This takes a user size input and creates a square of stars based on it

size = int(input("How big is the square:"))

start = 0
sides = 0
line = ""

while(start<size):
    while(sides<size):
        line = line+"* "
        sides+=1
    print(line)
    start+=1


    
