# finding missing page numbers
def listCheck(x,list1):
	list1 = set(list1) 
	if x in list1 :  
		return 1
	else:
		return 0

n=int(input("Enter number of pages of book = "))
print("Enter page number of that book which is there= ")	
list1= list(map(int, input().split()))

for page in range(1,n+1):
	if listCheck(page,list1)!=1:
		print(page)
	
