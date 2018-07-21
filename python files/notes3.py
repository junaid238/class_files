# 2 versions --> single machine
# default --> python --> 2.7
# explicilty --> python3 --> 3.x

# strings 
tech = "    python is an easy langauge.    "

# functions  ---> immutable 
# membership operators -> check --> in , not in --> T/F
# <char/substring> in <strName>
# <char/substring> not in <strName>
# print("a" in tech)
# print("z" not in tech)
# name = "Python"
# identity operators --> is , is not --> T/F
# exact copy of string
# print("Python" is not name )
# print("Python" is name )

# tech = "python is an easy langauge. "
# print(tech[5]) # n
# char assignment 
# tech[5] = "m"
# char  deletion
# del tech[5]
# deletion of entire string
# del tech
# print(tech)
# functions
# ---------
# checking  --> startswith() , endswith() -> T/F
# case based --> upper() , lower() , title() , capitalize() , swapcase()
# operational 
# -> len()
# -> count()
# -> split()
# -> join()
# -> strip()
# -> lstrip()
# -> rstrip()
# -> replace()
# -> index()
# -> find()
# -> zfill()

# types
# -----
# -> attribute fetching functions ( . )
# -> parameterised functions (<something>)

# <strName>.startswith(<substring>)
# print(tech.startswith("P"))
# print(tech.startswith("Pyt"))
# print(tech.startswith("z"))
# <strName>.endswith(<substring>)
# print(tech.endswith(" "))
# print(tech.endswith("e. "))
# print(tech.endswith("P"))

# <strName>.lower() --> return string with entire lower case
# print(tech.lower())
# # <strName>.upper() --> return string with entire upper case
# print(tech.upper())
# # <strName>.swapcase() --> swaps case of each character
# print(tech.swapcase())
# # <strName>.title() --> capital case of each word
# print(tech.title())
# # <strName>.capitalize() --> capitalize first char of string
# print(tech.capitalize())

# len(<strName>) --> length of string --> highest index + 1
# print(len(tech)) # 28
# <strName>.count(<char/substring>) --> number of repetitions of a char/substring
# print(tech.count("a"))
# print(tech.count("q"))
# print(tech.count("easy"))
# <strName>.index(<char/substring>) --> index value of a char (first occurence) from a string
# print(tech.index("n")) # 5
# print(tech.index("an")) # 10
# print(tech.index("z")) # error for unexisting  char
# <strName>.index(<char/substring> , <start> , <end>)
# print(tech.index("n" , 6)) # start = 6
# print(tech.index("n" , 6 , 22)) # start = 6 , end = 22
# find() --> index() --> replica
# <strName>.find(<char/substring>) --> index value of a char (first occurence) from a string
# print(tech.find("n")) # 5
# print(tech.find("an")) # 10
# print(tech.find("z")) # -1 for unexisting char
# <strName>.find(<char/substring> , <start> , <end>)
# print(tech.find("n" , 6)) # start = 6
# print(tech.find("n" , 12 , 22)) # start = 12 , end = 22
# <strName>.replace(<old> , <new>) --> replace oldchar/substring with new ones
# <strName>.replace(<old> , <new> , <count> )
# print(tech.replace("a" , "b"))
# print(tech.replace("an" , "as"))
dia = "iam in class in DL in Hyd.  "
# print(dia)
# print(dia.replace("in" , "out"))
# print(dia.replace("in" , "out" , 2)) # count = 2

# <strName>.strip() -->remove whitespaces from a string from lead and lag ends
# print(tech.strip())
# print(tech.lstrip()) # from left
# print(tech.rstrip()) # from right
# print(tech.strip(" py"))
# print(dia.strip(" iam"))
# lstrip() , rstrip() --> remove chars from string 
# <strName>.split(<delimiter>) ---> cut string at a delimiter
# print(tech.split()) # default delimiter = " "
# print(tech.split("a")) # delimiter = "a"
# print(dia.split("in")) # delimiter = "in"
# b = dia.split("in")
# print(b)
# <delimiter>.join(<splitstring>) --> join spltted strings using a delimiter
# print("".join(b)) # delimiter = ""
# print("in".join(b)) # delimiter = "in"
# print("-".join(b)) # delimiter = ""

# 0	0 	0
# 1	1	1
# 2	4	8
# 3	9	27
# 4	16	64
# 5	25	125
# XXX uniform XXX
# structured 

# <strName>.zfill(<length>) ---> filling zeroes at the lead end , left side 
# a = "tech"
# print(a.zfill(7))
# b = 20 
# print(str(b).zfill(6)) # number --> typecast + zfill

# EOL --> new line  , indentation
# control flow --> :

# input vs output
# ---------------
# print() --> output
# print , print() ---> cmd --> 2.7
# print() --> function --> 3.6
# c Cpp java --> print() , println() , printf()
# print("a" )# newline auto 
# print("b")
# print("c")
# # end --> keyword 3.6
# # end = "" --> print will continue 
# print("a",end = " ")# no newline auto 
# print("b",end = " ")
# print("c")

# types inputs
# ------------ 
# --> keyboard input ( input function )
# --> console input

# input function ( scanf , Scanner.util )
# --------------
# raw_input()  , input() --> 2.7
# input() --> 3.6
# raw_input()  --> XXX 3.6 XXX

# keyboard --> input function --> program

# 2.7
# ===
# 10  --> raw_input() --> 10
# "a" --> raw_input() --> "a"
# "10"--> raw_input() --> "10"

# 3.6 and 2.7
# ===========
# 10  --> input() --> "10" --> int(input()) --> 10
# "a" --> input() --> "a"
# "10"--> input() --> "10"

# syntax
# ------

# <identifier> = input(<dialouge>)
# <dialouge> 10
# <identifier> --> 10

# num1= int(input("enter a number")) # number --> typecasting
# num2= int(input("enter a number"))
# print(num1 + num2)

# conditional statements
# ----------------------
# descision making statements 
# 	-> condition ( mandatory ) --> T/F
# 	-> statement ( mandatory )
# - if else (2 statements)
# - if elif else (3 statements)
# - nested 
# 	if 	
# 		if else
#   	else
# - if (i statement)

# syntax
# ------
# if <condition>:
# 	<statement>

# if <condition>:
# 	<statement1>
# 	<statement2>
# else:
# 	<statement3>

# if (<condition1>):
# 	<statement1>
# 	<statement2>
# elif(<condition2>):
# 	<statement3>
# else:
# 	<statement4>

# if(condition1):
# 	if(condition2):
# 		<statements>
# 	else:
# 		<statements>
# else:
# 	<statements>

# even odd 
# --------
# num = int(input("enter a number"))
# num = 10
# if num%2 == 0:
# 	print("even number")
# else:
# 	print("odd number")

# if num%2 == 0:
# 	# print("even number")
# 	pass # skip execution
# else:
# 	print("odd number")


# tasks
# -----
# time = 16 -> input()
# 6 - 10 --> good morning
# 11- 14 --> good afnun
# 15 - 19 --> good eve
# 20 - 23 --> good night 
# 0 - 5 --> wrong time 

# time = 03:15:45AM
# ot = 03:15:45
# time = 03:15:45PM
# ot = 15:15:45
# time = 12:00:00AM
# ot = 00:00:00

# 3 & 5
# -----
# 3 --> multiple of 3 
# 10 --> multiple of 5
# 15 --> multiple of 3 , 5 
# 14 --> not a multiple of 3,5
# 60 --> multiple of 3 , 5
# 100 --> multiple of 5 