# for loops for strings 

# tech = "Python"

# for i in tech:
# 	print(i)
# for i in range(0,len(tech)):
# 	print(tech[i])

# multiplication table for 5 
# for i in range(1,11):
# 	print("5 X %d = %d" %(i , 5*i))
	# print("5 X " + str(i) + " = " + str(5*i))

# patterns 

# 1 star pattern
# for i in range(1,6):
# 	print("*" * i )

# 2 number pattern
# 1
# 22
# 333
# 4444
# 55555


# largest -- 55555
# ----<str(i)>---<i>
# print("1"    * 1)
# print("2"    * 2)
# print("3"    * 3)
# print("4"    * 4)
# print("5"    * 5)

# for i in range(1,6):
# 	print(str(i) * i)


# 3 pattern number
# 1
# 12
# 123
# 1234
# 12345

# largest = 12345 
# next largest = 1234 
# for i in range(1,6):
# 	print(i , end = "")
# print()
# for i in range(1,5):
# 	print(i , end = "")
# # print()
# for i in range(1,4):
# 	print(i , end = "")



# for j in range(1,6):
# 	for i in range(1,j+1):
# 		print(i , end = "")
# 	print()


# 54321
# 4321
# 321
# 21
# 1 


# for j in range(1,6):
# 	for i in range(j,6):
# 		print(6-i , end = "")
# 	print()

# for j in range(5,0,-1):
# 	for i in range(j,0,-1):
# 		print(i , end = "")
# 	print()


# compiste and prime clasifier

# num = int(input("enter a number"))
# count = 0
# for i in range(1,num+1):
# 	if(num%i == 0):
# 		count += 1 # count = count + 1 
# if(count > 2):
# 	print("composite number")
# else:
# 	print("prime number")


# start 12
# end 19

# 12 - composite
# 13 - prime
# 14 - composite
# .
# .
# .
# 19 - prime


# string --> "iam in. hyderabad"
# aeiou 
# i a i e a a 

# string = input("enter a string")

# for ch in string.lower():
# 	if(ch is "a" or ch is "e" or ch is "i" or ch is "o" or ch is "u"):
# 		print(ch)

# start = int(input("enter the start value"))
# endP = int(input("enter the end value"))

# for i in range(start , endP+1):
# 	if(i % 2 == 0):
# 		print( " %d %s" %(i , "even"))
# 	else:
# 		print( " %d %s" %(i , "odd"))


# while loop 
# --> infinite loops ( always it is true )
# --> True , forever true statement
#  	-> initialisation
#  	-> condition
#  	-> inc/dec

# do while XXX 
# while -> valid

# Syntax:
# -------
# < initialisation > 
# while(<condition>):  
# 	< implementation >
# 	inc / dec 

# while(True):
# 	print("hi")

# a=10
# while(a==10):
# 	print("hai")

# a = 0
# while(a<10):
# 	print(a)
# 	a = a + 1

# a = 10 
# while (a>0):
# 	print(a)
# 	a -= 1

# control statements:
# -------------------
# pass
# break 
# continue 

# pass --> overcome unimplemented blocks 

# # for ----:
# # 	pass

# break --> exit the loop using a condition when true 

# continue --> exit the loop using a condition when true and returns back after the condition 
# 		--> exit only at condition true point 

# tech = "Python"

# for i in tech:
# 	print(i)
# 	if(i == "h"):
# 		break

# for num in range(0,15):
# 	print(num)
# 	if(num == 10):
# 		break


# a = 0 
# while ( a< 10) :
# 	print(a)
# 	# a += 1
# 	if( a == 5 ):
# 		break 
# 	a += 1
	

# continue --> exit and return back 


# for i in range(12 , 30):
# 	if( i == 15 ):
# 		continue
# 	print(i)

# for i in tech:
# 	if (i is "h"):
# 		continue
# 	print(i)

# a = 12
# while(a<30):
# 	a += 1
# 	if( a == 15):
# 		continue
# 	print(a)

# Task 1  --> multiplication table continue 
# task 2 --> pattern stars break , continue
# task 3 --> numbers break , continue
