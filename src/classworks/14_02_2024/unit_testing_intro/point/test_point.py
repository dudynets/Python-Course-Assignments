import unittest
from point import Point

class TestPoint(unittest.TestCase):
    def test_initialization(self):
        p1 = Point()
        self.assertEqual(p1.x, 0)
        self.assertEqual(p1.y, 0)

        p2 = Point(3, 4)
        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 4)

        with self.assertRaises(ValueError):
            Point('a', 'b')

    def test_str(self):
        p = Point()
        self.assertEqual(str(p), "(0, 0)")

        p.move_to(3, 4)
        self.assertEqual(str(p), "(3, 4)")
        
        p.move_by(-1, -1)
        self.assertEqual(str(p), "(2, 3)")

    def test_set_x(self):
        p = Point()
        p.x = 5
        self.assertEqual(p.x, 5)

        with self.assertRaises(ValueError):
            p.x = 'a'

    def test_set_y(self):
        p = Point()
        p.y = 10
        self.assertEqual(p.y, 10)
        
        with self.assertRaises(ValueError):
            p.y = 'a'

    def test_move_by(self):
        p = Point(3, 4)
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

        p.move_by(-1, -1)
        self.assertEqual(p.x, 2)
        self.assertEqual(p.y, 3)

        with self.assertRaises(ValueError):
            p.move_by('a', 'b')

    def test_move_to(self):
        p = Point()

        p.move_to(7, 8)
        self.assertEqual(p.x, 7)
        self.assertEqual(p.y, 8)

        with self.assertRaises(ValueError):
            p.move_to('a', 'b')

if __name__ == "__main__":
    unittest.main()
