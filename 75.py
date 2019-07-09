gow=list(input())
if len(gow)%2==0:
    gow[int(len(gow)/2)]='*'
    gow[int(len(gow)/2)-1]='*'
else:
    gow[int(len(gow)/2)]='*'
for i in range(len(gow)):
    print(gow[i],end='')
