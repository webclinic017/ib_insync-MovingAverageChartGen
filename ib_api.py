# ib_insync makes IBKR interface simpler
from ib_insync import *
import pandas as pd
from datetime import datetime, date

ib = IB()

# get daily historical bar data from IBKR api
def fetch_ibdata(ticker, prime_exch, data_barcount):
    stock = Stock(ticker, 'SMART', 'USD', primaryExchange = prime_exch)
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=data_barcount, #365days max
        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
    bars = util.tree(bars)
    return bars

# reduce bar data down to closing price for easy moving avg calculation
def extract_closing_price(singlestock_bardata):
    closing_prices = []
    for day in range(len(singlestock_bardata)):
        closing_prices.append((singlestock_bardata[day]['BarData']['close']))
    return closing_prices

# reformat dict of IBKR values for mplfinance charting
def reformat_IBdata(fetched_data):
    reformatted_data = {}
    reformatted_data['Date'] = []
    reformatted_data['Open'] = []
    reformatted_data['High'] = []
    reformatted_data['Low'] = []
    reformatted_data['Close'] = []
    for dict in range(len(fetched_data)):
        reformatted_data['Date'].append(datetime.strptime(str(fetched_data[dict]['BarData']['date']), '%Y-%m-%d'))
        reformatted_data['Open'].append(fetched_data[dict]['BarData']['open'])
        reformatted_data['High'].append(fetched_data[dict]['BarData']['high'])
        reformatted_data['Low'].append(fetched_data[dict]['BarData']['low'])
        reformatted_data['Close'].append(fetched_data[dict]['BarData']['close'])
    # print("reformatted data:", reformatted_data)
    pdata = pd.DataFrame.from_dict(reformatted_data)
    pdata.set_index('Date', inplace=True)
    return pdata
