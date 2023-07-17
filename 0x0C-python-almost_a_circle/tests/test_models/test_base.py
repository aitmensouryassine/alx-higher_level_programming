import sys
import io
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class _AssertStdoutContext:
    """ captures stdout """
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


class TestBaseClass(unittest.TestCase):
    """ Test Base Class Instantiation """

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(33)
        self.assertEqual(b3.id, 33)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        b4.id = 4
        self.assertEqual(b4.id, 4)

    def test_id_int(self):
        self.assertEqual(Base(5).id, 5)

    def test_id_str(self):
        self.assertEqual(Base("yassine").id, "yassine")
    
    def test_id_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))
        
    def test_id_list(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])
        
    def test_id_dict(self):
        self.assertEqual(Base({"t": 1}).id, {"t": 1})
        
    def test_id_float(self):
        self.assertEqual(Base(3.5).id, 3.5)
        
    def test_id_byte(self):
        self.assertEqual(Base(b'yassine').id, b'yassine')
        
    def test_id_bool(self):
        self.assertEqual(Base(True).id, True)
        
    def test_id_set(self):
        self.assertEqual(Base({0, 1, 2}).id, {0, 1, 2})
        
    def test_id_inf(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))
        
    def test_id_nan(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_id_range(self):
        self.assertEqual(Base(range(5)).id, range(5))

    def test_id_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 1)

class TestBase_to_json_string(unittest.TestCase):
    """ Test to json string method """

    def test_tjs_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_tjs_none(self):
        string = Base.to_json_string(None)
        self.assertEqual(string, "[]")

    def test_tjs_empty_list(self):
        string = Base.to_json_string([])
        self.assertEqual(string, "[]")

    def test_tjs_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_rect_tjs_type(self):
        r = Rectangle(4, 5)
        d = r.to_dictionary()
        string = Base.to_json_string([d])
        self.assertEqual(str, type(string))
        
    def test_rect_tjs_one_dict(self):
        r = Rectangle(4, 5)
        d = r.to_dictionary()
        string = Base.to_json_string([d])
        self.assertTrue(len(string) == 53)
        
    def test_rect_tjs_two_dicts(self):
        d1 = Rectangle(4, 5).to_dictionary()
        d2 = Rectangle(10, 15).to_dictionary()
        string = Base.to_json_string([d1, d2])
        self.assertTrue(len(string) == 108)

    def test_square_tjs_type(self):
        s = Square(4)
        d = s.to_dictionary()
        string = Base.to_json_string([d])
        self.assertEqual(str, type(string))
        
    def test_square_tjs_one_dict(self):
        s = Square(4)
        d = s.to_dictionary()
        string = Base.to_json_string([d])
        self.assertTrue(len(string) == 39)
        
    def test_square_tjs_two_dicts(self):
        d1 = Square(4).to_dictionary()
        d2 = Square(10, 15).to_dictionary()
        string = Base.to_json_string([d1, d2])
        self.assertTrue(len(string) == 80)


class TestBase_save_to_file(unittest.TestCase):
    """ Test save to file method """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Base.json")
        except Exception:
            pass

    def test_stf_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_stf_empty_list(self):
        Base.save_to_file([])
        with open("Base.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_stf_none(self):
        Base.save_to_file(None)
        with open("Base.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_stf_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], 1)

    def test_stf_rect_one_obj(self):
        r = Rectangle(4, 5, 6, 7)
        Rectangle.save_to_file([r])
        with open("Rectangle.json") as f:
            self.assertTrue(len(f.read()), 52)

    def test_stf_rect_two_objs(self):
        r1 = Rectangle(4, 5, 6, 7)
        r2 = Rectangle(4, 5, 6, 7)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            self.assertTrue(len(f.read()), 104)

    def test_stf_square_one_obj(self):
        s = Square(5, 6, 7)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertTrue(len(f.read()), 38)

    def test_stf_square_two_objs(self):
        s1 = Square(5, 6, 7)
        s2 = Square(5, 6, 7)
        Square.save_to_file([s1, s2])
        with open("Square.json") as f:
            self.assertTrue(len(f.read()), 76)

    def test_stf_overwrite_file(self):
        s = Square(4, 5, 6)
        Square.save_to_file([s])
        s1 = Square(40, 50, 60)
        Square.save_to_file([s1])
        with open("Square.json") as f:
            self.assertTrue(len(f.read()), 79)
        
class TestBase_from_json_string(unittest.TestCase):
    """ Test from json string """

    def test_fjs_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_fjs_none(self):
        list_input = Base.from_json_string(None)
        self.assertEqual(list_input, [])

    def test_fjs_empty_list(self):
        list_input = Base.from_json_string("[]")
        self.assertEqual(list_input, [])

    def test_fjs_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", 1)

    def test_rect_fjs_type(self):
        list_input = Rectangle.from_json_string('[{"height": 4, "width": 10, "id": 89}]')
        self.assertEqual(list, type(list_input))
        
    def test_rect_fjs_one_dict(self):
        json_string = '[{"height": 4, "width": 10, "id": 89}]'
        list_input = Rectangle.from_json_string(json_string)
        self.assertTrue(len(list_input) == 1)
        
    def test_rect_fjs_two_dicts(self):
        json_string = '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 5, "id": 99}]'
        list_input = Rectangle.from_json_string(json_string)
        self.assertTrue(len(list_input) == 2)

    def test_square_fjs_type(self):
        list_input = Square.from_json_string('[{"size": 4, "id": 89}]')
        self.assertEqual(list, type(list_input))
        
    def test_square_fjs_one_dict(self):
        json_string = '[{"size": 4, "id": 89}]'
        list_input = Square.from_json_string(json_string)
        self.assertTrue(len(list_input) == 1)
        
    def test_square_fjs_two_dicts(self):
        json_string = '[{"size": 4, "id": 89}, {"size": 7, "id": 99}]'
        list_input = Square.from_json_string(json_string)
        self.assertTrue(len(list_input) == 2)


class TestBase_dict_to_inst(unittest.TestCase, _AssertStdoutContext):
    """ Test dictionary to instance method """

    def setUp(self):
        Base.reset()

    def test_dti_no_args(self):
        self.assertTrue(Base.create() == None)

    def test_dti_empty(self):
        d = {}
        self.assertTrue(Base.create(**d) == None)

    def test_dti_more_than_one_arg(self):
       with self.assertRaises(TypeError):
           Base.create(5)

    def test_dti_rect(self):
        d = {"width" : 5, "height": 4}
        r = Rectangle.create(**d)
        with self.assertStdout("[Rectangle] (1) 0/0 - 5/4"):
            print(r, end="")

    def test_dti_rect_is_rect(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)

    def test_dti_rect_equal_rect(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)

    def test_dti_square(self):
        d = {"size" : 5}
        s = Square.create(**d)
        with self.assertStdout("[Square] (1) 0/0 - 5"):
            print(s, end="")

    def test_dti_square_is_square(self):
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)

    def test_dti_rect_equal_rect(self):
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 == s2)

class TestBase_load_from_file(unittest.TestCase, _AssertStdoutContext):
    """ test load from file method """

    @classmethod
    def setUp(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Base.json")
        except Exception:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Base.json")
        except Exception:
            pass

    def setUp(self):
        Base.reset()
    
    def test_lff_rect_file_not_found(self):
        self.assertEqual(Rectangle.load_from_file(), [])
    
    def test_lff_square_file_not_found(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_lff_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        rects = Rectangle.load_from_file()

        with self.assertStdout("[Rectangle] (1) 2/8 - 10/7"):
            print(rects[0], end="")

        with self.assertStdout("[Rectangle] (2) 0/0 - 2/4"):
            print(rects[1], end="")

        self.assertFalse(r1 is rects[0])
        self.assertFalse(r1 == rects[0])

        self.assertFalse(r2 is rects[1])
        self.assertFalse(r2 == rects[1])

        self.assertTrue(type(rects[0]) == Rectangle)
        self.assertTrue(type(rects[1]) == Rectangle)

    def test_lff_square(self):
        s1 = Square(10, 7, 8)
        s2 = Square(2)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        squares = Square.load_from_file()

        with self.assertStdout("[Square] (1) 7/8 - 10"):
            print(squares[0], end="")

        with self.assertStdout("[Square] (2) 0/0 - 2"):
            print(squares[1], end="")

        self.assertFalse(s1 is squares[0])
        self.assertFalse(s1 == squares[0])

        self.assertFalse(s2 is squares[1])
        self.assertFalse(s2 == squares[1])

        self.assertTrue(type(squares[0]) == Square)
        self.assertTrue(type(squares[1]) == Square)
        

class TestBase_save_to_file_csv(unittest.TestCase):
    """ Test save to file csv method """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass
        try:
            os.remove("Base.csv")
        except Exception:
            pass

    def test_stf_csv_one_rect(self):
        r = Rectangle(10, 1, 2, 3, 4)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("4,10,1,2,3", f.read())

    def test_stf_csv_two_rects(self):
        r1 = Rectangle(10, 1, 2, 3, 4)
        r2 = Rectangle(20, 2, 4, 6, 8)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("4,10,1,2,3\n2,8,20,2,4,6", f.read())

    def test_stf_csv_one_square(self):
        s = Square(10, 1, 2, 3)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("3,10,1,2", f.read())

    def test_stf_csv_two_squares(self):
        s1 = Square(10, 1, 2, 3)
        s2 = Square(20, 2, 4, 6)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("3,10,1,2\n3,6,20,2,4", f.read())

    def test_stf_csv_cls_name(self):
        s = Square(10, 1, 2, 3)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("3,10,1,2", f.read())

    def test_stf_csv_overwrite(self):
        s = Square(10, 1, 2, 3)
        Square.save_to_file_csv([s])
        s = Square(20, 2, 4, 6)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("6,20,2,4", f.read())

    def test_stf_csv_none(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_stf_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """ Test load from file csv """

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass

    def test_lff_csv_rect(self):
        r1 = Rectangle(10, 1, 2, 3, 4)
        r2 = Rectangle(20, 2, 4, 6, 8)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_lff_csv_rect_type(self):
        r1 = Rectangle(10, 1, 2, 3, 4)
        r2 = Rectangle(20, 2, 4, 6, 8)
        Rectangle.save_to_file_csv([r1, r2])
        objs = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in objs))

    def test_lff_csv_square(self):
        s1 = Square(10, 1, 2, 3)
        s2 = Square(20, 2, 4, 6)
        Square.save_to_file_csv([s1, s2])
        squares = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(squares[0]))
        self.assertEqual(str(s2), str(squares[1]))

    def test_lff_csv_square_type(self):
        s1 = Square(10, 1, 2, 3)
        s2 = Square(20, 2, 4, 6)
        Square.save_to_file_csv([s1, s2])
        objs = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in objs))

    def test_lff_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_lff_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
