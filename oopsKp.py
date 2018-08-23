# OOPS 
# -> inheritance
# 	-- acquiring all properties from one class to other class 
# 		- one class --> parent / super
# 		- other class --> child / sub 
# 	-- compulsory till 2.7 --> object class 

# syntax:
# -------
# parent : as usual 

# child --> acquire
# single 
# ------
# class childName(<parentName 12>):
# 	< properties of parentName class  10 >
# 	< properties of childName class 10 > --> 20

# multiple 
# --------
# class childName(<parentName1 12>,<parentName2 12>):
# 	< properties of parentName1 class 12>
# 	< properties of parentName2 class 12>
# 	< properties of childName class 10> --> 34

# multilevel 
# ----------
# class childNameNew(<childName 20>):
# 	< properties of childName class 20>
# 	< properties of childNameNew class 10> --> 30 

# vehicle(super) --> car , bike , truck (child)
# employee(super) --> developer , manager , lead (child)

class vehicle():
	name = ""
	noOfWheels = 0
	speed = 0 
	# __init__  --> welcome
	def start(self,startSpeed):
		print("your "+self.name + " has started")
		self.speed = startSpeed
		print("current speed %d" %(self.speed))
	def acc(self,accSpeed):
		print("your "+self.name + " has accelarated")
		self.speed = self.speed + accSpeed
		print("current speed %d" %(self.speed))
	def brake(self,brakeSpeed):
		print("your "+self.name + " has reduced the speed ")
		self.speed = self.speed - brakeSpeed
		print("current speed %d" %(self.speed))
	def rev(self,revSpeed):
		print("your "+self.name + " has reversed ")
		print("current speed %d" %(self.speed))	
	def stop(self,stopSpeed):
		print("your "+self.name + " has been stopped ")
		self.speed = 0
		print("current speed %d" %(self.speed))

# v = vehicle()
# v.name = "my vehicle"
# print(v.name)
# v.start(20)
# v.acc(60)
# m = vehicle()
# m.name = "her vehicle"
# print(m.name)
# m.start(10)
# m.acc(40)
# print(v.speed)

class bike(vehicle):
	print("its my bike ")
	# __init__ thank you
	noOfWheels = 2

b = bike() # bike and vehicle
b.name = "abc"
b.start(30)
b.noOfWheels = 3
b.acc(90)
b.brake(70)
b.brake(30)
b.brake(30)















