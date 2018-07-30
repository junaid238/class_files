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