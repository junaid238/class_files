# iterators and decorators 
# generators 
# ----------
# -> method 
# -> sequences
# -> inc / dec 
# -> multiple return 
# -> keyword --> yield 
# -> yield --> return multiple times 

# end 
# start --> pre defined 
# condition --> yield the output 

# def genDou(last): # 5 
# 	start = 0  # 0 
# 	while start <= last: # 5 > 0 
# 		yield start*2
# 		start += 1

# for i in genDou(5):
# 	print(i)

# reverse double 

# def revgen(last): # 5
# 	start = 0  
# 	while last > start : 
# 		yield last * 2 # 10
# 		last -= 1

# for i in revgen(5):
# 	print(i)

# polymorphism 
# ------------
# - run time / overriding
# - compile time / overloading 

# overloading --> same method name 
# 				-> multiple parameters

# 				avg(a)
# 				avg(a,b)
# 				avg(a,b,c)

# 				avg(*args)

# overriding --> same method name 
# 			--> implementation changes 
# 				--> operator overloading
# 				--> __str__() , __repr__()



class employee:
	Cname = "Lync"
	address = "Hyd"
	def __init__(self , name):
		self.name = name 

	def __str__(self):
		details = "company name is "+ employee.Cname +  " and your name is "+self.name
		return details

	def __repr__(self):
		details = " name of company is "+ employee.Cname +  " and your name is "+self.name
		return details

e1 = employee("khan")
e2 = employee("ravi")
print(e2) # printing of object calls __str__() 
print(e1) # details of object 
print("hello")






3 + 3 --> 6 
3 + 3 --> 0 

num(3) + num(3) --> 0 
num(3) - num(3) --> 6 

+ --> __add__()
- --> __sub__()







