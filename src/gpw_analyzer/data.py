class Candle(object):

    def __init__(self, opening, closing, minimum, maximum, volume):
        self.opening = opening
        self.closing = closing
        self.min = minimum
        self.max = maximum
        self.volume = volume

    def is_black(self):
        return self.opening > self.closing

    def is_white(self):
        return self.opening < self.closing


class Chart(object):

    def __init__(self, name, candles):
        self.name = name
        self.candles = candles
