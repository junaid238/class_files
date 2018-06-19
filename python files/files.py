# # files demo code 

# # f_obj = open('srndemo.txt' , 'w')
# # f_obj.write("hello\n")
# # f_obj.close()


# # multi line writing
# # l1 = ["khan\n" , "hari\n" , "ram\n"]
# # with open('srndemo.txt' , "a") as fo:
# # 	fo.write("hey second \n input on file\n ") # appending 
# # 	fo.writelines(l1) # multi line writing

# # # reading the files 
# # read()
# # full file read , entire file 
# # f_obj = open('srndemo.txt' , 'r')
# # a = f_obj.read()
# # read with param
# # b = f_obj.read(5)
# # print(a)
# # print(b)

# # readline()
# # one line at a time
# # from start to \n 
# # e = f_obj.read()
# # print("full " +e)
# # c = f_obj.readline() # first line
# # print( c)
# # d = f_obj.readline() # next line from cursor currnet position 
# # print(d)
# # e = f_obj.read()
# # print(e)
# # readline with a param
# # m = f_obj.readline(3)
# # print(m)
# # readlines()
# # list of all new line endings
# # list of all lines 
# # example : ['hello\n', 'hey second \n', ' input on file\n', ' khan\n', 'hari\n', 'ram\n']
# # n = f_obj.readlines()
# # print(n)
# # readlines with param
# # p = f_obj.readlines(18)
# # print(p)

# # h = f_obj.read(12)
# # print(f_obj.tell())
# # o = f_obj.readline()
# # print(o)
# # print(f_obj.tell())
# # o = f_obj.readline()
# # print(o)
# # print(f_obj.tell())
# # current position of cursor 
# # .tell() --> int of position 

# # to relocate cursor 
# # seek() --> reloacte position of cursor 
# # params  --> offset , whence 
# # f_obj.seek(____ , _____) --> ???

# # f_obj.close()

# import sys,os

# def chklastnum():
# 	with open("srndemo.txt" , 'rb') as fc:
# 		a = fc.seek(-2, 2)
# 		# b = fc.seek(2, 1)
# 		# print(b)
# 		print(a)
# 		return fc.read(1)

# def genNums(num = int(sys.argv[1]) , start = chklastnum() ):
# 	nums = ''
# 	print(start)
# 	for i in range(int(start)+1,int(start)+num):
# 		nums = nums + str(i)
# 	print(nums)
# 	return nums
# genNums()

# def writFile(inp = genNums()):
# 	with open("srndemo.txt" , 'a') as fo:
# 		fo.write(inp + "\n")
# writFile()

# # def chklastnum():
# # 	with open("srndemo.txt" , 'rb') as fc:
# # 		a = fc.seek(-2, 2)
# # 		b = fc.seek(2, 1)
# # 		print(b)
# # 		print(a)
# # 		return fc.read(1)
# # chklastnum()












