#os module 
import os
# print(os.name)
# print(os.environ)
# print(os.getcwd())
# os.chdir('/Users/junaid/Desktop')
# print(os.getcwd())
if not os.path.exists('/Users/junaid/Desktop/dirs'):
    os.mkdir('/Users/junaid/Desktop/dis')
else:
	print("already exists")
# print(os.path.abspath('/Users/junaid/Desktop/newdir'))
# print(os.path.basename('/Users/junaid/Desktop/newdir'))
# print(os.path.dirname('/Users/junaid/Desktop'))

# os.mkdir('/Users/junaid/Desktop/newdir')
# os.rmdir('/Users/junaid/Desktop/newdir')
