def find_prosperity_engulfings(charts):
    return filter(lambda chart: is_prosperity_engulfing(chart.candles), charts)


def is_prosperity_engulfing(candles):
    if len(candles) < 2:
        return False
    current = candles[-1]
    previous = candles[-2]
    return (previous.is_black() and current.opening <
            previous.closing and current.closing > previous.opening)
