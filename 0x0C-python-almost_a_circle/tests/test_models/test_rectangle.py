import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):

    def setUp(self):
        Base.reset()
        
    def test_id(self):
        self.assertEqual(Rectangle(4, 5).id, 1)
        self.assertEqual(Rectangle(4, 5, 6, 7, 45).id, 45)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        self.assertEqual(Rectangle(4, 5).width, 4)

    def test_height(self):
        self.assertEqual(Rectangle(4, 5).height, 5)

    def test_x(self):
        self.assertEqual(Rectangle(4, 5).x, 0)
        self.assertEqual(Rectangle(4, 5, 12).x, 12)

    def test_y(self):
        self.assertEqual(Rectangle(4, 5).y, 0)
        self.assertEqual(Rectangle(4, 5, 12, 7).y, 7)


class TestRectangleSettersAndGetters(unittest.TestCase):

    def setUp(self):
        Base.reset()

    def test_set_get_with(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.width, 2)

        r.width = 8
        self.assertEqual(r.width, 8)

    def test_set_get_height(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.height, 4)

        r.height = 10
        self.assertEqual(r.height, 10)

    def test_set_get_x(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.x, 0)

        r1 = Rectangle(2, 4, 10)
        self.assertEqual(r1.x, 10)

        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_set_get_y(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.y, 0)

        r1 = Rectangle(2, 4, 10, 11)
        self.assertEqual(r1.y, 11)

        r1.y = 15
        self.assertEqual(r1.y, 15)


if __name__ == "__main__":
    unittest.main()
