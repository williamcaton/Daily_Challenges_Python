x = input()
x=list(x)
x.reverse()
place = -1
for i in range(int(len(x)/3)):
    place += 4
    j = len(x)
    x.append(' ')
    while j > place:
        x[j] = x[j-1]
        j-=1
    x[j] = ','
x.reverse()
print(x)
    
    
