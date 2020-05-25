#first 10 pairs of amicable numbers

def Sum(x):
	sum = 0
	for i in range(1,x):
		if x % i == 0:
			sum = sum + i
	return sum
	
def isAmicable(a,b):
	if Sum(a) == b and Sum(b) == a:
		return 1
	else: 
		return 0
		
count = 0
while count < 10:
	for x in range(1, 67000):
		for y in range(x, 67000):
			if isAmicable(x,y) and x != y:
				count += 1
				print("%d, %d " %(x, y))
				
