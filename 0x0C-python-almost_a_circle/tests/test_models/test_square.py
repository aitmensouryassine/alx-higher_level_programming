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


class TestSquareInstantiation(unittest.TestCase):

    def setUp(self):
        Base.reset()

    def test_is_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Square)
        
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_id(self):
        self.assertEqual(Square(4).id, 1)
        self.assertEqual(Square(4, 5, 6, 45).id, 45)

    def test_size_w(self):
        self.assertEqual(Square(4).width, 4)

    def test_size_h(self):
        self.assertEqual(Square(5).height, 5)

    def test_size_x(self):
        self.assertEqual(Square(5).x, 0)
        self.assertEqual(Square(5, 12).x, 12)

    def test_size_x_y(self):
        self.assertEqual(Square(5).y, 0)
        self.assertEqual(Square(4, 5, 7).y, 7)

    def test_size_x_y_id(self):
        self.assertEqual(Square(5, 4, 3, 2).id, 2)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_access_private_size(self):
        with self.assertRaises(AttributeError):
            Square(1, 2, 3).__size

    def test_size_getter(self):
        self.assertEqual(Square(1, 2, 3).size, 1)

    def test_size_setter(self):
        s = Square(1, 2, 3)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_size_setter_invalid_value(self):
        s = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            s.size = "5"


class TestSquareSize(unittest.TestCase):

    def test_size_with_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_with_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string")

    def test_size_with_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.5)

    def test_size_with_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5, 6))

    def test_size_with_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"x": 1, "y": 2})

    def test_size_with_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_size_with_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_size_with_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_size_with_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_size_with_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(10))

    def test_size_with_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Bytes')

    def test_size_with_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_size_with_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_size_with_negative_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_size_with_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        

class TestSquareAttrsValidation(unittest.TestCase):
    # x validation
    def test_x_validation(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, None)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, "invalid_x")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, 5.5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, complex(5, 6))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, {"a": 1, "b": 2})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, True)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, [1, 2, 3])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, {1, 2, 3})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, (1, 2, 3))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, range(5))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, b'Bytes')

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, float('inf'))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, float('nan'))

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(89, -1)

    # y validation
    def test_y_validation(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, "invalid_y")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, 5.5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, complex(5, 6))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, {"a": 1, "b": 2})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, True)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, [1, 2, 3])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, {1, 2, 3})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, (1, 2, 3))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, range(5))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, b'Bytes')

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, float('inf'))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(89, 89, float('nan'))

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(89, 89, -1)

    # test order of initialization
    def test_init_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_init_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 89, "invalid y")

    def test_init_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(89, "invalid x", "invalid y")


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(5, 0, 0, 7).area(), 25)

    def test_area_large(self):
        s = Square(987654321)
        self.assertEqual(975461057789971041, s.area())

    def test_area_changed_attrs(self):
        s = Square(10, 1, 1)
        s.size = 20
        self.assertEqual(400, s.area())

    def test_area_one_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.area(1)

class TestDisplaySquare(unittest.TestCase, _AssertStdoutContext):

    def test_display_size(self):
        with self.assertStdout("##\n##\n"):
            Square(2).display()

    def test_display_size_x(self):
        with self.assertStdout("  ##\n  ##\n"):
            Square(2, 2).display()

    def test_display_size_y(self):
        with self.assertStdout("\n\n##\n##\n"):
            Square(2, 0, 2).display()

    def test_display_size_x_y(self):
        with self.assertStdout("\n\n  ##\n  ##\n"):
            Square(2, 2, 2).display()

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)



class TestStrSquare(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_str_size(self):
        with self.assertStdout("[Square] (1) 0/0 - 5"):
            print(Square(5), end="")

    def test_str_size_x(self):
        with self.assertStdout("[Square] (1) 10/0 - 5"):
            print(Square(5, 10), end="")

    def test_str_size_x_y(self):
        with self.assertStdout("[Square] (1) 10/20 - 5"):
            print(Square(5, 10, 20), end="")

    def test_str_size_x_y_id(self):
        with self.assertStdout("[Square] (11) 10/20 - 5"):
            print(Square(5, 10, 20, 11), end="")

    def test_str_change_attrs(self):
        s = Square(8)
        with self.assertStdout("[Square] (1) 0/0 - 8"):
            print(s, end="")

        s.size = 10
        s.x = 8
        s.y = 5
        with self.assertStdout("[Square] (1) 8/5 - 10"):
            print(s, end="")

    def test_str_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)



class TestUpdateSquare_Args(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()
    
    def test_update_no_args(self):
        s = Square(5, 5, 5)
        s.update()
        with self.assertStdout("[Square] (1) 5/5 - 5"):
            print(s, end="")

    def test_update_id(self):
        s = Square(5, 5, 5)
        s.update(45)
        with self.assertStdout("[Square] (45) 5/5 - 5"):
            print(s, end="")

    def test_update_id_none(self):
        s = Square(5, 5, 5)
        s.update(None)
        with self.assertStdout("[Square] (2) 5/5 - 5"):
            print(s, end="")

        s.update(None)
        with self.assertStdout("[Square] (3) 5/5 - 5"):
            print(s, end="")

    def test_update_size(self):
        s = Square(5, 5, 5)
        s.update(45, 7)
        with self.assertStdout("[Square] (45) 5/5 - 7"):
            print(s, end="")

    def test_update_x(self):
        s = Square(5, 5, 5)
        s.update(45, 7, 8)
        with self.assertStdout("[Square] (45) 8/5 - 7"):
            print(s, end="")

    def test_update_y(self):
        s = Square(5, 5, 5)
        s.update(45, 7, 8, 9)
        with self.assertStdout("[Square] (45) 8/9 - 7"):
            print(s, end="")

    def test_update_args_more_than_four(self):
        s = Square(5, 5, 5)
        s.update(89, 10, 11, 12, 13)
        with self.assertStdout("[Square] (89) 11/12 - 10"):
            print(s, end="")

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        s.update(4, 5, 6, 89)
        with self.assertStdout("[Square] (4) 6/89 - 5"):
            print(s, end="")

    def test_update_args_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "invalid_size")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(99, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(99, -7)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(99, 99, "invalid_x")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 99, -7)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 99, 99, "invalid_y")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 99, 99, -7)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "invalid_size", "invalid_x")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(99, "invalid_size", 99, "invalid_y")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(99, 99, "invalid_x", "invalid_y")

            
class TestUpdateSquare_Kwargs(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_update_no_kwargs(self):
        s = Square(5, 5, 5)
        s.update()
        with self.assertStdout("[Square] (1) 5/5 - 5"):
            print(s, end="")

    def test_update_id(self):
        s = Square(5, 5, 5)
        s.update(id=45)
        with self.assertStdout("[Square] (45) 5/5 - 5"):
            print(s, end="")

    def test_update_id_size(self):
        s = Square(5, 5, 5)
        s.update(id=45, size=9)
        with self.assertStdout("[Square] (45) 5/5 - 9"):
            print(s, end="")

    def test_update_id_size_x(self):
        s = Square(5, 5, 5)
        s.update(id=45, x=7, size=9)
        with self.assertStdout("[Square] (45) 7/5 - 9"):
            print(s, end="")

    def test_update_id_size_x_y(self):
        s = Square(5, 5, 5)
        s.update(id=45, x=7, y=8, size=9)
        with self.assertStdout("[Square] (45) 7/8 - 9"):
            print(s, end="")

    def test_update_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        with self.assertStdout("[Square] (1) 10/10 - 10"):
            print(s, end="")

    def test_update_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=5, x=4)
        with self.assertStdout("[Square] (1) 4/10 - 5"):
            print(s, end="")


    def test_update_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=4)
        s.update(y=5, x=5, size=1)
        with self.assertStdout("[Square] (89) 5/5 - 1"):
            print(s, end="")

    def test_update_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid_size")

    def test_update_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid_x")

    def test_update_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-7)

    def test_update_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid_y")

    def test_update_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-7)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(99, 9, y=8)
        with self.assertStdout("[Square] (99) 10/10 - 9"):
            print(s, end="")

    def test_update_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(w=1, v=2)
        with self.assertStdout("[Square] (10) 10/10 - 10"):
            print(s, end="")

    def test_update_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=50, id=99, a=5, b=6)
        with self.assertStdout("[Square] (99) 10/10 - 50"):
            print(s, end="")


class TestSquareToDictionary(unittest.TestCase, _AssertStdoutContext):

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        self.assertCountEqual(s.to_dictionary(), {'x': 2, 'y': 3, 'id': 4, 'size': 1})

    def test_to_dict_type(self):
        s = Square(4)
        t = type(s.to_dictionary())
        
        with self.assertStdout("<class 'dict'>"):
            print(t, end="")

    def test_to_dict_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(10, 2, 1, 2)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dict_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

            
if __name__ == "__main__":
    unittest.main()
