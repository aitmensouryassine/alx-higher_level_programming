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

class TestBase_to_json_strin(unittest.TestCase):

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
        self.assertTrue(len(string) == 52)
        
    def test_rect_tjs_two_dicts(self):
        d1 = Rectangle(4, 5).to_dictionary()
        d2 = Rectangle(10, 15).to_dictionary()
        string = Base.to_json_string([d1, d2])
        self.assertTrue(len(string) == 106)

    def test_square_tjs_type(self):
        s = Square(4)
        d = s.to_dictionary()
        string = Base.to_json_string([d])
        self.assertEqual(str, type(string))
        
    def test_square_tjs_one_dict(self):
        s = Square(4)
        d = s.to_dictionary()
        string = Base.to_json_string([d])
        self.assertTrue(len(string) == 38)
        
    def test_square_tjs_two_dicts(self):
        d1 = Square(4).to_dictionary()
        d2 = Square(10, 15).to_dictionary()
        string = Base.to_json_string([d1, d2])
        self.assertTrue(len(string) == 79)

if __name__ == "__main__":
    unittest.main()
