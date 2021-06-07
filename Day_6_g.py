print(" all the numbers which are the pallindrome inside the list")

li = [55,36,363,454,500,77]
for i in li:
	n = str(i)
	if n==n[::-1]:
		print(i, end = " ")
