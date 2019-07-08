rgv1,rgv2=map(int,input().split())
mrk=list(map(int,input().split()))
for i in mrk:
 if(i==rgv2):
  print("yes")
  break
else:
 print("no")
