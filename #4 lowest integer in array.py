array = [3,4,-1,1,2,5]
num = 1
numstore = 0
while num != numstore:
    #print(num,numstore)
    numstore = num
    for i in array:
        if i == num+1:
            num += 1
            #print(num)
print(num+1)
    

