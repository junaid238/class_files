import pymysql
from python_mysql_dbconfig import read_db_config
def makeTable():
	dbdetails = read_db_config()
	try:
		conn = pymysql.connect(**dbdetails)
		if conn:
			print("connection is successfull")
			cur = conn.cursor()
			# print(cur)
			qu = '''CREATE TABLE IF NOT EXISTS users (
						id int(11) NOT NULL AUTO_INCREMENT,
							email varchar(45),
							password varchar(45),
								PRIMARY KEY (id)
								);'''
			a = cur.execute(qu)
			if a :
				print('table created good')
	except Exception as e:
		print(e)
	finally:
		conn.close()
		print("connection closed")

def getData(tablename):
	dbdetails = read_db_config()
	try:
		conn = pymysql.connect(**dbdetails)
		if conn:
			print("connection is successfull")
			cursor = conn.cursor()
			selectQ = "SELECT * FROM %s" %(tablename)
			cursor.execute(selectQ)
			rows = cursor.fetchall()
			for row in rows:
				print(row)
	except Exception as e:
		print(e)
	finally:
		conn.close()
		print("connection closed")

def insert_data(user , pwd):
 
	try:
		db_config = read_db_config()
		conn = pymysql.connect(**db_config)
		cursor = conn.cursor()
		sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
		cursor.execute(sql, (user, pwd)) 
		if cursor.lastrowid:
			print('last insert id', cursor.lastrowid)
		else:
			print('last insert id not found')
 
		conn.commit()
	except Exception as e:
		print(e)
 
	finally:
		cursor.close()
		conn.close()
 
# makeTable()
# insert_data("khan" , "9876")
getData("users")