# # python

# class parent:
# 	a = 10 
# 	b = 20 
# 	def add( self,m,n):
# 		self.sum = m + n
# 		print(self.sum)# python

# class parent2:
# 	name = "khan" 
# 	age  = 20 
	
# class child(parent , parent2):
# 	c = 100 
# 	d = 2000 
# 	def sub( self,x,y):
# 		self.diff = x - y
# 		print(self.diff)

# # p = parent()
# # print(p)
# # print(p.a , "from parent object")
# # print(p.b , "from parent object")
# # p.add(30,40 )
# # # print(p.c)
# ch = child()
# # print(ch)
# # print(ch.a , "from child object")
# # print(ch.b , "from child object")
# # ch.add(300,40 )
# # print(ch.c)
# print(ch.name)
# print(ch.age)
class employee:
	orgName = "Lync"
	def __init__(self , name , age):
		# print("hello")
		print(name + " is of "+str(age) +" years")
class manager(employee ):
	post = "Manager" 
	def __init__(self , name , age):
		# print("hai")
		super().__init__(name , age)
		print(name + " is of "+str(age) +" years has been promoted as Manager")
# emp1 = employee("khan" , 27)
# emp2 = employee("hari" , 30)
man1 = manager("khan" , 27)

