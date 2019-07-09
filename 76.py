gow=int(input())
for i in range(2,gow):
    if gow%i==0:
        print("yes")
        break
else:
    print("no")
