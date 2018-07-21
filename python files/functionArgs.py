# # functions
# --> return type 
# 	-> one return
# 	-> if no return then o/p from call = None
# --> parameters 

# parameter ---> inputs 
# return type ---> output

# parameter --> functions --> return 

# def addn(a,b):
# 	res = a+ b
# 	print(res)
# 	return res

# def diff(c,d):
# 	res = c-d
# 	print(res)

# ans = addn(30,40) # ans = 70 
# print(ans)
# diff( ans , 10)

# def say(name):
# 	print("Hey "+ name)

# def evenOdd(num , name):
# 	if num%2 == 0 :
# 		print("even")
# 		return say(name)
# 	else:
# 		print("odd")
# 		return "odd" 

# # print(evenOdd(10)) #return "even" 
# # print(evenOdd(101)) #return "odd"
# # evenOdd(10 , "khan")
# evenOdd(11 , "khan")

# Task 
# ----
# add(20,30) #50 
# diff(<50>, 10) #40
# mul(<40> , 10) #400
# div(<400> , 10) #40 

# def b(name):
# 	print("hello " +name)

# def func(a):
# 	print(a)
# 	return b

# d = func(10)
# print(d)
# d("khan")

# parameters
# ----------
# -> positional 
# -> default 
# -> variable 
# -> keyworded

# -> positional 
# def avg(a,b,c,d):
# 	print("a" , a)
# 	print("b" , b)
# 	print("c" , c)
# 	print("d" , d)

# 	mean = (a+b+c+d)//4
# 	print(mean)

# avg(10,20,d = 30,c = 40)

# -> default 
# cake -> cakes on call 

# shape = "round" , flavour = "choc" and weight ="2kg"

# 1 -> "round" , "vannila" , 2 kg (3)
# 2 -> "rect" , "choc" , 3 kg (3)
# 3 -> flavour = "mango" , shape = "square" , 1 kg (3 shuffled)
# 4 -> "pineapple " , 5 kg (2) [round]
# 5 -> "oval" , 2 kg (2) [choc]
# 6 -> cake (0) [choc , round , 2kg]

# def cakeShop(flavour = "choc" , weight ="2kgs" , shape = "square"):
# 	print("you have ordered \
# 	 " + flavour +" cake " +weight+ " of " \
# 		  +shape+ " shape ")

# cakeShop("vanilla" ,"2kg " , "round")
# cakeShop(shape = "rect" ,weight = "2kg " , flavour = "choc")
# cakeShop("pineapple" , "3kgs")
# cakeShop()

# -> variable 
# 0 , 1 , n --> multiple parameters -->variable params --> tuples
# avg -> 0
# avg -> 1
# avg -> n

# formal parameters --> *args , *vars , *abcd . . . .
# actual parameters --> values are passed 
# args , vars , abcd --> tuples
# variable parameters ==> not positional


# def meanN(a , b , *args):
# 	ans = 0 
# 	for i in args:
# 		ans += i
# 	l = len(args)
# 	if l == 0:
# 		l = 1
# 	ans = ans//l
# 	return ans

# print(meanN(10,20,30,40))
# print(meanN(30,40))
# print(meanN(40)) # not work
# print(meanN()) # not work









