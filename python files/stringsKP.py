# Strings 
# -------
# indexing 
# slicing 
# concatenation --> joining of two strings 

# string1 + string2 
# + and ,--> concatenation operator

# str1 = "Python "
# str2 = "Data Sceince"
# num  = 10

# str3 = str1 + str2
# print(str1 + str2) #concatenation of variables
# print(str1)
# print(str2)
# print(str3)
# print(str1 , num) #using , 
# print("%s %d " %(str1 , num)) # using string literals
# print(str1 + str(num)) # using type casting
# print("khan" + " Python") # concatenation of strings
# print("khan" + str1)

# Type casting 
# ------------
# conversion of one dt to other dt if allowed 

# string --> number (t&c)
# number --> string 

# int() --> string to number
# str() --> number to string

# a = 10 #int
# print(type(a)) #int 
# print(a + 1) # a+1 = 10+1 ==> 11

# a = str(a) #str
# print(type(a)) #str
# # print(a + 1)

# mobile --> 9876543210 --> string
# 3479832 ---> str()--->"3479832" #type casting

# t&c for str --> int conversion
# numStr = "nad"
# print(int(numStr))
# number = "9876"
# # print(number + 1)
# print(int(number) + 1)

# Functions on strings 
# --------------------
# tech = "i learn Python in Digital Lync and Data Science in Lync Digital"
# Case based Functions:
# 	lower() # string to lower case 
# 	upper() # string to upper case
# 	swapcase() # swap the cases of string chars
# 	capitalize() # make first letter uppercase

# len() # length of the string
# count() # return int (no of times a sub string repeats)
# replace(old , new) # replacing old with new sub string
# find() # -1 if not there to find a sub string in varible and return the index
# join() # join strings with a delimiter
# split() # split string at a delimiter

# print(tech)
# print(tech.capitalize())
# print(tech.lower())
# print(tech.upper())
# print(tech.swapcase())
# print(tech)

# print(len(tech))
# print(tech.count("i"))
# print(tech.count("Java"))

# print(tech.find("Data")) 
# print(tech[35:40])
# print(tech.find("Java")) #--> -1

# print(tech.replace("Lync" , "Era"))
# print(tech)

# print(tech.split()) # default space as delimiter
# print(tech.split("D")) # delimiter = "D"
# print(tech.split("in")) # delimiter = "in"

# split = tech.split()
# print(split)
# print("_".join(split)) # delimiter = "_"

# demo = ["Khan" , "27" , "M" , "Python"]
# print("-".join(demo)) # delimiter = "-"