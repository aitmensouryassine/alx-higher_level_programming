#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Creates a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is not None:
                        self.id = arg
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
                idx += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        attrs = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
