import requests
from io import StringIO
import pandas as pd
import numpy as np
import time
from datetime import datetime
date="20220201"
counter=250
#r = pd.read_html("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20220223&stockNo=2630")
#d=pd.read_html("https://www.tej.com.tw/webtej/doc/uid.htm")
#print(r[0].head())
#table=pd.read_excel("C:\\Users\\starg\\Downloads\\StockTable.xls",engine="xlrd")
import twstock
total=[]
for i in twstock.codes:
    total.append(twstock.codes[i])
df2=pd.DataFrame(total)
subdf=df2[df2["market"]=="上市"]
print(subdf)
date=datetime(2020,1,1)
for i in subdf["code"]:
    while date<datetime(2022,2,22):
        print(date)

        status=False
        try:
            print("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20220223&stockNo="+i)
            r=pd.read_html("https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20220223&stockNo="+i)
            print(r[0].head())
        except:
            print("not exist")
        time.sleep(5)
        date=date+datetime.timedelta(days=1)

