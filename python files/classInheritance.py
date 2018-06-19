# class parent():
# 	a = 10 
# 	b = 20 
# 	def __init__(self , name ):
# 		self.name = name
# 		print("hello " + self.name)
# 	def add(self,c , d):
# 		su = c+ d
# 		print(su)
# 		print(self.name)
# p = parent("khan") # calling the init
# q = parent("ravi")
# # print(p.a) # 10
# # print(p.b) # 20 
# p.add(20,30) # 50
# q.add(200,30) # 50
# # print(p) #obj refence from __str__

# class child(parent):
# 	e = 10 
# 	f = 20 
# 	def __init__(self , name):
# 		print("hai")
# 		super(child,self).__init__(name)
# 		super().__init__(name)
# 	def diff(self , m , n):
# 		print(m-n)
# c = child("khan")
# class employee():
# 	org_name = "Lync"
# 	count = 30
# 	def __init__(self , name , salary):
# 		# global count
# 		print(name + " has a salary of "+ str(salary))
# 		employee.count = employee.count + 1
		# count = count +1

# e1 = employee("khan" , 1000)
# e2 = employee("ravi" , 2000)
# print(employee.count)
# print(employee.org_name)


# private protected public 

# class vars:
# 	a = 10 # public 
# 	_b = 20 # protected
# 	__c = 30 # private 
# 	print(a)
# 	print(_b)
# 	print(__c)

# v = vars()
# print(v.a)
# print(v._b)
# print(v._vars__c)
# obj._classname__variable --> private --> outside the class 




