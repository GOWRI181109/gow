rgv=int(input())
mrk=0
i=0
while(rgv>0):
    i=rgv%10
    mrk=mrk+i
    rgv=rgv//10
print(mrk)
