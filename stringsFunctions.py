# strings 
dia = "      I have a class at KP for Python   "
# strip()
# lstrip()
# rstrip()
# split()
# join()
# zfill()

# strip() --> remove white spaces from both ends of string
# <stringname>.strip()
# print(dia)
# print(dia.strip())

# lstrip() --> remove white spaces from left end of string
			# --> remove spaces and chars from left
			# --> recursive pattern match
# <stringname>.lstrip()
# <stringname>.lstrip(" <char>")
# print(dia.lstrip())
# print(dia.lstrip(" I"))

# stmt = "    iam ian a class in kp.  "
# print(stmt.lstrip())
# print(stmt.lstrip(" iam"))

# rstrip() --> remove white spaces from right end of string
			# --> remove spaces and chars from right
# <stringname>.rstrip()
# print(dia.rstrip())

# zfill() --> make data of uniform length (without changing tha value)
# 		--> purely string method 

# <stringname>.zfill(<length>)

# 001 001 001 
# 002 004 008
# 003 009 027
# 004 016 064 
# 005 025 125 
# a = "Python"
# print(a.zfill(10))

# split() --> cut the string at delimiter and output the substrings
# delimiter --> reference to cut 
# <stringname>.split() --> delimiter = " " / space 
# print(dia.split())
# <stringname>.split(<delimiter>)
# print(dia.split("a")) # delimiter = "a"

# join() ---> joins substrings with a delimiter into a string
# <delimiter>.join(<substrings>)

# ss = dia.split()
# newstr = "_".join(ss)
# print(newstr)

# conditional statements 
# ----------------------
#  -> descision tree 
#   	- condition (mandatory) -> if elif 
#   	- statement (mandatory)

# condition --> T/F
# statement --> anything 

# -> nested conditional statement
# if else
# if elif else 

# XX switch case XX

# syntax
# ------

# if <condition> :
# 	_____
# 	_____ -> statements
# else:
# 	_____
# 	_____-> statements

# if (<condition1>) :
# 	_____
# 	_____ -> statements
# elif(<condition2>):
# 	_____
# 	_____-> statements
# else:
# 	_____-> statement

# if (<condition1>):
# 	if (<condition11>):
# 		_____
# 	else:
# 		_____

# if (<condition1>):
# 	if (<condition11>):
# 		_____
	
# a = 14
# if a>10:
# 	print("greater than 10")
# else:
# 	print("less than 10")

# pass --> control statement --> if else , loops , funcs , class 

# a = 1
# if (a>10):
# 	pass
# else:
# 	print("less than 10")

# even or odd  --> is_num , is_numeric
# -----------
# num = int(input("Enter a number "))
# num = "khan"
# if type(num) is str:
# 	print("enter only numbers")
# else:
# 	if num%2 == 0 :
# 		print("even")
# 	else:
# 		print("odd")

# a = 1
# if a>10:
# 	print("gerater than 10")
# elif a==10:
# 	print("equals 10 ")
# else:
# 	print("less than 10")



# num --> input 

# 6
# multiple of 3 only
# 15 
# multiple of 3 and 5 
# 10 
# multiple of 5 only
# 23 
# multiple of none 
# 25 
# multiple of 5 only
# 30 
# multiple of 3 and 5 

# time ="03:15:34 PM"
# 15:15:34

# time ="08:15:34 AM"
# 08:15:34

# time ="12:00:00 AM"
# 00:00:00













