# import pyodbc 
# # Some other example server values are
# # server = 'localhost\sqlexpress' # for a named instance
# # server = 'myserver,port' # to specify an alternate port

# #cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=srisql.database.windows.net,1433;Database=srisql;Uid=srinik@srisql;Pwd=FinedayFineday@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
# cursor = cnxn.cursor()
import pymysql 

host = "pysqlhostserver.database.windows.net"
username = "srinik"
password = "FinedayFineday@123"
database = "pysql"
#Server=tcp:pysqlhostserver.database.windows.net,1433;Initial Catalog=pysql;Persist Security Info=False;User ID={your_username};Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
conn = pymysql.connect(host, username, password, database)
cursor = conn.cursor()


