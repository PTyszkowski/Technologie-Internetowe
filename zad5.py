


import pymssql
import requests
import json
import numpy as np
from datetime import date, timedelta





conn = pymssql.connect(server = 'Adrian-Komputer', database = 'Lab7')
cursor = conn.cursor()




cursor.execute('select Date from dbo.Currency')





#pobieranie dat
A = []
row = cursor.fetchone()
while row:
    A.append(row[0].strftime('%Y-%m-%d'))
    row = cursor.fetchone()





dates = sorted(list(dict.fromkeys(A)))




rates = np.zeros_like(dates)
for i in range(len(dates)):
    try:
        resp = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/USD/'+dates[i]+'/?format=json')
        x = resp.json()['rates'][0]['mid']
        rates[i] = x
    except:
        continue




#uzupełnianie kursów
for i in range(len(rates)):
    if rates[i] == '':
        rates[i] = rates[i-1]



q = """select OrderDate from dbo.Sales_time """


for i in range(100):

    cursor.execute(q, i+1)
    row = cursor.fetchone()
    data = row[0].strftime('%Y-%m-%d')

    mySql_insert_query_value = """update dbo.Sales_Product set pln_value = ListPrice * %s where  = %d"""
    try:
        a = dates.index(data)
    except: print('not in list')
    try:
        recordTuple_value = (rates[a], i+1)
        cursor.execute(mySql_insert_query_value % recordTuple_value)
    except: print('lipa')
#

conn.commit()

