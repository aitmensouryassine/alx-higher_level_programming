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

    def test_rect_is_instance_base(self):
        self.assertIsInstance(Rectangle(4, 5), Base)
        
    def test_id(self):
        self.assertEqual(Rectangle(4, 5).id, 1)
        self.assertEqual(Rectangle(4, 5, 6, 7, 45).id, 45)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

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

    def test_area_large(self):
        r = Rectangle(987654321, 987654321, 0, 0, 1)
        self.assertEqual(975461057789971041, r.area())

    def test_area_changed_attrs(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 5
        r.height = 10
        self.assertEqual(50, r.area())

    def test_area_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.area(1)

class TestDisplayRectangle(unittest.TestCase, _AssertStdoutContext):

    def test_display_w_h(self):
        with self.assertStdout("##\n##\n"):
            Rectangle(2, 2).display()

    def test_display_w_h_x(self):
        with self.assertStdout("  ##\n  ##\n"):
            Rectangle(2, 2, 2).display()

    def test_display_w_h_y(self):
        with self.assertStdout("\n\n##\n##\n"):
            Rectangle(2, 2, 0, 2).display()

    def test_display_w_h_x_y(self):
        with self.assertStdout("\n\n  ##\n  ##\n"):
            Rectangle(2, 2, 2, 2).display()

    def test_display_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 10, 10, 10).display(1)


class TestStrRectangle(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_str_w_h(self):
        with self.assertStdout("[Rectangle] (1) 0/0 - 2/4"):
            print(Rectangle(2, 4), end="")

    def test_str_w_h_x(self):
        with self.assertStdout("[Rectangle] (1) 10/0 - 2/4"):
            print(Rectangle(2, 4, 10), end="")

    def test_str_w_h_x_y(self):
        with self.assertStdout("[Rectangle] (1) 10/20 - 2/4"):
            print(Rectangle(2, 4, 10, 20), end="")

    def test_str_w_h_x_y_id(self):
        with self.assertStdout("[Rectangle] (11) 10/20 - 2/4"):
            print(Rectangle(2, 4, 10, 20, 11), end="")

    def test_str_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 10, 20).__str__(0)


class TestUpdateRectangle_Args(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()
    
    def test_update_no_args(self):
        r = Rectangle(5, 5, 5, 5)
        r.update()
        with self.assertStdout("[Rectangle] (1) 5/5 - 5/5"):
            print(r, end="")

    def test_update_id(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(45)
        with self.assertStdout("[Rectangle] (45) 5/5 - 5/5"):
            print(r, end="")

    def test_update_id_none(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(None)
        with self.assertStdout("[Rectangle] (2) 5/5 - 5/5"):
            print(r, end="")

        r.update(None)
        with self.assertStdout("[Rectangle] (3) 5/5 - 5/5"):
            print(r, end="")

    def test_update_width(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(45, 7)
        with self.assertStdout("[Rectangle] (45) 5/5 - 7/5"):
            print(r, end="")

    def test_update_height(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(45, 7, 8)
        with self.assertStdout("[Rectangle] (45) 5/5 - 7/8"):
            print(r, end="")

    def test_update_x(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(45, 7, 8, 9)
        with self.assertStdout("[Rectangle] (45) 9/5 - 7/8"):
            print(r, end="")

    def test_update_y(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(45, 7, 8, 9, 10)
        with self.assertStdout("[Rectangle] (45) 9/10 - 7/8"):
            print(r, end="")

    def test_update_more_than_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(99, 1, 2, 3, 4, 5)
        with self.assertStdout("[Rectangle] (99) 3/4 - 1/2"):
            print(r, end="")

    def test_update_id_none_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 1, 2, 3)
        with self.assertStdout("[Rectangle] (1) 3/10 - 1/2"):
            print(r, end="")

    def test_update_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(99, 1, 2, 3, 4)
        r.update(88, 5, 4, 3, 2)
        with self.assertStdout("[Rectangle] (88) 3/2 - 5/4"):
            print(r, end="")

    def test_update_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, 3.5)

    def test_update_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -7)

    def test_update_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 89, 3.5)

    def test_update_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 89, 0)

    def test_update_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 89, -7)

    def test_update_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 89, 89, 3.5)

    def test_update_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 89, 89, -7)

    def test_update_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 89, 89, 89, 3.5)

    def test_update_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 89, 89, 89, -7)

    def test_update_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid_w", "invalid_h")

    def test_update_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid_w", 5, "invalid_x")

    def test_update_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid_w", 5, 6, "invalid_y")

    def test_update_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 5, "invalid_h", "invalid_x")

    def test_update_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 5, "invalid_h", 6, "invalid_y")

    def test_update_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 5, 6, "invalid_x", "invalid_y")
            
class TestUpdateRectangle_Kwargs(unittest.TestCase, _AssertStdoutContext):

    def setUp(self):
        Base.reset()

    def test_update_no_kwargs(self):
        r = Rectangle(5, 5, 5, 5)
        r.update()
        with self.assertStdout("[Rectangle] (1) 5/5 - 5/5"):
            print(r, end="")

    def test_update_id(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=45)
        with self.assertStdout("[Rectangle] (45) 5/5 - 5/5"):
            print(r, end="")

    def test_update_id_none(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=None)
        with self.assertStdout("[Rectangle] (2) 5/5 - 5/5"):
            print(r, end="")

    def test_update_width(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=45, width=9)
        with self.assertStdout("[Rectangle] (45) 5/5 - 9/5"):
            print(r, end="")

    def test_update_height(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=45, width=9, height=10)
        with self.assertStdout("[Rectangle] (45) 5/5 - 9/10"):
            print(r, end="")

    def test_update_x(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=45, x=7, width=9, height=10)
        with self.assertStdout("[Rectangle] (45) 7/5 - 9/10"):
            print(r, end="")

    def test_update_y(self):
        r = Rectangle(5, 5, 5, 5)
        r.update(id=45, x=7, y=8, width=9, height=10)
        with self.assertStdout("[Rectangle] (45) 7/8 - 9/10"):
            print(r, end="")

    def test_update_id_None_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=8, y=5)
        with self.assertStdout("[Rectangle] (1) 10/5 - 10/8"):
            print(r, end="")

    def test_update_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=99, x=2, height=4)
        r.update(y=7, height=6, width=5)
        with self.assertStdout("[Rectangle] (99) 2/7 - 5/6"):
            print(r, end="")

    def test_update_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width=3.5)

    def test_update_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-7)

    def test_update_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height=3.5)

    def test_update_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-7)

    def test_update_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x=3.5)

    def test_update_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-7)

    def test_update_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y=3.5)

    def test_update_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-7)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(99, 5, height=3, y=4)
        with self.assertStdout("[Rectangle] (99) 10/10 - 5/10"):
            print(r, end="")

    def test_update_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=3, b=4)
        with self.assertStdout("[Rectangle] (10) 10/10 - 10/10"):
            print(r, end="")

    def test_update_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=7, id=99, a=8, b=9, x=11, y=12)
        with self.assertStdout("[Rectangle] (99) 11/12 - 10/7"):
            print(r, end="")
        
            
class TestRectToDictionary(unittest.TestCase, _AssertStdoutContext):

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertCountEqual(r.to_dictionary(), {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})

    def test_to_dict_type(self):
        r = Rectangle(4, 5)
        t = type(r.to_dictionary())
        
        with self.assertStdout("<class 'dict'>"):
            print(t, end="")

    def test_to_dict_no_object_changes(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dict_pass_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.to_dictionary(0)
    
if __name__ == "__main__":
    unittest.main()
