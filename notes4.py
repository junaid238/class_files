# loopimg structures 
# --> iterative 
# --> repetitions 
# --> finite , infinite 

# --> for , while 
# --> XXX do while XXX

# components 
# 	- initialisation
# 	- limit / condition 
# 	- statements ( compulsory )

# 3 data types
# ------------
# - numbers 
# - strings 
# - collections 

# numbers --> range()
# range(<end>) --> 0 to end-1 (inc = 1)
# range(<start> , <end>) --> <start> to <end>-1 (inc =1)
# range(<start> , <end> , <step>) --> <start> to <end>-1 (inc =<step>)

# syntax
# ------
# for <dummy> in range():
# 	<statements>

# initialisation = 0
# condition = i <10
# statements = print(i)
# for i in range(10):
# 	print(i)

# for i in range(12,30):
# 	print(i)

# for i in range(12,30,3):
# 	print(i)

# dec step = -1 (--)
# ------------------
# for i in range(12,3,-1):
# 	print(i)

# patterns 
# --------
# star /char
# number 

# *
# **
# ***
# ****
# *****

# ***** --> print("*" * 5)
# **** --> print("*" * 4)
# print("*" * 3)
# print("*" * 4)
# print("*" * 5)
# for var in range(1,6):
# 	print("*" * var)

# for num in range(1,6):
# 	print(str(num) * num)
# 1
# 22
# 333
# 4444
# 55555

# n= 5
#     * # 4 space 1 star
#    ** # 3 space 2 star
#   *** # 2 space 3 star
#  **** # 1 space 4 star
# ***** # 0 space 5 star
# 		i 		n-i
# n = 6
# for i in range(n,0, -1):
# 	print((" "*i) + ("*"*(n-i)))

# task1 
# -----
	# *
 #   ***
 #  *****
 # *******
# task2
# -----
# num = 4
# 00 00 00
# 01 01 01
# 02 04 08
# 03 09 27
# 04 16 64

# num = 5
# 000 000 000
# 001 001 001
# 002 004 008
# 003 009 027
# 004 016 064
# 005 025 125

# nested loops 
# ------------
# for :
# 	for :
# 		for :
# 			<statements>

# for 
# 	if 
# 	else

# even odd classifier
# -------------------
# st = 100
# en = 120
# if type(st) is str or type(en) is str :
# 	print("enter only numbers")
# else:

# 	for i in range(st , en+1):
# 		if(i%2 == 0 ):
# 			print("%d is %s" %(i , "even"))
# 		else:
# 			print("%d is %s" %(i , "odd"))

# 1
# 12
# 123
# 1234
# 12345

# 12345 
# for i in range(1,6):
# 	print(i , end ="")
# print()
# # 1234 
# for i in range(1,5):
# 	print(i , end ="")
# print()
# # 123
# for i in range(1,4):
# 	print(i , end ="")

# for num in range(1,6):
# 	for var in range(1, num+1):
# 		print(var , end = "")
# 	print()

# for num in range(6,1,-1):
# 	for var in range(1, num):
# 		print(var , end = "")
# 	print()

# composite - 12 - 1,2,3,4,6,12
# prime - 7 - 1,7

# num = 12
# composite
# num = 13
# prime

# 12 % 1 ==0
# 12 % 2 ==0
# 12 % 3 ==0
# .
# .
# .
# .
# 12 % 12 ==0
# 0's - 6 - composite'

# 7 % 1 == 0 
# 7 % 2 != 0
# .
# .
# .
# 7 % 7 == 0
# 0's - 2 - prime'
# count = 0
# num = 12
# for i in range(1,num+1):
# 	if (num%i == 0 ):
# 		count += 1

# if(count > 2):
# 	print("%d is %s"%(num , "composite"))
# else:
# 	print("%d is %s"%(num , "prime"))

# s = 13
# e = 20

# 13 - prime 
# 14 - composite
# 15 - composite

# num = 5
# 5 * 1 = 5
# 5 * 2 = 10
# .
# .
# .
# 5 * 10 = 50

# composite and prime in a range

# num = 20
# e = 30

# for j in range(num , e+1):
# 	count = 0
# 	for i in range(1,j+1):
# 		if (j%i == 0 ):
# 			count += 1

# 	if(count > 2):
# 		print("%d is %s no of factors --> %d"%(j , "composite" , count))
# 	else:
# 		print("%d is %s"%(j , "prime"))

# for i in range(3,0,-1):
# 	for j in range(1,7,2):
# 		print(" "*i,end="")
# 		print("*"*j)
# n = 32
# l = len(str(n**3))
# for num in range(0,n):
# 	print("%s %s %s"%(str(num).zfill(l) , str(num**2).zfill(l) , str(num**3).zfill(l)))

# strings + loops 
# ----------------
# tech = "python and data sceinces and Data Analytics"
# print(tech[0])
# print(tech[1])
# print(tech[2])
# print(tech[3])
# all languages
# -------------
# for i in range(0,len(tech)):
# 	print(tech[i])

# syntax
# ------
# for <dummy> in strname:
# 	<statements>

# for dummy in tech:
# 	print(dummy)

# for i in tech:
# 	if(i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u" ):
# 		print(i , end =" ")

# n = 5
# a
# bb
# ccc
# dddd
# eeeee
# ASCII --> a-z => 97-122 , 65-90
# ord() chr()

# n = 4 
# en = 97 + n # 97 + 4 = 101 -> d
# st = ""
# for i in range(97,en):
# 	st = st+chr(i)
# print(st)

# for j in st:
# 	for i in range(1,5):
# 		print(j*i)

# for j in range(1,n+1):
# 	for i in range(97,en):
# 		print(chr(i) * (j))

# print(chr(97) * 1)
# print(chr(98) * 2)
# print(chr(99) * 3)
# print(chr(100) * 4)

# while loop
# ----------
# - initialisation
# - condition
# - statements
# - inc/dec
# - infinite loop

# syntax
# ------
# <initialisation>
# while (<condition/limit>):
# 	<statements>
# 	<inc/dec>

# infinite --> condition always true

# a = 1
# while (a<=10):
# 	print(a)
# 	a= a+1

# a = 10
# while (a>=1):
# 	print(a)
# 	a= a-1

# infinite loops
# a = 10
# while a ==10:
# 	print(a)

# while (True):
# 	print("hai")

# control statements
# -------------------
# pass , break , continue  --> keywords 

# pass --> overcome unimplementations / no statements
# 	- condition , loops , functions , classes
# break --> exit the loop at condition-> loops
# 		-> atm -- 3 wrong attempts 
# continue --> exit the loop at condition and returns ( pause )
# 		-> ticketing , queues 
		

# for i in range(1,40):
# 	if(i == 26):
# 		break
# 	print(i)

# d = 20
# while (d<40):
# 	print(d)
# 	d = d + 1
# 	if(d == 25):
# 		break

# d = 30 
# while (d<50):
# 	d += 1
# 	if(d == 40):
# 		continue
# 	print(d)

# for --> continue --> ??
# patterns --> while --> ??


# Collections:
# ------------
# derived data types 
# 	- lists
# 	- tuples
# 	- dictionaries

# 	- sets and frozen sets 

# collection ==> module ( queue )

# --> grouped storage spaces
# LIFO -> stack
# FIFO -> queue
# --> stacks

# Lists
# -----
# - heterogeneous collection
# - mutable 
# - infinite length 
# - 1 dimensional 
# - LIFO 
# - nested 
# - <class list>
# - iterable

# - indexed 
# - sliced
# - concatenated 
# - extended


# syntax
# ------
# names = [1 ,"1", "khan" , [1,2,3,4]]

# access(indexed/sliced)
# ------
# names[0] # 1
# names[1] # "1"
# names[3] # [1,2,3,4]
# names[3][3] # 4

l1 = [1,2,3,"a" , "khan" , [20,40,50,89]]
# print(l1)
# print(type(l1))
# indexing 
# --------
# print(l1[0])
# print(l1[4])
# print(l1[5])
# print(l1[5][0])
# print(l1[5][3])
l2 = [[[[[[[[5]]]]]]]] 
# print(l2[0][0][0][0][0][0][0][0])

# slicing 
# -------
# <listname>[<start>:<end>] --> start to end-1
# <listname>[:<end>] --> first element to end-1
# <listname>[<start>:] --> start to last element
# print(l1[2:5])
# print(l1[:5])
# print(l1[3:])

# concatenated
# print(l1 + l2 )
# print(l1)
# print(l2)

# iterable
# print(l1[0])
# print(l1[1])
# print(l1[2])
# for i in range(0,5):
# 	print(l1[i])

# for i in l1 :
# 	print(i)

# functions 
# ---------
# len(<listname>) --> length of list
# <listname>.index(<item>) --> index of item passed
# <listname>.count(<item>) --> frequency of items

names = ["khan" , "ravi" , "hari " ,"khan" ]
# print(names)
# print(len(names))
# print(names.index("ravi"))
# print(names.index("khan" , 1)) # index = 1
# print(names.count("khan"))

# mutable properties 
# ------------------
# add , del , remove , extend 
# add --> append() insert() # LIFO
# <listname>.append(<item>)
# names.append("rajesh")
# print(names)
# <listname>.insert( <index> , <item> )
# names.insert( 3, "kumar" )
# print(names)

# remove --> pop() , remove()
# pop() --> last element removed 
# remove(<item>) --> element gets removed 
# names.pop()
# print(names)
# names.pop()
# print(names)
# names.remove("khan")
# print(names)

# index --> indexing --> item(remove)

# delete single element
# del <listname>[<index>]
# del names[2]
# print(names)

# delete multiple element
# del <listname>[<start> : <end>]
# del names[2:4]
# print(names)

# delete entire list
# del <listname>
# del names 
# print(names)

# modify element ( indexing )
# --------------
# names[2] = "rajesh"
# print(names)

# modify multiple elements ( slicing )
# --------------
# names[2:4] = "rajesh" , "rahul"
# print(names)

# extending of lists:
# -------------------
# concatenated --> different 
# print(l1)
# l3 = names + l1
# print(l3)
# print(names)
# print(l1)

# <listname1>.extend(<listname2>)

# print(names)
# print(l1)
# print("after extending")
# names.extend(l1) # all l1 elements gets attached to names LIFO 
# print(names)
# print(l1)

# print(names)
# nums = [10,20,30,40,50]
# # print(nums)

# for i in names:
# 	nums.append(i)

# # print(names)
# print(nums)

repList = [1,2,3,4,5,7,8,23,5,13,19,2,1,2,3,4,5,6,78,8] # question list

# unique = [1,2,3,4,5,6. . .. . .] # all unique elements
# reps = [6 , 8 , 1 ,2 ,3, 4 ..  .] # all repeated elements

# print(6 in repList)
# print(60 in repList)

# make an empty list
unique = []
reps = []
for i in repList:
	if(i not in unique):
		unique.append(i)
	else:
		reps.append(i)

# print(unique)
# print(reps)

# squares of unique elements
# squ = []
# notPo = []
# for i in unique:
# 	if (type(i) is not str ):
# 		squ.append(i**2)
# 	else:
# 		notPo.append(i)

# print(squ)
# print(notPo)

# unpacking of lists 

# listinlist = [1,2,3,[4,5,7,8],23,5,13,[19,"a",2,1],2,3]
# # elems = [1,2,3,4,5,7,8,23,5,13,19,"a",2,1,2,3,]
# elems = []
# for i in listinlist:
# 	if(type(i) is list):
# 		for j in i:
# 			elems.append(j)
# 	else:
# 		elems.append(i)
# print(elems)

# enter no of elements 4
# enter element 10
# enter element 100
# enter element 20
# enter element 30

# [10,100,20,30]

# emp = []
# length = int(input("enter no of elems you need"))
# while length > 0 :
# 	ele = input("enter the element")
# 	emp.append(ele)
# 	length -= 1

# for i in range(0,length):
# 	ele = input("enter the element")
# 	emp.append(ele)
# print(emp)

# namesNums = [. . .. . ]
# 1 add element
# 2 remove element

# enter your option
# 1
# enter the element
# 10
# [ .. . . , 10]

# enter your option
# 2
# enter the element
# 10
# [ .. . . , ]

# namesNums = [10 , 20 , 30]
# print(namesNums)
# print("1. add an element.  ")
# print("2. remove an element. ")
# option = int(input("enter your option.  "))
# if option == 1:
# 	element = int(input("enter the element. "))
# 	namesNums.append(element)
# 	print(namesNums)
# elif option ==2 :
# 	print(namesNums)
# 	element = int(input("enter the element. "))
# 	namesNums.remove(element)
# 	print(namesNums)
# else:
# 	print("wrong input")

# print(repList)

# sort() , append() , remove() --> no return 

# <listname>.sort() # directly sort the list without return
# ascending order
# repList.sort()
# print("after sorting")
# print(repList)

# # descinding list
# repList.sort(reverse = True)
# print("sorting in reverse format")
# print(repList)

# names = ["a" , "c " , "r" , "w" , "b " , "e"]
# names.sort()
# print(names)


# Tuples 
# ------
# - collection
# - immutable 
# - <class tuple>
# - infinite length
# - heterogeneous collection
# - indexed , sliced , concatenated
# - iterable collection

# syntax
# ------
# <tupleName> = (<elements>)
# <tupleName> = <elements> , 

# nums = (1,2,3,4,5)
# print(nums)
# print(type(nums))
# names = "khan" , "hari" , "ravi" , 
# print(names)
# print(type(names))

# indexing 
# print(nums[0])
# print(nums[4])

# slicing
# print(nums[2:4])
# print(nums[1:3])
# a = nums[2:4]
# print(type(a))

# nums[2] = "khan"

# len() , index() , count() --> do not modify content 

# del nums # entire tuple
# del num[2] # cannot delete a single item

# print(nums.count(2))
# print(nums.index(2))
# print(len(nums))
# nums.append(4)

# tuple --> ??
# -> constants 
# mathconst = (3.14, 2.71 ,6.3)
# fees = ("20k" , "15k" , "25k")

# type casting 
# ------------
# list --> tuple ==> tuple()
# tuple --> list ==> list()
# print(fees)
# print(type(fees))
# fees = list(fees)
# print(fees)
# print(type(fees))
# fees[2] ="30k"
# fees = tuple(fees)
# print(fees)
# print(type(fees))

# List comprehensions
# -------------------
# -> making lists 
# 	-> assigned 
# 	-> assigned + condition
# 	-> assigned + operation + condition

#declaring an empty list
# nList = []
# # looping /iterating
# for i in range(0,10):
# 	# assignment
# 	nList.append(i)
# print(nList)

# <listname> = [  <assignmentVar> <loop structures>	]
# numList = [ x  for x in range(0,10)	]
# print(numList)

# #declaring an empty list
# emList = []
# # # looping /iterating
# for i in range(1,100):
# 	# condition check 
# 	if i % 5 == 0 :
# 		# assignment
# 		emList.append(i)
# print(emList)

# <listname> = [ <assignmentVar>  <looping structures> < condition> ]
# emList = [ x for x in range(1,100) if x%5 == 0 ]
# print(emList)

# # #declaring an empty list
# listo = []
# # # # looping /iterating
# for i in range(1,21):
# 	# assignment + operation
# 	listo.append(i**2)
# print(listo)

# <listname> = [ <assignmentVar + operation>  <looping structures> ]
# listo = [ x**2 for x in range(1,21) ]
# print(listo)

# <listname> = [ <assignmentVar + operation>  <looping structures> <condition]
# fiveMuls = [i**2 for i in range(1,100) if i%5 == 0 ]
# print(fiveMuls)

# Tuple comprehensions --> ???
# -------------------- 
# XXX no tuple comprehensions XXX 
# 			0		1	2		3		4		5			6
# form -> fname , lname , age , email , mobile , peradd , preadd 
# 1can -> ---- , ------ , -----,------ , ------ , ------ , ------  
# 2can -> ---- , ------ , -----,------ , ------ , ------  

# 1can[5] --> peradd
# 2can[5] --> preadd
# --> indices will be ours 
# --> named tuple and Dictionary

# Dictionary
# ----------
# -> collection
# -> <class dict>
# -> mutable 
# -> indexed 
# -> concatenated
# -> pairs of data --> keys and values 
# -> indices are customisable --> keys 
# -> elements --> values 
# -> keys + values --> items 
# -> heterogeneous (conditions)

# syntax
# ------
# empDict = {}
# namesDict = { <key1>:<value1> , <key2>:<value2> , <key3>:<value3> }

# keys --> immutable objects -> numbers , strings , tuples , unique  
# values --> anything
# print(empDict)
# print(type(empDict))

# formData = {"fname": "khan" , "age" :27  , "mobile": 9876543210 , "email": "khan@gmail.com"}
# keys -- fname , age , mobile , email
# values -- khan , 27 , 9876543210 , khan@gmail.com
# formData = {"fname": "khan" , (1,2,3,4) :27  , "mobile": 9876543210 , "email": "khan@gmail.com"}
# print(formData)
# keys -- fname , (1,2,3,4) , mobile , email
# formData = {"fname": "khan" , [1,2,3,4] :27  , "mobile": 9876543210 , "email": "khan@gmail.com"}
# print(formData)
# keys -- fname , [1,2,3,4] , mobile , email
# formData = {"fname": "khan" , (1,2,3,4) :[1,2,3,4,45] , "mobile": 9876543210 , "email": "khan@gmail.com"}
# print(formData)
# keys -- fname , (1,2,3,4) , mobile , email

# access of elements --> keying 
# -----------------------------
# <dictName>[<key>]
# print(formData["age"])
# print(formData["mobile"])
# print(formData["post"]) # key error unexisting

# re assignment of  values
# ------------------------
# <oldvalue> --> <newValue> # key is existing
# <dictName>[<key>] = <newValue>
# print(formData["age"])
# formData["age"] = 30 
# print(formData["age"])
# print(formData)

# if unexisting it adds at the last 
# formData["role"] = "py developer" 
# print(formData)

# functions 
# ---------
# len() --> length of keys 
# len(<dictName>)
# print(len(formData))

# .keys() --> all the keys in Dictionary
# <dictName>.keys()
# print(formData.keys())

# .values() --> all the values in Dictionary
# <dictName>.values()
# print(formData.values())

# .items() --> all the items in Dictionary
# <dictName>.items()
# print(formData.items())

# for i in formData.keys():
# 	print(i)

# for i in formData.items():
# 	print(i)

# pop() , popitem()
# <dictName>.pop(<key>) --> item of that key
# <dictName>.popitem() --> last item of that dictName

# formData.popitem()
# print(formData)
# formData.pop("age")
# print(formData)

# formData2 = {"lname": "khan" , "myage" :27  , "mob": 9876543210 , "mail": "khan@gmail.com"}
# # <dictName1>.update(<dictName2>)
# formData.update(formData2)
# print(formData)
# print(formData2)

# formData.update({"add" : "hyd" , "role" : "PyDev"})
# print(formData)

# dict --> list of Keys and list of values
# 2 lists --> 1 dict 

# l1 = [1,2,3,4,5]
# l2 = ["a" , "b" , "c" , "d" , "e"]
# chrDict = {}

# # o/p ---> {1:"a" , 2:"b" , 3:"c" , 4:"d" , 5:"e" }
# for i in range(0,len(l1)):
# 	chrDict[l1[i]] = l2[i]
# print(chrDict)

# zip() ---> lists => dict
# zip() --> XX dict XX ==> zip object --> type casting -->dict 

# <zipObject> = zip(<listname1> , <listname2>)
# <dictName> = dict(<zipObject>)

# zobj = zip(l1,l2)
# print(zobj) # <zip object at 0x1103bc848>
# chrdict = dict(zobj)
# print(chrdict)

# d = dict(zip(l1,l2))
# print(d)

# [1,2,3,4,5,6] i/p
# {1:1 , 2:4 , 3:9 ...} o/p
# sq = {}
# l1 = [1,2,3,4,5,6] 
# for i in l1:
# 	sq[i] = i**2
# print(sq)

# dictionary comprehensions
# -------------------------
# <dictName> = { <var1>:<var2> <loop with dependency> }
# sq = { x:x**2 for x in range(1,6)}
# print(sq)

# sq = { x:x**2 for x in range(1,30) if x%3 == 0 }
# print(sq)

# Sets and frozen sets 
# --------------------
# -> Collection
# -> 2.5 + , 3.X

# -> storage elements
# -> unique elements
# -> math sets 
# -> XXX indexed , sliced XXX
# -> iterated
# -> mutable 
# -> arbitary
# -> <class set>

# syntax
# ------
# numsSet = {1,2,3,4,5,6, 1,2 ,6 }
# numsSet = set({1,2,3,4,5,60})
# print(numsSet)
# print(type(numsSet))

# empSet = set({})
# print(type(empSet))

# print(numsSet[0])
# for i in numsSet:
# 	print(i)

# numsSet.add(100)
# print(numsSet)

# numsSet.remove(100)
# print(numsSet)
# numsSet.remove(1000) # KeyError: 1000
# print(numsSet)

# numsSet.discard(100)
# print(numsSet)
# numsSet.discard(1000) # XX no error XX
# print(numsSet)

# nuumsSet = { 1 ,3 }
# print(numsSet + nuumsSet)

# .union
# .intersection
# .difference
# .issubset
# .issuperset

# print(numsSet)
# print(nuumsSet)

# print(numsSet.union(nuumsSet)) # all elements
# print(numsSet.intersection(nuumsSet)) # common elements
# print(numsSet.difference(nuumsSet)) # only numsSet
# print(nuumsSet.difference(numsSet)) # only nuumsSet

# print(numsSet.issubset(nuumsSet))
# print(numsSet.issuperset(nuumsSet))

# chrTuple = ("a" ,"man " , "is "  ," learning")
# empstr = "-".join(chrTuple)
# print(empstr)
# print(type(empstr))

# Frozen sets --> ????
# sets --> immutable
# sets --> lists
# Frozensets --> tuples
# <class frozenset>
# syntax
# ------
# fsNum = frozenset((1,2,3,4,5))
# print(fsNum)
# print(type(fsNum))

# Functions
# ---------
# - block of a code 
# - only one task 
# - components
# 	- definition (mandatory)
	# - implementation (mandatory)
# 	- call (optional)
# - first class objects
# - nested functions also possible 

# - pre defined functions (python)
# - user definition functions (user)

# parameters 			return type
# 	0 					0 			sort()
# 	1					1			index(<item>)
# 	1					0			remove()
# 	0					1			pop()


# syntax
# ------
# def <functionName>():  ---> Function definition
# 	<implementation>   ---> Function implementation

# <functionName>() 	---> Function call 1
# <functionName>() 	---> Function call 2
# <functionName>() 	---> Function call 3
# <functionName>() 	---> Function call 4

# def sayHello(): # definition
# 	print("say hello") # implementation

# sayHello() # call 1
# sayHello() # call 2

# not recommended
# def sayHello(): # definition
# 	print("say hai ") # implementation
# sayHello() 

# Return type 
# ------------
# - output of a Function
# - one output
# - one return statement
# - var , value , Function , Function call , object 

# syntax
# ------
# return <component>

# - if no return --> None 
# - if return --> component
# - <component> --> save --> function call

# return a value 
# def sayHello(): # definition
# 	print("say hello")
# 	return " say hello "
# a = sayHello()
# print(a)

# return a variable 
# num = 100 
# def sayHai(): # definition
# 	print("say hai ")
# 	return num
# a = sayHai()
# print(a)

# return of function and function call
# def returner():
# 	print("returning a function name")
# 	return addNums
# print(type(returner)) # function
# print(type(returner())) # function
# a = returner()
# print(a(100,200))
# print(type(a)) # function
# print(type(a(100,200))) # int

# def returnerTwo(a , b):
# 	print("returning call ")
# 	return addNums(a , b)
# print(returnerTwo(20,30)) # 50 from addNums


# empty function --> pass
# --------------
# def empfunc():
# 	pass
# b = empfunc()
# print(b)

# multiple return type 
# --------------------
# def saybye(): # definition
# 	print("say bye ")
# 	return "bye"
# 	return "hai"

# a = saybye()
# print(a)

# parameters
# ----------
# - inputs to function
# - arguements 
# - any type 
# - two kinds
# 	- formal parameters
# 	- actual parameters
# - formal parameters ==> definition , variables
# - actual parameters ==> function call , values

# - 4 types 
# 	- positional 
# 	- default
# 	- variable 
# 	- keyworded 

# def hello(name): # name --> formal parameter
# 	print("Hai " + name)
# 	return name
# a = hello("khan") # "khan" --> actual parameter
# print(a)

# a = 10 # global variable
# def incnum(num):
# 	global a # bring global variable into the function
# 	# a = 100 # incnum variable (function variable)
# 	print("your parameter " , num) # formal parameter
# 	print("increment by " , a)
# 	print("after increment ")
# 	print(num + a)
# 	return num+a # variable + formal parameter
# incnum(20)
# print(a)

# multiple parameters 
# def addnum(a,b): # a=10 b = 20
# 	''' it calculates sum of two nums''' 
# 	''' dummy''' 
# 	ans = a+b # ans = 30
# 	print("sum is " , ans) # ans = 30 
# 	return ans # 30 -->XX ans = 30 XX , addnum(10 , 20) = 30

# print(addnum.__doc__)
# a = addnum(10 , 20)
# print(a)
# print(addnum(30,40))

# sumnum(20,30) # 50
# diff(<50> , 10) # 40
# mul(<40> , 10) # 400
# div(<400> , 20) # 20 


# enter your list length 
# 4
# enter num 10
# enter num 20
# enter num 30
# enter num 40
# enter your choice
# 1. mean 
# 2. median 
# 3. both
# 1 --> mean = 25
# 2 --> median = 25
# 3 --> mean = 25 , median = 25


# length = 4
# numberlist = [10,20,30,40]
# def calc(listNums):
# 	print("1. Mean")
# 	print("2. Median")
# 	print("3. Both")
# 	choice = int(input("Enter your choice"))
# 	if(type(choice) is int):
# 		if(choice == 1):
# 			mean(listNums)
# 		elif(choice == 2):
# 			median(listNums)
# 		elif(choice == 3):
# 			mean(listNums)
# 			median(listNums)
# 		else:
# 			print("enter 1 or 2 or 3 ")
# 	else:
# 		print("Enter only numbers")

# def mean(nums):
# 	sumOfList = 0
# 	for i in nums:
# 		sumOfList += i
# 	ans = sumOfList // len(nums)
# 	print("Mean is " , ans)

# def median(nums):
# 	if(len(nums) % 2 != 0):
# 		ans = nums[len(nums)//2]
# 		print("Median " , ans)
# 	else:
# 		ans = (nums[len(nums)//2] + nums[(len(nums)//2)+1]) //2
# 		print("Median " ,ans)

# calc(numberlist)

# docstring 
# ---------
# - decription of a function
# - string ''' '''
# - __doc__
# - just after definition

# print(range.__doc__)

# [_ , _ , _]
# [_ , _ , _]
# [_ , _ , _]

# enter player 1 X "khan"
# enter player 2 O "prabal"

# khan enter the position (1-9) 4
# [_ , _ , _]
# [X , _ , _]
# [_ , _ , _]

# prabal enter the position (1-9) 5
# [_ , _ , _]
# [X , O , _]
# [_ , _ , _]

# default parameters
# ------------------
# cake - flav  , wei  , shape 



# using positional parameters
# ---------------------------
# def makeCake(flav , wei , shape): # fixed values to formal parameters
# 	print("you have oredered " +flav +" flavoured cake of "+wei +"kgs and "+shape +" shape")

# # 1 - chco , 2 , square
# # 2 - 3 , vannila , round 
# # 3 - pine , 5 
# # 4 - almond , rect
# # 5 - cake 

# makeCake("chco" , "2" , "square")
# makeCake(wei = "3" , flav = "vannila" ,shape =  "round") # formal parameters in function call 
# makeCake("pine" , 5)
# makeCake("almond" , , "rect")
# makeCake()

# using default parameters
# ------------------------

# def makeCake(flav = "vannila" , wei ="1", shape = "round"): # fixed values to formal parameters
# 	print("you have oredered " +flav +" flavoured cake of "+wei +"kgs and "+shape +" shape")

# # # 1 - chco , 2 , square
# # # 2 - 3 , vannila , round 
# # # 3 - pine , 5 
# # # 4 - almond , rect
# # # 5 - cake 

# makeCake("chco" , "2" , "square")
# makeCake(wei = "3" , flav = "vannila" ,shape =  "round") # formal parameters in function call 
# makeCake("pine" , "5")
# makeCake(flav = "almond" , shape =  "rect")
# makeCake()

# makeList --> length , collection
# 4 , list  --> [ ]
# 5 , dictionary --> { }
# 3 , tuple --> ( )
# 6 --> [ ]

# variable parameters
# -------------------

# def addNum(a,b):
# 	ans = a+b
# 	print(ans)

# addNum(10,20)

# --> 0 - n
# --> tuple --> *args , *vars , *abcd -> formal parameters
# --> single , multiple arguements ---> actual parameters

# def addNum(*args):
# 	print(args)
# 	print(type(args))
# 	count = 0
# 	for i in args:
# 		count += i
# 	print(count)

# # addNum()
# # addNum(10)
# # addNum(10,20)
# addNum(10,20,30)

# positional arguements
# avg --> a,b,*args 
# avg() --> XX
# avg(10) --> XX
# avg(10,20) --> a = 10 , b = 20 , args = 
# avg(10,20,30) --> a = 10 , b = 20 , args = (30)

# def avgNums(a,b,*nums):
# 	count = a + b
# 	print("a is ",a)
# 	print("b is ",b)
# 	print("nums is ",nums)

# 	for i in nums:
# 		count += i
# 	ans = count / (len(nums) + 2)
# 	print(ans)
# avgNums()
# avgNums(10)
# avgNums(10,20)
# avgNums(10,20,47,50,39,100)

# Keyworded parameters
# --------------------
# - Dictionary args
# - **kwargs , **kwvars , **abcds 

# def makeCake(flav = "vannila" , wei ="1", **kwargs): # fixed values to formal parameters
# 	print(kwargs)
# 	print("you have ordered " +flav +" flavoured cake of "+wei +"kgs and ")

# makeCake(wei = "3" , flav = "vannila" ,shape ="round",toppings= "almonds")

# positional --> unlimited --> variable --> *args
# default --> unlimited --> keyworded --> **kwargs 

# inputs 
# ------
# - keyboard --> input()
# - console --> cmd
# - list of input values from cmd 

# c:/>python myFile.py  4
# 10 
# c:/>python myFile.py  5
# 15
# c:/>python myFile.py  "khan"
# a 

# list--> cmd args --> argv
# argv[0] --> fileName --> myFile.py
# argv[n] --> arguements followed -->"khan"

# import sys 
# print(sys.argv)

# import sys 
# print(sys.argv[1])

# Lambda functions
# ----------------
# - definition
# - implementation
# - call 

# Lambda functions - single line implementation
# anonymous functions / Lambda operator 
# auto returned 

# syntax
# ------
# <functionName> = lambda <parameters> : <implementation>

# def addNums(a,b):
# 	ans = a+b
# 	return ans # return 10 
# addNums(10,20)
# print(type(addNums))
# addNums = lambda a,b : a+b
# print(addNums(10,20))
# print(addNums(11,21))

# sq = lambda a : a**2
# print(sq(10))
# print(sq(110))

# map filter reduce 
# -----------------

l1 = [2,4,5,8,2]
l2 = [4,9,7,54,1]
# l3 = [6 .......,3]

# l3 = []
# for i in range(0,len(l1)): # i --> 0 1 2 3 4 --> indices
# 	l3.append(l1[i] + l2[i]) # l1[i] l1[0 1 2 3 4 ] --> element
# print(l3)

l4 = [1,2,4,4,7,8,6,5,43,2,2,1]
# even = []
# for i in l4:
# 	if i % 2 == 0 :
# 		even.append(i)
# print(even)

# map 
# ----
# - function
# - associative operation function
# - function and collections
# - return map object

# syntax
# ------
# <mapObject> = map(<function> , <collections>)
# mo = map(lambda a,b : a+b , l1 , l2 )
# print(mo)
# l4 = list(mo)
# print(l4)
# print(list(map(lambda a,b : a+b , l1 , l2 )))

# mo = map(lambda a : a**2 , l1  )
# print(mo)
# l4 = list(mo)
# print(l4)

# print(list.__doc__)

# filter 
# ------
# - function
# - associative checking function
# - function and collections
# - return filter object

# syntax
# ------
# <filterObject> = filter(<function> , <collections>)
# fo = filter(lambda a:a%2 != 0 , l4)
# print(fo)
# ans = list(fo)
# print(ans)

# print(list(filter(lambda a:a%2 != 0 , l4)))
# print(tuple(filter(lambda a:a%2 != 0 , l4)))

# reduce
# ------
# - cumulative operation 
# - return value 
# - function collections
# - not pre defined --> import from functools

# syntax
# ------
# from functools import reduce 
# <answer> = reduce(<function> , <collection>)

# from functools import reduce 
# res = reduce(lambda a,b : a+b , l4 )
# count = 0 = b
# a+b --> count += a
# print(res)

# res = reduce(lambda a,b : a*b , l4 )
# print(res)

# Modules and packages 
# --------------------
# module --> python file (.py , .ipynb, .....)

# pre built already imported  --> print()
# pre built explicitly imported --> reduce() , sys.argv
# external and explicitly imported 

# folder --> collection of Modules  
# package --> folder + initialisation module 
# initialisation module --> __init__.py

# folder --> + __init__.py --> package

# __init__.py --> empty file 


# importing 
# ---------
# import <moduleName>
# 	- import all the components from <moduleName>
# 	- use --> <moduleName>.<component>
# 	- first import creates _pycache_ folder

# import check 
# print(check.l)
# print(check.numprint())

# from <moduleName> import <component>
# 	- import only the component from moduleName
# 	- use --> <component>

# from check import l
# print(l)
# print(check.a) # error 

# from <moduleName> import *
# 	- import all components except some specials
# 	- use --> <component>

# from check  import *
# print(l)
# print(a)

# alias --> nick name to module
# -----------------------------
# import classEighteenOnline as ei
# print(ei.a)

# import check as ch
# print(ch.l)

# from <packageName> import <moduleName>
# import <packageName>.<moduleName>

# from <packageName>.<moduleName> import <component>
# import <packageName>.<moduleName>.<component>

# External Modules/packages
# -------------------------
# pip --> python packaging index 10.x 
# pip --> installed 
# 	- win --> auto installed with python
# 	- if not installed --> get-pip.py --> run in cmd 
# cmd --> c:/>pip
# 	commands in pip

# pip install <extPackage> # internet 
# pip uninstall <extPackage> # internet 
# pip list
# pip freeze

# location of download --> <python/install/path>/site-packages
# pip install numpy 
# pip uninstall numpy 

# Classes and Objects 
# -------------------
# class --> collection of entities
# 	entities --> variables and methods 
# 	variable --> where we do ?
# 	method   --> what we do ?

# three components
# ----------------
# - definition (mandatory)
# - implementation (mandatory)
# - object creation

# syntax
# ------
# class <className>: --> definition of a class
# 	<implementation1>
# 	<implementation2> --> implementation of a class
# 	<implementation3>

# object --> instance of class 

# class  --> function
# object --> call 

# Function --> 100 lines --> output
# Function --> 100 lines --> call --> output

# class --> 1000 lines --> output
# class --> 1000 lines --> object --> output

# single class --> multiple objects

# syntax
# ------
# <objectName> = <className>()

# --> entities 
# 	- class reference (.) --> <className>.<entity>
# 	- object reference (.) --> <objectName>.<entity>
# two kinds
# ---------
# - class attributes (variables and methods)
# - instance attributes (variables and methods)

# self --> stores instance or objectName which calls the method
class Employee: # class definition
	name = "Digital Lync" # class variables
	address = "Hyderabad" # class variables

	def named(self,name): # method with self # instance method
		print("hello " + name)
		print(self)

emp1 = Employee() # object creation 
# emp2 = Employee() # object creation 

# print(emp1.name) # object reference to name
# print(emp1.address) # object reference to address

# emp2.name = "Lync"
# print(emp2.name) # object reference to name
# # print(emp2.address) # object reference to address

# Employee.name = "DL"
# print(Employee.name) # class reference to name
# print(Employee.address) # class reference to address

# print(emp1.name) # object reference to name
# print(emp1.address) # object reference to address

# print(emp2.name) # object reference to name
# print(emp2.address) # object reference to address

# emp1.named("Khan") # object reference for a method
# emp2.named("Ravi") # object reference for a method
# Employee.named("Hari") # error for class reference

# three types of methods
# ----------------------
# - instance methods
# 	- self --> object name
# 	- object reference
# 	- XX class reference XX
# 	- changes -- instance , object
# - class methods
# 	- cls --> class name
# 	- class , object references
# 	- changes --> instance and class
# 	- decorator --> @classmethod 
# - static methods
# 	- logical implementation
# 	- XX parameter
# 	- object reference
# 	- XXX changes --> class or object
# 	- decorator --> @staticmethod

# constructor (__init__()) 
# -----------
# - initialisation of a class 
# 	- default constructor
# 	- parameterize constructor

# object create --> constructor --> class --> output
# <objectName> --> <__init__> --> <className> --> output

# syntax
# ------
# def __init__(self):
# # 	<implementation>

# class Organisation: # class definition

# 	org_name = "Digital Lync" # class variables
# 	address = "Hyderabad" # class variables

# 	def __init__(self,name,role):
# 		self.name = name 
# 		self.role = role 
# 		print("hello " + name + " has been assigned " + role +" role")		
	
# 	def details(self): # method with self # instance method
# 		print("Your name : " + self.name + "\n your role: " + self.role +" role")
	
# 	@classmethod
# 	def changeOrgName(cls , newname):
# 		cls.newname = newname
# 		cls.org_name = cls.newname
# 		print("Organisation name has been changed to "+cls.newname)	

# 	@staticmethod
# 	def calc(amount , perc):
# 		ans = ((amount * perc) //100) + amount
# 		print(ans)
# e1 = Organisation("khan" , "pd") # constructor is called name and role 
# e2 = Organisation("ravi" , "Dr")

# print(e1.org_name)
# print(e2.org_name)

# e1.details()
# e2.details()

# Organisation.changeOrgName("lync")

# print(e1.org_name)
# print(e2.org_name)
# print(Organisation.org_name)

# e1.calc(1876567 , 22)

# Modules 
# -------
# random , math , cmath , os 

# random
# ------
# pseudo random numbers 
# 	- numbers 
# 	- collection
# Functions
# ---------
# Numbers
# 	- random()
# 	- randrange()
# 	- randint()
# Collection
# 	- choice()
# 	- sample()
# 	- shuffle()

import random 
# random() --> float value 0<num<1
# print(random.random())
# randint(<start> , <end>) --> random integer b/w start and end inclusive 
# print(random.randint(2,40)) 
# randrange(<start> , <end>) --> random integer b/w start and end inclusive 
# print(random.randrange(2,40)) 

# l1 = [x for x in range(2,23)]
# print(l1)

# random.shuffle(<list>) --> all elements of a collection gets shuffled
# random.shuffle(l1)
# print(l1)

#random.choice(<list>) --> one random element from a collection
# print(random.choice(l1))

#random.sample(<list> , k=<population>) --> multiple elements from a collection
# print(random.sample(l1 , k = 2))

# c:/>python randChr.py 5 
# jdskb

# c:/>python randChr.py 9 4 
# ytgfvgkfi
# 8673

# import sys 
# print(sys.argv)
# count = 0
# for i in range(0, int(sys.argv[1])+1):
# 	count += i
# print(count)

# numbers --> ascii --> chars 
import sys , random
# char = ""
# for i in range(0 , int(sys.argv[1])):
# 	char = char + chr(random.randrange(97,122))
# print(char)

# char = ""
# num = ""
# for i in range(0 , int(sys.argv[1])):
# 	char = char + chr(random.randrange(97,122))
# print(char)
# for i in range(0 , int(sys.argv[2])):
# 	num = num + str(random.randrange(0,9))
# print(num)


# c:/>python p wdmake.py "khan"
# dfgg9821hgvj6536
# c:/>python pwdmake.py "Ravi"
# jhdf7236bfjb3390
# c:/>python pwdmake.py "khan"
# user already exists

# pwds.txt
# khan -- dfgg9821hgvj6536
# Ravi -- jhdf7236bfjb3390

# a = 10 
# b = 20 
# ans = a+b
# ans2 = a+ans 
# with open("demo.txt" , "w") as myf:
# 	myf.write(str(ans)+"\n")
# 	myf.write(str(ans2))
# # myf.close()
# with open("demo.txt" , "r") as myfr:
# 	listOflines = myfr.readlines()
# 	print(listOflines)
# 	res = int(listOflines[0][:-1]) + int(listOflines[1])
# 	print(res)