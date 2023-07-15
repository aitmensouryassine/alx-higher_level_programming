import unittest
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
