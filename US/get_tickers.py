import requests
import pandas
import io

url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'

dataString = requests.get(url).content
tickersRawData = pandas.read_csv(io.StringIO(dataString.decode('utf-8')))
print(tickersRawData)
#tickersRawData.to_csv("csv.csv")
#tickers = tickersRawData['Symbol'].tolist()
#print(tickers)
