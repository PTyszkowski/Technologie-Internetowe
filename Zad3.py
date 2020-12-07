import requests as rq
import json
from datetime import date, timedelta
import matplotlib.pyplot as plt

def API_call(api):

    api = rq.get(api).json()
    text = json.dumps(api,sort_keys=(True), indent = 4)
    x = json.loads(text)
    return x
def latest_rate_average(currency, days):
    today =  str(date.today())
    days_ago = str(date.today() - timedelta(days=days))
    api = 'https://api.exchangeratesapi.io/history?start_at=' + days_ago + '&end_at=' + today + '&base=PLN'
    data = API_call(api)
    sum = 0
    for rating_date in data['rates']:
        sum += data['rates'][rating_date][currency]
    return sum/len(data['rates'])

def latest_rate_plot(currency, days):
    today =  str(date.today())
    days_ago = str(date.today() - timedelta(days=days))
    api = 'https://api.exchangeratesapi.io/history?start_at=' + days_ago + '&end_at=' + today + '&base=PLN'
    data = API_call(api)
    rates = []
    for rating_date in data['rates']:
        rates.append(data['rates'][rating_date][currency])
    plt.plot(rates)
    plt.legend([currency, "rate"])



print(latest_rate_average('EUR',365/2))
print(latest_rate_average('USD',365/2))
latest_rate_plot('EUR',365/2)
latest_rate_plot('USD',365/2)

plt.title("USD and EUR rates")
plt.xlabel("time (days)")
plt.ylabel("rate (base PLN)")
plt.show()
plt.savefig("USD_and_EUR_rates.eps")