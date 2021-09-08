"""Repeating a beat in a loop."""

__author__ = "730391001"


b: str = str(input("What beat do you want to repeat? "))
n: int = int(input("How many times do you want to repeat it? "))
s: str = ""
if n <= 0:
    print("No beat...")
while n > 0:
    s = s + b + " "
    n = n - 1
print(s)