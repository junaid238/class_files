# # methods with same name 

# def add(a,b,c,d):
# 	sum = a+b+c+d
# 	print(sum)
# def add(a,b):
# 	sum = a+b
# 	print(sum)

# add(2,3)
# add(2,3 , 4 ,5 )


# # add(2,3 , 4 ,5 )
# # add(2,3)


# Default parameters
# python scripting 
# server -- tool -> on /off
# cake - flav   wei    shape 
# first - strw	3	round
# second- chco	2	rect
# third - vani	-	round. ---> 2
# fourth-  -      1		-  ----> vani sqaure
# fifth -      cake. 			---> vani 2 sqaure
# defaults --> flav = "vani" wei = 2 shape = "sqaure"
# values are directly given in the definition 
# def makecake(flav="vani" , wei = 2 , shape ="sqaure" ):
# 	print("you have ordered " + flav +"flavored cake of ", wei , " kgs of "+shape  +" shape")
# makecake("vanni " , 3 , "round")
# makecake("choc " , 3 , "round")
# makecake("pine" , 4)
# makecake()
# makecake(flav= "strw" ,shape =  "rect")


#. variable args 
# metod overloading XXXX--> var args 
# def add(a , b ,*args):

# 	print(args , " from args ") # variable 
# 	print(a , " from a ") # positional 
# 	print(b , " from b ") # positional
# 	sum = a+b
# 	for i in args:
# 		sum = sum +i
# 	print (sum)
# # add() #--> should error
# # add(1)#--> should error
# add(1,2)
# add(1,3,5)

# average of nums

# def avg(a , b ,*vars):
# 	sum = a+b 
# 	print(type(vars))
# 	for i in vars:
# 		sum = sum +i
# 	mean = sum / (len(vars)+2)
# 	return mean
# print(avg(20 , 30))
# print(avg(20 ,60, 30))
# print(avg(20 ,60, 50 ,30))
# avg()

# keyworded params 
# extension to defaults 
# def makecake(flav="vani" , wei = 2 , shape ="sqaure"   , **kwargs):
# 	print(kwargs)
# 	print("you have ordered " + flav +"flavored cake of ", wei , " kgs of "+shape  +" shape")
# makecake("vanni " , 3 , "round")
# makecake()
# makecake(flav= "strw" ,shape =  "rect" , toppings = "lava")


#doc string -- meta data of a function 
# print(makecake.__doc__)

# def dummy():
# 	'''this is a dummy method '''# doc string
# 	print("hi")
# print(dummy.__doc__)

# #output
# 1 - arith
# 2 - logical 
# 3 - bitwise 
# enter an option 1
# 1 - add
# 2 - sub
# 3 - mul 
# 4 - div
# enter an option 2
# enter a number 10
# enter a number 5
# diff = 5


# def calc():
# 	''' 1 - Arith 
# 	2 - logical
# 	3 - bitwise '''
# 	print(calc.__doc__)
# 	cat = int(input("Enter the Category"))
# 	if(cat == 1):
# 		arith()
# 	elif(cat == 2):
# 		logical()
# 	elif(cat == 3):
# 		bitwise()
# 	else:
# 		print("wrong input")
# 		calc()
# def arith():
# 	''' 1 - sum 
# 	2 - sub
# 	3 - mul 
# 	4 - div'''
# 	print(arith.__doc__)
# 	ope = int(input("Enter the Operation"))
# 	if(ope == 1):
# 		add()
# 	elif(ope == 2):
# 		sub()
# 	elif(ope == 3):
# 		mul()
# 	elif(ope == 4):
# 		div()
# 	else:
# 		print("wrong input")
# def add():
# 	a = int(input("enter a number"))
# 	b = int(input("enter a number"))
# 	print(a+b)
# def sub():
# 	a = int(input("enter a number"))
# 	b = int(input("enter a number"))
# 	print(a-b)
# def mul():
# 	a = int(input("enter a number"))
# 	b = int(input("enter a number"))
# 	print(a*b)
# def div():
# 	a = int(input("enter a number"))
# 	b = int(input("enter a number"))
# 	if(b==0):
# 		print("error")
# 	else:
# 		print(a//b)

# calc()



