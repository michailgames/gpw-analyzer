def find_full_candle_breakthrough(
        candles, max_candles=50, minimum_drop=0.05, max_bottoms_delta=0.03):
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
    if middle_max < yesterday.closing:
        return None

    left_candles = bottom_candles[1:middle_index]
    right_candles = bottom_candles[middle_index + 1: -1]
    if not left_candles or not right_candles:
        return None

    left_bottom = min(c.min for c in left_candles)
    right_bottom = min(c.min for c in right_candles)

    max_bottom_value = (1 - minimum_drop) * middle_max
    if left_bottom > max_bottom_value or right_bottom > max_bottom_value:
        return None

    lower_bottom = min(left_bottom, right_bottom)
    higher_bottom = max(left_bottom, right_bottom)
    if lower_bottom / higher_bottom < (1 - max_bottoms_delta):
        return None

    return True
