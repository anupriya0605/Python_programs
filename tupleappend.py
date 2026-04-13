tuple1=(10,20,30,10,20,40,30)
unique=[]
for i in tuple1:
   if i not in unique:
      unique.append(i)
t=tuple(unique)
print t
