#!/usr/bin/python3
""" Square module """


class Square:
    """ Creates a square """

    def __init__(self, size=0, position=(0, 0)):
        if len(position) > 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return the square area """
        return self.__size ** 2

    @property
    def size(self):
        """ gets the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ gets the position of the square """
        return self.__position

    @position.setter
    def position(self, position):
        """ sets the position of the square """
        if len(position) > 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        if self.area() == 0:
            print()
        else:
            x, y = self.position
            for i in range(0, self.size):
                if y >= 0:
                    for k in range(0, x):
                        print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print()
