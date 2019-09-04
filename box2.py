#This creates a box based on user inputted parameters

height = int(input("How tall is the square:"))
width = int(input("How wide is the square:"))
i = 0

while(i < height):
    if(i==0 or i==height-1):
        print("* "*width)
    else:
        print("* " + "  "*(width-2) + "*")
    i+=1
