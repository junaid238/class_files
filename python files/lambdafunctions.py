# keyworded parameters
# --------------------
# positional ---> variable 
# default ---> keyworded
# dictionary --> toppings --> key
# 			   almonds  --> value 

# error
# def cakeShop(flavour = "choc" , weight ="2kgs" , shape = "square"):
# 	print("you have ordered \
# 	 " + flavour +" cake " +weight+ " of " \
# 		  +shape+ " shape ")

# cakeShop("vanila" , "5kg" , "rectangle",toppings = "almonds")
# syntax
# ------
# **kwargs **kwvars **abcd
# kwargs --> dictionary
# def cakeShop(flavour = "choc" , weight ="2kgs" , shape = "square" ,**kwargs):
# 	print(kwargs)
	# print(type(kwargs))
	# print(kwargs.keys())
	# print(kwargs.values())
# 	for i in kwargs.items():
# 		print(i)

# cakeShop(flavour = "choc" , weight ="2kgs" , shape = "square",toppings = "almonds")

# Lambda functions / anonymous functions
# ---------------------------------------
# -> def 
# -> impl	
# -> call
# auto returned

# def addnUm(a,b):
# 	res = a+b 
# 	return res 
# print(addnUm(10,30))

# syntax
# ------
# <functName> = lambda <params> : <operation>

# addnUm = lambda a,b : a+b
# print(addnUm(10,30))

# map , reduce , filter 
# ---------------------

# -> functions
# -> collections 
# -> reduce is not auto imported 

# l1 = [1,2,3,4]
# l2 = [10,20,30,40]

# [11,22,33,44]

# map()
# --> associative operation on collections
# --> function(return) , collection
# --> return map object 

# syntax
# ------
# <mapObject> = map(<function> , <collection(s)>)

# a = map(lambda x:x**2 , l1)
# print(a) # <map object at 0x10047f400>
# print(list(a))

# b = map(lambda x,y : x+y , l1,l2)
# print(b) # <map object at 0x10095a588>
# print(list(b))

# c = map(lambda x,y : x*y , l1,l2)
# print(list(c))


# filter() 
# --------
# associative check of elements 
# listNums = [x for x in range(10,40)]
# -> function , collection
# -> filter object

# syntax
# ------
# <filterObj> = filter(<function>, <collection>)

# ob = filter(lambda x:x%2==0 , listNums)
# print(list(ob))

# reduce()
# --------
# -> function
# -> value 
# -> cumulative operation 
# -> function , collection

# syntax
# ------
# from functools import reduce
# <redValue> = reduce(<function> , <collection>)

# val = reduce(lambda x,y:x+y , l1)
# val2 = reduce(lambda x,y:x*y , l1)
# print(val)
# print(val2)