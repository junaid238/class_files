def incNum(a):
	print(a+1)
	return a+1
# print(incNum(10))
# a = incNum(20)
# print(type(a))
# print(type(incNum))

# def caller(f , arg):
# 	print("hello")
# 	return f(arg)
# caller(incNum , 20)

# def callerWarg(f):
# 	print("hai")
# 	return f
# a = callerWarg(incNum)
# print(type(a))
# a(30)


# def super():
# 	print("hello from super")

# 	def sub1():
# 		print("hey from. sub 1")
# 	def sub2():
# 		print("hey from. sub 2")
# 	sub1()
# 	sub2()
# super()



def deco(func):
	print("from decorator")

	def wrapper():
		print("from wrapper")
		func()
	return wrapper

@deco
def printme():
	print("print from outside")

# deco(printme)
# b = deco(printme)
# b()
printme()


