import unittest
import day06

class TestDay06(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.realfile = "../data/day06.txt"
    
    def test_day6_1(self):
        self.assertEqual(day06.day6_1(self.dummy), 7)
        self.assertEqual(day06.day6_1(self.realfile), 1757)

    def test_day6_2(self):
        self.assertEqual(day06.day6_2(self.dummy), 19)
        self.assertEqual(day06.day6_2(self.realfile), 2950)