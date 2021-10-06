x = str(input())
x1 = len(x)
print("Lungimea șirului este:", x1)
x2 = x.count(x)
x3 = x[0:1]
if(x3=="A" or x3=="a"):
   print("Sirul începe cu ",x3)
else:
    print("Sirul nu incepe cu A sau a ")
    print("Sirul incepe cu :", x3);
x4 = x[-1]
if(x4=="."):
    print("Sirul se termina cu . ")
else:
    print("Sirul nu se termina cu .")
