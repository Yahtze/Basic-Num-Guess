import random
guessNum = random.randint(1,10)
chances = 3
while (chances!=0):
    guessUser = input("Guess A Number Between 1 And 10: ")
    if guessUser.isdigit():
        if (guessUser>10 or guessUser<0):
            print("Enter Number In Given Range")
            continue
        else:
            if (guessUser == guessNum):
                print(str(guessNum) + " Is The Correct Number!")
                break
            else:
                print("Wrong. You have " + str(chances-1) + " Chances Left")
            chances-=1
    else:
        print("Enter An Integer Bobo")

