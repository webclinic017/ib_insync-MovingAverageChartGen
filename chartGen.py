# from ib_insync import*
import mplfinance as mpf
import os
from buckets import *
from datetime import datetime, date
today_date = date.today().strftime('%m-%d-%y')

from subplot import masubplot, upperbb_subplot, lowerbb_subplot
from googledrive import gdrive_authentication, gdrive_new_daily_folder, gdrive_file_upload
from ib_api import fetch_ibdata, extract_closing_price, reformat_IBdata, ib


# create chart of candlesticks, 9SMA, 20SMA, 50SMA, 200SMA, Bollinger Bands for stocks w/ full data
def plot_d(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, numofdays, ticker, defining_ma):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff', width=1)
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06', width=1)
    sma50dict = mpf.make_addplot(sma50['data'][-numofdays:], color='#3a7821', width=1)
    sma200dict = mpf.make_addplot(sma200['data'][-numofdays:], color='#483e8b', width=1)
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c', width=1)
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c', width=1)
    mpf.plot(pdata[-numofdays:], type='candle', style='charles',
                addplot=[sma9dict, sma20dict, sma50dict, sma200dict, lowerbbdict, upperbbdict],
                # figscale=.9,
                tight_layout=False,
                ylabel='',
                savefig=f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf''')
    chartFilePath = f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf'''
    chartFileTitle = f'''{ticker}_{defining_ma}_{today_date}.pdf'''
    # gdrive_file_upload(drive, daily_folder_id, chartFilePath, chartFileTitle)

# create chart of candlesticks, 9SMA, 20SMA, 50SMA, Bollinger Bands for stocks w/ partial data
def plot_j1(pdata, sma9, sma20, sma50, lowerbb, upperbb, numofdays, ticker, defining_ma):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff', width=1)
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06', width=1)
    sma50dict = mpf.make_addplot(sma50['data'][-numofdays:], color='#3a7821', width=1)
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c', width=1)
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c', width=1)
    mpf.plot(pdata[-numofdays:], type='candle', style='charles',
                addplot=[sma9dict, sma20dict, sma50dict, lowerbbdict, upperbbdict],
                # figscale=.9,
                tight_layout=False,
                ylabel='',
                savefig=f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf''')
    chartFilePath = f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf'''
    chartFileTitle = f'''{ticker}_{defining_ma}_{today_date}.pdf'''
    # gdrive_file_upload(drive, daily_folder_id, chartFilePath, chartFileTitle)

# create chart of candlesticks, 9SMA, 20SMA, Bollinger Bands for stocks w/ less days of data
def plot_j2(pdata, sma9, sma20, lowerbb, upperbb, numofdays, ticker, defining_ma):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff', width=1)
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06', width=1)
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c', width=1)
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c', width=1)
    mpf.plot(pdata[-numofdays:], type='candle', style='charles',
                addplot=[sma9dict, sma20dict, lowerbbdict, upperbbdict],
                # figscale=.9,
                tight_layout=False,
                ylabel='',
                savefig=f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf''')
    chartFilePath = f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf'''
    chartFileTitle = f'''{ticker}_{defining_ma}_{today_date}.pdf'''
    # gdrive_file_upload(drive, daily_folder_id, chartFilePath, chartFileTitle)

# create abbreviated chart of candlesticks, 9SMA, 20SMA, Bollinger Bands for stocks w/ minimal days of data
def plot_j3(pdata, sma9, sma20, lowerbb, upperbb, numofdays, ticker, defining_ma):
    sma9dict = mpf.make_addplot(sma9['data'][-numofdays:], color='#c87cff', width=1)
    sma20dict = mpf.make_addplot(sma20['data'][-numofdays:], color='#f28c06', width=1)
    lowerbbdict = mpf.make_addplot(lowerbb['data'][-numofdays:], color='#b90c0c', width=1)
    upperbbdict = mpf.make_addplot(upperbb['data'][-numofdays:], color='#b90c0c', width=1)
    mpf.plot(pdata[-numofdays:], type='candle', style='charles',
                addplot=[sma9dict, sma20dict, lowerbbdict, upperbbdict],
                # figscale=.9,
                tight_layout=False,
                ylabel='',
                savefig=f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf''')
    chartFilePath = f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}/{ticker}_{defining_ma}_{today_date}.pdf'''
    chartFileTitle = f'''{ticker}_{defining_ma}_{today_date}.pdf'''
    # gdrive_file_upload(drive, daily_folder_id, chartFilePath, chartFileTitle)

# print best chart possible for available days of data... if ValueError still persists, print len of lists for debugging
def plot_total(bucket, bucket_nickname, days):
    try:
        plot_d(pdata, sma9, sma20, sma50, sma200, lowerbb, upperbb, days, bucket[security][0], bucket_nickname)
    except ValueError:
        try:
            plot_j1(pdata, sma9, sma20, sma50, lowerbb, upperbb, days, bucket[security][0], bucket_nickname)
        except ValueError:
            try:
                plot_j2(pdata, sma9, sma20, lowerbb, upperbb, days, bucket[security][0], bucket_nickname)
            except ValueError:
                try:
                    plot_j3(pdata, sma9, sma20, lowerbb, upperbb, 40, bucket[security][0], bucket_nickname)
                except ValueError:
                    print(f'''pdata: {len(pdata[-40:])}''')
                    print(f'''Closings: {len(closing_prices[-40:])}''')
                    print(f'''9SMA: {len(sma9['data'][-40:])}''')
                    print(f'''20SMA: {len(sma20['data'][-40:])}''')
                    print(f'''50SMA: {len(sma50['data'][-40:])}''')
                    print(f'''200SMA: {len(sma200['data'][-40:])}''')
                    print(f'''lowerBB: {len(lowerbb['data'][-40:])}''')
                    print(f'''upperBB: {len(upperbb['data'][-40:])}''')
    except IndexError:
        try:
            plot_j1(pdata, sma9, sma20, sma50, lowerbb, upperbb, days, bucket[security][0], bucket_nickname)
        except IndexError:
            try:
                plot_j2(pdata, sma9, sma20, lowerbb, upperbb, days, bucket[security][0], bucket_nickname)
            except IndexError:
                try:
                    plot_j3(pdata, sma9, sma20, lowerbb, upperbb, 40, bucket[security][0], bucket_nickname)
                except IndexError:
                    print(f'''pdata: {len(pdata[-40:])}''')
                    print(f'''Closings: {len(closing_prices[-40:])}''')
                    print(f'''9SMA: {len(sma9['data'][-40:])}''')
                    print(f'''20SMA: {len(sma20['data'][-40:])}''')
                    print(f'''50SMA: {len(sma50['data'][-40:])}''')
                    print(f'''200SMA: {len(sma200['data'][-40:])}''')
                    print(f'''lowerBB: {len(lowerbb['data'][-40:])}''')
                    print(f'''upperBB: {len(upperbb['data'][-40:])}''')
# list to be appended with stocks that meet conditions to prevent chart duplicates
hits = []


# # connect to IBKR api (TWS Workstation Paper Trading)
# ib = IB()
# if ib.isConnected() == False:
#     ib.connect('127.0.0.1', 7497, clientId=4)

# connect to IBKR api (TWS Workstation Paper Trading)
if ib.isConnected() == False:
    ib.connect('127.0.0.1', 4002, clientId=4)

# create new folder daily to store charts
path = f'''/Users/mike/Desktop/ib_insync-MovingAverageChartGen/9-200SMA_{today_date}'''
os.mkdir(path)

# drive = gdrive_authentication()
# daily_folder_id = gdrive_new_daily_folder(drive)


# cycle through all baskets indefinitely, print chart when conditions are met
while True:
    for security in range(len(SMA9_securities)):
        ib.sleep(1)
        fetched_data = fetch_ibdata(SMA9_securities[security][0], SMA9_securities[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma9 = masubplot(9, closing_prices)
        if SMA9_securities[security][0] not in hits:
            if (closing_prices[len(closing_prices)-1] < (SMA9_securities[security][4] * sma9['data'][len(sma9['data'])-1])):
                hits.append(SMA9_securities[security][0])
                sma20 = masubplot(20, closing_prices)
                sma50 = masubplot(50, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total(SMA9_securities, '9SMA', 60)
            else:
                print(f'''{SMA9_securities[security][0]} not in buying range.''')
    print(hits)

    for security in range(len(SMA20_securities)):
        ib.sleep(1)
        fetched_data = fetch_ibdata(SMA20_securities[security][0], SMA20_securities[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma20 = masubplot(20, closing_prices)
        if SMA20_securities[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < (SMA20_securities[security][4] * sma20['data'][len(sma20['data'])-1]):
                hits.append(SMA20_securities[security][0])
                sma9 = masubplot(9, closing_prices)
                sma50 = masubplot(50, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total(SMA20_securities, '20SMA', 75)
            else:
                print(f'''{SMA20_securities[security][0]} not in buying range.''')
    print(hits)

    for security in range(len( SMA50_securities_A)):
        ib.sleep(1)
        fetched_data = fetch_ibdata( SMA50_securities_A[security][0],  SMA50_securities_A[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma50 = masubplot(50, closing_prices)
        if  SMA50_securities_A[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < ( SMA50_securities_A[security][4] * sma50['data'][len(sma50['data'])-1]):
                hits.append( SMA50_securities_A[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total( SMA50_securities_A, '50SMA', 120)
            else:
                print(f'''{ SMA50_securities_A[security][0]} not in buying range.''')
    print(hits)

    for security in range(len( SMA50_securities_B)):
        ib.sleep(1)
        fetched_data = fetch_ibdata( SMA50_securities_B[security][0],  SMA50_securities_B[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma50 = masubplot(50, closing_prices)
        if  SMA50_securities_B[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < ( SMA50_securities_B[security][4] * sma50['data'][len(sma50['data'])-1]):
                hits.append( SMA50_securities_B[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total( SMA50_securities_B, '50SMA', 120)
            else:
                print(f'''{ SMA50_securities_B[security][0]} not in buying range.''')
    print(hits)

    for security in range(len( SMA50_securities_C)):
        ib.sleep(1)
        fetched_data = fetch_ibdata( SMA50_securities_C[security][0],  SMA50_securities_C[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma50 = masubplot(50, closing_prices)
        if  SMA50_securities_C[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < ( SMA50_securities_C[security][4] * sma50['data'][len(sma50['data'])-1]):
                hits.append( SMA50_securities_C[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total( SMA50_securities_C, '50SMA', 120)
            else:
                print(f'''{ SMA50_securities_C[security][0]} not in buying range.''')
    print(hits)

    for security in range(len(SMA200_securities)):
        ib.sleep(1)
        fetched_data = fetch_ibdata(SMA200_securities[security][0], SMA200_securities[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        sma200 = masubplot(200, closing_prices)
        if SMA200_securities[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < (SMA200_securities[security][4] * sma200['data'][len(sma200['data'])-1]):
                hits.append(SMA200_securities[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma50 = masubplot(50, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total(SMA200_securities, '200SMA', 120)
            else:
                print(f'''{SMA200_securities[security][0]} not in buying range.''')
    print(hits)

    for security in range(len(BB_securities)):
        ib.sleep(1)
        fetched_data = fetch_ibdata(BB_securities[security][0], BB_securities[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
        if BB_securities[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] < (1 * lowerbb['data'][len(lowerbb['data'])-1]):
                hits.append(BB_securities[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma50 = masubplot(50, closing_prices)
                sma200 = masubplot(200, closing_prices)
                upperbb = upperbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total(BB_securities, 'LowerBB', 120)
            else:
                print(f'''{BB_securities[security][0]} not in buying range.''')
    print(hits)

    for security in range(len(BB_securities)):
        ib.sleep(1)
        fetched_data = fetch_ibdata(BB_securities[security][0], BB_securities[security][1], '365 D')
        closing_prices = extract_closing_price(fetched_data)
        upperbb = upperbb_subplot(closing_prices, 20, 2.5)
        if BB_securities[security][0] not in hits:
            if closing_prices[len(closing_prices)-1] > (1 * upperbb['data'][len(upperbb['data'])-1]):
                hits.append(BB_securities[security][0])
                sma9 = masubplot(9, closing_prices)
                sma20 = masubplot(20, closing_prices)
                sma50 = masubplot(50, closing_prices)
                sma200 = masubplot(200, closing_prices)
                lowerbb = lowerbb_subplot(closing_prices, 20, 2.5)
                pdata = reformat_IBdata(fetched_data)
                plot_total(BB_securities, 'UpperBB', 120)
            else:
                print(f'''{BB_securities[security][0]} not in buying range.''')
    print(hits)
