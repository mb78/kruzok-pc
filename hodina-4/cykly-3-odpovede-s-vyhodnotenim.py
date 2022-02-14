#!/bin/env python3

# Ako nacitat 10 odpovedi ?
# a ako odpovede spracovat, napriklad vypisat ich do riadku ?

print("Ake zvierata mas najradsej ? napis ich 5")
zvierata=[]
for i in range(1,6):
    zvierata.append(input(str(i)+". zviera: "))
print("Mas rad/rada zvierata: ",end="")
for zviera in zvierata:
    print(zviera+", ",end="")
print()
