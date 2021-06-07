list1 = [10,21,4,45,66,93,1]
even_no,odd_no = 0,0

for num in list1:
	if num % 2 == 0:
		even_no += 1

	else:
		odd_no +=1
print("Even Numbers in the list : ",even_no)
print("Odd Numbers in the list : ",odd_no)

