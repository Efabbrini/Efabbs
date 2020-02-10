import random, sys

while True:
    try:
        print("Please select (E)asy, (M)edium or (H)ard. You make also (Q)uit.")
        difficulty = input()
    except NameError:
        print("Please make a valid selection")
    if difficulty.upper() == "Q" or difficulty.upper() == "Q":
        sys.exit()
    ##Easy difficulty
    if difficulty.upper() == "EASY" or difficulty.upper() == "E":
        ranNumb = int(random.randint(0, 20))
        print("I am thinking of a number between 0 & 20")

        for i in range(1, 10):
            print("Guess an number!")
            guess = int(input())
            if guess > ranNumb:
                print("Your guess is too high!")
            elif guess < ranNumb:
                print("Your guess is too low!")
            else:
                break
    ##Medium difficulty
    if difficulty.upper() == "MEDIUM" or difficulty.upper() == "M":
        ranNumb = int(random.randint(0, 30))
        print("I am thinking of a number between 0 & 100")

        for i in range(1, 10):
            print("Guess an number!")
            guess = int(input())
            if guess > ranNumb:
                print("Your guess is too high!")
            elif guess < ranNumb:
                print("Your guess is too low!")
            else:
                break
    ##Hard difficulty
    if difficulty.upper() == "HARD" or difficulty.upper() == "H":
        ranNumb = int(random.randint(0, 50))
        print("I am thinking of a number between 0 & 50")

        for i in range(1, 10):
            print("Guess an number!")
            guess = int(input())
            if guess > ranNumb:
                print("Your guess is too high!")
            elif guess < ranNumb:
                print("Your guess is too low!")
            else:
                break
    if guess == ranNumb:
        print("Your correct, The number was " + str(ranNumb) + "!")
    else:
        print("Your wrong, The number I was thinking of was " + str(ranNumb) + "!")
