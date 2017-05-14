class Candle(object):

    def __init__(self, opening, closing, minimum, maximum, volume):
        self.opening = float(opening)
        self.closing = float(closing)
        self.min = float(minimum)
        self.max = float(maximum)
        self.volume = float(volume)

    def is_black(self):
        return self.opening > self.closing

    def is_white(self):
        return self.opening < self.closing


class Chart(object):

    def __init__(self, name, candles):
        self.name = name
        self.candles = candles
