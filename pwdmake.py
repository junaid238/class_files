import random as r 
usersdict = {}
def chkuser(name):
	if name in usersdict.keys():
		print("User already exists")
		return 0
	else:
		return 1

def makeNums(n):
	numpwd = ""
	for i in range(0 , n):
		numpwd = numpwd + str(r.randint(0,9))
	# print(numpwd)
	return numpwd
def makeChrs(n):
	chrpwd = ''
	l1 = []
	for i in range(0 , n):
		a = chr(r.randint(65 , 90))
		b = chr(r.randint(97 , 122))
		l1.append(a)
		l1.append(b)
		r.shuffle(l1)
	ans = r.sample(l1 , k = n)
	for i in ans:
		chrpwd = chrpwd +i
	# print(chrpwd)
	return chrpwd

def genpwd(name):
	if chkuser(name) == 1:
		password = makeChrs(4)+ makeNums(4)+makeChrs(4)+makeNums(4)
		usersdict[name] = password
		print(password)
		return password
	
genpwd("khan")
genpwd("Hari")
genpwd("khan")

