gow=int(input())
lan,man=0,1
print(man,end=" ")
for i in range(1,gow):
 wan=lan+man
 print(wan,end=" ")
 lan,man=man,wan
