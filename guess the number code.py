import random

target = random.randint(1,100)

while True:
    userchoice = input("Take a guess between 1 to 100 or Quit(Q) : ")
    if(userchoice == "Q"):
        break

    userchoice = int(userchoice)

    if(userchoice == target):
        print("You guessed it right!")
        break
    elif(userchoice < target):
        print("Too low, try again!")
    else:
        print("Too high, try again!")
    
print("-----GAME OVER-----")
