gw=input()
count=0
for y in range(len(gw)):
 if(gw[y].isdigit() or gw[y].isalpha() or gw[y]==(" ")):
  continue
 else:
  count+=1
print(count)
