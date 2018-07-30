# os module 
# - paths (os.path)
# - directories /folders 
# 	- dependent on OS
import os

# dir(<module>)
# list of all methods in the module
# print(dir(os))

# the name of operating system -- linux/unix/mac --> posix
# print(os.name)

# sys variables , environment variables --> c:/> python , pip , git

# python --> /usr/local/bin/python
# pip --> /usr/local/bin/pip
# returns environment variables with their paths 
# print(os.environ)

# return current working directory (pwd-->cmd)
# print(os.getcwd())
# changes directory to a existing directory
# os.chdir("/usr/local/bin/")
# print(os.getcwd())

# making directories
# ------------------
# - mkdir
# - makedirs
# os.chdir("/Users/junaid/Desktop/") 
# mkdir --> single empty directory
# os.mkdir("demoKp")
# makedirs --> multiple empty directories
# os.makedirs("pythonMe/tasks/code")

# remove directories
# --------------------
# - empty directories ONLY
# - rmdir
# - removedirs 

# remove empty single directory existing
# print(os.rmdir("/Users/junaid/Desktop/demoKp"))

# remove empty nested directories existing
# os.chdir("/Users/junaid/Desktop/")
# print(os.getcwd())
# os.removedirs("pythonMe/tasks/code")

# XXX empty XXX --> files in directories
# os --> XXX files in directories XXX
# shutil --> work on directories with files 

# os for paths (os.path)
# ----------------------
# XXX os. XXX
# os.path.<_____>
# print(os.path.abspath('/Users/junaid/Desktop/class_files/'))
# print(os.path.basename('/Users/junaid/Desktop/class_files/'))
# a = os.path.exists('/Users/junaid/Desktop/class_files') # returns T/F
# b = os.path.exists('/Users/junaid/Desktop/files') # returns T/F
# print(a) 
# print(b) 
# os.path.join(path1 , path2 )

# os.walk()
# -> input --> path 
# -> output --> three components 
# 	- path 
# 	- directories
# 	- files 

# walkAns = os.walk("/Users/junaid/Desktop/class_files")

# for paths , dirs , files in walkAns:
# # 	# print(paths)
# 	for i in dirs:
# 		if i.startswith("."):
# 			print(i)


# os.path.splitext --> path with filename , extension 
fpth , ext = os.path.splitext("/Users/junaid/Desktop/class_files/python files/arguements.py")
print(fpth)
print(ext)


# os.path.splitext --> path  , filename + extension 
pth , fext = os.path.split("/Users/junaid/Desktop/class_files/python files/arguements.py")
print(pth)
print(fext)


















