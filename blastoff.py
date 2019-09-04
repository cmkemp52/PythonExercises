#Counts down to blast off based on the number given by the user

import time

num = int(input("Please give a number: "))

if(num>20):
    print("Too large!")
else:
    while(num!=0):
        print(num)
        time.sleep(1)
        num-=1
    print("Blast off!!!")
