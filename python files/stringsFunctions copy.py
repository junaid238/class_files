# functions in strings 

# tech = "Python"
# dia = "Iam in a class in Hyderabad in Python class"

# print(len(tech))
# print(len(dia))

# print(tech.startswith("P"))
# print(tech.startswith("z"))

# print(tech.endswith("n"))
# print(tech.endswith("m"))

# print(tech.count("P"))
# print(dia.count("a"))
# print(dia.count("in"))
# print(dia.count("Hyderabad"))
# print(dia.count("Vizag"))

# print(tech.index("P"))
# print(tech.index("n"))
# print(dia.index("in" , 10))
# print(dia.index("out"))

# print(tech.find("P"))
# print(tech.find("n"))
# <str_name>.find(<substring> , start , end)
# print(dia.find("in" ,10 , 20 ))
# print(dia.find("out"))

# print(dia)
# newdia = dia.replace("in" , "out" , 3)
# print(newdia)
# print(dia)

# print(dia)
# # print(dia.split()) # default space 
# print(dia.split("i")) # delimiter = "i"  
# print(dia.split("in")) # delimiter = "in"  
# print(dia.split("class"))


# emp = ["khan" , "29" , "M" , "Python"]
# print(" ".join(emp))
# print("-".join(emp))
# print("@".join(emp))

# a = 34
# b = str(a).zfill(6)
# print(b)

# strip , lstrip , rstrip 
# strip--> remove spaces 

# dialouge = "     khan teaches  Python.     "
# print(dialouge)
# print(dialouge.strip())
# print(dialouge.lstrip())
# print(dialouge.rstrip())
# print(dialouge.lstrip("khan"))
# print(dialouge.lstrip(" khan"))

# print(dialouge.split())
# coll = (dialouge.split())
# print("".join(coll))

# string = "100"
# print(string)
# print(int(string))

#ASCII
# char - num(ASCII)  ---> ord()
# num(ASCII) - char  ---> chr()

# char = "A"
# print(ord(char))
# num = 122
# print(chr(122))
# zero = 30
# print(chr(zero))


# conditional statements
# if else 
# if elif else 

# a = 100
# if(a > 5):
# 	print("Hi")
# else:
# 	print("Hello ")

# if(a > 5):
# 	pass
# else:
# 	print("Hello ")

# if(a>100):
# 	print("from if")
# elif(a==100):
# 	print("from elif 1")
# elif(a!=10):
# 	print("from elif 2")
# else:
# 	print("not a numer")


# is_num() , is_alpha() , is_char()
# even and odd
# num = input("enter a number")	
# if (type(num) is "str"):
# 	num= int(num)
# 	if(num%2 == 0):
# 		print("even number")
# 	else:
# 		print("odd number")
# else:
# 	print("not a number")
# type(num) --> str , int 

# gm ga ge gn 
# time = int(input("enter the time"))
# if(time>= 0 and time<= 24):
# 	if(time>=5 and time<=11):
# 		print("good morning")
# 	elif(time >= 12 and time<=15):
# 		print("good afternoon")
# 	elif(time >= 16 and time<=22):
# 		print("good evening")
# 	else:
# 		print("good night")
# else:
# 	print("wrong time input")


# Looping structures 
# for 
# 	- limit (condition)
# 	- statement
# 	- inc / dec 

# ++ --> XXXX not valid XXXX

# for i in range(10):
# 	print(i)

# for i in range( 2, 29):
# 	print(i , end = " ")

# for i in range( 2, 29 , 3):
# 	print(i , end = " ")

# for i in range( 29, 2 , -1):
# 	print(i , end = " ")

