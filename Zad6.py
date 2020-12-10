import pyodbc
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-835DRDL;' #nazwa serwer (komputera)
                      'Database=Currency;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT SUM(SubTotalPLN), SUM(SubTotal), OrderDate FROM SalesOrdeHeader GROUP BY OrderDate ORDER BY OrderDate')

a = cursor.fetchall()

USD = []
PLN = []
dates = []
for i in a:
    PLN.append(i[0])
    USD.append(i[1])
    dates.append(i[2])

plt.subplot(2, 1, 1)
plt.plot(dates, USD)
plt.title('Sales in USD')
plt.ylabel('Sales Value')


plt.subplot(2, 1, 2)
plt.plot(dates, PLN)
plt.xlabel('Sales in PLN')
plt.ylabel('Sales Value')

plt.show()
plt.savefig("USD_PLN_Sales.eps")