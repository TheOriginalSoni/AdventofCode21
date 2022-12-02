lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a = []
for line in lines:
    a.append(int(line))

s=0
for b in range(len(a)-1):
    if(a[b]<a[b+1]):
        s=s+1 
print(s)
    
s=0
for b in range(len(a)-3):
    if(a[b]<a[b+3]):
        s=s+1 
print(s)
