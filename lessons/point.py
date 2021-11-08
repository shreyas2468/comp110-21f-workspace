"""Example of a Point class."""
from __future__ import annotations

class Point:
    x: float
    y: float

    def __int__(self, x: float, y: float):
        """Initialize a point with its x and y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiples components by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x,y)
        return scaled_point


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
p1: Point = p0.scale(2.0)

print(f"(p1.x), (p1.y)")