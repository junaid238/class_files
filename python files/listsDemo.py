# Lists  --> mutable 
# #-----
dia = " iam in hyd in a class in DL kP "
a = dia.split()
# print(a)

# accessing -->single --> indexing 
# accessing -->multiple --> slicing  
# re assignment 
# <listname>[<index>] = <new element>
# a[8] = "GB" # indexing change
# print(a)

# a[4:6] = "out " , "session"  # slicing change
# print(a)

# membership operators in ,not in 
# --------------------------------
# print("GB" in a)
# print("DL" in a)
# print("GB" not in a)
# print("DL" not in a)


# Functions 
# ----------
# len(<listname>) --> length of list , no of elements
# <listname>.count(<element>) --> frequency of element in listname
# <listname>.index(<element>) --> index of element in a listname

# print(len(a)) # 9
# print(a.count("DL")) # 1
# print(a.count("GB")) # 0
# print(a.index("DL")) # 7
# print(a.index("GB")) # 'GB' is not in list'

# adding an element --> append() ,  insert()
# <listname>.append(<element>) ---> lIFO , last entry 
# <listname>.insert(<index> , <element>) ---> add an element at index 

# a.append(10)
# print(a)
# a.insert(3,"1bc")
# print(a)

# removing --> pop() , del , remove()

# <listname>.pop() --> remove last element --> LIFO --> stack
# <listname>.remove(<element>) --> removes element from listname
# del <listname>[<index>] ---> delete element at index 

# del <listname> --> entire list will be deleted

# a.pop()
# print(a)

# a.pop()
# print(a)

# a.remove("hyd")
# print(a)

# del a[5]
# print(a)

l1 = [1,2,3,4,6,7,85,4,19,13,3,21,3,4,6,8,9,7,5,3,2,1,2,90]
print(len(l1))
unique = [] # all unique elements
reps = [] # all repeated in list

# in ,not in 
# for i in l1:
# 	if i not in unique:
# 		unique.append(i)
# 	else:
# 		reps.append(i)
# print(unique)
# print(reps)
print(l1)
# 1. add
# 2. remove 

# enter your option
# 1
# enter your element
# 100
# [1,2,3,4,6,7,85,4,19,13,3,21,3,4,6,8,9,7,5,3,2,1,2,90,100]

# enter your option
# 2
# enter an element from list
# 21
# [1,2,3,4,6,7,85,4,19,13,3,3,4,6,8,9,7,5,3,2,1,2,90]

# print("1. add")
# print("2. remove")
# option = int(input("enter your option"))
# if(option == 1):
# 	element = input("enter your element")
# 	l1.append(element)
# 	print(l1)
# elif(option == 2):
# 	element = int(input("enter your element"))
# 	l1.remove(element)
# 	print(l1)
# else:
# 	print("wrong input")


# enter the length of list you need
# 4
# enter the element
# 10
# enter the element
# 20
# enter the element
# 30
# enter the element
# 40

# [10,20,30,40]

# [1,2,3,4,5,6] -->input
# [1,4,9,16,25,36] --> output