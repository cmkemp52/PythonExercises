#This is a "Guess a number" game where users have to guess the randomly generated number

import random
def game():
    print("I am thinking of a number between 1 and 10")
    tries = 5
    answer = random.randint(1,10)
    while(tries > 0):
        guess = int(input("What's the number? "))

        if(answer > guess):
            print("Your guess is too low")
            tries-=1
        elif(answer < guess):
            print("Your guess is too high")
            tries-=1
        else:
            print("You got it!")
            tries = 0


playagain = "yes"

while(playagain == "yes"):
    game()
    playagain = input("Would you like to play again? ")
print("Thanks for playing!")