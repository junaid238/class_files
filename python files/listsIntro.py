# # # lists 
# # --> heterogenous collections 
# # --> Mutable 
# # --> 1XN order 
# # --> indexed , sliced and concat
# # --> nested lists are possible 
# # --> MxN XXX
# # --> infinite length 


# # syntax 
# # ------
# # <listname> = [<item1> , <item2>]
# # type(<listname>) --> < class list >

nums = [1,2,3,4,55,6]
# print(type(nums))
# print(nums)
# # indexing
# # print(nums[1])
# # print(nums[3])
# # slicing 
# # print(nums[0:3])
# # print(nums[2:5])

# # modifing an element in list ( indexing )
# nums[4] = 100
# print(nums)
# nums[0] = 11
# print(nums)

# # modifing an element in list ( slicing )
# # start = 0 end = 3
# nums[0:3] = ["khan" , "hari" , "ravi"]
# print(nums)
# # start. = ?? end = 5
# nums[:5] = [10 , 20 ,30 ,40 , 58]
# print(nums)
# # start. = 3 end = ??
# nums[3:] = [100, 200, 300]
# print(nums)

# # reversing a list 
# # print(nums[::-1])

# # deleting an element

# # del <listname>[<index>]
# del nums[4]
# print(nums)

# deleting a complete list
# del nums 
# print(nums)

# listInlist = [["khan" , 27 , "Py"] , ["hari" , 25 , "Js"] , ["Ravi" , 28 , "De"]]
# print(listInlist)
# print(listInlist[0])
# print(listInlist[1])
# print(listInlist[2])
# print()
# print(listInlist[2][0])
# print(listInlist[2][1])
# print(listInlist[2][2])

# nested = [[[[[[[[[1]]]]]]]]]
# print(nested)
# # print(nested[0])
# print(nested[0][0])
# # print(nested[0][0][0][0][0][0][0][0][0])
# nested[0][0] = 2
# print(nested )

# # iterate over a list 
# for i in nums:
# 	print(i)

# # indexing + iterating
# for i in range(0,5):
# 	print(nums[i])

task 1
----
if else , in not in , str() int() , split()
time = 03:45:30AM
output --> 03:45:30

time = 03:45:30PM
output --> 15:45:30

time = 12:00:00AM
output --> 00:00:00

task2
-----
3 ---> zfill() str()
num sqnum cunum 
03  09  27
04	 16  64

3 --> 9 ---> 27
4 --> 16 ---> 64 
5 --> 25 ---> 125 
.
.
10 --> 100 --> 1000


list functions and list comprehensions 




