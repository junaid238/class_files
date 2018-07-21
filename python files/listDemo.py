# List functions 
# --> len(<listname>) --> no of elements in list
# --> listname.count(<item>) --> repetetions of item
# --> listname.index(<item>) --> index value for item 

# Adding / removing 
# -----------------
# stacks --> LIFO  ??
# queues --> FIFO  ??

# Python --> LIFO  --> stacks


# listname.append(<item>)
# 	---> add am element at the last (LIFO)

# listname.pop()
# 	---> remove an element from last (LIFO)

# listname.insert(<index> , <item>)
# 	---> add an item at particular index

# listname.remove(<item>)
# 	---> remove particular item from list

# del listname[<index>]
# 	---> delete item from a particular index

# max(<listname>) 
# 	---> maximum value from the list
# min(<listname>)
# 	---> minimum value from the list
# <listname>.sort()
# 	---> only numbers , only strings
# 	---> sort the list in ascending order 

# <listname>.sort(reverse = True)
# 	---> sort the list in descending order

# sort() , insert() , remove()  ---> no return values 

# Concat
# ------

# --> joining of 2 lists 

# l1 = [1,2,3,4]
# l2 = ["a" , "b" , "c" , "d"]

# l1 + l2 ---> [1,2,3,4 ,"a" , "b" , "c" , "d" ]
# l3 = l1 + l2 


# extending of lists:
# -------------------

# l1 = [1,2,3,4]
# l2 = ["a" , "b" , "c" , "d"]

# <list1>.extend(<list2>)
# l1.extend(l2)

# l1 = [1,2,3,4 ,"a" , "b" , "c" , "d"]
# l2 = ["a" , "b" , "c" , "d"]

# l2.extend(l1)
# l1 = [1,2,3,4]
# l2 = [1,2,3,4 ,"a" , "b" , "c" , "d"]


# l1 = [20,30,4010,20,30,40 , 30]
# l2 = ["a" , "b" , "c" , "d"]

# print(len(l1))
# print(len(l2))

# print(l1.count(30))
# print(l2.count("c"))

# print( 70  not in l1)
# print( 30   in l1)

# print(l2.index("c"))
# print(l1.index(30))
# print(l2[2])

# print(l1)
# a = l1.append(100)
# print(l1)
# # print(a)

# l2.append(200)
# print(l2)

# a = l1.insert(3 , "khan")
# # print(a)
# print(l1)

# a = l1.pop()
# print(a)
# print(l1)
# l1.pop()
# print(l1)
# l1.pop()
# print(l1)

# a = l2.remove("c")
# print(l2)
# # print(a)
# print(l2)
# l3 = l1 + l2
# print(l3)

# l1.extend(l2)
# print(l1)
# print(l2)

# a = l1.sort()
# # print(a)
# print(l1)
# l2.sort()
# print(l2)

# l1.sort(reverse = True)
# print(l1)
# l2.sort(reverse = True)
# print(l2)
# l3 = l1 + l2 
# l3.sort()
# print(l3)

# task 1
# ------
# input
# -----
# list1 = [10 , 30 ,23 ,4 , 5 , 10 ,23 , 45 , 100 , 3 , 6 , 5]
# expected output
# ---------------
# uni = [10 , 30 , 23 , 4,5 , 10 ,45, 100 ,3, 6]
# rep = [10 , 5 , 23]

# uni = []
# rep = []

# for i in list1:
# 	print(i)
# 	if i not in uni :
# 		uni.append(i)
# 	else:
# 		rep.append(i)

# print(" Unique elements " , uni)
# print(" Repeated elements " , rep)

# squ = []
# list1.sort()
# for i in list1:
# 	squ.append(i**2)
# print(squ)


# num = 7
# l = len(str((num**3)))
# for i in range(num):
# 	print("%s    %s    %s" %(str(i).zfill(l) , str(i**2).zfill(l)  , str(i**3).zfill(l)))



# list Comprehensions 
# -------------------
# --> making lists 
# 	--> normal elements
# 	--> elements with operation
# 	--> elements with checking and operation


# syntax:
# -------
# --> normal elements
# <listName> = [<assignmnet> <loop> ]


# declaration
# normal = []
# # looping over elements
# for i in range(2,21):
# # assignment 
# 	normal.append(i)
# print(normal)

# nor = [ i  for i in range(2,21)  ]
# print(nor)


# --> elements with operation

#declaration
# squ = []
# # looping over elements
# for i in nor :
# 	# assignment with operation
# 	squ.append(i**2)
# print(squ)

# syntax:
# ------
# <listName> = [<assignment+ operation> <loop>]

# squLC = [ i**2 for i in range(2,21)]
# print(squLC)

# --> elements with checking and operation
# declaration
# evenSq = []
# looping over elements
# for i in nor:
# 	# checking 
# 	if i % 2 == 0:
# 		# assignment + operation
# 		evenSq.append(i**2)
# print(evenSq)

# syntax:
# -------
# <listName> = [<assignment+ operation> <loop> <check>]
# evenSqLC = [ i**2  for i in range(2,21) if (i%2==0)]
# print(evenSqLC)

tasks
-----
expected output
---------------
python filename.py 
enter length of list 
4
enter the element 1
enter the element 2
enter the element 30
enter the element 400

[1,2,30,400]

n - gram
--------

dia = "given member of the test dataset and in turn make a prediction"

enter the n 
1 
["given" , "member" . . . . ., "prediction"]

enter the n 
2
["given member" , "member of" , "of the ", ..... , "a prediction"]

enter the n 
3
["given member of " , " of the test" , , ..... , "make a prediction"]