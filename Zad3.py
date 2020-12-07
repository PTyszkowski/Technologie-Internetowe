import requests as rq
import json
from datetime import date, timedelta

def API_call(api):

    api = rq.get(api).json()
    text = json.dumps(api,sort_keys=(True), indent = 4)
    x = json.loads(text)
    return x
def latest_rate(currency, days):
    today =  str(date.today())
    days_ago = str(date.today() - timedelta(days=days))
    api = 'https://api.exchangeratesapi.io/history?start_at=' + days_ago + '&end_at=' + today + '&base=PLN'
    data = API_call(api)
    sum = 0
    for rating_date in data['rates']:
        sum += data['rates'][rating_date][currency]
    return sum/len(data['rates'])

print(latest_rate('EUR',5))