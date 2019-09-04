touse = list((input("Please give a string to swap: ")).upper())

dictionary = {"A":"4","E":"3","G":"6","I":"1","O":"0","S":"5","T":"7"}
result = ""

check = 0
check2 = 0
for letter in touse:
    for definition in dictionary:
        if(letter==definition):
            result=result+dictionary[definition]
            check+=1
    if(check==check2):
        result=result+letter
        check+=1        
    check2+=1    



print(result)