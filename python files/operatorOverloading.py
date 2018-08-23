class Number:
    def __init__(self, x): # initialising a Number
        self.x = x
    def __str__(self):
    	# print(self.x)
        return "%d" %(self.x)
    def __sub__(self , other):
        x = self.x + other.x
        # print(self.x)
        # print(other.x)
        return Number(x )
    def __add__(self , other):
        x = self.x - other.x
        # print(self.x)
        # print(other.x)
        return Number(x)

n1 = Number(10)
# print(n1)
n2 = Number(100)
# print(n2)
print(n1 + n2) # __add__()
print(n1 - n2) # __sub__()


# num1 = Number(5)
# num2 = Number(2)
# print(num1-num2)
# print(num1+num2)