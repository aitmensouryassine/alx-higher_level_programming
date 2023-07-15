import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class _AssertStdoutContext:

    def __init__(self, testcase, expected):
        self.testcase = testcase
        self.expected = expected
        self.captured = io.StringIO()

    def __enter__(self):
        sys.stdout = self.captured
        return self

    def __exit__(self, exc_type, exc_value, tb):
        sys.stdout = sys.__stdout__
        captured = self.captured.getvalue()
        self.testcase.assertEqual(captured, self.expected)

    def assertStdout(self, expected_output):
        return _AssertStdoutContext(self, expected_output)


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


class TestPrivateAttrs(unittest.TestCase):

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2).__y


class TestAttrValidation(unittest.TestCase):

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(3.5, 1)

        with self.assertRaises(TypeError):
            Rectangle((4, 5), 1)

        with self.assertRaises(TypeError):
            Rectangle([5, 6], 1)

        with self.assertRaises(TypeError):
            Rectangle("string", 1)

        with self.assertRaises(TypeError):
            Rectangle(None, 1)

        with self.assertRaises(TypeError):
            Rectangle(True, 1)

        with self.assertRaises(TypeError):
            Rectangle(b'string', 1)

        with self.assertRaises(TypeError):
            Rectangle(complex(1, 2), 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 1)

        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

        r = Rectangle(1, 5)
        self.assertEqual(r.width, 1)


    def test_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(1, None)

        with self.assertRaises(TypeError):
            Rectangle(1, 3.5)

        with self.assertRaises(TypeError):
            Rectangle(1, (4, 5))

        with self.assertRaises(TypeError):
            Rectangle(1, [5, 6])

        with self.assertRaises(TypeError):
            Rectangle(1, "string")

        with self.assertRaises(TypeError):
            Rectangle(1, True)

        with self.assertRaises(TypeError):
            Rectangle(1, b'string')

        with self.assertRaises(TypeError):
            Rectangle(1, complex(1, 2))

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

        with self.assertRaises(ValueError):
            Rectangle(1, -1)

        r = Rectangle(1, 5)
        self.assertEqual(r.height, 5)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 3.5)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, (4, 5))

        with self.assertRaises(TypeError):
            Rectangle(1, 1, [5, 6])

        with self.assertRaises(TypeError):
            Rectangle(1, 1, "string")

        with self.assertRaises(TypeError):
            Rectangle(1, 1, True)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, b'string')

        with self.assertRaises(TypeError):
            Rectangle(1, 1, complex(1, 2))

        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

        r = Rectangle(1, 1, 5)
        self.assertEqual(r.x, 5)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, None)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, 3.5)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, (4, 5))

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, [5, 6])

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, "string")

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, True)

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, b'string')

        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, complex(1, 2))

        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1)

        r = Rectangle(1, 1, 0, 5)
        self.assertEqual(r.y, 5)


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Rectangle(4, 2).area(), 8)
        self.assertEqual(Rectangle(4, 2, 0, 0, 7).area(), 8)


class TestDisplayRectangle(unittest.TestCase, _AssertStdoutContext):

    def test_display_w_h(self):
        with self.assertStdout("##\n##\n"):
            Rectangle(2, 2).display()

    def test_display_w_h_x(self):
        with self.assertStdout("  ##\n  ##\n"):
            Rectangle(2, 2, 2).display()

    def test_display_w_h_x(self):
        with self.assertStdout("\n\n  ##\n  ##\n"):
            Rectangle(2, 2, 2, 2).display()


class TestStrRectangle(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_str_w_h(self):
        with self.assertStdout("[Rectangle] (1) 0/0 - 2/4\n"):
            print(Rectangle(2, 4))

    def test_str_w_h_x_y(self):
        with self.assertStdout("[Rectangle] (1) 10/20 - 2/4\n"):
            print(Rectangle(2, 4, 10, 20))

    def test_str_w_h_x_y_id(self):
        with self.assertStdout("[Rectangle] (11) 10/20 - 2/4\n"):
            print(Rectangle(2, 4, 10, 20, 11))


if __name__ == "__main__":
    unittest.main()
