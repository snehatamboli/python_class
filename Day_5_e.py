t = int(input("Enter the number of terms = "))
sum=0
for i in range(1,t+1):
	k='2'*i
	k=int(k)
	sum=sum+k
	i+=1 
	print("The sum of series is =",sum)

