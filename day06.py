import re
from collections import Counter

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a = [int(x) for x in lines[0].split(",")]

a2 = []
for i in range(9):
    a2.append(a.count(i))
    

for t in range(80):
    a2_new=[0]*len(a2)
    for x in range(len(a2)):
        if(x==0):
            a2_new[6]=a2_new[6]+a2[x]
            a2_new[8]=a2_new[8]+a2[x]
        else:
            a2_new[x-1]=a2_new[x-1]+a2[x]
    a2=a2_new.copy()
    
print(sum(a2))

a2 = []
for i in range(9):
    a2.append(a.count(i))
    
for t in range(256):
    a2_new=[0]*len(a2)
    for x in range(len(a2)):
        if(x==0):
            a2_new[6]=a2_new[6]+a2[x]
            a2_new[8]=a2_new[8]+a2[x]
        else:
            a2_new[x-1]=a2_new[x-1]+a2[x]
    a2=a2_new.copy()
    
print(sum(a2))
