#This creates a box based on user inputted parameters

height = int(input("How tall is the square:"))
width = int(input("How wide is the square:"))

iheight = 0
iwidth = 0
line = ""

while(iheight<height):
    while(iwidth<width):
        if(iheight==0 or iheight==height-1):
            line = line+"* "
        elif(iwidth==0 or iwidth==width-1):
            line = line+"* "
        else:
            line = line+"  "
        iwidth+=1
    print(line)
    line = ""
    iwidth = 0
    iheight+=1
    
