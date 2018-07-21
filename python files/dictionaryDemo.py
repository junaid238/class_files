# list --> tuple conversion 
# list --> tuple ====> tuple()
# tuple --> list ====> list()

# fee = ("20k" , "25k" , "30k")
# print(fee)
# # print(type(fee))
# # conversion of tuple to list ]
# fee = list(fee)
# # print(fee)
# # print(type(fee))
# fee[1] = "27k"
# # print(fee)
# fee = tuple(fee)
# print(fee)
# print(type(fee))


# dictionaries 
# --> key , value pairs

formData = {"fanme" : "khan" , "mobile" : 987 , "tech" : "Py"}
print(formData)
print(type(formData))

# list of all varibales and functions of particular component
# # print(dir(dict))
# # accessing 
# print(formData["tech"])
# # print(formData["lname"])


# # modify 
# formData["tech"] = "PHP"
# print(formData)
# formData["lname"] = "Junaid"

# print(formData)

# functions 

# print(formData.keys())
# print(formData.values())
# print(formData.items())

# for i in formData:
# 	print(i)
# for i in formData.keys():
# 	print(i)
# for i in formData.values():
# 	print(i)
# for i in formData.items():
# 	print(i)

# iterkeys()
# itervalues()
# iteritems()

# formData.clear()
# print(formData)

# copy = formData.copy()
# print(copy)

# key pair of fanme is removed
# a= formData.pop("fanme")
# print(formData)
# print(a)
# # last item removed
# b = formData.popitem()
# # print(formData)
# print(b)

# nums = {1:2 , 3:4 , 4:5 }

# nums.update(formData)
# print(nums)

# formData.update({10:20 , 30:40})
# print(formData)

# print(len(formData))


# dict -->list 
# .items()

# l1 = [10,20,30,40,50,60]
# l2 = ["a" , "b " ,"c" , "d" , "e"]

# list -->dict 
# zip() --> zip(list1 , list2) --> zip object
# # type casting to a dictionary
# dict(zip object)

# z = zip(l1,l2)
# print(z)

# d = dict(z)
# print(d)

# enumerate 
# enumerate()

# e = enumerate(l1)
# print(e)
# print(dict(e))

# e = enumerate(l1 , 100)
# print(e)
# print(dict(e))

# dictionary comprehensions 

# key --> relation with value

# num = 4
# sq = {1:1 , 2:4 , 3:9 , 4:16}

# 1 2 3 4  --> list1

# l1 = [i for i in range(1,5)]
# l2 = [i**2 for i in range(1,5)]

# 1 4 9 16 --> list2 
# print(dict(zip (l1 , l2)))

# declartion
# d = {}
# # looping
# for i in range(1,5):
# 	# opeartion and assignment of keys and values
# 	d[i] = i**2
# print(d)



# syntax
# ------
# <dictName> = { <key> : <value>   <looping>      }

# di = {x:x**2   for x in range(1,5)}
# print(di)

# task1
# -----
# listTask = [10,20,30,[2,4,5] , 100 , (11,34,19) , 13]
# output = [10,20,30,2,4,5, 100 ,11,34,19, 13]

# for i , j in listTask,output:
# 	print(i)
# 	print(j)

# l1 = [1,2,3,4]
# l2 = [10,20,30,40]
# output = [11,22,33,44]

# cumulativeSum = 10
# cumulativeSumTwo = 100

# R&D:
# ----
# exec() ---> ???
# .sorted() ---> ???
# .all() ---> ???