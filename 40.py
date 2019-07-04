start=int(input())
nmg1,nmg2=0,1
print(nmg2,end=" ")
for i in range(1,start):
  res1=nmg1+nmg2
  print(res1,end=" ")
  nmg1,nmg2=nmg2,res1
