# system arguements 
# how can we pass. cmd/terminal input ??
# using sys --> module and argv --> list 

# import sys 
# # print(sys.argv)
# print(sys.argv[0])

# print(sys.argv)
# print(sys.argv[1])
# print(sys.argv[2])
# print(int(sys.argv[1]) + int(sys.argv[2]))

# Tuples
# ------
# second --> collections 
# --> indexed
# --> sliced 
# --> iterated 
# --> immutable
# --> concat 
# --> del entire tuple 
# --> < class tuple > 
# --> default collections are all tuples 
# --> final collections --> once defined --> final 
# --> heterogeneous 

# Syntax
# ------
# start -> ( , ,  , ) <-- end 
# mutable functions --> XX tuples XX

# pi = 3.14
# epsilon = 2.71

# school --> fee --> 2yrs 
#  + 2yrs 



numsTuple = (20,40,60,100)
# print(numsTuple)
# print(type(numsTuple))

# a , b ,c = 10, 20 , 30 
# print( a , b , c)

# d = 10,20,30,
# print(d)
# print(type(d))

# e = ()
# print(e)


# accesing /indexed
# -----------------
# print(numsTuple(2)) # ()XXXX --> []
# print(numsTuple[2])
# print(numsTuple[0:2])
# numsTuple[2] = 600
# del numsTuple[3]
# del numsTuple
# print(numsTuple)
# namesTuple = "khan" , "hari" , "ravi " , "kiran"
# print(numsTuple + namesTuple)


# print(len(numsTuple))
# print(numsTuple.index(60))
# numsTuple.sort()
# print(numsTuple)
# print(numsTuple.count(60))
# numsTuple.append(100)


# ans = []
# length = int(input("enter the length of list ")) # 4
# while(length > 0 ):
# 	num = input("enter the number")
# 	ans.append(num)
# 	length -= 1 
# print(ans)

# ecluid distance 
# ---------------
# . (x,y,z,w) 		.(a,b,c,d)
# dis = sqrt(sq(x-a) + sq(y-b))

# tuple comprehensions  XXXX
# --------------------
# XXXX res = (x for x in range(2,21)) XXXX

# dictionaries

# empdict = {}
# print(empdict)
# print(type(empdict))

# empDict = {"fname" : "junaid" , "lname" : " khan" , "tech" : "py"}

# keys --> fname , lname , tech
# values --> junaid , khan ,py
# print(empDict)
# keys --> unique , immutable objects
# values --> anything

# # non unique keys
# empsDict = {"fname" : "junaid" , "fname" : " khan" , "tech" : "py"}
# print(empsDict)

# no list as a key 
# listDict = {"fname" : "junaid" , [1,2,3] : " khan" , "tech" : "py"}
# print(listDict)


# emp 		sal			mob --> keys 
# ---			----		----
# ---			----		----
# ---			----		----
# ---			----		----
# ---			----		----
# ---			----		----
# value 		value 		value

# empdetails = {"emp" : [---- , --- , ----] , "sal" :[---, ---, ----] , "mob" : [ ---,---,---]}












