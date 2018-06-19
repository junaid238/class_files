# Python online 28-05-2018 strings (functions) part - 3
# -----------------------------------------
# operations 
# ----------
# -> case based  functions
# -> functional  functions

# -> immutable 

# -> atrribute fecthing functions (use of .)
# -> parameterised functions ( use (something here))

# tech = "python"
# .lower()
# .upper()
# .swapcase()
# .capitalize()

# len()
# count()
# .split()
# .join()
# .strip()
# find()
# index()
# replace()
# .lstrip()
# .rstrip()
# zfill()

# tech = "python"
# stringName.functionName() --> AFM
# dialouge = " I am in class in Hyd right now in Python session.   "
# print(dialouge.lower())
# print(dialouge.upper())
# print(dialouge.swapcase())
# print(dialouge)

# len()--> len(stringName)
# print(len(dialouge))
# .strip() --> stringName.strip()
# print(dialouge.strip()) # remove spaces from left and right
# print(dialouge.lstrip()) #remove spaces from left
# print(dialouge.rstrip()) #remove spaces from right

# count() --> stringName.count(<char / substring>) # count repetitions of substring
# print(dialouge.count("in")) #substring count
# print(dialouge.count("i"))
# print(dialouge.count("s")) # char count
# print(dialouge.count(" I am in class in Hyd right now in Python session.   "))
# print(dialouge.count(" ")) # space count
# print(dialouge.count("in class"))
# print(dialouge.count("java")) # no appearance returns 0

# replace() --> stringName.replace("old" , "new")
# replaces old substring with new substring

# print(dialouge.replace("in" , "out")) # in ---> out
# print(dialouge.replace("java" , "out")) # same string as output
# print(dialouge)
# new_dialouge= dialouge.replace("in" , "out" ) # re assigning
# print(new_dialouge) # changed for all in s 
# new_dialouge_two= dialouge.replace("in" , "out" , 2 )
# print(new_dialouge_two) # only 2 in s changed to out  
# print(dialouge.replace("i" , "j")) # changing single char

# join() and split() 
# stringName.split(<delimiter>)
# delimiter.join(<collection>)

# 		delimiter
# space 	(" ") 	--> seperator --> 11 words
# hyd 	("Hyd")	--> seperator --> 2 words
# in 		("in") --> seperator --> 4 words

# print(dialouge.split()) # default delimiter ==> "  " --> space
# print(dialouge.split(" ")) # delimiter ==> " "
# print(dialouge.split("Hyd")) # delimiter ==> "Hyd"
# print(dialouge.split("in"))
# print(dialouge.split("i"))

# join()--> delimiter.join(collection)
# details = ["python" , "1991" , "Oops" , "Popular"]
# print(" ".join(details)) # delimiter = " " -> space
# print("-".join(details)) # delimiter = "-"
# print(" is ".join(details))

# find() --> index of char or substring if available in sting 
# stringName.find(char / substring)
# print(dialouge)
# print(dialouge.find("in" )) # index of i in first in
# print(dialouge.find("Python")) # index of P in Python 
# print(dialouge.find("out")) # returns -1 as no out in dialouge
# print(dialouge.find("r")) # r's index at 22 position

# index()
# print(dialouge.index("r")) # index of r at 22 position
# print(dialouge.index("in")) # index of i in first in
# print(dialouge.index("out")) # error as no out in dialouge

# zfill() --> only strings  zero fill
# stringName.zfill(size)

# uniformity in data

# 000 	000 	000
# 001		001		001
# 002		004		008
# 003		009		027
# 004		016		064
# 005		025 	125 --> digits one two three
# tech = "python"
# print(tech.zfill(10)) # python as len of 10 chars adding zeros

# num = "30"
# print(num.zfill(7))# 30 as len of 7 chars adding zeros

# cube = 64
# print(str(cube).zfill(3)) # type cast number to string and apply zfill

