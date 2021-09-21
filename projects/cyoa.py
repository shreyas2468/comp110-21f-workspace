"""First Project!"""

__author__ = "730391001"

from random import randint

points: int = 0

player: str = " "

emoji: str = "\U0001F600"


def main() -> None:
    """Starting place for user!"""
    global points
    points = 0

    greet()

    x: int = int(input("Pick a number 1-3 to signify what door you want to pick \n 1) Door 1 \n 2) Door 2 \n 3) Door 3 \n"))

    if x == 1:
        print("Sorry, wrong door")
        bad_ending()
    else: 
        if x == 2:
            print("Sorry, wrong door")
            bad_ending()
        else:
            print("Correct, you get one point! On to the next level")
            points = points + 1
            level_two()   


def level_two() -> None:
    """Level Two."""
    print("Welcome to level two " + player)
    y: int = int(input("Pick a number 1-3 to signify the next door you want to pick \n 1) Door 1 \n 2) Door 2 \n 3) Door 3 \n"))
    global points
    if y == 1:
        print("Sorry, wrong door")
        bad_ending()
    else: 
        if y == 3: 
            print("Sorry, wrong door")
            bad_ending()
        else:
            print("Correct, you get another point! However, this time, you get the chance to answer a question right for an extra three points!")
            print("Now we are gonna give you a random question")
            question = randint(1, 3)
            if question == 1:
                o: str = str(input("Does an Octopus have eight legs? "))
                if (o == "Yes" or o == "Yes" or o == "yes"):
                    points = points + 4
                    print(f'That is correct, now you have {points}!')
                else: 
                    print("Sorry, that is incorrect")
            else:
                if question == 2:
                    q: str = str(input("Does a human have 10 fingers? "))
                    if (q == "Yes" or q == "Yes" or q == "yes"):
                        points = points + 4
                        print(f'That is correct, now you have {points}!')
                    else:
                        print("Sorry, that is incorrect")
                else:
                    h: str = str(input("Can dogs speak english? "))
                    if (h == "Yes" or h == "Yes" or h == "yes"):
                        points = points + 4
                        print(f'That is correct, now you have {points}!')
                    else:
                        print("Sorry, that is incorrect") 
    final_level()


def final_level() -> None:
    """Final Level."""
    global points
    print("Welcome to the final level " + player)
    z: int = int(input("Pick a number 1-2 to signify the last door you want to pick \n 1) Door 1 \n 2) Door 2 \n"))

    if z == 1: 
        print("Sorry, wrong door")
        bad_ending()
    else:
        print("Correct, you get another 10 points!")
        points = points + 10
        ending()


def ending() -> None:
    """End of Game."""
    global player
    global points
    a: str = str(input("Congrats, " + player + ", you scored " + str(points) + " points. Do you want to play again? "))

    if (a == "Yes" or a == "Yes" or a == "yes"):
        main()
    else:
        print("Alright, hope you had fun, have a good rest of your day! " + emoji)


def bad_ending() -> None:
    """Game Over."""
    g: str = str(input("Do you want to play again? "))
    if (g == "Yes" or g == "Yes" or g == "yes"):
        main()
    else:
        print("Alright, hope you had fun, have a good rest of your day! " + emoji)


def greet() -> None:
    """Greeting the player!"""
    print("Hello, I hope you are doing well! " + emoji)
    global player
    player = input("What is your name or a nickname that we can call you? ")
    print("Hey " + player + ", welcome to the guess the correct door game, hope you enjoy!")


if __name__ == "__main__":
    main()