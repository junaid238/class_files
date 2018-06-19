import pymysql
from configParserGB import readFile
dbdetails = readFile()
try:
	# making a connection object 
	conn = pymysql.connect(**dbdetails)
	# making a cursor object cur
	cur = conn.cursor()
	if conn:
		print("connection is successful")
	else:
		print("connection is not successful")
	names = ["M.Anand Rahul","adarsh Sharma","Robin Babu P","Deba Prasad Mishra","Sowjanya","Kariveda Vishal Reddy","D.Suresh Kumar","D Suresh Kumar friend ","D Suresh Kumar friend ","D Suresh Kumar friend ","Shravan Kumar.M","Shravan Kumar friend ","Shravan Kumar friend ","Shravan Kumar friend ","tirunagari Raghavendra"]
	mobiles = ["8143827119","7702323131","7384426616","9581912305","9100593362","9640582662","9959965968","9959965968","9959965968","9959965968","9885569118","9885569118","9885569118","9885569118","9700149039"]

	'''CreQ = "CREATE table class(id INT(45) NOT NULL AUTO_INCREMENT , name VARCHAR(56) NOT NULL , mobile VARCHAR(16) NOT NULL , PRIMARY KEY (id) )" '''
	# execute the query 
	# cur.execute(CreQ)
	insQ = "INSERT into class(id , name , mobile) VALUES (NULL, %s , %s)"
	namesMobiles = dict(zip(names , mobiles))
	# print(namesMobiles)
	for i in namesMobiles:
		cur.execute(insQ , (i, namesMobiles[i]))
	# # do commit the query for insert using connection
		conn.commit()
except Exception as e:
	print(e) 
finally:
	conn.close()
	print("connection has been closed")
