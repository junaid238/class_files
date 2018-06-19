import pymysql
from configparserpy import getcreds
try:
	# conn = pymysql.connect(host="localhost" , user = "root" , password="khan" , database = "demodb")
	dbdetails = getcreds()
	# establishing a connection
	conn = pymysql.connect(**dbdetails)
	cur = conn.cursor()
	if conn:
		print("connection made successfully")
		# making a cursor object
		'''creQ = "CREATE table IF NOT EXISTS caseHarshith(id int(45) NOT NULL AUTO_INCREMENT,name VARCHAR(256) NOT NULL, mobile VARCHAR(45) NOT NULL, PRIMARY KEY (id))"
		cur.execute(creQ)'''
		names = ["M.Anand Rahul","adarsh Sharma","Robin Babu P","Deba Prasad Mishra","Sowjanya","Kariveda Vishal Reddy","D.Suresh Kumar","D Suresh Kumar friend ","D Suresh Kumar friend ","D Suresh Kumar friend ","Shravan Kumar.M","Shravan Kumar friend ","Shravan Kumar friend ","Shravan Kumar friend ","tirunagari Raghavendra"]
		mobiles = ["8143827119","7702323131","7384426616","9581912305","9100593362","9640582662","9959965968","9959965968","9959965968","9959965968","9885569118","9885569118","9885569118","9885569118","9700149039"]
		namesMobiles = dict(zip(names, mobiles))
		print(namesMobiles)
		for i in namesMobiles:
			insQ = "INSERT INTO `caseHarshith`(`id`,`name`,`mobile`) VALUES (NULL,%s,%s)"
			cur.execute(insQ,( i , namesMobiles[i]))
			conn.commit()


except Exception as e:
	print(e)

finally:
	conn.close()
	print("connection has been closed ")
