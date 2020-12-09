
import pymssql
import requests
import json
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt




conn = pymssql.connect(server = 'Adrian-Komputer', database = 'Lab7')

cursor = conn.cursor()




startDate = '2019-11-11'
endDate = '2020-10-18'
resp2_USD = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/USD/'+startDate+'/'+endDate+'/?format=json')
resp1_USD = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/USD/2018-11-12/2019-11-11/?format=json')
print(resp1_USD)
print(resp2_USD)


usd_rates = []
usd_dates = []

for i in resp1_USD.json()['rates']:
    usd_rates.append(i['mid'])
    usd_dates.append(i['effectiveDate'])

for i in resp2_USD.json()['rates']:
    usd_rates.append(i['mid'])
    usd_dates.append(i['effectiveDate'])

dates = []

sdate = date(2018, 11, 12)
edate= date(2020, 10, 18)

delta = edate-sdate
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates.append(day)


#skopiowanie istniejących wartości
rates = np.zeros_like(dates)

for i in range(len(dates)):
    for j in range(len(usd_dates)):
        if dates[i].strftime('%Y-%m-%d') == usd_dates[j]:
            rates[i] = usd_rates[j]





#uzupełnianie pustych wartości
for i in range(len(rates)):
    if rates[i] == 0:
        rates[i] = rates[i-1]


for i in range(len(dates)):
    print(type(dates[i]))
    cursor.execute("INSERT INTO dbo.Currency(ID, BaseCurrency, Currency, Rate , Date) VALUES ({}, 'pln', 'usd', {},CONVERT(VARCHAR(10), {}, 111))".format(i, rates[i],dates[i] ))

conn.commit()

cursor.execute('select * from dbo.Currency')
row = cursor.fetchone()
while(row):
    print(row)
    row = cursor.fetchone()

