# types of methods 
# ----------------
# - instance methods 
# - class methods 
# - static methods 

# java - access specifiers, modifiers 
# python - keywords as parameters

# instance methods
# ----------------
# - accessed by only object reference 
# - self as parameter
# - self --> object that is calling 
# - affect only the instance/object
# - <object>.<methodname>

# class methods
# -------------
# - accessed by object and class reference
# - cls as parameter
# - cls --> class name 
# - affects both class and object
# - <classname>.<methodname> or <object>.<methodname>
# - decorator --> @classmethod

# static methods
# --------------
# - accessed by objects
# - no parameter
# - affects none of class and object 
# - <classname>.<methodname> or <object>.<methodname>
# - logical implementation 
# - decorator --> @staticmethod

# to customise --> print of object --> __str__() and __repr__()

OOPS 
----
inheritance  --> C++
	- simple /single 
	- multiple
	- multi level
polymorphism 
	- overriding 
	- overloading
	- compiler time polymorphism
	- run time polymorphism
encapsulation 
abstraction 

operator overloading 












# class company:
# 	# class variables 
# 	nameCompany = "digitalLync"
# 	address = "hyd"
# 	ecount = 20
# 	elist = []

# 	# hiring method --> employee --> instance method dunder 
# 	def __init__(self,name, role , salary):
# 		self.name = name 
# 		self.role = role 
# 		self.salary = salary 
# 		# print(self.name + " have been hired to DL ")
# 		company.ecount = company.ecount + 1
# 		company.elist.append(self.name)

# 	# company details --> company --> class method
# 	@classmethod
# 	def compDetails(cls):
# 		print("company name " + cls.nameCompany)
# 		print("company address " + cls.address)
# 		for i in cls.elist:
# 			print("employees " + i , end = " , ")
# 		print("total employees " + str(cls.ecount))

# 	# change entire company and employees
# 	@classmethod
# 	def changeCompName(cls,newname):
# 		cls.nameCompany = newname
# 		print("company's name changes to " + cls.nameCompany)

# 	@staticmethod
# 	def hikeCalc(sal , perc):
# 		ans = (sal*perc) + sal
# 		print(ans)
# 		return ans

# 	def salhike(self,perc):
# 		self.finalsal = self.hikeCalc(self.salary , perc)
# 		self.salary += self.finalsal 
# 		print(" your salary has incremented to " + str(self.salary))

# e1 = company("khan" , "PD" , 1)
# e2 = company("satish" , "PD" , 10)
# e1.compDetails()
# company.compDetails()
# company.changeCompName("DL")
# print(e1.nameCompany)
# e2.compDetails()
# company.hikeCalc(10000 , 10)
# e2.hikeCalc(10000 , 10)
# print(e1.salary)
# e1.salhike(hikeCalc())
# e2.salhike(10)
# print(e1)
