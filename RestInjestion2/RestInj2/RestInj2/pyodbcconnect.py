import os
import sys
import time
import pyodbc
import pandas as pd

host = "pysqlhostserver.database.windows.net"
username = "srinik"
password = "FinedayFineday@123"
database = "pysql"
#Server=tcp:pysqlhostserver.database.windows.net,1433;Initial Catalog=pysql;Persist Security Info=False;User ID={your_username};Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=server_name;'
#                       'Database=db_name;'
#                       'Trusted_Connection=yes;')

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                         'SERVER=tcp:pysqlhostserver.database.windows.net,1433;'
#                         'DATABASE=pysql;'
#                         'UID=srinik;'
#                         'PWD=FinedayFineday@123;')

conn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=tcp:pysqlhostserver.database.windows.net,1433;'
                        'DATABASE=pysql;'
                        'UID=srinik;'
                        'PWD=FinedayFineday@123;')

cursor = conn.cursor()

cursor.execute('SELECT * FROM sys.tables where type=\'u\'')

Tables = cursor.fetchall()




# All tables, views, functions
#cursor.execute('SELECT * FROM sys.objects')



#print('Total tables: ?'format(len(cursor)))


for each_table in Tables:
    print('Table Name0 : ' + each_table[0])
    #cursor.execute("SELECT * from {}".format(each_table[0]))
    #i+=1
    tableResult = pd.read_sql("SELECT * from {}".format(each_table[0]), conn)
    for rows in tableResult:
      print(rows)
    #cursor2.close()
cursor.close()