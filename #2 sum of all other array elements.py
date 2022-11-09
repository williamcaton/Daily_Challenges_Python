array = [1,2,3,4,5]
Sum=[1]*5
for i in range(len(array)):
    for j in range(len(array)):
        if i!=j:
            Sum[i] *= array[j]
print(Sum)
