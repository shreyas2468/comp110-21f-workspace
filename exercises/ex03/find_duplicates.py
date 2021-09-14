"""Finding duplicate letters in a word."""

__author__ = "730391001"

word: str = str(input("Enter a word: "))
dup: bool = False
i: int = 0
while i < len(word):
    counter: int = 0
    dupcounter: int = 0
    while counter < len(word):
        if word[i] == word[counter]:
            dupcounter = dupcounter + 1
        if dupcounter >= 2:
            dup = True
        counter = counter + 1
    i = i + 1
print("Found duplicate: " + str(dup))
