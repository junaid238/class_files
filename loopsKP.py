# Loops 
# 	- repetative implementation 
# 	- initialisation 
# 	- condition / limit 
# 	- inc /dec 
#   - nested for loops

# for 
# while XX ( do while ) XX

# for 	
# 	- numbers 
# 	- strings 
# 	- collections
# numbers --> range() , xrange()

# range(<end>) --> 0 to end values inc = +1
# range(<start> , <end>) --> start to end-1 values inc = +1
# range(<start> , <end> , <step>) --> start to end-1 values inc = + step  start < end
# range(<start> , <end> , -<step>) --> start to end-1 values dec = - step start > end

# if empty for loop --> pass in implementation

# syntax:
# -------

# for <dummy> in range(<start> , <end>):
# 	if:
# 		___
# 	____
# 	____

# for <dummy> in range(<start> , <end>):
# 	pass

# end
# for i in range(10):
# 	print(i)

# start and end 
# for i in range(2,20):
# 	print(i)

# start , end and step
# for i in range(10 , 30 , 3):
# 	print(i)

# for i in range(100 , 80 , -1):
# 	print(i)


# for i in range(100 , 10 , -10):
# 	print(i)


# empty for loop --> pass
# --------------
# for i in range(10):
# 	pass

# even odd 
# --------

# start = 20 
# endp =  50 

# for i in range(20,50):
# 	if(i % 2 == 0):
# 		print(str(i) + " is even")
	# else:
	# 	print(str(i) + " is odd")

# for i in range(20,50,2):
# 	print(str(i) + " is even")

# nested loops 
# -------------
# for loop 1 :
# 	implementation of for loop1 
# 	for loop 2:
# 		implementation of for loop 2 
# 		for loop 3:
# 			pass


# c:/>python multiply.py 
# Enter the inputs
# "b"
# invalid inputs

# patterns 
# --------
# logic --> pattern
# pattern --> logic

# n = 4
# *
# **
# ***
# ****

# largest line --> ****

# print("*" * 1)
# print("*" * 2)
# print("*" * 3)
# print("*" * 4)
# for i in range(1,n+1):
# 	print("*" * i)

# ****
# ***
# **
# *
# for i in range(n,1, -1):
# 	print("*" * i)



# n = 4
#    * -> 3 space + 1 stars
#   ** -> 2 space + 2 stars
#  *** -> 1 space + 3 stars
# **** -> 0 space + 4 stars

# 		  i       n-i
# **** 
# print(" "*0 +"*" * 4)
#  ***
# print(" "*1 + "*" * 3)
#   ** 
# print(" "*2 + "*" * 2)
#    *
# print(" "*3 + "*" * 1)
# ****
#  ***
#   **
#    *
# for i in range(n):
# 	print((" " * i) + ("*" * (n-i)))

# n = 5

# 1
# 22
# 333
# 4444
# 55555 
# print(str(4) * 4)
# print(str(5) * 5)

# for i in range(1 , n+1):
# 	print(str(i) * i)


# userInput  = "a"

# a
# bb
# ccc
# dddd
# for i in range(ord(userInput) , ord(userInput)+4):
# 	print(chr(i) * ((int(i)- int(ord(userInput)))+1))

# ord(userInput) = 97
# i -> 97 98 99 100 
# a - 1 --> (97 - 97) + 1
# b - 2 --> (98 - 97) + 1 
# c - 3 --> (99 - 97) + 1
# d - 4 --> (100 - 97) + 1


# task2 
# -----
#    1
#   333
#  55555
# 7777777

# task3
# ----- 
# userNum = 5
# a
# bb
# ccc
# dddd
# eeeee

# task1
# -----

# c:/>python multiply.py 
# Enter the inputs
# 5
# 5 X 1 = 5
# .
# .
# . 
# 5 X 10 = 50


# nested loops and usage --> while 
# ----------------------------------------

# 1
# 12
# 123
# 1234
# 12345


# 12345 
# print("12345")
# for i in range(1,2):
# 	print(str(i) , end ="")
# print()
# for i in range(1,3):
# 	print(str(i) , end ="")
# print()
# for i in range(1,4):
# 	print(str(i) , end ="")
# print()
# for i in range(1,5):
# 	print(str(i) , end ="")
# print()
# for i in range(1,6):
# 	print(str(i) , end ="")


# n = 5
# for j in range(2,n+2):
# 	for i in range(1,j):
# 		print(str(i) , end ="")
# 	print()

# task -1
# -------
# a
# ab
# abc
# abcd 
# abcde

# prime vs composite 
# 0,n 		>2 factors

# 3 --> 1,3
# 13 --> 1,13
# 6 --> 1,2,3,6
# 15 --> 1,3,5,15
# 9 --> 1,3,9

# num = 15 
# 1
# 3
# 5
# 15
# prime / composite

# 12 % 1 == 0   --> c
# 12 % 2 == 0   --> c>2 
# 12 % 3 == 0   --> c
# 12 % 4 == 0   --> c
# 12 % 5 != 0   --> f
# .
# .
# 12 % 12 == 0   --> c



# num = 19
# count = 0 
# for i in range(1,num+1):
# 	if num % i == 0:
# 		print(num//i , end = "  ")
# 		count = count + 1

# if count>2:
# 	print("composite number")
# else:
# 	print("prime number")


# st = 13
# en = 35


# for num in range(st,en):
# 	count = 0 
# 	for i in range(1,num+1):
# 		if num % i == 0:
# 			print(num//i , end = "  ")
# 			count = count + 1
# 	if count>2:
# 		print("composite number")
# 	else:
# 		print("prime number")

# 13 -> prime number --> 2 factors
# 14 -> composite number --> 4 factors
# .
# .
# .
# 35 -> composite number --> 4 factors
# ----------------------------------------

# for with strings
# ----------------

# dia = " iam in a class in hyd with Python session "

# print(len(dia))
# for i in range(0,len(dia)):  # 0 , 43
# 	print(dia[i] , end = "") # indexing using for 

# for ch in dia: # i --> i to n
# 	print(ch , end = "")


# aeiou --> vowels 
# i a i a a i i o e i o 
# 11
# c = 0 
# for i in dia:
#	if ((i is "a") or (i is "e") or (i is "i") or (i is "o") or (i is "u") ):
# 		print(i)
# 		c += 1
# print("no of vowels " + str(c))

# co = 0
# vowels = "aeiou"
# for ch in dia:
# 	if ch in vowels:
# 		print(ch)
# 		co += 1
# print(co)


# task - 2
# --------
# count no of digits --> 923789 
# 6 

# task - 3
# --------
# "i have a 1 session at 7 pm "
# 1 7 


# anagram 

# " iam in a class in hyd with Python session " 2 
# iam in 
# in a
# a class 
# class in 
# in hyd 
