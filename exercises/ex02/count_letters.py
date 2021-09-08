"""Counting letters in a string."""

__author__ = "730391001"

letter = input("What letter do you want to search for? ")
word = input("Enter a word: ")

i = 0
count = 0
while(i < len(letter)):
    if(letter[i] == word):
        count = count + 1
    i = i + 1

print("Count: ", + count)