gow=input()
for i in range(0,len(gow)):
   if(gow[i].isalpha() and gow[i].isdigit()):
    print("No")
else:
  print("Yes")
