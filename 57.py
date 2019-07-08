rgv,rgv2=map(int,input().split())
mrk=list(map(int,input().split()[:rgv]))
rk=0
for i in mrk:
   if(i==rgv2):
      rk=rk+1
print(rk)
