import unittest
import day02

class TestDay02(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.realfile = "../data/day02.txt"
    
    def test_day2_1(self):
        self.assertEqual(day02.day2_1(self.dummy), 15)
        self.assertEqual(day02.day2_1(self.realfile), 10941)

    def test_day2_2(self):
        self.assertEqual(day02.day2_2(self.dummy), 12)
        self.assertEqual(day02.day2_2(self.realfile), 13071)
