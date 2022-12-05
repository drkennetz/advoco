import unittest
import day04

class TestDay04(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.realfile = "../data/day04.txt"

    def test_day4_1(self):
        self.assertEqual(day04.day4(self.dummy, part=1), 2)
        self.assertEqual(day04.day4(self.realfile, part=1), 498)
        self.assertEqual(day04.day4(self.dummy, part=2), 4)
        self.assertEqual(day04.day4(self.realfile, part=2), 859)