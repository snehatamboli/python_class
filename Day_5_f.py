st = 'python programming is the best language'
for i in range (len(st)):
     end_value ='-'

     if st[i] == ' ' or i == len(st)-1 or st[i+1] == ' ':
         end_value = ''

     if i%2 ==0:
  	   print(st[i].upper(),end=end_value)
     else:
  	    print(st[i],end=end_value)
 



