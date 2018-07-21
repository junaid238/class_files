# # Functional Programming 
# Functions 
# 	-> small snippet of code 
# 	-> one/single task 
# 	-> Method ( class )
# 	-> first class objects 

# 3 basic components 
# ------------------
# 	-> declaration / definition --> once , mandatory
# 		--> make memory for your function and assign the identifier
# 	-> implementation --> once , mandatory
# 		--> to work on logic and provide with output 
# 	-> function call --> multiple , optional
# 		--> to make the function work / execute 

# C / C++ --> function prototype

# functionNames ---> identifiers

# two types ( availability ):
# 	-> pre defined 
# 		- print()
# 		- len()
# 		- range()
# 		- sort()
# 		- input()
# 	-> user defined

# four types ( functionality ):
# 	return Type    parameters 
# 		0 				0
# 		1				1
# 		1				0
# 		0				1

# Syntax
# ------
# def <functionName>(): ---> definition
#   |
#   |<implementation>
#   |<business logic>
#   |<algorithm>

# <functionName>() --> function call1
# <functionName>() --> function call2
# <functionName>() --> function call3
# <functionName>() --> function call4
# <functionName>() --> function call5

# return type --> assign call to variable --> value
# no return type --> assign --> None 

# parameter --> (<something>) --> something = parameter

# 1 1 --> len()
# 0 0 --> sort() , print()
# 0 1 --> append()
# 1 0 --> pop()

# Hello 
# def printme(): # --> definition
# 	print("Hello") # --> implementation
# printme() # --> function call

# empty function
# def emp():
# 	pass  # skip the implementation
# 	# anything
# emp()

# parameters / arguements
# -----------------------
# 4 types
# --> positional
# --> default 
# --> variable
# --> keyworded

# --> 2 kinds 
# 	--> formal parameters / variables --> definition
# 	--> actual parameters / values--> call

# function with parameter
# def sayHi(aa): # formal parameter --> aa
# 	print("Hello "+ aa) 

# sayHi("Khan") # actual parameter --> Khan
# sayHi("Hari") # actual parameter --> Hari

# def sayHi(aa):
# 	print("hi "+aa)
# sayHi("Hey")
# sayHi("Ravi")
# sayHi("Suresh")

# sum of numbers 
# def addNums(a,b):
# 	res = a+b
# 	print(res)
# addNums(10,20)

# def addme(a,b):
# 	res = a+b
# 	print(res)
# values --> actual parameter
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# addme(a,b)

# 2 functions ---> len of list 
# enter len --> 5 --> one function
# enter element --> 10 --> two function


# accept length 
# l1 = []
# def takeEle():
# 	a = input("enter the element")
# 	l1.append(a)
# 	print(l1)
# def makeList():
# 	l = int(input("enter the length"))
# 	for i in range(l):
# 		takeEle()
# makeList()

# doc string --> description of function

# Syntax
# ------
# just after definition
# 	''' ''' 
# __doc__ ---> doc string is stored here
# print(<functionName>.__doc__)

# def sayHello(name):
# 	''' this function says hello to the name'''
# 	print("hello " + name)
# sayHello("khan")
# print(sayHello.__doc__)

# print(len.__doc__)
# print(print.__doc__)

# Task 
# ----
# c:/> python functionTask.py
# 1 . Arithmetic
# 2 . Logical
# 3 . Comparision

# Enter your category
# 1

# 1. sum
# 2. diff
# 3. mul
# 4. div

# Enter your operation
# 1

# enter the number 10
# enter the number 20
# 30 