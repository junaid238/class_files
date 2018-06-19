class Number:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
    	# print(self.x)
        return "%d" %(self.x)
    
    def __sub__(self , other):
        x = self.x + other.x
        # print(self.x)
        # print(other.x)
        return Number(x)

num1 = Number(5)
num2 = Number(2)
print(num1-num2)