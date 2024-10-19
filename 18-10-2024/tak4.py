#	Write a python programe to check if the two list are having atleast one common element?
	
l = [1,2,3,4,5,6,7,8,9]
l1 = [1,4,5,7,8,24,6]
result = set(l).intersection(set(l1))
print(list(result))