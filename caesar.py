num = int(input("By how many?: "))
st = list((input("Give a string to be cyphered: ")).lower())


newst = ""
for letter in st:
    if(letter == " "):
        newst = newst+" "
    else:
        curr = ord(letter)+num
        if(curr>122):
            curr-=26
        newst = newst+str(chr(curr))


print(newst)