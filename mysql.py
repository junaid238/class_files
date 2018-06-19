# python standard fr db is DB-API
# MySQL C API --> MySQLdb 
import pymysql
from python_mysql_dbconfig import read_db_config
# make a connection to DB
# conn = pymysql.connect(host='localhost',database='dbdemo',user='root',password='khan')
# print(conn)
def connect():
	dbDetails = read_db_config()
	try:
		# conn = pymysql.connect(host='localhost',database='dbdemo',user='root',password='khan')
		conn = pymysql.connect(**dbDetails)

		if conn:
			print("Db is connected successfully")
		
	except Exception as e:
		print(e)
	finally:
		conn.close()
		print("closed the connection")

connect()

