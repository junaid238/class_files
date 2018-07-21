# Python decorators
# -----------------
# Methods --> first class objects 

# decorator - method --> adds extra functionality to other function

# func 1 - dec
# funct2 + dec --> extra functionality

# @classmethod  --> cls
# @staticmethod --> non cls and self 

# self -- default

def printInc(num):
	return num+1
# a = printInc(3)
# print(a)
# print(type(a))
def printDec(num):
	return num-1


def caller(methodname ):
	# returning a call of first method dynamically
	return methodname

print(caller(printInc ))
aa = caller(printInc )
print(aa(10))
# print(caller(printDec , 5))


# nested functions / methods 
# super function
# 	sub1 function
# 	sub2 function

# def superFunc():
# 	print("from super function ")

# 	def sub1():
# 		print("from sub 1 function")
		
# 	def sub2():
# 		print("from sub 2 function")

# 	sub1()
# 	sub2()
# superFunc()


# def takeNum(a):
# 	def hi():
# 		return ("hi from hi method sub1") 
# 	def bye():
# 		return ("bye from bye method sub2")
# 	if a%2 == 0:
# 		return hi
# 	else:
# 		return bye

# n = takeNum(10) # n = hi not hi()
# m = takeNum(23) # m = bye not bye()

# # reference of methods 
# print(n)
# print(m)

# # method call but n , m are not methods
# print(n())
# print(m())


def deco(methodName):
	def wrapper():
		print("hello from wrapper")
		methodName()
		print("hello after the deoc call ")
	return wrapper
	# wrapper()
@deco
def numprint():
	print("output from deco using @ ")
numprint()

# def printNum():
# 	print( "output from printNum method ")

# printNum()

# a = deco(printNum)
# a()

# MultiThreading
# --------------
# thread --> entity of a sequential execution 
# --> time of execution
# --> variables 
# --> progress 

# --> register set and stack 

# --> import threading 

# thread objects --> function call
# t1 = funct1
# t2 = funct2

# syntax 
# ------
# t1 = threading.Thread(target = printNum)
# t2 = threading.Thread(target = printInc)

# t1.start()
# t2.start()

# t1 --> after t1 --> t2

# # for waiting till t1 is completed
# t1.join()
# # for waiting till t2 is completed
# t2.join()

# module for wait or sleep --> time 
# import time 
# time.sleep(5)

# import threading

# def prinTnum(num ):
# 	print("the num entered is " , num)

# def incNumPrint(num):
# 	print("the number icremented is ", num+1)

# t1 = threading.Thread(target = prinTnum , args = (10 ,))
# t2 = threading.Thread(target = incNumPrint , args =(20 ,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Beautiful Soup --> ?? task 

# PythonDecorators/decorator_function_with_arguments.py
# def decorator_function_with_arguments(arg1, arg2, arg3):
# 	def wrap(f):
# 		print("Inside wrap()")
# 		def wrapped_f(*args):
# 			print(args)
# 			print("Decorator arguments: Inside wrapped_f()", arg1, arg2, arg3)
# 			f(*args)
# 			print("After f(*args)")
# 		return wrapped_f
# 	return wrap
 
# @decorator_function_with_arguments("hello", "world", 42)
# def sayHello(a1, a2, a3, a4):
# 	print('sayHello arguments:', a1, a2, a3, a4)
# sayHello(10,30,48,89)
# print("After decoration")
# print("Preparing to call sayHello()")
# sayHello("say", "hello", "argument", "list")
# print("after first sayHello() call")
# sayHello("a", "different", "set of", "arguments")
# print("after second sayHello() call")