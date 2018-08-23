# list comprehensions

# l1 = [10,20,30,40]
# ans = [100,400,900,1600]

# # declaring an empty list
# ans = []
# # looping over list1
# for i in l1:
# 	# operation and assignment to answer list
# 	ans.append(i**2)
# print(ans)

# declaring an empty list
# l2 = []
# # looping over range
# for i in range(10):
# 	# assignment to answer list
# 	l2.append(i)
# print(l2)

# declaring an empty list
# l3 = []
# # looping over list
# for i in ans:
# 	# checking using if condition
# 	if ( i % 2 == 0 ):
# 		# assignment to answerList
# 		l3.append(i)

# l4 = []
# for x in range(20):
# 	if(x%2 !=0):
# 		l4.append(x**2)
# print(l4)

# 1. assignment and looping 
# <ansListName> = [<varName>  <looping over range>]
# ans = [x for x in range(11)]
# print(ans)

# 2. operation and assignment with looping
# <ansListName> = [<varName + assignment>  <looping over range>]
# ans = [x**2 for x in range(11)]
# print(ans)

# 3. assignment with condition over loop
# <ansListName> = [<assignment>  <looping over range>  <condition>]
# ans = [x for x in range(10) if(x%2 == 0 )]
# print(ans)

# 4. assignment + operation + condition + loop
# <ansListName> = [<operation + assignment>  <looping over range>  <condition>]
# ans = [x**2 for x in range(20) if(x%2 != 0)]
# print(ans)

# Tuples
# ------
# - collection 
# - immutable 
# - indexed , sliced and concatenated 
# - default collections 
# - < class tuple >
# - heterogeneous collection
# - infinite length
# - nested tuples

# syntax
# ------
# <tupleName> = ( <element1> , <element2>)
# <tupleName> = element1 , element2 , element3 ,

# numsTuple = (1,2,3,4,5)
# print(numsTuple)
# print(type(numsTuple))

# namesTuple = "khan" , "hari "  ," ram" , "ravi" ,
# print(namesTuple)
# print(type(namesTuple))

# indexed sliced and concatenated
# --------------------------------
# <tupleName>[<index>]
# print(namesTuple[2])
# print(numsTuple[2])
# # print(numsTuple[20])
# print(namesTuple[0:3])
# print(namesTuple[:4])
# print(namesTuple[2:])

# print(numsTuple + namesTuple)
# print(namesTuple)
# print(numsTuple)

# functions in tuple
# ------------------
# len()
# index()
# count()
# print(len(namesTuple))
# print(namesTuple.index("ravi"))
# print(namesTuple.count("ravi"))
# namesTuple.append(10)
# del namesTuple[2]

# print(namesTuple)
# namesTuple[2] = "rakesh"
# print(namesTuple)
# del namesTuple
# print(namesTuple)

# constants --> pi , epsilon , mu
# long time constant values --> school fee , taxes 

# taxes = (0.05 , 0.18 , 0.26 )
# print(taxes)
# type casting 
# ------------
# tuple --> list ===> list()
# modification 
# list --> tuple ===> tuple()

# taxes = list(taxes)
# print(taxes)
# taxes[1] = 0.20
# print(taxes)
# taxes = tuple(taxes)
# print(taxes)

# for i in namesTuple:
# 	if(len(i) == 4):
# 		print(i)

# tuple comprehensions
# --------------------
# XXX NO XXX

# l1 = [1,2,3,[4,67,76],(10,40,34) , 45,9,90,[4,39,3,5,5,65]]
# ans= []

# for i in l1:
# 	if type(i) is list or type(i) is tuple:
# 		for j in i:
# 			ans.append(j)
# 	else:
# 		ans.append(i)
# print(ans)

# l1 = [[1,2,3] , [10,20,30] , [100,200,300]]
# l2 = [[1,2,3] , [10,20,30] , [100,200,300]]
# ans = [[2,4,6] , [20,40,60] , [200,400,600]]

# inputs 
# ------
# -> keyboard --> input()
# -> console  --> sys.argv

# keyboard
# --------
# enter a number 10 
# a = 10

# console
# -------
# c:/>python mytask.py 10 
# a = 10 

# a = input("enter a number")
# print(a)

# argv --> list --> console inputs after python 
# argv --> from sys module 
# import sys 

# argv[0] --> always file name (py)

# import sys 
# print(sys.argv)
# print(sys.argv[0])

# c:/>python mytask.py 10 
# 55

# c:/>python mytask.py "data" 
# a a

# import sys
# # print(sys.argv[1]) # 10 
# count = 0 
# if len(sys.argv) > 2:
# 	print("Enter only one number next time ")
# 	# for i in range(0,int(sys.argv[1])+1):
# 	# 	count += i
# else:
# 	for i in range(0,int(sys.argv[1])+1):
# 		count += i
# print(count)

# [[_,_,_] , [_,_,_] , [_,_,_]]

# [_,_,_]
# [_,_,_]
# [_,_,_]

# enter player 1 X
# "khan"
# enter player 2 O
# "ravi"

# khan enter first move 4
# [_,_,_]
# [X,_,_]
# [_,_,_]

# ravi enter first move 9
# [_,_,_]
# [X,_,_]
# [_,_,O]

# khan enter first move 9
# position is not empty

# Dictionary
# ----------
# form -- fname 	lname 	mob 	email  	preadd peradd  gen
# emp1 --[khan. 	khan. 	98		@khan 	hyd	   bnglr.  m]
# emp2 --[ravi. 	ravi. 	98		@ravi 	del	     m]
# emp3 --[ravi. 	ravi. 	@ravi 	del	     m]


# emp2[4] --> del 
# emp1[2] --> 98
# emp1[5] --> bnglr. --> peradd
# emp2[5] --> m --> gen

# indices --> 0 1 2 3 . . . . n 

# Named tuple        , Dictionary
# collections module , python libs

# - collection data type 
# - mutable
# - arbitary 
# - <class dict>
# - key value pairs 
# - customise indices --> keys 
# - keys => indices , values => elements , keys + values => items
# - indexed 
# - XX sliced XX
# - concatenated (special)

# - keys => unique , immutable objects 
# - values => anything 

# syntax
# ------
# emptyDict = { }
# print(type(emptyDict))
# print(emptyDict)

# formDict = {"fname" : "khan" , "lname":"Junaid" , "gen" : "m" , "age" : 27 , 91 : 987654321 , (17,27) : 27 }
# keys --> fname , lname , gen , age , 91 , (1,2)
# values --> khan , Junaid , m , 27 , 987654321 , 27
# print(formDict)

# access elements from keys 
# -------------------------
# print(formDict["gen"])
# print(formDict["age"])
# print(formDict["email"])

# modification of elements
# ------------------------
# if existing --> modify
# if not existing --> add key , value at end of Dictionary
# formDict["age"] = 30 
# print(formDict)
# formDict["email"] = "khan@khan.com"
# print(formDict)

# functions
# ---------
# add  --> modfy 
# removing 
# concatenated
# keys --> list of keys 
# values --> list of values 
# items --> list of items 

# <dictName>.keys() --> all keys in Dictionary
# print(formDict.keys())

# <dictName>.values() --> all values in Dictionary
# print(formDict.values())

# <dictName>.items() --> all items in Dictionary
# print(formDict.items())

# <dictName>.pop(<key>)
# 	- remove key and value of a particular key provided 
# <dictName>.popitem()
# 	- remove last key and value from Dictionary

# formDict.pop("gen")
# print(formDict)
# formDict.popitem()
# print(formDict)

# qual = {"high" : "Mtech" , "grad" : "BE" , "spec" : "ECE" , 20 : 12}

# <dictName1>.update(<dictName2>)
# all from dictName2 --> added to --> dictName1

# formDict.update(qual)
# print(formDict)
# print(qual)

l1 = [1,2,3,4]
# sqdict = {1:1 , 2:4 , 3:9 , 4:16}

# sq = {}
# for i in l1:
# 	sq[i] = i**2 # operation + assignment
# print(sq)

l2 = ["a" , "b" , "c" , "d"]

# c:/>python dictTask.py 4
# {1:"__" , 2: "__" , 3: "__" , 4: "__" }

# l2 = [2,3,5,5]
# dicki = {}
# for i in range(0,len(l1)):
# 	dicki[l1[i]] = l2[i]

# print(dicki)

# print(l1)
# print(l2)

# convert l1 , l2 to a Dictionary
# -------------------------------
# zip() --> zip object
# <zObj> = zip(<list1> , <list2>)
# <ansDict> = dict(zObj)

# zoo = zip(l1,l2)
# print(zoo)
# d = dict(zoo)
# print(d)
# print(dict(zip(l1,l2)))

# Dictionary comprehensions
# -------------------------

# key --> dependent --> value

# <sqdict> = { <assignment for key/value>   <looping>}
# sq = {i:i**2 for i in range(10)}
# print(sq)
# esq = {i:i**2 for i in range(10) if i%2 ==0}
# print(esq)

# Sets and FrozenSets 
# -------------------
# Sets 
# ----
# - collection
# - mutable
# - XX indexed XX
# - XX sliced XX
# - XX concatenate XX
# - math sets 
# - <class set>
# - UNIQUE elements

# syntax
# ------
# numsSet = {1,2,3,4,5}
# NumSet = set([1,23,4,5,6,6,24])
# print(NumSet)
# print(numsSet)
# print(type(numsSet))

# empSetDict = {}
# print(type(empSetDict))

# EmpSet = set()
# print(EmpSet)
# print(type(EmpSet))

# for i in numsSet:
# 	print(i)

# print(numsSet+NumSet) # error

# functions
# ---------
# add() , remove() , discard()

# <setName>.add(<element>)
# numsSet.add(100)
# print(numsSet)
# numsSet.add(10)
# print(numsSet)
# numsSet.add(3)
# print(numsSet)

# <setName>.remove(<element>) --> remove existing element else error
# numsSet.remove(10)
# print(numsSet)
# numsSet.remove(2)
# print(numsSet)
# numsSet.remove(100) # KeyError: 100
# print(numsSet)

# <setName>.discard(<element>) --> remove existing element else no error
# numsSet.discard(10)
# print(numsSet)
# numsSet.discard(2)
# print(numsSet)
# numsSet.discard(100) # no error 
# print(numsSet)

# Math functions on sets --> 2sets
# ----------------------
# .union()
# .intersection()
# .difference()
# .issubset() 
# .issuperset()

# <set1>.union(<set2>)
# print(numsSet.union(NumSet))

# <set1>.intersection(<set2>)
# print(numsSet.intersection(NumSet))

# <set1>.difference(<set2>)
# print(numsSet.difference(NumSet))
# print(NumSet.difference(numsSet))

# <set1>.issuperset(<set2>)
# print(numsSet.issuperset(NumSet))
# print(NumSet.issuperset(numsSet))

# <set1>.issubset(<set2>)
# print(numsSet.issubset(NumSet))
# print(NumSet.issubset(numsSet))

# functions    --> operators
# union 	     --> | 
# intersection --> &
# difference   --> -
# issubset 	 --> >
# issuperset 	 --> <


# print(numsSet | NumSet) # <set1>.union(<set2>)
# print(numsSet & NumSet) # <set1>.intersection(<set2>)
# print(numsSet - NumSet) # <set1>.difference(<set2>)
# print(NumSet  - numsSet) # <set2>.difference(<set1>)
# print(NumSet  > numsSet) # <set1>.issuperset(<set2>)
# print(NumSet  < numsSet) # <set1>.issubset(<set2>)

# FrozenSets
# ----------
# - UNIQUE element collection
# - immutable
# - XX indexed XX
# - XX sliced XX
# - iterated 

# syntax
# ------
# <FrozenSetName> = frozenset([<elements>])

# numsFrozenSet = frozenset([1,2,3,56,53])
# print(numsFrozenSet)
# print(type(numsFrozenSet))

# for i in numsFrozenSet:
# 	print(i)

# functions ( functional programming ):
# ------------------------------------
# - snippet of code
# - few lines of code 
# - only one purpose (recommended)
# - input --> functions --> output 

# c --> prototypes 
# java --> access modifiers , access specifiers 

# function
	# - definition (mandatory , once)
	# - implementation (mandatory , once)
	# - call (optional , multiple)
# two kinds
# ---------
# 	- pre defined --> len() , print() , sort()
# 	- user defined --> ???

# functionality -- 4 types 
# ------------------------
# parameters 		return value
# 	0 				0 --> sort()
# 	1				1 --> index()
# 	1				0 --> append()
# 	0				1 --> pop()

# calls - two kinds
# -----------------
# - attribute fetching ( . )
# - parameterised 

# syntax:
# -------

# def <functionName>(): ---> definition
# 	<implementation1>
# 	<implementation2> ---> implementation
# 	<implementation3>

# <functionName>() --> function call 1
# <functionName>() --> function call 2

# def emptyFunction():
# 	pass --> no implementation

# def numPrint(): # definition of numPrint function
# 	print("100") # implementation of numPrint function

# print(numPrint) # address of function
# print(type(numPrint)) # type ---> function
# numPrint()
# numPrint()

# a = 10 
# if a>3:
# 	numPrint() # call can be made anywhere 
# else:
# 	print("hey")


# def numPrint(): # definition of numPrint function second time
# 	print("200") # implementation of numPrint function second time

# numPrint() # 200

# l1 = [x for x in range(10)]
# print(l1)

# no return type / value --> call--> variable ---> None
# app = l1.append(20) # add 20 at last
# print(app) # None

# return type --> call --> return value
# poped = l1.pop() # removes last element
# print(poped) # 20

# s = l1.sort()
# print(s)

# ind = l1.index(6)
# print(ind)

# doc string 
# ----------
# - string
# - description of a function
# - ''' <doc string> ''' 
# - immediately after definition(first)
# - stored --> __doc__
# - not a mandatory
# - <functionName>.__doc__

# def sayHi():
# 	''' this function will say "hello" ''' # docsting
# 	''' my second doc string ''' # comment
# 	print("hello")

# print(sayHi.__doc__)
# sayHi()

# print(list.__doc__)
# print(list.sort.__doc__)
# print(print.__doc__)
# print(list.append.__doc__)

# return type
# -----------
# - only one --> one function
# - returns components -  value , variable , call , functionName , object
# - uses keyword --> return 
# - return <component>
# - stores component in function call
# - output from a function

# a =10
# def pnum():
# 	print(300) # 300
# 	print(a) # 10
# 	return "hai" 
# comp = pnum()
# print(comp) # 100 

# a =10
# def pnum():
# 	print(300) # 300
# 	print(a) # 10
# 	return a
# 	return 500
# comp = pnum()
# print(comp)

# num = 500
# def classify():
# 	if num > 5:
# 		return "greater" # 6,7,8,...n
# 	else: # 0,2,3,4,5 
# 		return "lesser"
# print(classify())

# parameters / arguments
# ----------------------
# - inputs to function
# - four kinds 
	# - positional 
	# - default 
	# - variable
	# - keyworded 
# - two types 
# 	- formal arguments --> definition --> variables
# 	- actual arguments --> call --> values 


# def sayhello(name , age , role): # formal parameter
# 	print("hello " + name + " welcome to "+ role + " role")
# 	print("your age is " + str(age))

# sayhello("khan" , 27 , "PD") # actual parameter
# sayhello("satish" , 28 , "D")
# # print(a)

# def addNums(a,b):
# 	res = a+b
# 	print(res)
# addNums(10,20)

# def avgNums(a,b,c,d):
# 	res =(a+b+c+d)//4
# 	print(res)

# avgNums(10,20,30,40)
# 25

# def nims(x,y):
# 	res = x.split(y)
# 	return res 

# l1 = nims("khan is a python techie" , "a")
# ["kh" , "n is" , "python techie"]
# print(l1)

# l2 = nims("khan is a python techie" , " ")
# ["khan" , "is" , "a" , "python" , "techie"]
# print(l2)




# 1. arith 
# 2. logic 
# 3. bitwise

# enter your option 
# 1 

# 1. add
# 2. sub 

# enter your operation 
# 1 

# enter your number 1
# 10
# enter your number 2
# 20
# 30



# addnums(20,30) # 50 
# subnums(<50>,10) # 40
# mulnums(<40>,10) # 400
# divnums(<400>,10) # 40 

# def addNums(nu1 , nu2):
# 	ans = nu1 + nu2 
# 	print("sum of numbers is " +str(ans))
# 	return ans 

# def subNums(nu1 , nu2):
# 	ans = nu1 - nu2
# 	print("diff of numbers is " +str(ans))
# 	return ans

# def mulNums(nu1 , nu2):
# 	ans = nu1 * nu2
# 	print("mul of numbers is " +str(ans))
# 	return ans


# def divNums(nu1 , nu2):
# 	ans = nu1 // nu2
# 	print("quo of numbers is " +str(ans))
# 	return ans

# sans = addNums(20,10)
# dans = subNums(sans , 10)
# mans = mulNums(dans , 10)
# qans = divNums(mans , 10)


# def optionSelect():
# 	'''
# 	1. Arith
# 	2. Logical
# 	3. Bitwise '''
# 	option = int(input("enter your option "))
# 	if option == 1:
# 		arith()
# 	elif option == 2:
# 		logical()
# 	elif option == 3:
# 		bitwise()
# 	else:
# 		print("Enter given options only")
# def arith():
# 	'''
# 	1. Add
# 	2. Sub
# 	3. Mul
# 	4. Div '''
# 	print(arith.__doc__)
# 	operation = int(input("enter your operation"))
# 	num1 = int(input("enter your number "))
# 	num2 = int(input("enter your number "))
# 	if operation == 1:
# 		addNums(num1 , num2)
# 	elif operation == 2:
# 		subNums(num1 , num2)
# 	elif operation == 3:
# 		mulNums(num1 , num2)
# 	elif operation == 4:
# 		divNums(num1 , num2)
# 	else:
# 		print("Enter given operation only")

# print(optionSelect.__doc__)
# optionSelect()



# def firstFunc():
# 	print("first  function ")
# 	print("hello from firstFunc")
# 	return 10 

# def caller():
# 	print("caller  function ")
	

# # print(caller) # address --> name of function
# # print(type(caller)) # function
# print(caller()) # call --> None
# print(type(caller())) # NoneType 

# def caller():
# 	print("caller  function ")
# 	return "hai"

# print(caller()) # call --> hai
# print(type(caller())) # str 

# def caller():
# 	return firstFunc	# name of function

# print(caller) # address --> name of function
# print(type(caller)) # function
# print(caller()) # call --> firstFunc # print(firstFunc)
# print(type(caller())) # --> function
# a = caller() # firstFunc
# a --> firstFunc
# a() # firstFunc()

# def caller():
# 	return firstFunc() # call of firstFunc

# # print(caller) # address
# # print(type(caller)) # function
# print(caller()) # firstFunc() --> 10
# print(type(caller())) # int 

# default parameters
# ------------------
# def makeAcake(flav = "chcocolate" , wei = 3 , shape = "square"): # actual parameters / values in function definition
	# print(''' you have ordered %s flavoreded cake of %d kgs %s shape'''%(flav,wei,shape))

# makeAcake("vannilla" , 2 , "round")
# makeAcake(shape = "square" , wei = 2 , flav = "choc") # formal parameters in function call  
# makeAcake(flav = "pine" , wei = 5)
# makeAcake(shape = "rect" , flav = "mango")
# makeAcake()


# variable parameters
# -------------------

# def avgNums(a,b,c,d):
# 	res =(a+b+c+d)//4
# 	print(res)
# avgNums(10,20,30,40)
# avgNums(10,20,40)
# avgNums()

# - unlimited parameters 
# - call --> values (variable number of)
# - definition --> tuple --> *args 
# - *args --> 0 to n parameters
# - *args , *vars , *abcd

# def avgNums(a, b ,*nums):
	# print("from a "+str(a))
	# print("from b "+str(b))
	# print(nums)
	# print(type(nums))

# 	res = a + b 
# 	for i in nums:
# 		res = res + i
# 	ans = res // (len(nums) + 2)
# 	print(ans)

# avgNums(10,20)	
# avgNums(10,20,30,40)
# # avgNums(10)
# # avgNums()	

# make(4,l)
# enter your element 12
# enter your element 13
# enter your element 124
# enter your element 1221
# [12,13,124,1221]
# mean = __
# median = __
# max = __

# make(4,t)
# enter your element 12
# enter your element 13
# enter your element 124
# enter your element 1221
# (12,13,124,1221)
# mean = __
# median = __
# max = __



# make(4)
# enter your element 12
# enter your element 13
# enter your element 124
# enter your element 1221
# [12,13,124,1221]
# mean = __
# median = __
# max = __


# def makeAcake(flav = "chcocolate" , wei = 3 , shape = "square"): # actual parameters / values in function definition
# 	print(''' you have ordered %s flavoreded cake of %d kgs %s shape'''%(flav,wei,shape))
# makeAcake(flav = "vannilla" , shape = "rect")
# almonds toppings
# makeAcake(toppings = "almonds") #error --> formal and actual parameters

# keyworded parameters
# --------------------
# -> store both formal and actual parameters more than defined ones 
# -> dict is used as storage for arguments
# -> formal --> **kwargs , **kwvars , **_____
# -> type(kwargs) --> Dictionary
# -> 0 ... n keyworded / default arguments

# def makeAcake(flav = "chcocolate" , wei = 3 , shape = "square" , **specs): 
# 	# print(specs)
# 	# print(type(specs))
# 	for i in specs.items():
# 		# print(i)
# 		print(''' you have ordered %s flavoreded cake of %d kgs %s shape with  %s %s'''%(flav,wei,shape,i[0],i[1]))
# # makeAcake(flav = "vannilla" , shape = "rect")
# # almonds toppings
# makeAcake(toppings = "almonds") #error --> formal and actual parameters

# positional (limited) --> variable (unlimited)
# default (limited) --> keyworded (unlimited)

# multiply function
# -----------------
# def funcMul(a,b): #-> definition
# 	c = a*b  #--> implementation
# 	# print(c)
# 	return c #-> return value
# print(funcMul(10,20)) #-> function call

# Lambda functions / Lambda operator / anonymous function
# -------------------------------------------------------
# -> single line operation
# -> auto returned 
# -> lambda is a keyword
# syntax
# ------
# <functionName> = lambda <parameters> : operation

# mulNums = lambda a,b : a*b
# print(mulNums(10,30))

# sumAll = lambda l : sum(l)
# print(sumAll((1,2,3,4)))

# map , filter and reduce 
# -----------------------

# l1 = [2,4,6,9,10,8]
# l2 = [20,40,60,90,100,78]
# ans = [22,44,66,99,110]
# ans = []

# for i in range(0,len(l1)):
# 	ans.append(l1[i] + l2[i])
# print(ans)

# map()
# -----
# -> associative operation
# -> collections
# -> map function
# -> return map object 
# -> map object --> list --> type casting 
# syntax
# ------
# <mapObject> = map(<function> , <collections>)

# res = map(lambda a,b : a+b , l1 , l2) 
# print(res)
# print(list(res))

# print(list(map(lambda a,b : a+b , l1 , l2)))
# print(list(map(lambda a :a + 10  , l1)))

# l3 = [x for x in range(2,38)]
# # print(l3)
# ans = []

# for i in l3:
# 	if(i%2 == 0):
# 		ans.append(i)
# print(ans)

# filter():
# ---------
# -> associative check / conditional statement 
# -> filter object 
# -> type cast --> list 
# -> no need to use if else 
# -> collections

# syntax
# ------
# <filterObject> = filter(<function> , <collection>)
# fo = filter(lambda a : a%2 !=0 , l3)
# print(fo)
# print(list(fo))


l4 = [2,3,4,6,7,8,90]
# ans = 0
# for i in l4:
# 	ans = ans + i
# print(ans)

# reduce()
# --------
# -> not a default function
# -> imported --> from functools import reduce
# -> cumulative operation
# -> return a value 
# syntax
# ------
# from functools import reduce
# <reduceValue> = reduce(<function> , <collection>)

# rv = reduce(lambda a,b : a+b , l4)
# print(rv)
# rv1 = reduce(lambda a,b : a*b , l4)
# print(rv1)

# Modules and packages 
# --------------------
# module --> python file (.py , .pyc , .ipynb)
# c:/> python <modulename>.<ext>

# module1 --> all program components
# module2 --> module1 (variables and functions) 

# 3 kinds
# 	- default
# 	- internal imported 
# 	- external imported

# default 
# --------
# print("Hello")
# print(len(l1))

# internal imported
# ------------------
# import <modulename> 
# XX download XX 
# os , sys , math , cmath , random 

# external imported
# -----------------
# import <modulename> 
# downloaded
# numpy , pandas , shutil 

# external modules /packages
# --------------------------
# pip --> python packaging index (package manager)
# conda --> anaconda 
# windows --> installation + pip 
# pip - 10.4 

# c:/>pip
# error

# bootstrap --> get-pip.py --> copy contents 
# save contents as get-pip.py
# c:/>python get-pip.py
# pip gets installed 

# c:/>pip 
# --
# --- 
# --- 
# --- 


# external modules /packages --> pip , conda , third party 

# install --> c:/>pip install <package>
# uninstall --> c:/>pip uninstall <package>
# list of downloaded packages --> c:/>pip list 
# list of downloaded packages --> c:/>pip freeze 

# downloaded --> pip --> site-packages  

# 3 types of import
# -----------------

# import <modulename>
# 	- all components from modulename
# 	- <modulename>.<component>

# from <modulename> import <component>
# 	- only component from modulename
# 	- <component>

# from <modulename> import *
# 	- all components from modulename
# 	- <component>

# imported --> once 
# run --> imported code --> __pychache__ 

# import tuples
# print(tuples.l1)
# print(tuples.numsSet)

# from tuples import numsSet,numsTuple
# print(numsSet)
# print(numsTuple)

# from tuples import *
# print(numsSet)
# print(numsTuple)

# aliasing --> naming modules 

# import <modulename> as <alias>
# <alias>.<component>

# import tuples as t
# print(t.l1)
# print(t.numsSet)

# packages
# --------
# - folder with __init__.py file 
# - collection of Modules

# folder --> + __init__.py --> package
# __init__.py --> empty file
# 			--> initialise the folder to package

# from <packageName> import <modulename>
# import <packagename>.<modulename>
# 	-> all components from modulename
# 	-> <modulename>.<component>

# from <packageName> import <modulename>.<component>
# import <packageName>.<modulename>.<component>
# from <packageName>.<modulename> import <component>
# 	-> only component
# 	-> XX (.) XX

# package
# 	module
# 		component

# tasks  --> folder name --> package name
# 	1.py
# 	2.py
# 	3.py
# 	__init__.py --> file

# 2.py 	
# 	from tasks import 3

# os ,  random 
# os --> deals wth operating systems , directories(folders)
# 	os.path --> sys paths and path manipulations 

# random --> pseudo random number generation 
# 	- numbers 
# 	- collections
# 	- XX chars , strings XX

import random 

# random() --> random float value b/w 0 and 1 
# print(random.random())

# randint(<start> , <end>) --> random integer b/w start and end 
# print(random.randint(2,100))
# randrange(<start> , <end>) --> random integer b/w start and end 
# print(random.randrange(2,100))

# uniform(<start> , <end>) --> random float b/w start and end 
# print(random.uniform(2,100))

l1 = [1,2,3,4,125,831,5,5,3,32,21,1,432]

# shuffle() --> shuffle elements of a list with no return 
# print(random.shuffle(l1))
# print(l1)

# choice() --> choose a single random element from a collection
# print(random.choice(l1))

# sample() --> random slice of k element collection from a collection 
# print(random.sample(l1,k=2))


# c:/>python mytask.py 4
# 8618

# c:/>python mytask.py 4  6
# 2713
# hdvrhg

# c:/>python pwdgen.py "khan"
# jgwd7659vhcj7267 

# c:/>python pwdgen.py "hari"
# jhdf6981hvjh3431

# c:/>python pwdgen.py "khan"
# user already exists 

# jhdf 6981 hvjh 3431
# namesDict = {user:pwd}
# check user --> 0 --> user already exists 
# 		   --> 1 --> chars(4) + nums(4) + chars(4) + nums(4)



# import random  
# n = 4
# for i in range(4):
# 	print(random.randint(1,9) , end ="")

# def genNums(m):
	# empList = []
	# nums = ""
	# for i in range(m):
	# 	nums = nums + str(random.randrange(0,9))
	# return nums
# res = genNums(9)
# print(res)


# def genChars(m):
# 	chars = ""
# 	pwd = ""
# 	l = []
# 	for i in range(m//2):
# 		chars = chars + chr(random.randrange(67,90))
# 		chars = chars + chr(random.randrange(97,122)) #jedj
# 	for c in chars:
# 		l.append(c)
# 		random.shuffle(l)
# 		pwd = "".join(l)

# 	return pwd

# res = genChars(4)
# print(res)


# user check
# gen pwd 

# nDict = {}
# def userCheck(name):
# 	if name in nDict.keys():
# 		return 0 
# 	else:
# 		return 1 

# def genPwd(name):
# 	if userCheck(name) == 0:
# 		print("User already exists")
# 	elif userCheck(name) == 1:
# 		password = genChars(4) + genNums(4) + genChars(4) + genNums(4)
# 		nDict[name]  = password
# 		print(" %s -- %s" %(name , password))
# 		return password
# 	else: 
# 		print("Some issue ")


# genPwd("khan")
# genPwd("hari")
# genPwd("ravi")
# genPwd("hari")
# print(nDict)


# files / file handling 
# ---------------------
# file - various formats
# 	 - storage of data
# 	 - volatile 
# 	 - pdf , txt , png , mp3 , mp4
# 	 - default --> location is local 

# working --> file handling --> Python

# create 
# open -> read / write
# save 
# close 

# files --> stored --> directories(folders)
# files --> independent of OS 
# directories --> dependent on OS ( OS module )


# files in python
# ---------------
# - default --> format --> .txt 
# - default --> location --> immediate after the code 
# - default --> mode --> read / write --> ??
# - files -- auto saved

# file --> 3 mandatory
# 	- filename.<ext>
# 	- location
# 	- mode 

# open() --> open the file if it exists
# 	   --> create and open the file if it does not exists
# 	   --> return the file object
# 	   --> location/filename.<ext> , mode

# syntax 
# ------
# <fileobj> = open(<location/filename.ext> , mode) # opening of file
# <fileobj>
# <fileobj>
# <fileobj>
# <fileobj>
# <fileobj>.close() # closing of file 

# modes --> 7 
# -----------
# read (r)
# write (w)
# append (a)
# read binary (rb)
# write binary (wb)
# update (+)

# location --> /Users/junaid/Desktop/djkp
# pdf --> pypdf2 
# excel , csv --> pandas , [xlsxwriter , csv]
# image --> PIL 

fobj = open("/Users/junaid/Desktop/djkp/demo.txt" , "w")
# print(fobj)
# writing to files -> W mode ONLY 
# 		- write()
# 		- writelines()
# 			- strings
# syntax
# ------
# <fileObject>.write(<string1>\n)
# <fileObject>.write(<string2>\n)
# <fileObject>.write(<string3>\n)

lines = ["first\n" , "second\n" , "third\n"]
# <fileObject>.writelines(linesCollec)
fobj.write("hello\n")
fobj.write("hai\n")
fobj.writelines(lines)
fobj.close()

# syntax 2
# --------
# with open(<location/filename.ext> , mode) as <fileObject>:

with open("/Users/junaid/Desktop/djkp/demo.txt" , "a") as foo:
	foo.write("new line using with\n")


with open("/Users/junaid/Desktop/djkp/demo.txt" , "a") as foo:
	foo.write("third time writing a line\n")

# write and writelines --> these functions overwrite entire file with latest content 

# append --> mode --> XX delete provided content XX

with open("/Users/junaid/Desktop/djkp/demo.txt" , "a") as foo:
	foo.write("fourth time writing a line")

with open("myfile.txt" , "w") as nfo:
	nfo.write("hey")

# task --> password
# -----------------
# khan  - ________________
# hari  - ________________
# ravi  - ________________

# csv module --> csv file 


# reading of files  --> r mode ONLY
# ----------------
# read()
# 	- entire content from file 
# 	- <fileObject>.read()
# 	- <fileObject>.read(<chars>)
# 	- chars = 10 --> read only 10 chars 
# 	- cursor is placed at last read char 
# readline()
# 	- read only first line of file from cursor 
# 	- till \n
# 	- <fileObject>.readline()
# 	- <fileObject>.readline(<chars>)
# 	- chars = 10 --> read only 10 chars 
# 	- cursor is placed at first char of next line 
# readlines()
# 	- read entire content 
# 	- returns list of lines with \n

# with open("/Users/junaid/Desktop/djkp/demo.txt" , "r") as fr:
	# con = fr.read() # cursor position is at end 
	# print(con)
	# c = fr.read(50) # nothing 
	# print(c)

	# print(fr.readline()) # cursor --> end of first line
	# print(fr.readline())  # cursor --> end of second line
	# print(fr.readline())  # cursor --> end of third line
	# print(fr.readline(3)) # at c
	# print(fr.read()) # after c to end 
	# print(fr.readline()) # nothing

	# print(fr.readlines())

# task
# ----
# readUser() --> # user's names from the file 


# directories --> folders 

# empty directories --> OS module (pre built)
# non empty directories --> shutil (external)

# os --> directory , os related manipulations 
# os.path --> system path manipulations


import os
# print(os.name) # posix
# --> getting operating system name of machine 
# print(os.environ)
# --> name and location of environment / system variables
# print(os.getcwd())
# --> get current working directory 
# os.chdir("/Users/junaid/Desktop/")
# --> changing directory to other directory
# print(os.getcwd())
# os.chdir("/Users/junaid/Downloads/Python_Material/")
# print(os.getcwd())
# make directories
# mkdir(<location/dirName>)
# --> make single empty directory (dirName) at location
# makedirs(<location/directory1/directory2>)
# --> multiple empty directories tree at location provided 

# remove directories
# rmdir(<location/dirName>)
# --> remove single empty directory (dirName) at location
# removedirs(<location/directory1/directory2>)
# --> remove multiple empty directories tree at location provided 

# os.mkdir("khanTasks")
# os.rmdir("khanTasks")

# os.makedirs("/Users/junaid/Downloads/khan/python/tasks")
# os.removedirs("/Users/junaid/Downloads/khan/python/tasks")
# os.rmdir("/Users/junaid/Downloads/Python_Material/") #error -66

# a=os.listdir("/Users/junaid/Downloads/Python_Material/")
# --> list of all components in the directory
# print(a)

# print(dir(os))
# print(os.removedirs.__doc__)
# print(os.rmdir.__doc__)

# os.path
# -------
# -> path manipulations
# -> walk 

# print(dir(os.path))
# basename(<location>) --> directory name in path provided
# abspath(<location>) --> path and directory name in path provided

# print(os.path.basename(os.getcwd()))
# print(os.path.abspath(os.getcwd()))


# split(<location/directory>) --> slipt path and directory
# path , direct = os.path.split(os.getcwd())
# path , direct = os.path.split("/Users/junaid/Desktop/djkp")
# print(path)
# print(direct)

# splitext(<location/file.ext>) --> split path,file and extension
# pfile , ext = os.path.splitext("/Users/junaid/Downloads/Python_Material/Python Material/part-4 Documentation/Materials/exeptional handling.pdf")
# print(pfile) # path and file name
# print(ext) # extension of file 


# os.walk() --> 3 outputs 
# 		-> paths 
# 		-> dirs 
# 		-> files 


# for i in os.walk("/Users/junaid/Downloads/Python_Material/"):
	# print(i[0])
	# print(i[1])
	# print(i[2])
	# print(i)

Repository management 
---------------------

git --> technology 
install --> machine
	-> git libs 
	-> git shell (terminal for git) 
	-> git GUI 

-> files and directories

git + directory --> 3 areas
		-> working area  --> editor
		-> staging area 
		-> local Repository

file --> working --> staging --> local --> user

remote Repository --> global Repository
	-> git server 
	-> third party git Repositories (public/private)
		-> github
		-> bit bucket
		-> gitlab 

file --> working --> staging --> local --> remote --> everyone

git --> installed
codes --> + git --> goto
		--> git init --> initialise the codes directory with git 
				-> working area  
				-> staging area 
				-> local Repository

git init

git add <filename.ext> --> working to staging
git add . 

git commit -m "<dialouge>" --> staging to local Repository

local --> remote Repository

git remote add origin <git link>

git push origin master 
	- origin --> remote Repository
	- master --> machine 


git status --> current status of Repository


git remote add origin https://github.com/junaid238/kp3pm.git


























