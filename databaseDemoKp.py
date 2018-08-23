# # mysql --> queries
# # python --> code

# # python + mysql 

# # connection
# # executing queries in python
# # check insertions in mysql

# # connector --> module /package -->  mysql , PyMysql , MysqlDB , . . . .
# # pip install <connector>

# # 4 inputs --> host    --> host -> localhost
# # 			 user 	 --> user -> root
# # 			 pwd	 --> password -> khan
# # 			 db name --> database -> kpdemo

# # PyMysql 
# # -------
# # import pymysql 

# # conn = pymysql.connect(host = "" , username = "" , password = "" , database = "")

# # connect() --> make connection object 
# # 						--> execute queries


# # if(conn):
# # 	print("success")
# # 	_____
# # 	_____
# # 	_____
# # else:
# # 	print("connection not made")

# # conn.close()



import pymysql
# # print(dir(pymysql))
# # print(pymysql.connect.__doc__)

# conn = pymysql.connect(host= "localhost" , user = "root" , password = "khan" , database = "kpdemo")
# if(conn):
# 	print("success")
# else:
# 	print("connection not made ")
# conn.close()

# config --> meta data 
# configuration file --> usage file 
# parsing 
# - xml , yaml , yml , ini , config 

# .ini
# 	- section 
# 	- data pairs 

# [<sectionname>]
# ___ = _____
# ___ = _____
# ___ = _____
# ___ = _____


# [mysql1]
# host = localhost
# user = root
# password = khan
# database = kpdemo

# [mysql2]
# host = localhost
# user = root
# password = khan
# database = gbdemo


# parsing --> configparser --> ConfigParser()
# 	inputs-> config file name 
# 		  -> section name

# 	output --> dictionary 

# 	dictionary  --> python file connect()


# from parsing import retDict
# dbdet = retDict(section = "mysqlT")
# conn = pymysql.connect(**dbdet)
# if(conn):
# 	print("success")
# else:
# 	print("connection not made ")
# conn.close()


# conn = pymysql.connect(____)
# cur = conn.cursor()

# queries --> string 
# conn object 
# execute query --> conn --> cur --> cur.execute(<query>) 
# cur.execute(<query>) --> True --> if done
# cur.execute(<query>) --> False --> if not done
# insert --> cur.execute(<query>) --> execute query in Python
# cur.commit() --> save into DB
# conn.close()


# getting of data --> select data --> table name 

# cur.lastrowid() --> latest insertion into db 
# one latest row --> cur.fetchone()
# fetchall()
# 	- all rows data 
# 	- collection 
# rows = cur.fetchall()

# for row in rows :
# 	print(row)

# fetchmany() --> ???

# c:/>python pwdmake.py show 
# ________
# ________
# ________
# ________

# c:/>python pwdmake.py khan
# jkedb390479jnrfkls 

# c:/>python pwdmake.py khan
# user exists 


# exception handling :
# -------------------
# - compile time errors --> developer 
# - run time errors --> end user 

# 	 errors
# error vs exception 

# 	exception 
# exceptions --> errors

# - handled exception
# - unhandled exception

# try , catch , final , finally 
# try , except , finally
# try , except , except , except , except ,finally

# throw --> raise 
# all exceptions --> classes 
# 				--> sub classes  of Exception super class


# try --> code expecting error 
# except --> handle the occured exceptions
# 		--> know the name of error and class 
# finally --> no error or errors 
# 		--> executed without fail 

# try except finally
# ___ XXXXXX _______ -> no error
# ___ ______ _______ -> error has been handled



# syntax
# ------
# try:
# 	________
# 	________ --> expected error code 
# 	________

# except <errorClassName>:
# 	print(<dialouge>)
# finally:
# 	<closing of files / connections>


# try:
# 	________
# 	________ --> expected error code 
# 	________
# except <errorClassName1>:
# 	print(<dialouge1>)
# except <errorClassName2>:
# 	print(<dialouge2>)
# except <errorClassName3>:
# 	print(<dialouge3>)
# finally:
# 	<closing of files / connections>



# try:
# 	________
# 	________ --> expected error code 
# 	________

# except <errorClassName1> , <errorClassName2> , <errorClassName3>:
# 	print(<common_dialouge>)
# finally:
# 	<closing of files / connections>


# try:
# 	________
# 	________ --> expected error code 
# 	________

# except Exception:
# 	print(<dialouge>)
# finally:
# 	<closing of files / connections>

# try:
# 	________
# 	________ --> expected error code 
# 	________

# except Exception as e :
# 	print(e)
# finally:
# 	<closing of files / connections>



# try :
# 	def addnums(a,b):
# 		res = a+b
# 		print(res)
# 		print(c) # NameError
# 		return res
# 	addnums(10,20) # TypeError
# except TypeError  :
# 	print("Type not matched")
# except NameError :
# 	print("Name not available")
# finally:
# 	print("Bye")
# def addnums(a,b):
# 		res = a+b
# 		print(res)
# 		return res
# addnums(10,"b")

# area(l , b)
#  --> nums 
#  --> positive 
#  --> XX 0 XX