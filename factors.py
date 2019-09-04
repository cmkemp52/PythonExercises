#This finds the factors of a user inputted number

num = int(input("Please give a number "))

factors = []

while(num>1):
    test = 2
    while(num>1):
        if(num%test==0):
            factors.append(test)
            num = int(num/test)
        else:
            test+=1

print(factors)
