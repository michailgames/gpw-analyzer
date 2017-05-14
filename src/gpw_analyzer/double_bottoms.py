def find_full_candle_breakthrough(candles, max_candles=50):
    effective_candles = candles[-max_candles:]
    if len(effective_candles) < 2:
        return None
    today = effective_candles[-1]
    yesterday = effective_candles[-2]
    if not today.is_white() or today.closing <= max(
            yesterday.closing, yesterday.opening):
        return None

    bottom_candles = None
    for i, candle in reversed(list(enumerate(effective_candles[:-2]))):
        if candle.max > today.closing:
            bottom_candles = effective_candles[i + 1:-1]
            break
    if not bottom_candles:
        return None

    middle_index, middle_max = max(
        enumerate([c.max for c in bottom_candles]), key=lambda p: p[1])
    if middle_max > yesterday.closing:
        left_candles = bottom_candles[1:middle_index]
        right_candles = bottom_candles[middle_index + 1: -1]
        return True
    else:
        return None
