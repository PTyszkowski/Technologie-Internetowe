import requests as rq
import json
from datetime import date, timedelta
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-835DRDL;' #nazwa serwer (komputera)
                      'Database=Currency;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def API_call(api):
    api = rq.get(api).json()
    text = json.dumps(api,sort_keys=(True), indent = 4)
    x = json.loads(text)
    return x

def get_rates(currency, days):
    today =  str(date.today())
    days_ago = str(date.today() - timedelta(days=days))
    api = 'https://api.exchangeratesapi.io/history?start_at=' + days_ago + '&end_at=' + today + '&base=PLN'
    data = API_call(api)
    sum = 0
    rates = {}
    for d in data['rates'].keys():
        #rates.append(data['rates'][d]['EUR'])
        rates[d] = data['rates'][d]['EUR']
    return  rates

dates = []
today =  date.today()

EUR_rate = get_rates('USD', 365*5)

for i in range(365*5):
    dates.append(str(today - timedelta(days=i+1)))
dates.append(today)

print(len(list(EUR_rate.keys())))
print(len(dates))

last_rate = API_call('https://api.exchangeratesapi.io/' + str(today - timedelta(days=i)) + '?base=USD')['rates']['EUR']
up_or_down = {}

for i in dates:
    if i not in list(EUR_rate.keys()):
        EUR_rate[i] = last_rate
    if EUR_rate[i] > last_rate:
        up_or_down[i] = -1
    elif EUR_rate[i] < last_rate:
        up_or_down[i] = 1
    else:
        up_or_down[i] = 0
    last_rate = EUR_rate[i]

print(len(list(EUR_rate.keys())))
print(len(dates))

# for i in EUR_rate:
#     print('%s, %f'%(i ,EUR_rate[i]))

id = 0
for i in EUR_rate:
    cursor.execute("INSERT INTO Currency VALUES ('%d','PLN','USD','%f','%s')"%(id,EUR_rate[i],i))
    id += 1
#conn.commit()
print(up_or_down)