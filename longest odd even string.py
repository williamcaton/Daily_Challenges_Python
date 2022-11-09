string = "225424272163254474441338664823"
current = string[0]
currentlongest = ""
for i in range(1,len(string)):
    if (int(string[i])%2)!=(int(string[i-1])%2):
        current += string[i]
    else:
        if len(current)>len(currentlongest):
            currentlongest = current
        current = string[i]
print(currentlongest)
        
    
