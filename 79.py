gow1,gow2=map(int,input().split())
p3=gow1*gow2
for i in range(0,p3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
