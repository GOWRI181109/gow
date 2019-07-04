gw=input()
count=0
for s in range(len(gw)):
 if(gw[s].isdigit() or gw[s].isalpha() or gw[s]==(" ")):
  continue
 else:
  count+=1
print(count)
