# l1 = [x for x in range(10)]
# print(l1) # call
# print(len(l1)) # Returntype
# # l1 --> parameter 
# len(l1) --> call


# def greet():# definition
# 	print("hello ") # implementation


# greet()
# greet()
# greet() # calls
# greet()
# greet()
# greet()


def say_hello(name ):#formal
	print( " hello " + name )

# say_hello("khan" )#actual param
# say_hello("Hari")
# say_hello("Ravi")
# say_hello("Ram")
# say_hello("Rajesh")

#default args 
# def makeCake(flav = "Vanilla" , wei  = "1kg" , shape ="rectangle" ):
# 	print( flav + "   " + wei + "   " +shape)

# makeCake("vanilla " , "3kgs" , "round")
# makeCake("chocolate" , "4kgs")
# makeCake(flav = "chocolate" , shape = "Square")


# def add(a , b):
# 	sum = a+b 
# 	print(sum)


# def add(a , b , c):
# 	sum = a+b+c 
# 	print(sum)
# add(3,4 , 8)
# add(3,4)


# variable args 
# def add_nums(*args):
# 	print(args) #tuple
# 	sum = 0 
# 	for j in args:
# 		sum = sum +j
# 	print(sum)

# add_nums(90)
# add_nums(90,45)
# add_nums(90,23,34)
# add_nums(90,23,4,6,8,9)


#keyworded args 
# def makeCka(flav = "vanila" , wei = "1kg" , shape = " round",  **kwargs):
# 	print(flav +wei+shape)
# 	print(kwargs) # dictionary 
# 	for j in kwargs.values():
# 		print(flav +wei+shape+j)
# makeCka(flav ="pine" , wei= "4kg" , shape="rect")
# makeCka(flav ="pine" , wei= "4kg" , shape="rect" , topping = "dryfruits" , types = "coolcake")












