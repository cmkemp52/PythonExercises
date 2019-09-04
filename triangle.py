#This creates a triangle based on a user inputted height

height = int(input("How tall should it be? "))

#maxfloor is the maximum number of stars that'll be on the bottom level
maxfloor = (2*height)+1
#currfloor is the number of stars that'll be on the current floor
currfloor = 1

#iterates until it currfloor reaches maxfloor
while(currfloor<maxfloor):
    #prints spaces followed by stars based on which floor is being printed
    print(" "*(int((maxfloor-currfloor)/2)) + "*"*(currfloor))
    #adds 2 stars for the next floor
    currfloor+=2