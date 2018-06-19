# class Org():
# 	# class vars
# 	org_name  = "Digital Lync"
# 	emp_count = 20
# 	# custom constructor
# 	def __init__(self ):
# 		print("hello " )

# e1 = Org() # implicitly calls __init__
# e1.__init__()
# print(e1.org_name)

# class company():
	# class vars
	# org_name  = "Digital Lync"
	# emp_count = 20
	# parameterised constructor
	# def __init__(self , name , age ):
	# 	company.emp_count = company.emp_count + 1
	# 	print("hello " + name + " " + str(age) + "empid. is " + str(company.emp_count))
	# instance method --> self
	# def add(self , a , b):
	# 	self.a = a
	# 	self.b = b
	# 	self.sum = self.a + self.b
	# 	print(self.sum)

# 	@classmethod
# 	def change_name(cls , newname):
# 		cls.newname = newname
# 		cls.org_name = cls.newname
# 		print(cls.org_name)

# 	@staticmethod
# 	def calc(salary , perc):
# 		ans = salary +(salary * perc)
# 		print(ans)

# e2 = company("khan" , 27)
# e3 = company("Ravi" , 28)
# print(company.emp_count)

# self --> e2
# e2.add(20,30) # instance method call
# print(e2.org_name)
# company.change_name("newDigitalLync")
# print(e2.org_name)
# print(company.org_name)
# e2.calc(48797 , 0.05)
# print(e2.ans)

# a = 10
# def add( c , b ):

# 	global a 
# 	sum= a+b 
# 	print(a)
# 	print(c)
# 	print(sum )
# add(13,19)

		