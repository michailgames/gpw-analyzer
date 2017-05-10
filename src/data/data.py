class Candle(object):
    def __init__(self, opening, closing, minimum, maximum, volume):
        self.opening = opening
        self.closing = closing
        self.min = minimum
        self.max = maximum
        self.volume = volume