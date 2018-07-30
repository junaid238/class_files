# list1=[2,4,51,6,72,12,22]
# l = ["_" ,"_"]
# l[1] = "a"
# print(l)
# sum=0
# for i in range(0,len(list1)):
# 	sum=sum+list1[i]
# print(sum)

# for i in range (1,11):
# 	if (i%5==0):
# 		print("*"*i)
# 		continue
# 	print(str(i)*i)

# for i in range (1,11):
# 	if (i%5==0):
# 		for j in range(1,i+1):
# 			print(j,end="")
# 		print()
# 		continue
# 	print(str(i)*i)

# list1=[1,2,3,4,5,"aaa","bbb",4,5,"aaa","ccc",10]
# unique=[]
# for i in range(0,len(list1)):
# 	if (list1[i] not in unique):
# 		unique.append(list1[i])
# print(unique)

# list1=[1,2,3,4,5,"aaa","bbb",4,5,"aaa","ccc",10]
# for i in list1:
# 	if i not in unique:
# 		unique.append(list1[i])
# print(unique)
		
# def sqgen(last = 0):
# 	n = 0 
# 	if n<=last:
# 		yield n**2
# 		n +=1

# for i in sqgen(5):
# 	print(i)
# try:
# 	def division(a ,b):
# 		res = a/b
# 		print(res)
# 	division(10,5)
# 	division(10,10)
# 	division(10,1)	
# 	print("hai")
# 	division(8,2)

# except Exception as e :
# 	print(e)

# finally:
# 	print("hello")

# names = ["M.Anand Rahul","adarsh Sharma","Robin Babu P","Deba Prasad Mishra","Sowjanya","Kariveda Vishal Reddy","D.Suresh Kumar","D Suresh Kumar friend ","D Suresh Kumar friend ","D Suresh Kumar friend ","Shravan Kumar.M","Shravan Kumar friend ","Shravan Kumar friend ","Shravan Kumar friend ","tirunagari Raghavendra"]
# mobiles = ["8143827119","7702323131","7384426616","9581912305","9100593362","9640582662","9959965968","9959965968","9959965968","9959965968","9885569118","9885569118","9885569118","9885569118","9700149039"]
# namesMobiles = dict(zip(names, mobiles))
# print(namesMobiles)

# l1 = [1,2,3,4,5 ,(1,11) , ((100,50), 120)]
# ans = []
# print(l1)
# print(type(l1))
# a = type(l1)
# b = str(a)
# print(str(a))
# print(type(b))
# for i in l1:
# 	if str(type(i)) == "<class 'tuple'>" or str(type(i)) == "<class 'list'>":
# 		print(i)
# 		for j in i:
# 			ans.append(j)
# 	else:
# 		ans.append(i)
# print(ans)

# [1, 2, 3, 4, 5, (1, 11), ((50, 11), 12)]

# def addElem(i):
# 	if str(type(i)) == "<class 'tuple'>" or str(type(i)) == "<class 'list'>":
# 		for j in i:
# 			addElem(j)
# 	else:
# 		ans.append(i)
# 		return i
# for e in l1:
# 	addElem(e)
# print(ans)

l=[1,6,7,3,[19,20],2,8,(80,90)]
# output=[]
# for i in l:
# 	if(type(i) is list or type(i) is tuple):
# 		for j in i:
# 			output.append(j)
# 	else:
# 		output.append(i)
# print(output)

# def deco(methodName):
# 	def wrapper():
# 		print("hello from wrapper")
# 		methodName()
# 		print("hello after the deoc call ")
# 	return wrapper
# 	# wrapper()
# @deco
# def numprint():
# 	print("output from deco using @ ")
# numprint()

# def printNum():
# 	print( "output from printNum method ")
# printNum()

# a = deco(printNum)
# a()

# prog = 'print("The sum of 5 and 10 is", (5+10))'
# exec(prog)


# random_string = '   this is good '


# print(random_string.lstrip(" si t"))

# Arithmetic 
a = 23
# b = 7
# print(23+ 7)
# print(23-7)
# print(23* 7)
# print(23/ 7)
# print(23// 7)
# print(23%7)
# print(23** 7)


# c = 90.89
# print(type(c))
# print(type(a))


# d = 4 + 5j
# print(type(d))

# e = 987654321234567890987654321234567898765432123456789
# print(type(e))

# comparisoin operators 

# print(a == b)
# print(a >= b)
# print(a <= b)
# print(a != b)
# print(a > b)
# print(a < b)

# logiacal operators

# print(a == b and a <= b)
# print(a == b or a >= b)
# print(10 and 20 and 56 and 56)
# print(10 or 20 or 40 or 455)

# bitwise operators

# print( 10 & 20 ) # 0000 0000
# print( 10 | 20 ) 
# print(~(10))
# print(10>>2)
# print(10<<2)

# print("Python")
# print("Data Sceinces ")

# print("Python", end = " ")
# print("Data Sceinces" , end = " ")
# print("DevOps")

# Tasks
# -----
# new = "pythonbestforbeginners"
# exOutput = "yhnetobgnes"

# starting at 1 till end odd indexing 
# print(new[1::2])

# print(new)
# reverse a string new 
# start =  end = step = -1
# print(new[::-1])

# print(new)
# exOutpu = "py@ho@be@tf@rb@gi@ne@s"
# all every repeated --> loop

# for i in range(0,len(new)): 
# 	if(i%3==0):
# 		new[i]='@'
# for i in range(0 , len(new)+1):
# 	if(i%3 == 0):
# 		# new = new.replace(new[i] , "@")
# 		# print(new[i])
# 		new.replace(new[i] , "@")
# print(new)
# print(new)


# user = input("enter a string ")
# for i in range(0,len(user)):
# 	if(i % 3 == 0):
# 		print(user[i])

# a = 10 
# b = 20 

# exOutput:
# --------
# b ---> 10 
# a ---> 20

# using temp 
# temp = a
# print(temp)
# a = b 
# print(a , " from a ")
# b=temp
# print(b , " from b")

# Without using temp 
# a = a+b # 30 
# b = a-b # 20
# a = a-b # 10 
# print(a , " from a ")
# print(b , " from b")


# l1 = [1,2,3,5,6,7,2 ,53,5, 3,2,6,7,8,90,9]
# largest = 90
# second largest = 9
# print(max(l1)) # get largest number 
# l1.sort()
# print(l1)
# print("second largest number " , l1[len(l1) - 2])

# mode --> maximum repetition number
# temp = 0
# for i in l1:
# 	# print(i , l1.count(i))
	
# 	if(l1.count(i) > temp):
# 		temp = l1.count(i)
# 		print(i)
# print(temp)

# even number make a new list
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []

# for i in a:
# 	if i % 2 == 0:
# 		b.append(i)
# print(b)


# 5) Write a program to add two matrices?

# list1 = [1,2,3,4]
# list2 = [10,20,30,40]
# exp = []
# if(len(list1) == len(list2)):
# 	for i in range(0 , len(list2)):
# 		exp.append(list1[i] + list2[i])
# else:
# 	print("lengths of lists are unequal ")
# print(exp)


# passing list as an arguement to a function 

# def avgList(a):
# 	print(a)

# my = [1,2,3,4,5]
# avgList(my)
# myList = []
# def genList(length):
# 	for i in range(0,length):
# 		ele = input("enter the element")
# 		appender(ele)

# def appender(element):
# 	myList.append(element)
# 	print(myList)

# length = int(input("Enter the length of list you need"))
# genList(length)

# number squares cubes of numbers 
# num = 10
# l = len(str((num-1)**3))
# for i in range(num):
# 	print("%s       %s       %s" %(str(i).zfill(l) , str(i**2).zfill(l) , str(i**3).zfill(l)))

# import operator
# distances = [([2,2,2],5.2 ),([4,4,4] , 1.732)]
# print(distances)
# # sort as per distances value 1 of the tuple in a list of distances
# distances.sort(key=operator.itemgetter(1))
# print(distances)

# import operator
# def getResponse(neighbors):
# 	classVotes = {}
# 	for x in range(len(neighbors)):
# 		response = neighbors[x][-1]
# 		if response in classVotes:
# 			classVotes[response] += 1
# 		else:
# 			classVotes[response] = 1
# 	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
# 	return sortedVotes[0][0]
# neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
# response = getResponse(neighbors)
# print(response)

# dictionary = {'fname': "khan", 'age': 27, 'mobile': 987, 'address': [4,"hyd"]}
# print(dictionary["fname"] + str(dictionary["age"]))
# print(dictionary["age"])

# print(dictionary)
# dictionary.pop('one')
# print(dictionary)
# dictionary.popitem()
# print(dictionary)
# dictionary.update({1: "one", 2: "two"})
# print(dictionary)
# dictionary.clear()
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
# print(len(dictionary))
# print(enumerate(dictionary))
# print(list(enumerate(dictionary)))
# print(list(enumerate(dictionary,10)))
# print(list(enumerate(dictionary.values())))
# for i in dictionary.values():
# 	print(i)
# l1 = [1,2,3,4]
# l2 = ["a","b","c","d"]
# demo = { x:x**2 for x in l1}
# print(demo)

# listTask = [10,20,30,[2,4,5] , 100 , (11,34,19) , 13]
# elements = []
# for i in listTask:
# 	if type(i) is list or type(i) is tuple:
# 		for j in i :
# 			elements.append(j)
# 	else:
# 		elements.append(i)
# print(elements)

# for i in listTask:
# 	if type(i) == str("<class 'list'>")  or type(i) == str("<class 'tuple'>"):
# 		for j in i :
# 			elements.append(j)
# 	else:
# 		elements.append(i)
# print(elements)
# 
# .(a,b,c) .(x,y,z)
# t1 = (3,4,5)
# t2 = (30,40,50)
# d = dict(zip(t1,t2))
# l = []
# for i in d.keys():
# 	l.append((i - d[i])**2)
# print(l)
# print(sum(l)**0.5)
# import csv
# import random
# import math
# import operator
# trai = []
# test = []
# with open("iris.csv", 'r') as csvfile:
# 		# capture data into a data object 
# 		lines = csv.reader(csvfile)
# 		print(lines)
# 		# type cast each of the line to a list 
# 		dataset = list(lines)
# 		# print(dataset)
# 		for i in range(len(dataset) - 1):
# 			# for y in range(4):
# 			# 	dataset[i][y] = float(dataset[i][y])
# 			if(random.random() < 0.67):
# 				trai.append(dataset[i])
# 			else:
# 				test.append(dataset[i])
# print(len(test))
# print(len(trai))


# l1 = [x for x in range(10)]
# # print(l1)
# # a = l1.pop()
# # print(a)
# # b = l1.sort()
# # print(b)
# c = len(l1) --> l1 --> call , actual parameter
# print(len(l1))
# print(c)
# d = l1.append(100)
# print(d)

# e = print(10)
# print(e)
# print()

# l1 = [1,2,3,[10,30] , (30,40) , 11 , 330 , [22,49] , 300]

# elements = []
# for i in l1:
# 	if type(i) is list or type(i) is tuple:
# 		for j in i:
# 			elements.append(j)
# 	else:
# 		elements.append(i)

# print(elements)


# num = 10 # str --> XX enter XX type(num)
# if(type(num) is str ):
# 	print("enter number")
# else:
# 	if (num == 10):
# 		print("gm")

# 	elif(num == 20):
# 		print("gn")

# 	else:
# 		print("wrong time ")