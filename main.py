from random import *


def main():

    print("Welcome to number guessing game")


while True:

    random_number = randint(1,10)
    guess = int(input("Please enter a number 1-10"))
    if guess == random_number:

        print ("You win!")

        break

    else:
        
        print (f"you lost the correct number was {random_number}")


main()