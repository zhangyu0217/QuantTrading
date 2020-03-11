# encoding:utf-8
import tushare
import pandas
import datetime

#Step 1 get the tickers online
tickersRawData = tushare.get_stock_basics()
print(tickersRawData)
#tickers = tickersRawData.index.tolist()
print(tickersRawData)

#Step 2 save the ticker list to a local fila
dataToday = datetime.datetime.today().strftime('%y%m%d')
file = 'Tickers_list'+dataToday+'.csv'
tickersRawData.to_csv(file,encoding="utf_8_sig")

print("Tickers saved")

