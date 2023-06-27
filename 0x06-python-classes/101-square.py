#!/usr/bin/python3
""" Square module """


class Square:
    """ Creates a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Init square attributes """
        self.size = size
        self.position = position

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
    def position(self, value):
        """ sets the position of the square """
        if len(value) != 2 or not isinstance(value, tuple) \
                or not all((isinstance(n, int) and n >= 0) for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ Print square using # symbol """
        if self.size == 0:
            print()
        else:
            x, y = self.position

            for line in range(0, y):
                print()
            for i in range(0, self.size):
                for k in range(0, x):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print()

    def __str__(self):
        """ Define the print() representation of a Square """
        if self.size != 0:
            x, y = self.position

            for line in range(0, y):
                print()
            for i in range(0, self.size):
                for k in range(0, x):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                i != self.size - 1 and print()
        return ""
