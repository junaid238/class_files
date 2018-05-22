# Strings
# -------
# index 
# slicing 
# concat 

# functions on strings
# --------------------
# case based functions
# 	capitalize --> python --> python
# 	lowercase 
# 	uppercase
#   swapcase

# count
# len
# replace
# strip
# join 
# split
# zfill
# find

tech = "python and Data Sceinces is a good thing to learn in 2018 and is popular"
# print(len(tech))
# print(tech.capitalize())
# print(tech.swapcase())
# print(tech.lower())
# print(tech.upper())


# count() --> substring
# int --> return

# print(tech.count("ng to lear"))
# print(tech.count("is"))
# print(tech.count("Sceinces"))
# print(tech.count("Java"))

# replace -->old substring to new one 
# no change in string
# print(tech)

# technew = tech.replace("popular" , "trending")
# print(technew)
# print(tech)

# find --> substring -> existence and index 

# print(tech.find("learn")) # at 44 index of tech
# print(tech.find("java"))# does not exist in tech

# join and spilt ---> delimiter --> spliting and joining the strings 

# print(tech.split()) #default delimiter is space
# print(tech.split("i")) #delimiter = "i"
# print(tech.split("a")) #delimiter = "a"

# splitStr = ["khan" , "27" , "M" , "Python" , "DS"]
# joinedStr= " ".join(splitStr)
# print(joinedStr)
# print(splitStr)
# print(joinedStr.count("_"))

# name = str(100)
# print(name.zfill(10))
# print(name.zfill(20))#fill zeroes from left


