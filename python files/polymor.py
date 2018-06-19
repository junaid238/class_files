# # method overloading 
# # * args 
# # method ovverriding

# class over:
# 	# constructor 
# 	def __init__(self,name, age):
# 		self.name = name
# 		self.age = age 
# 		print("hello")
# 	# make custom object printing __str__()
# 	def __str__(self):
# 		# print(self.name , self.age)
# 		return "%s %d %s"  %(self.name , self.age , "str")

# 	# # make custom object printing __repr__()
# 	def __repr__(self):
# 		return "%s %d %s" %(self.name , self.age , "repr")

# obj = over("khan" , 30 )
# # printing an obj by using __str__()
# print(obj)
# obj2 = over("Hari" , 35 )
# # printing an obj2 by using __str__()
# print(obj2)

# class vars:
# 	a = 10  # public variable 
# 	print(a , "from class") # without reference
# 	_b = 20  # private  variable 
# 	print(_b , "from class")
# 	__c = 200 # protected variable
# 	print(__c, "from class")
# v = vars 
# print(v.a , "from obj reference") # obj reference 
# print(vars.a,"from class reference") # class reference
# print(v._b , "from obj reference")
# print(vars._b  ,"from class reference")
# protected variable not accessible outside the class 
# print(v.__c , "from obj reference")
# protected variable not accessible outside the class 
# print(vars.__c  ,"from class reference")
# object._classname__variable
# print(v._vars__c ,"from class reference")

# Operator overloading 

# + __add__()
# - __sub__()
# * __mul__()
# / __div__()
# // __floordiv__()


# class num:
# 	def __init__(self,a ):
# 		self.a = a
# 		print(self.a)

# 	def __sub__(mine , your):
# 		x = mine.a
# 		y = your.a
# 		return x+y

# h = num(10)
# g = num(20)
# print(h-g)



# num1 num2
# 10 + 2
# + 10  2 
# 10 2 + 

