# Python program to print positive Numbers in a List

# list of numbers
list1 = [12, -7, 5, 64, -14]
num = 0

while(num < len(list1)):
	
	# checking condition
	if list1[num] >= 0:
		print(list1[num], end = " ")
	
	# increment num
	num += 1

#list2
list2 = [12, 14, -95, 3]
num1 = 0

while(num1 < len(list2)):
	
	# checking condition
	if list2[num1] >= 0:
		print(list2[num1], end = " ")
	
	# increment num
	num1 += 1