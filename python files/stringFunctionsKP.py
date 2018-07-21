# functions 
# attribute fetching 
# parameterised 

# case
# .lower()
# .upper()
# .swapcase()
# .capitalize()
# .title()

para = "python is a Easy Language "
# print(para.capitalize())
# print(para.lower())
# print(para.upper())
# print(para.title())
# print(para.swapcase())

# print(para)
# ckecking 
# .startswith()
# .endswith()
# print(para.startswith("p"))
# print(para.startswith("pyt"))
# print(para.startswith("z"))

# print(para.endswith("ge "))
# print(para.endswith("e "))
# print(para.endswith("z"))

# operational

# print(len(para))
# print(para.index("h"))
# print(para.index("th"))
# print(para.index("a" , 11 , 20))
# print(para.index("j"))

# print(para.find("h"))
# print(para.find("th"))
# print(para.find("a" , 11 , 20))
# print(para.find("j"))

dia = "    iam in a class in hyd in KPHB    "
# print(dia.replace("in" , "out"))
# print(dia.replace("in" , "out" , 2))
# print(dia)

# print(dia.count("Z"))
# print(dia.count("in"))
# print(dia.count("i"))

# a = 10
# print(str(a).zfill(10))
# print(dia)
# print(dia.strip())
# print(dia.strip(" iam"))
# print(dia.strip("iam"))
# print(dia.lstrip())
# print(dia.rstrip())

# split and join 

# syntax
# ------
# spilt --> " " --> string is cut at " "
# " " --> delimiter 

# print(dia.split()) # delimiter =" "
# print(dia.split("i")) # delimiter = "i" char
# dummy = dia.split("in")
# print(dia.split("z"))
# print(dummy)

# join 
# <delimiter>.join(collection)
# print("in".join(dummy))
# print("- ".join(dummy))
# print("".join(dummy))
