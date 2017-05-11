import unittest

from gpw_analyzer import engulfings
from gpw_analyzer.data import Candle


class Test(unittest.TestCase):

    def test_proper_prosperity_engulfing(self):
        candles = [Candle(9, 5, 4, 10, 100), Candle(4, 10, 3, 11, 100)]
        self.assertTrue(engulfings.is_prosperity_engulfing(candles))

    def test_no_prosperity_engulfing_when_first_candle_is_white(self):
        candles = [Candle(5, 9, 4, 10, 100), Candle(4, 10, 3, 11, 100)]
        self.assertFalse(engulfings.is_prosperity_engulfing(candles))

    def test_no_prosperity_engulfing_when_second_candle_is_black(self):
        candles = [Candle(9, 5, 4, 10, 100), Candle(10, 4, 3, 11, 100)]
        self.assertFalse(engulfings.is_prosperity_engulfing(candles))

    def test_no_prosperity_engulfing_when_second_candle_closing_is_not_higher(
            self):
        candles = [Candle(9, 5, 4, 10, 100), Candle(4, 9, 3, 11, 100)]
        self.assertFalse(engulfings.is_prosperity_engulfing(candles))

    def test_no_prosperity_engulfing_when_second_candle_closing_is_not_lower(
            self):
        candles = [Candle(9, 5, 4, 10, 100), Candle(5, 10, 3, 11, 100)]
        self.assertFalse(engulfings.is_prosperity_engulfing(candles))


if __name__ == "__main__":
    unittest.main()
