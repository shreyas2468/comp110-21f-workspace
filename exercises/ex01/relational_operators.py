"""Relational operator program."""

__author__ = "730391001"

lhs: int = int(input("Left-hand side: "))
rhs: int = int(input("Right-hand side: "))
print(str(lhs) + " < " + str(rhs) + " is " + str(bool(lhs < rhs)))
print(str(lhs) + " >= " + str(rhs) + " is " + str(bool(lhs >= rhs)))
print(str(lhs) + " == " + str(rhs) + " is " + str(bool(lhs == rhs)))
print(str(lhs) + " != " + str(rhs) + " is " + str(bool(lhs != rhs)))