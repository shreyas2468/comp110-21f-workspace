"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
d: int = int(input("Depth: "))
i: int = 0
while i < d:
    print(TREE * int(i + 1))
    i = i + 1

    