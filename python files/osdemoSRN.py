# OS MODULE 
# --------
# directories -- os dependent 
# os module -- mandatory 
import os 
# print(dir(os))
# print(os.name)
# print(os.environ)

# os.mkdir()# making a single directory 
# os.makedirs()# making a tree / parentchild directories

# os.rmdir() # remove a single directory EMPTY
# os.removedirs() # remove a parentchild directories EMPTY

# os.getcwd() # current directory 
# os.chdir() # change current directory
# print(os.getcwd()) # class_files
# os.chdir('/Users/junaid/Desktop') # redirects to Desktop
# print(os.getcwd()) # return Desktop

# os.mkdir("khandemo") #create khandemo directory
# os.makedirs("khan/demo/class/codes") # multiple inner directories

# os.rmdir('khandemo')
# os.removedirs('khan/demo/class/codes')

# removedirs with files SHUTIL


# os with paths
# -------------
# os.path._____
# print(os.path.abspath('/Users/junaid/Desktop/class_files/'))
# print(os.path.basename('/Users/junaid/Desktop/class_files'))
# os.path.exists('path') # returns T/F 
# os.path.join(path1 , path2 )
# os.walk()



# for paths , dirs ,files in os.walk('/Users/junaid/Desktop/newdir'):
# 	# print(paths)
# 	for i in paths:
# 		print(i , end = "")
# 	for i in dirs:
# 		print(i)
# 	for i in files:
# 		print(i)
	# print(dirs)
	# print(files)







file , ext = os.path.splitext('/Users/junaid/Desktop/class_files/osdemoSRN.py')
print(file)
print(ext)


file , ext = os.path.split('/Users/junaid/Desktop/class_files/osdemoSRN.py')
print(file)
print(ext)








