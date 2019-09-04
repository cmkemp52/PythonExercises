hotel = {'1': {'101': ['George Jefferson', 'Wheezy Jefferson'],},'2': {'237': ['Jack Torrance', 'Wendy Torrance'],},'3': {'333': ['Neo', 'Trinity', 'Morpheus']}}

def checkroom(floornum, roomnum):
    for rnum in hotel[floornum]:
        if(rnum==roomnum):
            return False
    return True


chk = (input("Check in or check out?: ")).lower()
floor = input("Please enter floor: ")
room = input("Please enter room number: ")

if(chk == "check in"):
    if(checkroom(floor,room)==True):
        guests = int(input("How many guests will be staying?: "))
        guestnames = []
        while(guests>0):
            guestnames.append(input("Please give guest name: "))
            guests-=1
        hotel[floor][room] = [guestnames]
    else:
        print("Room is already occupied")
elif(chk == "check out"):
    if(checkroom(floor,room)==False):
        print("Checking guest out!")
        del hotel[floor][room]
    else:
        print("Room is unoccupied!")
else:
    print("Please follow directions!")

print(hotel)