# encoding:utf-8
import tushare
import pandas
import datetime
import os
import time
import requests
import io
import json

def dataframeFromUrl(url):
    #    url = "http://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
#    response = requests.request("GET", url)
    response = requests.request("GET",url)
    content = response.text
#    with open("myCY2016.csv", "wb") as code:
#            code.write(content)

    print(content)
    # response.text返回的是 unicode 文本对象，response.content 返回的是 byte 文本对象a
    tickersRawData = pandas.read_csv(io.StringIO(content.decode('utf-8')), index_col=0)
    print(tickersRawData)
    return tickersRawData



def stockPriceIntraday(ticker, folder):
    #Step 1 get intraday data online
#    intraday = tushare.get_hist_data(ticker, ktype='5')
    url = 'http://quotes.money.163.com/service/chddata.html?code=0{ticker}&start=20000101&end=202000310&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'.format(ticker=ticker)
    print(url)
    intraday = dataframeFromUrl(url)
    print(intraday)
    #Step 2 if the history exists, append
    file = folder+"/"+ticker+'.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file,index_col=0)
        intraday.append(history)
    #Step 3 inverse based on index
    intraday.sort_index(inplace=True)
    intraday.index.name='timestamp'
    #Step 4 save
    intraday.to_csv(file)
    print("intraday for ["+ticker+"] saved")

start = time.time()

#Step 1 get the tickers online
tickersRawData = tushare.get_stock_basics()
print(tickersRawData)
tickers = tickersRawData.index.tolist()
print(tickersRawData)

#Step 2 save the ticker list to a local fila
dataToday = datetime.datetime.today().strftime('%y%m%d')
file = 'Tickers_list'+dataToday+'.csv'
tickersRawData.to_csv(file,encoding="utf-8")

print("Tickers saved")

# Step 3 get stock price (intrady) for all
for i, ticker in enumerate(tickers):
    try:
        print("Intraday", i, '/', len(tickers))
        stockPriceIntraday(ticker, folder="result_all")
    except:
        pass
#    if i> 3:
#        break

end = time.time()
print("finish all downloading")
print("total time : "+(str)(end-start)+" second")


