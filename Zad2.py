import pyodbc

f = open("Zad1.csv", "w")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-835DRDL;' #nazwa serwer (komputera)
                      'Database=Currency;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('CREATE TABLE Currency (ID int,BaseCurrency varchar(3), Currency varchar(3),Rate money,Date date)')