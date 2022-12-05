import unittest
import day05

class TestDay05(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy = "../data/dummy.txt"
        self.realfile = "../data/day05.txt"

    def test_day5_1(self):
        self.assertEqual(day05.day5_1(self.dummy), "CMZ")
        self.assertEqual(day05.day5_1(self.realfile), "ZBDRNPMVH")
        self.assertEqual(day05.day5_2(self.realfile), "WDLPFNNNB")