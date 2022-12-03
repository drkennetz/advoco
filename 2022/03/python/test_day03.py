import unittest
import day03

class TestDay03(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.dummy2 = "../data/dummy2.txt"
        self.realfile = "../data/day03.txt"

    def test_day3_1(self):
        self.assertEqual(day03.day3_1(self.dummy), 157)
        self.assertEqual(day03.day3_1(self.realfile), 7872)
        self.assertEqual(day03.day3_2(self.dummy2), 70)
        self.assertEqual(day03.day3_2(self.realfile), 2497)