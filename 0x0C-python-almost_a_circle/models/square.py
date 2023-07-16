#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is not None:
                        self.id = arg
                    else:
                        self.__init__(self.width, self.x, self.y)
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
                idx += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
