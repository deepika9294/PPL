#geometric series

def nextnum (n,r):
	num = n*r
	return num
	
a = int(input(" Enter a: "))
r = int(input(" Enter r: "))
n = 10
i = 0
while i < n:
	print(a)
	a = nextnum(a,r)
	i = i+1

