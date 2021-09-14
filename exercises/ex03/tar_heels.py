"""An exercise in remainders and boolean logic."""

__author__ = "730391001"

i: int = int(input("Enter an int: "))

if (i % 2) == 0 and (i % 7) == 0:
    print("TAR HEELS")
else:
    if (i % 2) == 0:
        print("TAR")
    else:
        if (i % 7) == 0:
            print("HEELS")
        else: 
            print("CAROLINA")