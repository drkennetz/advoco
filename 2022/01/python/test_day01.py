import unittest
import day01

class Day01Test(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.realfile = "../data/day01.txt"

    def test_day1(self):
        self.assertEqual(day01.day1(self.dummy, 1), 24000)
        self.assertEqual(day01.day1(self.realfile, 1), 71300)
        self.assertEqual(day01.day1(self.dummy, 2), 45000)
        self.assertEqual(day01.day1(self.realfile, 2), 209691)
        with self.assertRaises(ValueError):
            raise ValueError
        
