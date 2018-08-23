# python
# ------
# class 
# object 

# class with default constructor
# class company:
# 	nameOfCompany = "DigitalLync"
# 	address = "Kp Hyd"

# 	# method printing details
# 	# instance method --> self -->object reference storage
	
# 	# constructor 
# 		# - __init__(self) --> default constructor
# 		# - object --> constructor --> class --> creation 
# 		# - e1 --> __init__() --> company --> e1.

	# def __init__(self):
	# 	print("hello to constructor")

# 	def details(self , name): # e1
# 		# print(self)
# 		self.name = name
# 		print("your name is %s" % (self.name))
# 		print("Name of the company is %s " %(self.nameOfCompany)) # e1.nameOfCompany
# 		print("company is located at %s " %(self.address))

# e1 = company()
# e2 = company()
# e1.__init__() # explicit call to constructor can also be made 
# e3 = company()
# e4 = company()

# print(e1.address)
# print(e2.nameOfCompany) #object reference 
# print(company.nameOfCompany) # class reference

# e1.details("khan") # 2 lines
# e2.details("satish") # 2 lines
# company.details() # 2 lines 
# e4.details("ravi")


# class with parameterised constructor
# ------------------------------------class company:
class company:	
	nameOfCompany = "DigitalLync"
	address = "Kp Hyd"

	def __init__(self , name , role):
		self.name = name
		self.role = role
		# print("%s has been hired to %s role" %(self.name , self.role))
		# print("%s has been hired to %s role" %(name , role))
		# print("hello to constructor")

	def details(self): # e1
		# print(self)
		# self.name = name
		print("your name is %s" % (self.name))
		print("Name of the company is %s " %(self.nameOfCompany)) # e1.nameOfCompany
		print("company is located at %s " %(self.address))

e1 = company("khan" , "pd")
e2 = company("satish" , "d")
# e3 = company()
e1.details() #--> name role company address
e2.details()

compdetails --> count of employees , list of employees , nameOfCompany , address


e1.compdetails()
	-> 2
	-> khan satish 
	-> DigitalLync
	-> Kp hyd

e2.compdetails()
	-> 2
	-> khan satish 
	-> DigitalLync
	-> Kp hyd






