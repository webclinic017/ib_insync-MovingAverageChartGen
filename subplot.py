from statistics import stdev

# create desired length moving average list of values for charting
def masubplot(length, closing_prices):
    ma_length = length
    i = 0
    averages = {'data':[]}
    while i < len(closing_prices) - ma_length + 1:
        this_window = closing_prices[i : i + ma_length]
        window_average = round(sum(this_window) / ma_length, 2)
        averages['data'].append(window_average)
        i += 1
    return averages

# create desired upper bollinger band list of values for charting
def upperbb_subplot(closing_prices, period, std):
    length = period
    i = 0
    bb = {'data':[]}
    while i < len(closing_prices) - length + 1:
        this_window = closing_prices[i : i + length]
        window_bb = round((sum(this_window) / length) + (2.5 * stdev(this_window)), 2)
        bb['data'].append(window_bb)
        i += 1
    return bb

# create desired lower bollinger band list of values for charting
def lowerbb_subplot(closing_prices, period, std):
    length = period
    i = 0
    bb = {'data':[]}
    while i < len(closing_prices) - length + 1:
        this_window = closing_prices[i : i + length]
        window_bb = round((sum(this_window) / length) - (2.5 * stdev(this_window)), 2)
        bb['data'].append(window_bb)
        i += 1
    return bb
