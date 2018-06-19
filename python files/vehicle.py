# car speed classifier
class car:
	speed = 0
	def __init__(self , name , wheels , bhp):
		self.name = name
		self.wheels = wheels
		self.bhp = bhp
		print("your " + self.name +" is of "+ self.bhp)

	def start(self , start_speed):
		# speed = 0
		car.speed = car.speed + start_speed
		print("your  " + self.name +" has started")

	def acc(self , acc_speed):
		car.speed = car.speed + acc_speed
		if car.speed > 120:
			car.speed = 120
			print("your  " + self.name +" has exceeded speed " + str(car.speed))
		else:
			print("your  " + self.name +" has  speed of " + str(car.speed))


	def brake(self , brake_speed):
		car.speed = car.speed - brake_speed
		print("your  " + self.name +" has reduced to a speed of" + str(car.speed))

	def stop(self):
		car.speed = 0
		print("your  " + self.name +" has stopped")

v = car("verna " , 4 , "2 bhp")
v.start(30) # 30
print(v.speed)
v.acc(90) # 120
v.acc(30) # 150 --> 120 
v.brake(50) # 70
c = car("city" , 4 , "3 bhp")
v.stop() # 0
print(v.speed) # 0
c.start(40)
v.start(50)
c.acc(40)
v.brake(20)
v.start(40)




# if car.speed == 0 :
# 	car.start()

# if car.speed !=0 :
# 	car.stop()
