import unittest

from gpw_analyzer.data import Candle


class CandleTest(unittest.TestCase):

    def test_black_candle_has_lower_closing_than_opening(self):
        candle = Candle(3.4, 5.2, 3, 6, 10)
        self.assertFalse(candle.is_black())

        candle = Candle(5.2, 3.4, 3, 6, 10)
        self.assertTrue(candle.is_black())

    def test_white_candle_has_lower_closing_than_opening(self):
        candle = Candle(3.4, 5.2, 3, 6, 10)
        self.assertTrue(candle.is_white())

        candle = Candle(5.2, 3.4, 3, 6, 10)
        self.assertFalse(candle.is_white())


if __name__ == "__main__":
    unittest.main()
