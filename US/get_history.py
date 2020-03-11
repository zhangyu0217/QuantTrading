import pandas
import io
import requests
import json
import os
import time
import yfinance as yf
import datetime

def dataframeFromUrl(url):
#    url = "http://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
    response = requests.request("GET", url)
    content = response.content
    # response.text返回的是 unicode 文本对象，response.content 返回的是 byte 文本对象a
    tickersRawData = pandas.read_csv(io.StringIO(content.decode('utf-8')), index_col=0)
    return tickersRawData

def stockPriceIntraday(ticker, folder, start, end):
    # Step 1. get data online
#    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&outputsize=full&apikey=H28WP5KK9APTZX3H&datatype=csv'.format(ticker=ticker)
#    intraday = dataframeFromUrl(url)
    start_time=time.time()
    yf_ticker = yf.Ticker(ticker)
    #intraday = yf_ticker.history(start = start, end=end)
    intraday = yf_ticker.history(period="max")
    # Step 2, append if history exists
    file = folder+"/"+ticker+".csv"
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    # Step 3, reverse based on index
    intraday.sort_index(inplace=True)
    # Step 4, save
    intraday.to_csv(file)
    end_time=time.time()
    print("intraday for ["+ticker+"} saved")
    print("Using "+(str)(end_time-start_time)+" second!")






start=time.time()

url = "http://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
response = requests.request("GET", url)
content = response.content
tickersRawData = pandas.read_csv(io.StringIO(content.decode('utf-8')))
tickers = tickersRawData['Symbol'].tolist()

# Step 3, gt stock price(intraday)
starttime=(datetime.datetime.now()+datetime.timedelta(days=-14)).strftime("%Y-%m-%d")
endtime=(datetime.datetime.now()+datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
for i,ticker in enumerate(tickers):
    if i < 978 :
        continue
    try:
        print("Intraday",i,"/",len(tickers))
        print(ticker)
        stockPriceIntraday(ticker,folder="result",start = starttime,end = endtime)
        time.sleep(12)
    except:
        pass
#    if i>0:
#        break
end=time.time()

#stockPriceIntraday("NVDA", folder="result")

print("intraday for all stocks got.")
print("using time "+(str)(end-start)+" second")
