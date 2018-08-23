# mylist = [1,2,3,4,78,5,6,7,8]
# itera = iter(mylist)
# print(itera) # reference of iterable object
# print(next(itera))
# print(next(itera))
# print(next(itera))

# class double:
# 	def __init__(self,last =0 ):
# 		self.last = last
# 	def __iter__(self):
# 		self.n = 0 
# 		return self
# 	def __next__(self):
# 		if self.n<=self.last:
# 			res = 2* self.n
# 			self.n +=1
# 			return res
# 		else:
# 			raise StopIteration
# print(double(5))
# a = double(5)
# i =iter(a)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# # for i in double(10):
# # 	print(i)
# # # A simple generator function
# def gen():
#     n = 1
#     yield n
#     n += 1
#     yield n
#     n += 1
#     yield n
#     n += 1
#     yield n

# for i in gen():
# 	print(i)
# # # Using for loop
# # for item in gen():
# #     print(item)    
def doubler(last = 0):
	n = 0
	while n < last:
	    yield n*2
	    n += 1

# for i in doubler(5):
# 	print(i)

# try:
# 	def div(a , b):
# 		ans = a/b
# 		print(ans)
# 	div(10,"a")
# except ZeroDivisionError as e:
# 	print("invalid. b value ")
# except TypeError as e:
# 	print("invalid char in b ")


# class numEr(Exception):
# 	def __init__(self):
# 		print("error occured")
# try:
# 	a = 100
# 	if(a>20):
# 		raise numEr
# except numEr as e:
# 	print(e)


class revrange:
	def __init__(self,last = 0):
		self.last = last
	def __iter__(self):
		self.n = self.last
		return self
	def __next__(self):
		if self.n>0:
			self.n -=1
			return self.n
		else:
			raise StopIteration
for i in revrange(10):
	print(i)


