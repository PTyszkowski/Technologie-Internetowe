import pyodbc

f = open("Zad1.csv", "w")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-835DRDL;' #nazwa serwer (komputera)
                      'Database=AdventureWorksTI2014;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT OH.CustomerID, SalesPersonID, StoreID,OH.TerritoryID, OH.AccountNumber FROM AdventureWorksTI2014.Sales.SalesOrderHeader OH JOIN AdventureWorksTI2014.Sales.Customer C ON OH.CustomerID = C.CustomerID')

f.write('CustomerID,SalesPersonID,StoreID,TerritoryID,AccountNumber\n')
for row in cursor:
    for i in str(row)[1:-1]:
        if i == ' ':
            continue
        if i == "'":
            continue
        else:
            f.write(i)
    f.write("\n")

f.close()