numinput = input()
modresult = 0
savearray = ['']
position = 0
i=0
for i in range(len(numinput)):
    if modresult != int(numinput[i])%2:
        savearray[position] += str(numinput[i])
    else:
        savearray.append('')
        position+=1
        savearray[position] = str(numinput[i])
    modresult = int(numinput[i])%2
print(savearray)
position = 0
length = 0
for i in range(len(savearray)):
    if len(savearray[i]) > length:
        position = i
        length = len(savearray[i])
print(savearray[position])
    
    
        
        
