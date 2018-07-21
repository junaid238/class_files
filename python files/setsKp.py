# sets and frozensets 
# sets
# ---> storage components
# ---> unique elements
# ---> { }
# ---> set([])
# ---> < class set > 
# ---> XXX indexed /sliced XXX
# ---> iterations 
# ---> concat 
# ---> pre defined functions 
# ---> mutable 
# ---> maths functions ( corrsponding to maths sets )
# Syntax
# ------
# numsSet = {1,2,3,4,5}
# secondSet = set([1,2,3,4,5])
# print(numsSet)
# print(secondSet)
# print(type(secondSet))

#empty set 
# empSet = {}
# print(empSet)
# print(type(empSet)) # dictionary 

# # declare empty set using set()
# empSetReal = set([])
# print(type(empSetReal))

# XXX indexing is not possible 
# print(numsSet[2])
# XXX slicing is not possible
# print(numsSet[0:3])
# iterations are possible
# for i in numsSet:
# 	print(i)

# modifications (Functions)
# print(len(numsSet)) # length / count of elements
# <setName>.add(<element>) # adding an element in LIFO 
# numsSet.add(100)
# print(numsSet)
# <setName>.remove(<element>) # removing an existing element in LIFO 
# numsSet.remove(4)
# print(numsSet)
# error if element is unavailable
# numsSet.remove(200)
# <setName>.discard(<element>) # removing an element in LIFO 
# numsSet.discard(2)
# print(numsSet)
# no error if element is unavailable
# numsSet.discard(200)
# print(numsSet)

# deletion of element is not possible ,
# entire set can be deleted
# del numsSet
# print(numsSet)
# doesnt add an existing element to set
# numsSet.add(100)
# print(numsSet)

# repSet = {1,2,3,4,6,7,10,3,1,2,3,4,5}
# print(repSet)

# chars set 
# chrset = {"a" , "b" , "c" , "a"}
# print(chrset)

# copying set to other 
# copied = numsSet.copy()
# print(copied)

# clear all elements from the set
# numsSet.clear()
# print(numsSet)

# Maths Functions in sets 
# -----------------------
# union ( all elements from 2 sets )
# intersection ( all common elements from 2 sets )
# difference ( only elements of first set )
# issubset ( check if first is inner/sub part of second )
# issuperset ( check if first is outer/super part of second )

# setA = {10,20,30,40,"a" , "akhil" , "rajesh"}
# setB = {30,"rajesh" , 40 , "b" , 70 }

# allelements = {10,20,30,40,"a" , "akhil" , "rajesh","b" , 70 }
# common = {30,"rajesh" , 40}
# onlya = {10,20,"a","akhil"}
# onlyb = {"b" , 70}

# <setName1>.union(<setName2>)
# allelements = setA.union(setB)
# print(allelements)

# # <setName1>.intersection(<setName2>)
# common = setA.intersection(setB)
# print(common)

# # <setName1>.difference(<setName2>)
# onlya = setA.difference(setB)
# print(onlya)
# # <setName2>.difference(<setName1>)
# onlyb = setB.difference(setA)
# print(onlyb)

# # <setName1>.issuperset(<setName2>)
# superstatus = setA.issuperset(setB)
# print(superstatus)

# # <setName1>.issubset(<setName2>)
# substatus = setA.issubset(setB)
# print(substatus)

# maths functions --- operators 
# -----------------------------
# union        ---> |
# intersection ---> &
# difference   ---> -
# issuperset   ---> >
# issubset 	 ---> <

# # union using |
# print(setA | setB)
# # intersection using &
# print(setA & setB)
# # difference setA using -
# print(setA - setB)
# # difference setB using -
# print(setB - setA)
# # issubset  using <
# print(setB < setA)
# # issuperset  using >
# print(setB > setA)

# frozen sets 
# --> sets without mutations 
# --> immutable 
# --> XXX modification XXX
# --> < class frozenset >
# --> delete an entire frozenset
# --> tuple of sets 

# Syntax
# # ------
# empFro = frozenset([])
# print(empFro)
# print(type(empFro))

# chrFro = frozenset(["a" , "b" , "c"])
# print(chrFro)

# del chrFro
# print(len(chrFro))
# frozenset.add(100)













