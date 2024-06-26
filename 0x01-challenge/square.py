#!/usr/bin/python3
"""Perfect square."""


class Square():
    """
    Square class

    Attributes:
        width: int
        hight: int
    """

    def __init__(self, width=0, height=0):
        """
        Initialize square width and height.

        Attributes:
            width: int
            height: int
        """
        try:
            self.width = int(width)
            self.height = int(height)
        except ValueError as e:
            self.width = 0
            self.width = 0

    def area_of_my_square(self):
        """
        Area of the square.

        Returns:
            int: the area of the square
        """

        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Perimeter of the square.

        Returns:
            int: perimeter of the square
        """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        String representation.

        Returns:
            str: string representation of square
        """

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
