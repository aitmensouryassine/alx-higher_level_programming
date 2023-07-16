import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

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

class TestBase_to_json_string(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
