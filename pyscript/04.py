import pymssql  

conn = pymssql.connect(server='10.99.110.150', user='a_lms', password=r'1234%abc', database='LMSJuly')  
cursor = conn.cursor()  
cursor.execute('SELECT TOP 100 CId,Id,Name FROM dbo.t_State;')  
row = cursor.fetchone()  
while row:  
    print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()


conn.close()

import _mssql

conn=_mssql.connect(server='10.99.110.150', user='a_lms', password=r'1234%abc', database='LMSJuly')
conn.execute_query('')
