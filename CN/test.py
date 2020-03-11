import tushare as ts
import pandas as pd
import numpy as np

#pro = ts.pro_api("01ee66441ec5ceb98bcc821a667f2ccbaf7241580a02203cc19a452f")
#pro = ts.pro_api("01ee66441ec5ceb98bcc821a667f2ccbaf7241580a02203cc19a452f")
#help(pro)
#print(pro.stock_basic())
#a=pro.daily(ticker=600031,start_date='20180901', end_date='20181001')
#a.to_csv("test.csv")
#df = pro.query('daily', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
#stocks_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#print(stocks_list)


hist = ts.get_hist_data("600030")
print(hist)
#codes=[
#        (u'招商证券','600999'),(u'广发证券','000776'),(u'万科a','000002'),
#        (u'保利地产','600048'),(u'招商银行','600036'),(u'工商银行','601398'),
#        (u'恒瑞医药','600276'),(u'同仁堂','600685'),(u'大族激光','002008'),
#        (u'三安光电','600703'),(u'中国石油','601857'),(u'中国石化','600028'),
#        (u'ST中富','000659'),(u'ST山水','600234'),(u'沪深300','hs300')
#        ]
#
#for c in codes:
#    df=ts.get_hist_data(c[1],start='2007-10-31',end='2017-10-31')
#    df.to_csv('assets/'+c[0]+'.csv')
#    print ('now '+c[0]+' earliest='+str(df.index[-1]))
