# control statements
# ------------------
# pass 
# - non implemented blocks 
# - ifelse , loops , functions , classes .. ..
# break 
# - exit loop at a condition
# - loops only 
# continue
# - exit and return to loop at a condition
# - loops only
# for i in range(12):
# 	pass

# for i in range(1 ,12):
# 	# print(i) # inclusive condition
# 	if(i == 5): # -->exit
		# break
# 	print(i) # exclude condition

# a = 1
# while a<10:
# 	print(a)
# 	if a == 5 :
# 		break
# 	a +=1 # include post increment 

# while a<10:
# 	a += 1 
# 	if(a == 5):
# 		continue
# 	print(a)

# continue --> for -- ??
# do while --> XXX
# switch case --> XXX

# collections 
# -----------
# -> derived  data types 
# 	-> lists 
# 	-> tuples 
# 	-> dictionaries 

# 	-> sets 
# 	-> frozen sets 

# --> storage elements (arrays, sets , linkedlists)

# two types 
# ---------
# LIFO -->stacks --> default    
# FIFO -->queues --> collections(import)

# lists
# -----
# -> heterogeneous data types 
# -> mutable 
# -> infinite length 
# -> <class list>

# -> indexed 
# -> sliced 
# -> concatenated 
# -> nested lists
# -> iterable

# Syntax
# ------ 
# <listName> = [<element1> , <element2> , <element3> , <element4>]
# numslist = [1,2,3,4,5]
# name of list  --> numslist
# 1 ,2 ,3, 4 ,5 --> items 
# namesList = ["khan" , "ravi" , "hari" ]
# mixedlist = ["a" , 10.09 , "b" , 20 , "khan" , "python", 200]
# nest = [1,2,3,4,["a" , 10.09 , "b" ],[1,2,3,6]]
# 1 ,2 ,3 ,4 , "a"-"b" ,1-6 --> 6 items 


# accessing items of list
# -----------------------
# indexing --> 0 - n , -n to -1 

# namesList = ["khan" , "ravi" , "hari" ]
# print(namesList)
# print(type(namesList))

# <listName>[<index>]

# print(namesList[0])
# print(namesList[1])
# print(namesList[2])
# print(namesList[-2])

# slicing start and end 

# numslist = [1,2,3,4,5,"a" , 10.09 , "b" , 20 , "khan" , "python", 200]
# <listName>[<start>:<end>] --> start to end -1 
# <listName>[:<end>] --> index 0 to end -1 
# <listName>[<start>:] --> start to end 

# print(numslist[2:8]) # start = 2 end = 8 last item = 7th index
# print(numslist[:8]) # start is index 0
# print(numslist[2:]) # end is last item
# print(namesList+numslist)

# for i in range(0,8):
# 	print(numslist[i])

# for i in numslist:
# 	print(i)


nest = [1,2,3,4,["a" , 10.09 , "b" ],[1,2,3,6]]
# print(nest[4]) # ["a" , 10.09 , "b" ]
# nest[4,2] XXX
# nest[4[2]] XXX
# print(nest[4][2])
# print(nest[5][2])

# print(nest[4]) # ["a" , 10.09 , "b" ]
