a=input("Enter elements with space seperated: ")
set1=set(a.split())
b=input("Enter elements with space seperated: ")
set2=set(b.split())
s1={}
s1=set(set1.intersection(set2))
print("Intersection is: ",s1)
s2=set()
s2=set1.union(set2)
print("Union is: ",s2)
s3=set1.difference(set2)
print("Diffference is: ",s3)
[23bee001@mepcolinux pyt]$cat 8d.py
a=input("Enter set1 elements: ")
set1=set(a.split())
b=input("Enter set2 elements: ")
set2=set(b.split())
print("Set1= ",set1)
print("Set2= ",set2)
c=set1.issubset(set2)
if (c==True):
   print("Set1 is a subset of Set2")
else:
   print("Set1 is not a subset of Set2")
d=set2.issubset(set1)
if(d==True):
   print("Set2 is a subset of Set1")
else:
   print("Set2 is not a subset of Set1")
