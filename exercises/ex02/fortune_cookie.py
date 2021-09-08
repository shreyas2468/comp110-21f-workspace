"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730391001"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

fortune = (randint(1, 4))

if fortune >= 3:
    if fortune == 4:
        print("You will do great on your next quiz")
    else:
        print("Something good will happen to you")
else: 
    if fortune == 2:
        print("You will find the love of your life")
    else:
        print("You will become a millionare")

print("Now, go spread positive vibes!")
