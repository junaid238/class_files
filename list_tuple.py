l=[1,6,7,3,[19,20],2,8,(80,90)]
output=[]
for i in l:
	if(type(i) is list or type(i) is tuple):
		for j in i:
			output.append(j)
	else:
		output.append(i)
print(output)
