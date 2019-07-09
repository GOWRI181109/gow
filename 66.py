rgv=int(input())
for v in range(2,rgv):
    if rgv%v==0:
        print("no")
        break
else:
    print("yes")
