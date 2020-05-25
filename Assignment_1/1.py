bank1 = set(["Grass", "Goat", "Tiger"])
bank2 = set([])
flag = 1 			#flag = 1 for bank1 
d1 = set(["Grass", "Goat"])
d2 = set(["Goat", "Tiger"])
#i = 0
while len(bank1) != 0 :
	if flag == 1 :
		x = bank1.pop()
		if bank1 == d1 or bank1 == d2 :
			bank1.add(x)
			#print("x : ", x)
			flag = 1
		else :
			print("Man takes ", x, "from bank1 to bank2.")
			bank2.add(x)
			flag = 2
	else :
		if bank2 != d1 and bank2 != d2 :
			flag = 1
			print("Man returns alone")
		else :
			x = bank2.pop()
			bank1.add(x)
			flag = 1
			print("Man takes ", x, "from bank2 to bank1.")
			
	
print("Bank1 : ", bank1)
print("Bank2 : ", bank2)



