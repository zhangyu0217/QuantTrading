import pandas
import io
import requests
import json

url = "http://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
response = requests.request("GET", url)
content = response.content
print(content)
# response.text返回的是 unicode 文本对象，response.content 返回的是 byte 文本对象a
tickersRawData = pandas.read_csv(io.StringIO(content.decode('utf-8')))
print(tickersRawData)
#content = json.loads(content)  # 将字符串数据转换成字典类型数据
tickers = tickersRawData['Symbol'].tolist()

file = "Tickers_list_US.csv"
tickersRawData.to_csv(file, index=False, encoding="utf-8")
