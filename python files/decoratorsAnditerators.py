# iterators and decorators
# ------------------------
# @classmethod 
# @staticmethod

# --> add special functionlaity to function immediate to it 
# --> functions --> first class objects 
# --> funct --> functionality
# --> funct + dec --> extra functionality

def sayHi():
	print("hi")
	return "hello"
# print(sayHi) # address
# print(sayHi()) # hi hello 
# print(type(sayHi)) # function
# print(type(sayHi())) # string 

# def numPrint():
# 	print("first line")
# 	def sub1():
# 		print("from sub1")
# 	def sub2():
# 		print("from sub2")

# 	return sub1()
# numPrint() # sub1()
# print(numPrint()) # first line from sub1

# def deco(methodname):
# 	print("from deco")
# 	def wrapper():
# 		print("from wrapper")
# 		methodname()
# 	return wrapper
	
# @deco # deco(numsprint)
# def numsprint():
# 	print("hello from numsprint")
# numsprint() # direct call 


# iterators 
# ---------
# --> repetative jobs 
# --> start , end , inc/dec
# --> classes
# range(3,24) --> 3 . . . . 23 
# list()

# iter object --> range, list , string  --> __iter__() 
# next object --> elements --> __next__()
# limit ends --> StopIteration 


# l1 = [3,321,6,8,9,0,6,5,4,32]
# itObj = iter(l1) # list --> iter object
# print(itObj)
# print(next(itObj))
# print(next(itObj))



# iterator --> class
# 	--> __init__() --> end point
# 	--> __iter__() --> start point
# 	--> __next__() --> logic / limit 

# double(5) --> 0 , 2 , 4 , 6 , 8 , 10
class double:
	def __init__(self , last = 0):
		self.last = last
	def __iter__(self):
		self.n = 0
		return self 
	def __next__(self):
		if self.n <= self.last:
			res = 2*self.n 
			self.n+=1
			return res
		else:
			raise StopIteration

itObject = double(5)
# print(iter(itObject))
# print(next(itObject))
# print(next(itObject))

for i in double(7):
	print(i)









