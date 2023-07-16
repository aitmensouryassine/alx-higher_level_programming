import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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


class TestSquareValidation(unittest.TestCase):

    def setUp(self):
        Base.reset()

    def test_id(self):
        self.assertEqual(Square(4).id, 1)
        self.assertEqual(Square(4, 5, 6, 45).id, 45)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_width(self):
        self.assertEqual(Square(4).width, 4)

    def test_height(self):
        self.assertEqual(Square(5).height, 5)

    def test_x(self):
        self.assertEqual(Square(5).x, 0)
        self.assertEqual(Square(5, 12).x, 12)

    def test_y(self):
        self.assertEqual(Square(5).y, 0)
        self.assertEqual(Square(4, 5, 7).y, 7)


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(5, 0, 0).area(), 25)


class TestDisplaySquare(unittest.TestCase, _AssertStdoutContext):

    def test_display_size(self):
        with self.assertStdout("##\n##\n"):
            Square(2).display()

    def test_display_size_x(self):
        with self.assertStdout("  ##\n  ##\n"):
            Square(2, 2).display()

    def test_display_size_x_y(self):
        with self.assertStdout("\n\n  ##\n  ##\n"):
            Square(2, 2, 2).display()


class TestStrSquare(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_str_size(self):
        with self.assertStdout("[Square] (1) 0/0 - 5"):
            print(Square(5), end="")

    def test_str_size_x_y(self):
        with self.assertStdout("[Square] (1) 10/20 - 5"):
            print(Square(5, 10, 20), end="")

    def test_str_size_x_y_id(self):
        with self.assertStdout("[Square] (11) 10/20 - 5"):
            print(Square(5, 10, 20, 11), end="")
