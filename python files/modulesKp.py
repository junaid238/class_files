# Modules and packages 
# --------------------
# module
# 	-> a python file 
# 	-> .py .pyc .ipynb
# 	-> imported and reused in other modules
# 	-> all components 
# Types
# -----
# internal
# 	- auto imported --> print()
# 	- import 
# 		--> libs 
# 		--> not auto imported in file 
# external 
# print() --> XX download XX XX import XXX
# reduce() --> XX download XX imported 
# numpy , pandas , sns , PIL --> download and imported

# syntax
# ------
# import <moduleName>
#  --> all components get imported
#  --> pycache is generated 
#  --> <moduleName>.<component>

# from <moduleName> import <component>
#  --> only a component is imported
#  --> <component>

# from <moduleName> import * ---> ???

# aliasing
# --------
# import <moduleName> as <somealias>
# <somealias>.<component>

# import check.py XXX
# import check
# print(check.l1)
# print(check.t1)

# from check import l1,t1
# print(l1)
# print(t1)

# from check import * 
# print(l1)
# print(t1)

# import check as c 
# print(c.l1)
# print(c.t1)
# print(check.l1)

# package
# -------
# --> folder / directory
# --> collection of python files / modules

# XX demo --> 1.py , 2.py , 3.py XX 
# demo folder + __init__.py = demo package
# __init__.py --> empty file 

# from <packageName> import <moduleName>
# --> all components 
# <moduleName>.<component>

# import <packageName>.<moduleName>.<component>
# --> only one component
# <component>

# from <packageName>.<moduleName> import <component>

# External packages
# -----------------
# --> downloaded and imported
# --> package manager 
# --> pip --> python packaging index 
# --> conda 

# pip - 10.0.1
# ----
# --> win --> auto installed 
# 	--> get-pip.py file 
# 	--> copy contents , save and run 
# --> pyhton36/site-packages 
# 			--> downloaded packages

# --> pip install < package name>
# --> pip uninstall < package name>
# --> pip freeze --> get list of packages installed
# --> pip list --> get list of packages installed

# import numpy
# print(dir(numpy) )
# import six
# print(dir(six) )

# --> os , random , math 
# --> numpy , pandas , csv 
