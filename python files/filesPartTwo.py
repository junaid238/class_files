# files 
# open() --> create and open / just open --> file path , mode 
# operated --> read write (auto save) --> file object
# close() --> file object
# file object --> open() / with open()

# "w" --> one time opening 

# created and opened a demo.txt file
# fobj = open("demo.txt" , "a")
# write --> write() , writelines() --> w , a , r+ , rb+ --> string
# <fileObject>.write(<content>)
# fobj.write("hello") # wriiten hello to demo.txt
# fobj.write("hello\n") # wriiten hello twice to demo.txt
# fobj.write("bye")
# # write multiple lines 
# fobj.write("dfghj\n dfghj\n fdghjj\n sfdcvfgty\n")
# l1 = ["1,2,3,4,5,6,6\n" , "abc\n" , "third\n"]
# fobj.writelines(l1)

# read from a file
# read()
# readline()
# readlines()
# read() --> entire content from file 
# a = fobj.read()
# print(a)

# fobj.close() # closed fobj


# # "w" --> file empty
# fobj = open("demo.txt" , "r")
# # fobj.write("hey")
# a = fobj.read(14)
# print(a)
# fobj.close()


# read()
#  --> entire content
#  read(<count>) --> count number of chars 
# readline()
#  --> first line of cursor
#  

# with open("demo.txt" , "r") as fc:
# 	print(fc.readline()) # first line
# 	print(fc.tell())
# 	print(fc.readline()) # second line
# 	print(fc.tell())
# 	print(fc.readline()) # third line
# 	print(fc.tell())
# 	# print(fc.read()) # entire content from 4th line 
# 	print(fc.readline(3)) 

# readline() ---> first line from cursor
# readline(<charcount>) ---> first charcount chars from cursor

# with open("demo.txt" , "r") as fc:
# 	print(fc.readlines())
# 	print(fc.readlines(18))

# tell() --> to get cursor location
# seek() --> move cursor to a location
# seek --> from start , end , current position 




