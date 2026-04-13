tup=('6','anu','10','murugan')
n=raw_input("Enter value to check: ")
for i in tup:
   if(i==n):
      print "Element exist"
      break
else:
   print "Element not exist"
