"""Counting letters in a string."""

__author__ = "730391001"

letter = input("What letter do you want to search for? ")
word = input("Enter a word: ")
count = 0
i = 0
while(i < len(word)):
    if(word[i] == letter):
        count = count + 1
    i = i + 1
print("Count:" + " " + str(count))