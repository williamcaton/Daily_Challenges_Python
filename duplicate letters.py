a = input()
letters = []
check = 0
for i in range(len(a)):
    for j in range(len(letters)):
        if letters[j] == a[i]:
            check = 1
    if check == 0:
        letters.append(a[i])
    else:
        print('duplicate!')
    check = 0
